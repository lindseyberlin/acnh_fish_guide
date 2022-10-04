import pandas as pd
import numpy as np

import warnings
warnings.filterwarnings('ignore')

def subset_fish(data, hemisphere, month):
    '''
    Inputs:
    data: pandas dataframe
        needs to have where/where_sub and min/max spawn
    hemisphere: str
        either "sh" or "nh"
    month: str
        3-letter abbreviation for month (ie "jun")
        
    Output:
    monthdf: pandas dataframe
        version of data with only fish that appear in that month 
        for that hemisphere
    '''
    cols = ['name', 'sell', 'shadow', 'spawn_rates',
            'rain_snow_catch_up', 'where', 'where_sub',
            'min_spawn', 'max_spawn']
    month_col = hemisphere + "_" + month
    cols.append(month_col)

    monthdf = data[cols]
    
    monthdf = monthdf.loc[~monthdf[month_col].isna()]

    return monthdf

def parse_times(monthdf, name_col):
    """
    Inputs:
    monthdf: pandas dataframe
        output of subset_fish, based on hem and month
        
    name_col: string
        combo of hem and month, to match "hh_mmm" pattern
        example: "nh_jul"
        
    Output:
    concatdf: pandas dataframe
        monthdf plus additional columns to match hour data
    """
                
    # Defining availability times based on original values
    avail_times = {
        # 4am - 9pm, aka 4:00 - 21:00
        '4 AM – 9 PM': list(range(4, 21)),

        # 9am - 4pm, aka 9:00 - 16:00
        '9 AM –\xa04 PM': list(range(9, 16)),

        # 4pm - 9am, aka 16:00 - 9:00
        '4 PM –\xa09 AM': list(range(16, 24)) + list(range(0, 9)),

        # 9pm - 4am, aka 21:00 - 4:00
        '9 PM –\xa04 AM': list(range(21, 24)) + list(range(0, 4)),

        # piranha: 9am - 4pm and 9pm - 4am
        '9 AM –\xa04 PM; 9 PM – 4 AM': list(range(9, 16)) + list(range(21, 24)) + list(range(0, 4)),

        # all day, functionally 0:00 - 24:00
        'All day': list(range(0, 24)),
    }

    # Creating a blank df for hours 0-23, to match the monthdf
    blank_df = pd.DataFrame(np.zeros(shape=(len(monthdf), 24), dtype='int'))
    
    # Resetting the blank df index to match monthdf
    blank_df = blank_df.set_index(monthdf.index)
    
    # Adding empty columns to original monthdf
    concatdf = pd.concat([monthdf, blank_df], axis=1)
    
    for i, row in concatdf.iterrows():
        time_value = row[name_col]
        cols_to_fill = avail_times[time_value]
        for col in cols_to_fill:
            concatdf.at[i, col] = 1
        
    return concatdf

def subset_by_hour(concatdf, current_hour):
    """
    Inputs:
    concatdf: pandas dataframe
        output of parse_times, showing fish available for the hem/month
        and including hour cols
    current_hour: int
        current hour in military time, between 0 and 23

    Output:
    current: pandas dataframe
        subset of all fish available at that hour
    """
    # Don't want all of those hour cols after this
    # So, finding all non_hour_cols ny the type of the col name
    non_hour_cols = [c for c in concatdf.columns.to_list()
                     if isinstance(c, str) == True]

    current = concatdf.loc[concatdf[current_hour] == 1]
    return current[non_hour_cols]

def show_current_fish(data, hemisphere, month, name_col, current_hour):
    '''
    Combines all details/subsets to show only currently active fish
    '''
    monthdf = subset_fish(data, hemisphere, month)
    timedf = parse_times(monthdf, name_col)
    current = subset_by_hour(timedf, current_hour)

    return current

def find_current_locs(current_df):
    '''
    Finds currently active location subtypes
    '''
    current_locs = []
    for i  in current_df.index:
        row_loc = [current_df['where'][i], current_df['where_sub'][i]]
        if row_loc in current_locs:
            continue
        else:
            current_locs.append(row_loc)
    return current_locs

