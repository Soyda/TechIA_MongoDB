from pathlib import Path
import pandas as pd
import streamlit as st
import numpy as np

cars_db = pd.read_csv('./data/data.csv')

st.title('Cars dataset')

st.write(cars_db)

cars_filtered = st.container()

