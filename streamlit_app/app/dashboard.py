import streamlit as st
import pandas as pd
import numpy as np
import scipy.stats
from scipy.stats import norm
import plotly.express as px

st.set_page_config(
    page_title = "A/B Testing Streamlit App", initial_sidebar_state= "expanded"
)

st.write(
    """
# A/B Testing App
Upload your experiment results to see the significance of your A/B test.
"""
)

uploaded_file = st.file_uploader("Upload CSV", type=".csv")

use_example_file = st.checkbox(
    "Use example file", True, help="Use in-built example file to demo the app"
)

ab_default = None
result_default = None

# If CSV is not uploaded and checkbox is filled, use values from the example file
# and pass them down to the next if block
if use_example_file:
    uploaded_file = "data/cookie_cats.csv"
    ab_default = ["variant"]
    result_default = ["converted"]
