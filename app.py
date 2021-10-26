import streamlit as st

import time
from datetime import datetime

clock_place = st.empty()

while True:
    clock_place.markdown(f'# {datetime.now().strftime("%m/%d/%Y, %H:%M:%S")}')
    time.sleep(5)