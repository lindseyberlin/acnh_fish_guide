import pandas as pd
import numpy as np

import warnings
warnings.filterwarnings('ignore')

def subset_bugs(data, hemisphere, month):
    '''
    Inputs:
    data: pandas dataframe
        needs to have where/how and time
    hemisphere: str
        either "sh" or "nh"
    month: str
        3-letter abbreviation for month (ie "jun")
        
    Output:
    monthdf: pandas dataframe
        version of data with only bugs that appear in that month 
        for that hemisphere
    '''
    cols = ['name', 'sell', 'weather', 'spawn_rates',
            'where', 'how', 'time']
    month_col = hemisphere + "_" + month
    cols.append(month_col)

    monthdf = data[cols]
    
    monthdf = monthdf.loc[~monthdf[month_col].isna()]

    return monthdf

def parse_times(monthdf):
    """
    Inputs:
    monthdf: pandas dataframe
        output of subset_bugs, based on hem and month
        
    Output:
    concatdf: pandas dataframe
        monthdf plus additional columns to match hour data
    """
                
    # Defining availability times based on original values
    avail_times = {
        # all day, functionally 0:00 - 24:00
        'all': list(range(0, 24)),    
        
        # 4am - 5pm, aka 4:00 - 17:00
        '4a-5p': list(range(4, 17)),
        
        # 4am - 7pm, aka 4:00 - 19:00
        '4a-7p': list(range(4, 19)),
        
        # 8am - 4pm, aka 8:00 - 16:00
        '8a-4p': list(range(8, 16)),
        
        # 8am - 5pm, aka 8:00 - 17:00
        '8a-5p': list(range(8, 17)),
        
        # 8am - 7pm, aka 8:00 - 19:00
        '8a-7p': list(range(8, 19)),

        # 4pm - 11am, aka 16:00 - 11:00
        '4p-11a': list(range(16, 24)) + list(range(0, 11)),    
        
        # 5pm - 4am, aka 17:00 - 4:00
        '5p-4a': list(range(17, 24)) + list(range(0, 4)),
        
        # 5pm - 8am, aka 17:00 - 8:00
        '5p-8a': list(range(17, 24)) + list(range(0, 8)),
        
        # 7pm - 4am, aka 19:00 - 4:00
        '7p-4a': list(range(19, 24)) + list(range(0, 4)),
        
        # 7pm - 8am, aka 19:00 - 8:00
        '7p-8a': list(range(19, 24)) + list(range(0, 8)),

        # 11pm - 8am, aka 23:00 - 8:00
        '11p-8a': list(range(23, 24)) + list(range(0, 8)),

        # 11pm - 4pm, aka 23:00 - 16:00
        '11p-4p': list(range(23, 24)) + list(range(0, 16)),
        
        # evening cicada: 4am - 8am and 4pm - 7pm
        '4a-8a-4p-7p': list(range(4, 8)) + list(range(16, 19)),
        
        # walking stick: 4am - 8am and 5pm - 7pm
        '4a-8a-5p-7p': list(range(4, 8)) + list(range(17, 19)),
    }

    # Creating a blank df for hours 0-23, to match the monthdf
    blank_df = pd.DataFrame(np.zeros(shape=(len(monthdf), 24), dtype='int'))
    
    # Resetting the blank df index to match monthdf
    blank_df = blank_df.set_index(monthdf.index)
    
    # Adding empty columns to original monthdf
    concatdf = pd.concat([monthdf, blank_df], axis=1)
    
    for i, row in concatdf.iterrows():
        time_value = row['time']
        cols_to_fill = avail_times[time_value]
        for col in cols_to_fill:
            concatdf.at[i, col] = 1
        
    return concatdf

def subset_by_hour(concatdf, current_hour):
    """
    Inputs:
    concatdf: pandas dataframe
        output of parse_times, showing bugs available for the hem/month
        and including hour cols

    current_hour: int
        current hour in military time, between 0 and 23

    Output:
    current: pandas dataframe
        subset of all bugs available at that hour
    """
    # Don't want all of those hour cols after this
    # So, finding all non_hour_cols by the type of the col name
    non_hour_cols = [c for c in concatdf.columns.to_list()
                     if isinstance(c, str) == True]

    current = concatdf.loc[concatdf[current_hour] == 1]
    return current[non_hour_cols]

