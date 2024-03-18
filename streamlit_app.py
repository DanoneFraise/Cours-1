import streamlit as st
name=st.text_input("Dan")
st.write ("Hello " + name)

import streamlit as st 
import pandas as pd

voc = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSeARXO3MT92XWpg2IwyQOQ8Wi2upeEkqJvNJz5i3bRqHdJIrTchGBBclVu-3Jd1ohYKM4IxecgV64I/pub?output=csv')
st.dataframe(voc)
