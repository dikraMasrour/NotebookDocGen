from opcode import stack_effect
import streamlit as st
from streamlit_ace import st_ace

st.set_page_config(
    page_title="Magic notebook",
    page_icon="✨",
)


st.title("Generated documentation for your DS & ML notebooks")
st.header("")


with st.expander(" 🪄 - About the app", expanded=True):

    st.write(
        """     
-   The *Generated documentation for your DS & ML notebooks* app is an easy-to-use interface where you can uploade your notebook containning only code cells and get in return a commented notebook !
	    """
    )

    st.markdown("")

st.markdown("")
st.markdown("## 📋 Upload your notebook")

with st.form(key="my_form"):

    st.warning("Note : Not all notebooks have a specific Domain and Technique!")
 
    domain = st.checkbox('Domain')
    technique = st.checkbox('Technique')
    uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
    for uploaded_file in uploaded_files:
        bytes_data = uploaded_file.read()
        st.write("filename:", uploaded_file.name)
        st.write(bytes_data)

    submit_button = st.form_submit_button(label="✨ Generate documentation!")