def show_current_bugs(data, hemisphere, month, current_hour):
    '''
    Combines all details/subsets to show only currently active bugs
    '''
    monthdf = subset_bugs(data, hemisphere, month)
    timedf = parse_times(monthdf)
    current = subset_by_hour(timedf, current_hour)

    return current

def find_bug_icon(bug_name):
    bug_icon_dict = {
        'Agrias Butterfly': 'Ins6',
        'Ant': 'Ins26',
        'Atlas Moth': 'Ins10',
        'Bagworm': 'Ins36',
        'Banded Dragonfly': 'Ins24',
        'Bell Cricket': 'Ins31',
        'Blue Weevil Beetle': 'Ins80',
        'Brown Cicada': 'Ins17',
        'Centipede': 'Ins60',
        'Cicada Shell': 'Ins69',
        'Citrus Long-horned Beetle': 'Ins39',
        'Common Bluebottle': 'Ins72',
        'Common Butterfly': 'Ins0',
        'Cricket': 'Ins30',
        'Cyclommatus Stag': 'Ins49',
        'Damselfly': 'Ins81',
        'Darner Dragonfly': 'Ins23',
        'Diving Beetle': 'Ins28',
        'Drone Beetle': 'Ins75',
        'Dung Beetle': 'Ins40',
        'Earth-boring Dung Beetle': 'Ins42',
        'Emperor Butterfly': 'Ins5',
        'Evening Cicada': 'Ins20',
        'Firefly': 'Ins41',
        'Flea': 'Ins56',
        'Fly': 'Ins59',
        'Giant Cicada': 'Ins65',
        'Giant Stag': 'Ins47',
        'Giant Water Bug': 'Ins76',
        'Giraffe Stag': 'Ins77',
        'Golden Stag': 'Ins50',
        'Goliath Beetle': 'Ins55',
        'Grasshopper': 'Ins32',
        'Great Purple Emperor': 'Ins74',
        'Hermit Crab': 'Ins66',
        'Honeybee': 'Ins11',
        'Horned Atlas': 'Ins52',
        'Horned Dynastid': 'Ins51',
        'Horned Elephant': 'Ins53',
        'Horned Hercules': 'Ins54',
        'Jewel Beetle': 'Ins44',
        'Ladybug': 'Ins37',
        'Long Locust': 'Ins13',
        'Madagascan Sunset Moth': 'Ins79',
        'Man-faced Stink Bug': 'Ins78',
        'Mantis': 'Ins15',
        'Migratory Locust': 'Ins14',
        'Miyama Stag': 'Ins46',
        'Mole Cricket': 'Ins33',
        'Monarch Butterfly': 'Ins4',
        'Mosquito': 'Ins58',
        'Moth': 'Ins9',
        'Orchid Mantis': 'Ins16',
        'Paper Kite Butterfly': 'Ins73',
        'Peacock Butterfly': 'Ins3',
        'Pill Bug': 'Ins57',
        'Pondskater': 'Ins27',
        "Queen Alexandra's Birdwing": 'Ins8',
        'Rainbow Stag': 'Ins48',
        "Rajah Brooke's Birdwing": 'Ins7',
        'Red Dragonfly': 'Ins22',
        'Rice Grasshopper': 'Ins67',
        'Robust Cicada': 'Ins18',
        'Rosalia Batesi Beetle': 'Ins82',
        'Saw Stag': 'Ins46',
        'Scarab Beetle': 'Ins43',
        'Scorpion': 'Ins63',
        'Snail': 'Ins29',
        'Spider': 'Ins61',
        'Stinkbug': 'Ins64',
        'Tarantula': 'Ins62',
        'Tiger Beetle': 'Ins70',
        'Tiger Butterfly': 'Ins2',
        'Violin Beetle': 'Ins38',
        'Walker Cicada': 'Ins19',
        'Walking Leaf': 'Ins34',
        'Walking Stick': 'Ins35',
        'Wasp': 'Ins12',
        'Wharf Roach': 'Ins71',
        'Yellow Butterfly': 'Ins1'
    }
    icon_name = bug_icon_dict[bug_name]
    return icon_name