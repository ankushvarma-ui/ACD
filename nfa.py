import os

# Graphviz path
os.environ["PATH"] += os.pathsep + r"C:\Program Files\Graphviz\bin"

from graphviz import Digraph

# Create NFA
nfa = Digraph("NFA", format="png")
nfa.attr(rankdir="LR")

# States
nfa.node("q0", "q0")
nfa.node("q1", "q1")
nfa.node("q2", "q2", shape="doublecircle")

# Start arrow
nfa.node("start", "", shape="point")
nfa.edge("start", "q0")

# NFA transitions
nfa.edge("q0", "q0", label="0,1")
nfa.edge("q0", "q1", label="0")
nfa.edge("q1", "q2", label="1")
nfa.edge("q2", "q2", label="0,1")

# Generate visualization
nfa.render("nfa", view=True)