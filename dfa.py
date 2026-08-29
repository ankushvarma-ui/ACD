import os

# Tell Python where Graphviz is installed
os.environ["PATH"] += os.pathsep + r"C:\Program Files\Graphviz\bin"

from graphviz import Digraph

# Create DFA
dfa = Digraph("DFA", format="png")

# Left to right
dfa.attr(rankdir="LR")

# States
dfa.node("q0", "q0")
dfa.node("q1", "q1", shape="doublecircle")

# Start arrow
dfa.node("start", "", shape="point")
dfa.edge("start", "q0")

# Transitions
dfa.edge("q0", "q0", label="0")
dfa.edge("q0", "q1", label="1")
dfa.edge("q1", "q0", label="0")
dfa.edge("q1", "q1", label="1")

# Generate image
dfa.render("dfa", view=True)