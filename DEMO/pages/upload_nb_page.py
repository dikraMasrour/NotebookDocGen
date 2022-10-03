import streamlit as st
import demo_utils as du
import json
import os
import streamlit_ace as st_ace
from strimlitbook.reader import read_ipynb


# '''TODO : 
#  prep help strings 
#  implement models
# '''

DUMP_PATH_COM = r'DEMO'
RUN_PATH = r'..\Classification_Task\notebooks\scripts\run.py'



# page config
st.set_page_config(
    page_title="Magic notebook",
    page_icon="✨",
)

# sidebar
st.sidebar.markdown("# Upload your notebook Page🎉")


# session state initializing
du.initialize_session(st.session_state)


if st.session_state.uploaded_file == None:
    st.error('No file has been uploaded. Please navigate to the main page and upload a notebook.')
    st.session_state.go_back_main =  st.button('Main page')
    if st.session_state.go_back_main:
        du.switch_page('demo')

else:

    indent, top_class_but, top_doc_but, top_go_but = st.columns([2, 5, 4, 1], gap='small')

    # back button
    with indent:
        st.write(' ')
        st.write(' ')
        st.session_state.go_back_main02 =  st.button('Upload another notebook')
        if st.session_state.go_back_main02:
            du.switch_page('demo')

    # classification
    with top_class_but:
        classify = st.multiselect('Classify the notebook by', ['Domain', 'Technique'], help='help')

    # doc gen
    with top_doc_but:
        gendoc = st.selectbox('Generate documentation using', ('-', 'PLBART'), help='help')

    # go button
    with top_go_but:
        if (len(classify) != 0) | (gendoc != '-'):
            st.write(' ')
            st.write(' ')
            top_go_button = st.button('Go!')
    
  

 


    # classify by domain
    if ('Domain' in classify) and (len(classify) == 1) and (top_go_button):
        os.system('python ' + RUN_PATH + ' ' + 'dump.json ' + '--class domain >> file.txt')
        with open('file.txt') as f:
            contents = str(f.readlines()[-1])
        
        dom, tech = du.prep_classification(contents)
        # horizontal divider
        '''
        ---
        '''
        st.write("Your notebook's domain is : ", dom)
        '''
        ---
        '''
        


    # classify by technique
    elif ('Technique' in classify) and (len(classify) == 1) and (top_go_button):
        os.system('python ' + RUN_PATH + ' ' + 'dump.json ' + '--class technique >> file.txt')
        with open('file.txt') as f:
            contents = str(f.readlines()[-1])

        dom, tech = du.prep_classification(contents)
        # # horizontal divider
        '''
        ---
        '''
        st.write("Your notebook's technique is : ", tech)
        '''
        ---
        '''
        

    # classify by both
    elif ('Technique' in classify) and ('Domain' in classify) and (top_go_button):
        os.system('python ' + RUN_PATH + ' ' + 'dump.json ' + '--class both >> file.txt')
        with open('file.txt') as f:
            contents = str(f.readlines()[-1])

        dom, tech = du.prep_classification(contents)    
        # horizontal divider
        '''
        ---
        '''
        st.write("Your notebook's domain & technique are : ", dom, ' & ', tech) 
        '''       
        ---
        '''

    du.display_nb()