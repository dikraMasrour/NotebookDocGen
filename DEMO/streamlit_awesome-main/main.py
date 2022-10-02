import streamlit as st


def load_text(file_path):
    """A convenience function for reading in the files used for the site's text"""
    with open(file_path) as in_file:
        return in_file.read()


if __name__ == '__main__':

    header = load_text('header.md')
    st.write(header)

    # Don't use <script>, just import CSS directly
    css_example = load_text('css.md')
    st.write(css_example, unsafe_allow_html=True)

    # HTML component
    st.write('### Component Example')
    component_example = load_text('awesome.html')
    st.components.v1.html(component_example)
