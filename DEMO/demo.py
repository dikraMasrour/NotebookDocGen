from random import random
from streamlit_ace import st_ace
import streamlit as st
import pandas as pd
import numpy as np
import demo_utils as du

# page config
st.set_page_config(
    page_title="Magic notebook",
    page_icon="✨",
)


# session state initializing
du.initialize_session(st.session_state)


# title
magic = du.load_text("streamlit_awesome-main\magic_icon.md")
st.write(magic, unsafe_allow_html=True)

# about section
with st.expander("About the app"):

    st.markdown("No time to comment all your code cells ? Need a quick way to organise your notebooks by domains and techniques used? We've got you covered !")
    github_icon = du.load_text('streamlit_awesome-main\github_icon.md')
    st.write(github_icon, unsafe_allow_html=True)




# decide whether to upload a notebook or work on the app
with st.container():
    upload_nb = st.radio(
    "I have a notebook to upload !",
    ('Yes !', "No, I want to use the app's interface"))


# horizontal divider
'''
---
'''


if upload_nb == 'Yes !':
    du.show_upload_form(st.session_state)

elif upload_nb == "No, I want to use the app's interface":
    st.session_state.addButton = st.button(' ➕ Add code cell')
    
    dict_len = len(st.session_state.codeCells)

    if st.session_state.addButton:
        st.session_state.codeCells[dict_len] = 'Write your code'


    for codecell in st.session_state.codeCells.copy():
        
        with st.container() as c: 
            coll, colr = st.columns([4,2])
            with coll:
                code =  st_ace(placeholder=str(codecell), language='python', height=80, auto_update=True)
            
            st.session_state.codeCells[codecell] = code

            with colr:
                st.write(st.session_state.codeCells[codecell])








    
# @st.cache
# def load_data(nrows):
#     data = pd.read_csv(DATAURL, nrows=nrows)
#     lowercase = lambda x: str(x).lower()
#     data.rename(lowercase, axis='columns', inplace=True)
#     data[DATECOL] = pd.to_datetime(data[DATECOL])
#     return data 

# load data
# data_load_state = st.text('Loading data ...')
# data = load_data(10000)
# data_load_state.text('Loading data ... done! (using cache)')

# # toggle to show raw data
# if st.checkbox('Show raw data'):
#     st.subheader('Raw data')
#     st.write(data)

# # histogram of pickups per hour
# st.subheader('Number of pickups per hour')
# hist_values = np.histogram(data[DATECOL].dt.hour, bins=24, range=(0,24))[0]
# st.bar_chart(hist_values)

# slider to filter data per time
# hour_to_filter = st.slider('hour', 0, 23, 17) # min 0h, max 23h, default 17h
# st.subheader(f'Map of all pickups at {hour_to_filter}:00')
# filtered_data = data[data[DATECOL].dt.hour == hour_to_filter]
# st.map(filtered_data)


# def add_code_cell():
#     if 'codeCells' not in st.session_state:
#         st.session_state.codeCells = []
#     st.session_state.codeCells.append(st.text_input(label=f'code {random()}'))


# st.session_state.addButton = st.button('add code cell', on_click=add_code_cell)

# st.write(st.session_state.addButton)

# if st.session_state.addButton:
#     # add_code_cell()
#     st.write(st.session_state.codeCells)


# ''' TODO:  
# implement classification model
# give choice of classification (domain, tech)
# give choice to upload ready notebook
# implement docgen model
# prep notebook file to be dowloaded after docgen
# make more aesthetic


# '''

# if 'codeCells' not in st.session_state:
#     st.session_state.codeCells = {}

# st.session_state.addButton = st.button('add code cell')


# dict_len = len(st.session_state.codeCells)

# if st.session_state.addButton:
#     st.session_state.codeCells[dict_len] = 'write code'


# for codecell in st.session_state.codeCells.copy():
    
#     with st.container() as c: 
#         coll, colr = st.columns([4,2])
#         with coll:
#             code =  st_ace(placeholder=codecell, language='python', height=80, auto_update=True)
        
#         st.session_state.codeCells[codecell] = str(code)

#         with colr:
#             st.write(st.session_state.codeCells[codecell])









# st.markdown("")
# st.markdown("## 📋 Upload your notebook")

# with st.form(key="my_form"):

#     st.warning("Note : Not all notebooks have a specific Domain and Technique!")
 
#     domain = st.checkbox('Domain')
#     technique = st.checkbox('Technique')
#     uploaded_files = st.file_uploader("Choose a .ipynb file")
#     for uploaded_file in uploaded_files:
#         bytes_data = uploaded_file.read()
#         st.write("filename:", uploaded_file.name)
#         st.write(bytes_data)

#     submit_button = st.form_submit_button(label="✨ Generate documentation!")


