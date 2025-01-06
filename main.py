import streamlit as st
import webbrowser
st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to Information APP! 👋")

# st.sidebar.success("Select a Dataframe From Below.")


st.markdown(
    """
    #### Select The Dataset From Below
"""
)
temp1 = st.selectbox('', ('', 'original dataset', 'modified dataset'))
if temp1 == 'original dataset':
    if st.button("Go to Original Dataset"):
        webbrowser.open("https://graph2-hejpjqhrvm6vthevrm4cns.streamlit.app/")
elif temp1 == 'modified dataset':
    if st.button("Go to Modified Dataset"):
        webbrowser.open("https://fcjzyvc2du68da5fhp2rgu.streamlit.app/")
else:
    st.write("Please select a dataset to open a link.")