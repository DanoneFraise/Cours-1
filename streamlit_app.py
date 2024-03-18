import streamlit as st
name=st.text_input("Dan")
st.write ("Hello " + name)

import streamlit as st 
import pandas as pd
import numphy as np
voc = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSeARXO3MT92XWpg2IwyQOQ8Wi2upeEkqJvNJz5i3bRqHdJIrTchGBBclVu-3Jd1ohYKM4IxecgV64I/pub?output=csv')

st.dataframe(voc)
l = voc.shape[0]
i = hp.random.choice(range(l))
word_fr = voc['Définition'].value[i]
word_chi = voc['Pinyin'].values[i]
st.write(word_fr+" "+word_chi)