def find_minmax_perc(sub_group):
    """
    Shoutout to bees, creator of newhorizonshq.com , for the insight
    
    Input:
    sub_group: pandas dataframe
        slice of fish df, needs min_spawn and max_spawn cols
    
    Output:
    sub_group_with_perc: pandas dataframe
        input df plus two more columns, min_perc and max_perc
    """
    
    # Creating new columns to add min/max percs
    sub_group.loc[:,'min_perc'] = 0.0
    sub_group.loc[:,'max_perc'] = 0.0
    
    for i in sub_group.index:
        # Grabbing min/max value for that row for ease of use
        i_min = sub_group['min_spawn'][i]
        i_max = sub_group['max_spawn'][i]
    
        # Grabbing min/max of all other rows by taking sum and
        # subtracting relevant row
        min_else = sub_group['min_spawn'].sum() - i_min
        max_else = sub_group['max_spawn'].sum() - i_max

        # Finding min and max percentages
        sub_group.at[i, 'min_perc'] = i_min / (max_else + i_min)
        sub_group.at[i, 'max_perc'] = i_max / (min_else + i_max)
        
    return sub_group

def find_fish_icon(fish_name):
    fish_icon_dict = {
        'anchovy': 'Fish81',
        'angelfish': 'Fish30',
        'arapaima': 'Fish36',
        'arowana': 'Fish33',
        'barred knifejaw': 'Fish47',
        'barreleye': 'Fish84',
        'betta': 'Fish77',
        'bitterling': 'Fish0',
        'black bass': 'Fish19',
        'blowfish': 'Fish73',
        'blue marlin': 'Fish58',
        'bluegill': 'Fish17',
        'butterfly fish': 'Fish42',
        'carp': 'Fish5',
        'catfish': 'Fish14',
        'char': 'Fish24',
        'cherry salmon': 'Fish23',
        'clown fish': 'Fish40',
        'coelacanth': 'Fish63',
        'crawfish': 'Fish10',
        'crucian carp': 'Fish2',
        'dab': 'Fish50',
        'dace': 'Fish3',
        'dorado': 'Fish34',
        'football fish': 'Fish56',
        'freshwater goby': 'Fish12',
        'frog': 'Fish11',
        'gar': 'Fish35',
        'giant snakehead': 'Fish16',
        'giant trevally': 'Fish70',
        'golden trout': 'Fish79',
        'goldfish': 'Fish7',
        'great white shark': 'Fish62',
        'guppy': 'Fish29',
        'hammerhead shark': 'Fish61',
        'horse mackerel': 'Fish46',
        'killifish': 'Fish9',
        'king salmon': 'Fish28',
        'koi': 'Fish6',
        'loach': 'Fish13',
        'mahi-mahi': 'Fish82',
        'mitten crab': 'Fish66',
        'moray eel': 'Fish55',
        'Napoleonfish': 'Fish43',
        'neon tetra': 'Fish31',
        'nibble fish': 'Fish67',
        'oarfish': 'Fish69',
        'ocean sunfish': 'Fish60',
        'olive flounder': 'Fish51',
        'pale chub': 'Fish1',
        'pike': 'Fish20',
        'piranha': 'Fish32',
        'pond smelt': 'Fish21',
        'pop-eyed goldfish': 'Fish8',
        'puffer fish': 'Fish45',
        'rainbowfish': 'Fish80',
        'ranchu goldfish': 'Fish85',
        'ray': 'Fish59',
        'red snapper': 'Fish49',
        'ribbon eel': 'Fish71',
        'saddled bichir': 'Fish68',
        'salmon': 'Fish27',
        'saw shark': 'Fish74',
        'sea bass': 'Fish48',
        'sea butterfly': 'Fish37',
        'sea horse': 'Fish39',
        'snapping turtle': 'Fish78',
        'soft-shelled turtle': 'Fish65',
        'squid': 'Fish52',
        'stringfish': 'Fish26',
        'sturgeon': 'Fish75',
        'suckerfish': 'Fish83',
        'surgeonfish': 'Fish41',
        'sweetfish': 'Fish22',
        'tadpole': 'Fish64',
        'tilapia': 'Fish76',
        'tuna': 'Fish57',
        'whale shark': 'Fish72',
        'yellow perch': 'Fish18',
        'zebra turkeyfish': 'Fish44'
        }
    icon_name = fish_icon_dict[fish_name]
    return icon_name