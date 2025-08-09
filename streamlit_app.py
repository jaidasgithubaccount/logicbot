import streamlit as st

def Home():
    # Show title and description
    st.title("🦾 The LogicBot")
    st.header("Argument-Strength analyzer", divider="blue")

    st.subheader("... what's that?")
    st.markdown("The LogicBot :blue-background[reads English sentences] and arguments and :blue-background[evaluates them for their strength] by using regular expressions aided by natural language processing methods.")
    st.markdown("The current LogicBot handles **Propositional Logic** and **_Monadic_ Predicate Logic**.")
    firstcol, secondcol = st.columns(2)
    with firstcol:
        st.markdown(":blue-background[**Propositional Logic**] refers to the logical relationships between phrases that can be true or false, aka *propositions*.")
    with secondcol:        
        st.markdown(":blue-background[**Predicate Logic**] refers to the logical relationships of propositions within a given Universe of Discourse (or domain).")
        st.markdown("Our current iteration considers only :blue-background[*Monadic*] Predicate logic - predicates only have one subject, and don't concern themselves with a (relational) object.")
    
    left, center, right = st.columns([0.1, 0.7, 0.1])
    with center:
        st.image("photos/hungryfarmers.jpeg", use_container_width=True)
    bigleft, smallcenter, bigright = st.columns([0.3, 0.4, 0.3])
    with smallcenter:
        st.page_link("logicbot.py", label="ENTER THE LOGICBOT", icon='🦾')


pages = [st.Page(Home, default=True), st.Page("logicbot.py", title="LogicBot"), st.Page("info.py", title="About")]
pg = st.navigation(pages)
pg.run()