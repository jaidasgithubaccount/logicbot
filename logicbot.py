import streamlit as st
# functions:

# website:
st.title("Use the LogicBot...")
st.header("Explore the functionalities below:", divider="blue")

with st.popover("⚙️ SETTINGS"):
    share_defs = st.toggle("Share Definitions")
    globalload = st.toggle("Spacy Sentence Split")
    nf_default = st.pills("Default Normal Form", ["CNF", "DNF"], default="DNF")
    nf_behavior = st.pills("Normal Form Behavior", ["DEFAULT", "PROMPT", "GUESS"], default="PROMPT")

# bot body/inputs:




st.divider()
st.page_link("info.py", icon='🦴', label="How does this work?")