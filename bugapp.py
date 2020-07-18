import streamlit as st
import pandas as pd
import numpy as np
import datetime
import pytz
import utils_bugs as utilsb

st.title('Hello, Bugs!')

now = datetime.datetime.now()
ct_now = pytz.timezone("America/Chicago").localize(now)
now_month = ct_now.month
now_hour = ct_now.hour

st.header('Tell me about your game:')

hems = ['Northern', 'Southern']
hem_key = st.radio('Which hemisphere are you in?', options=hems, index=0)

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
month_key = st.selectbox('Which month is it?', options=months, index = now_month -1)

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
    '11:00AM - 11:59AM' : 11,
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
hour_key = st.selectbox('What time is it?', options = hours, index = now_hour)

bug_df = pd.read_csv('data/bugs_clean.csv')

hem_arg = hem_key[0].lower() + "h"
mon_arg = month_key[:3].lower()

current_time = time_names[hour_key]

current = utilsb.show_current_bugs(bug_df, hem_arg, mon_arg, current_time)

type_titles = ['Trees', 'Flowers', 'Water', 'Other']

type_key = st.selectbox('Which type of bug would you like to see?', options=type_titles)

if type_key == 'Other':
    st.subheader(f'Showing currently active {type_key.lower()} bugs')
else: 
    st.subheader(f'Showing currently active bugs related to: {type_key}')

st.write(f'{hem_key} hemisphere, {month_key}, some time between {hour_key}')

loc_current = current.loc[(current['where'] == type_key.lower())]

how_types = loc_current['how'].unique()
for how_ty in how_types:
    how_loc_current = loc_current.loc[loc_current['how'] == how_ty]
    if len(how_loc_current) == 0:
        continue
    image_capt_dict = {}
    st.write(how_ty.title())
    for i in how_loc_current.index:
        bug_icon = utilsb.find_bug_icon(how_loc_current['name'][i])
        path = 'images/'
        image_loc = f"{path}{bug_icon}.png"
        caption = f"{how_loc_current['name'][i].title()}: {how_loc_current['sell'][i]:,} bells"
        image_capt_dict[image_loc] = caption
    
    st.image(list(image_capt_dict.keys()), caption=list(image_capt_dict.values()), width=100)

st.subheader("Please note!")
st.write("Some species will not spawn on your island until you have caught a certain number of bugs, but all bugs will spawn if you've caught more than 100 bugs. You can check your total lifetime catch number looking at the Nook Miles achievement 'You've Got the Bug'")

st.subheader('Contact')
st.markdown('Have an issue or suggestion? Go to the [GitHub Repository](https://github.com/lindseyberlin/acnh_fish_guide) for this app to open an issue.')
st.markdown('Questions? Ask me on [Twitter](https://twitter.com/Lindsey_Dev).')
st.markdown('Data sourced from the [Community Data Spreadsheet](https://tinyurl.com/acnh-sheet).')