import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to Diet Recommendation powered by SugarCare! 👋")

st.sidebar.success("Select a recommendation type.")

st.markdown(
    """
        Diet Recommendation for Diabetic Patients concerned over their nutritional health for Sugar Care application.
    """
)
