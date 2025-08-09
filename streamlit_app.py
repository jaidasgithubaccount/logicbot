import streamlit as st

def Home():
    # Show title and description
    st.title("🦾 The LogicBot")
    st.header("Argument-Strength analyzer", divider="red")

    st.subheader("... what's that?")
    st.markdown("The LogicBot :red-background[reads English sentences] and arguments and :red-background[evaluates them for their strength] by using regular expressions aided by natural language processing methods.")
    st.markdown("The current LogicBot handles **Propositional Logic** and **_Monadic_ Predicate Logic**.")
    firstcol, secondcol = st.columns(2)
    with firstcol:
        st.markdown(":red-background[**Propositional Logic**] refers to the logical relationships between phrases that can be true or false, aka *propositions*.")
    with secondcol:        
        st.markdown(":red-background[**Predicate Logic**] refers to the logical relationships of propositions within a given Universe of Discourse (or domain).")
    
    left, center, right = st.columns([0.1, 0.8, 0.1])
    with center:
        st.image("photos/hungryfarmers.jpeg", use_container_width=True)
        st.page_link("logicbot.py", label="LogicBot", icon='🦾')
        st.markdown("_Argument-Strength Analyzer_")


pages = [st.Page(Home, default=True)]
pg = st.navigation(pages)
pg.run()