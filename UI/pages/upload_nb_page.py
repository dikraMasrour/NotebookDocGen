from opcode import stack_effect
import streamlit as st
from streamlit_ace import st_ace
from strimlitbook.reader import read_ipynb


st.set_page_config(
    page_title="Magic notebook",
    page_icon="✨",
)

print(st.session_state.uploaded_file)

## TODO : convert byte data to nb or json locally then pass path to strimlitbook


# nb = read_ipynb(st.session_state.uploaded_file)
# nb.display()

# st.title("Generated documentation for your DS & ML notebooks")
# st.header("")


# with st.expander(" About the app"):

#     st.write(
#         """     

# The *Generated documentation for your DS & ML notebooks* app is an easy-to-use interface where you can uploade your notebook containning only code cells and get in return a commented notebook !

# 	    """
#     )



