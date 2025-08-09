import streamlit as st

# website:
st.title("About the LogicBot...")
st.header("Motivations, further work, and other notes", divider="rainbow")

motives, technotes, furtherwork = st.tabs(["Project Motivations", "Tech Notes and Sources", "Further Work and Research"])

st.header("Project Motivations:")

st.markdown('''
1. I'm a __big__ fan of [Warren Goldfarb](https://archive.org/details/deductivelogic0000gold).
2. I was _not_ a fan of having to hand-schematize arguments to check students' work back in undergrad, and less a fan of having to hand-check their proofs.
3. Computational solutions existed to [schematize](https://colab.research.google.com/github/norvig/pytudes/blob/master/ipynb/PropositionalLogic.ipynb) arguments, and to [check if they're valid or satisfiable](https://docs.sympy.org/latest/modules/logic.html), but none of the tools I'd used did _both_.
            ''')