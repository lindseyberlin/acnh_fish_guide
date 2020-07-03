import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import utils as utils

st.title('Hello, Fish!')

now = datetime.now()
now_month = now.month
now_hour = now.hour

st.sidebar.markdown('# Tell me about your game:')

hems = ['Northern', 'Southern']
hem_key = st.sidebar.selectbox('Which hemisphere are you in?', options=hems, index=0)

month_names = {
    'January' : 1, 
    'February' : 2, 
    'March' : 3, 
    'April' : 4,
    'May' : 5, 
    'June' : 6, 
    'July' : 7, 
    'August' : 8, 
    'September' : 9, 
    'October' : 10, 
    'November': 11, 
    'December': 12
    }
months = list(month_names.keys())
month_key = st.sidebar.selectbox('Which month is it?', options=months, index = now_month -1)

time_names = {
    'Midnight - 12:59AM' : 0,
    '1:00AM - 1:59AM' : 1,
    '2:00AM - 2:59AM' : 2,
    '3:00AM - 3:59AM' : 3,
    '4:00AM - 4:59AM' : 4,
    '5:00AM - 5:59AM' : 5,
    '6:00AM - 6:59AM' : 6,
    '7:00AM - 7:59AM' : 7,
    '8:00AM - 8:59AM' : 8,
    '9:00AM - 9:59AM' : 9,
    '10:00AM - 10:59AM' : 10,
    '11:00AM - 11:59AM:' : 11,
    'Noon - 12:59PM' : 12,
    '1:00PM - 1:59PM' : 13,
    '2:00PM - 2:59PM' : 14,
    '3:00PM - 3:59PM' : 15,
    '4:00PM - 4:59PM' : 16,
    '5:00PM - 5:59PM' : 17,
    '6:00PM - 6:59PM' : 18,
    '7:00PM - 7:59PM' : 19,
    '8:00PM - 8:59PM' : 20,
    '9:00PM - 9:59PM' : 21,
    '10:00PM - 10:59PM' : 22,
    '11:00PM - 11:59PM' : 23,
}

hours = list(time_names.keys())
hour_key = st.sidebar.selectbox('What time is it?', options = hours, index = now_hour)

st.write(f'Showing currently active fish for:')
st.write(f'{hem_key} hemisphere, in {month_key}, at some time between {hour_key}')

fish_df = pd.read_csv('data/fish_clean.csv')

hem_arg = hem_key[0].lower() + "h"
mon_arg = month_key[:3].lower()
col_name = hem_arg + "_" + mon_arg

current_time = time_names[hour_key]

current = utils.show_current_fish(fish_df, hem_arg, mon_arg, col_name, current_time)

current_locs = utils.find_current_locs(current)

for loc in current_locs:
    if loc[0] != loc[1]:
        title = f"{loc[0].title()}: {loc[1].title()}"
        spec_loc = current.loc[current['where_sub'] == loc[1]]
        rest_loc = current.loc[(current['where'] == loc[0]) & (
            current['where_sub'] == loc[0])]
        loc_current = pd.concat([spec_loc, rest_loc])
    else:
        title = loc[0].title()
        loc_current = current.loc[(current['where'] == loc[0]) & (
            current['where_sub'] == loc[0])]
    st.subheader(f"{title}")
    st.dataframe(loc_current[['name', 'sell', 'shadow']], height=2000)

