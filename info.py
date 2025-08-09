import streamlit as st

# website:
st.title("About the LogicBot...")
st.header("Motivations, further work, and other notes", divider="blue")

motives, technotes, furtherwork, sources = st.tabs(["Project Motivations", "Tech Notes", "Further Work and Research", "Sources and Attributions"])

with motives:
    st.header("Project Motivations:")
    st.markdown('''
1. I'm a __big__ fan of [Warren Goldfarb](https://archive.org/details/deductivelogic0000gold).
2. I was _not_ a fan of having to hand-schematize arguments to check students' work back in undergrad, and less a fan of having to hand-check their proofs.
3. Computational solutions existed to [schematize](https://colab.research.google.com/github/norvig/pytudes/blob/master/ipynb/PropositionalLogic.ipynb) arguments, and to [check if they're valid or satisfiable](https://docs.sympy.org/latest/modules/logic.html), but none of the tools I'd used did _both_.
            ''')
    
with technotes:
    st.header("Propositional Logic")
    st.subheader("_Using Regular Expressions_")
    introduction, legend = st.columns(2)
    with introduction:
        st.markdown("As a proof of concept, I started by integrating Peter Norvig's [regular-expression propositional logic code](https://colab.research.google.com/github/norvig/pytudes/blob/master/ipynb/PropositionalLogic.ipynb) with [SymPy](https://docs.sympy.org/latest/modules/logic.html), a Python package that can check schematized arguments for ***satisfiability***.")
        st.markdown("A proposition -- like _P & ~Q_ --  is ***satisfiable*** if there's at least one consistent truth-assignment for all the literals (variables) in the proposition. In this case, if P were True, and Q were False, then _P & ~Q_ would evaluate to True -- this assignment ***satisfies*** that schema.")
    with legend:
        st.markdown("Here's a key of the logical operators you'll see on this page:")
        st.markdown("""| Operator | Symbol | Another Form |
| ---------------- | ------ | ---------- |
| NOT              | -      | ~          |
| AND              | •      | &          |
| OR               | v      | \|         |
| THEREFORE        | >      | >>         |
| BICONDITIONAL    | ≡      | << >>          |""")
        
    st.header("Predicate Logic")
    st.subheader("_Now With Natural Language Processing!_")
    st.markdown("Future iterations of the LogicBot will utilize natural language processing to determine the ***Universe of Discourse*** and ***Scope of Discourse*** for certain sentences. The Universe of Discourse refers to the kinds of things enclosed by a variable like 'x' in a schema. The Scope refers to whether one refers to *all* elements in the universe, or only *some*.")
    st.markdown("Here's how a similar concept might be understood with different scopes of discourse:") 
    table, lits = st.columns([0.8, 0.2])
    with table:
        st.markdown('''
| Type                                     | Sentence                  | Schema       |
| ---------------------------------------- | ------------------------- | ------------ |
| **Propositional Logic (named variable)** | Paul is a firefighter.    | Fp           |
| **Predicate Logic - Existential Scope**  | There is a firefighter.   | (Ǝx)(Fp)     |
| **Predicate Logic - Universal scope**    | Everyone's a firefighter. | (∀x)(x > Fx) |
''')
    with lits:
        st.caption("""**LITERALS:**   
Fx = x is a Firefighter  
p = Paul""")
    
    st.markdown("... and different universes:")
    antable, anlits = st.columns([0.8, 0.2])
    with antable:
        st.markdown('''
:blue-background[**Sentence:** All poets in the accelerated program received an A+.]
| Universe of Discourse              | Schema                  |
| ---------------------------------- | ----------------------- |
| **Everyone and Every Thing**       | (∀x)(Px ⋀ Qx ⋀ Rx > Sx) |
| **Persons**                        | (∀x)(Qx ⋀ Rx > Sx)      |
| **Poets (*assumed to be People*)** | (∀x)(Rx > Sx)           |
| **Accelerated Program Poets**      | (∀x)(x > Sx)            |          
''')
    with anlits:
        st.caption("""**LITERALS:**   
Px = x is a Person  
Qx = x is a Poet   
Rx = x is in the Accelerated Program   
Sx = x received an A+    """)
        

with furtherwork:
    st.subheader("Further Work: Validity and Soundness")
    st.markdown("This logibot checks for vaildity, and will tell you if your arguments' premises don't necessarily imply your conclusion (and the circumstances that poke holes in your reasoning). It can't tell you if a valid argument is in any way ***sound***, or whether its premises are factual.")
    st.markdown("""Here's an out-of-the box NLI way to check for soundness, if you dare:  
            1. download the relevant packages and dependencies for [Google's Gemini AI API](https://ai.google.dev/gemini-api/docs)  
            2. run a _model.generate_content()_ call with each proposition (or predicate clause) added as an input to a generic 'is X proposition true?' search query. 
            
But, that'd be computationally intense, and there are still fundamental issues with Logical Reasoning and English Language Parsing, so no.""")

with sources:
    st.subheader("Sources and Attributions:")
    st.markdown("""**Propositional Logic Jupyter Notebook**  
            [GitHub](https://github.com/norvig/pytudes/blob/main/ipynb/PropositionalLogic.ipynb) | [Google Colab](https://colab.research.google.com/github/norvig/pytudes/blob/master/ipynb/PropositionalLogic.ipynb)  
            _Copyright (c) 2010-2017 Peter Norvig_""")
    st.markdown("""**SymPy: Python Library for Symbolic Mathematics**  
            [GitHub](https://github.com/sympy/sympy)   
            Meurer A, Smith CP, Paprocki M, Čertík O, Kirpichev SB, Rocklin M, Kumar A, Ivanov S, Moore JK, Singh S, Rathnayake T, Vig S, Granger BE, Muller RP, Bonazzi F, Gupta H, Vats S, Johansson F, Pedregosa F, Curry MJ, Terrel AR, Roučka Š, Saboo A, Fernando I, Kulal S, Cimrman R, Scopatz A. (2017) SymPy: symbolic computing in Python. _PeerJ Computer Science_ 3:e103 [https://doi.org/10.7717/peerj-cs.103](https://doi.org/10.7717/peerj-cs.103)   
            _Copyright (c) 2006-2023 SymPy Development Team_""")
    st.markdown("""**ALSO NEED A CITE FOR SPACY NLP!!!**""")