import streamlit as st

page1 = st.Page('./app/pages/page1.py', title="Home", icon=":material/home:")
page2 = st.Page('./app/pages/page2.py', title="Example", icon=":material/home:")

pg = st.navigation([page1, page2])
st.set_page_config(page_title="FHE", page_icon=":material/edit:")
pg.run()