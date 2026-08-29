import os

# Graphviz path
os.environ["PATH"] += os.pathsep + r"C:\Program Files\Graphviz\bin"

from graphviz import Digraph


# -----------------------------
# NFA TRANSITIONS
# -----------------------------

nfa = {
    ("q0", "0"): {"q0", "q1"},
    ("q0", "1"): {"q0"},

    ("q1", "0"): set(),
    ("q1", "1"): {"q2"},

    ("q2", "0"): {"q2"},
    ("q2", "1"): {"q2"}
}


# -----------------------------
# NFA -> DFA CONVERSION
# -----------------------------

start = frozenset(["q0"])

dfa_states = [start]
dfa_transitions = {}

i = 0

while i < len(dfa_states):

    current = dfa_states[i]
    i += 1

    for symbol in ["0", "1"]:

        next_state = set()

        # Find transitions for every NFA state
        for state in current:

            if (state, symbol) in nfa:
                next_state.update(
                    nfa[(state, symbol)]
                )

        next_state = frozenset(next_state)

        dfa_transitions[(current, symbol)] = next_state

        # Add new DFA state
        if next_state and next_state not in dfa_states:
            dfa_states.append(next_state)


# -----------------------------
# PRINT DFA
# -----------------------------

print("DFA States:")

for state in dfa_states:
    print(state)

print("\nDFA Transitions:")

for (state, symbol), next_state in dfa_transitions.items():

    print(
        set(state),
        "--", symbol, "-->",
        set(next_state)
    )


# -----------------------------
# VISUALIZATION
# -----------------------------

dfa = Digraph("DFA", format="png")

dfa.attr(rankdir="LR")


# Create state names
names = {}

for i, state in enumerate(dfa_states):

    names[state] = "D" + str(i)

    label = "{"

    if state:
        label += ",".join(sorted(state))

    label += "}"


    # Accepting state if q2 exists
    if "q2" in state:

        dfa.node(
            names[state],
            label,
            shape="doublecircle"
        )

    else:

        dfa.node(
            names[state],
            label
        )


# Start arrow
dfa.node("start", "", shape="point")

dfa.edge(
    "start",
    names[start]
)


# Draw transitions
for (state, symbol), next_state in dfa_transitions.items():

    if next_state:

        dfa.edge(
            names[state],
            names[next_state],
            label=symbol
        )


# Generate image
dfa.render(
    "nfa_to_dfa",
    view=True
)