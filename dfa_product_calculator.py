import tkinter as tk
from tkinter import messagebox

class DFAInputGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("DFA Input")
        
        self.dfa1_label = tk.Label(root, text="DFA 1")
        self.dfa1_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        
        self.dfa2_label = tk.Label(root, text="DFA 2")
        self.dfa2_label.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)
        
        self.dfa1_states_label = tk.Label(root, text="States:")
        self.dfa1_states_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        
        self.dfa1_states_entry = tk.Entry(root)
        self.dfa1_states_entry.grid(row=1, column=1, padx=10, pady=5)
        
        self.dfa2_states_label = tk.Label(root, text="States:")
        self.dfa2_states_label.grid(row=1, column=2, padx=10, pady=5, sticky=tk.W)
        
        self.dfa2_states_entry = tk.Entry(root)
        self.dfa2_states_entry.grid(row=1, column=3, padx=10, pady=5)
        
        self.dfa1_alphabet_label = tk.Label(root, text="Alphabet:")
        self.dfa1_alphabet_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        
        self.dfa1_alphabet_entry = tk.Entry(root)
        self.dfa1_alphabet_entry.grid(row=2, column=1, padx=10, pady=5)
        
        self.dfa2_alphabet_label = tk.Label(root, text="Alphabet:")
        self.dfa2_alphabet_label.grid(row=2, column=2, padx=10, pady=5, sticky=tk.W)
        
        self.dfa2_alphabet_entry = tk.Entry(root)
        self.dfa2_alphabet_entry.grid(row=2, column=3, padx=10, pady=5)
        
        self.dfa1_transitions_label = tk.Label(root, text="Transitions:")
        self.dfa1_transitions_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
        
        self.dfa1_transitions_entry = tk.Entry(root)
        self.dfa1_transitions_entry.grid(row=3, column=1, padx=10, pady=5)
        
        self.dfa2_transitions_label = tk.Label(root, text="Transitions:")
        self.dfa2_transitions_label.grid(row=3, column=2, padx=10, pady=5, sticky=tk.W)
        
        self.dfa2_transitions_entry = tk.Entry(root)
        self.dfa2_transitions_entry.grid(row=3, column=3, padx=10, pady=5)
        
        self.dfa1_initial_label = tk.Label(root, text="Initial State:")
        self.dfa1_initial_label.grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)
        
        self.dfa1_initial_entry = tk.Entry(root)
        self.dfa1_initial_entry.grid(row=4, column=1, padx=10, pady=5)
        
        self.dfa2_initial_label = tk.Label(root, text="Initial State:")
        self.dfa2_initial_label.grid(row=4, column=2, padx=10, pady=5, sticky=tk.W)
        
        self.dfa2_initial_entry = tk.Entry(root)
        self.dfa2_initial_entry.grid(row=4, column=3, padx=10, pady=5)
        
        self.dfa1_final_label = tk.Label(root, text="Final States:")
        self.dfa1_final_label.grid(row=5, column=0, padx=10, pady=5, sticky=tk.W)
        
        self.dfa1_final_entry = tk.Entry(root)
        self.dfa1_final_entry.grid(row=5, column=1, padx=10, pady=5)
        
        self.dfa2_final_label = tk.Label(root, text="Final States:")
        self.dfa2_final_label.grid(row=5, column=2, padx=10, pady=5, sticky=tk.W)
        
        self.dfa2_final_entry = tk.Entry(root)
        self.dfa2_final_entry.grid(row=5, column=3, padx=10, pady=5)
        
        self.submit_button = tk.Button(root, text="Submit", command=self.submit)
        self.submit_button.grid(row=6, column=1, columnspan=2, padx=10, pady=10)
        
    def submit(self):
        try:
            dfa1_states = set(self.dfa1_states_entry.get().split(','))
            dfa1_alphabet = set(self.dfa1_alphabet_entry.get().split(','))
            dfa1_transitions = self.parse_transitions(self.dfa1_transitions_entry.get())
            dfa1_initial = self.dfa1_initial_entry.get()
            dfa1_final = set(self.dfa1_final_entry.get().split(','))
            
            dfa2_states = set(self.dfa2_states_entry.get().split(','))
            dfa2_alphabet = set(self.dfa2_alphabet_entry.get().split(','))
            dfa2_transitions = self.parse_transitions(self.dfa2_transitions_entry.get())
            dfa2_initial = self.dfa2_initial_entry.get()
            dfa2_final = set(self.dfa2_final_entry.get().split(','))
            
            dfa1 = DFA(dfa1_states, dfa1_alphabet, dfa1_transitions, dfa1_initial, dfa1_final)
            dfa2 = DFA(dfa2_states, dfa2_alphabet, dfa2_transitions, dfa2_initial, dfa2_final)
            
            product_dfa = product(dfa1, dfa2)
            draw_product_dfa(product_dfa)
            
            messagebox.showinfo("Product DFA", "The product DFA has been drawn.")
            
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    def parse_transitions(self, transitions_str):
        transitions = {}
        for transition in transitions_str.split(';'):
            state1, trans = transition.split(',')
            symbol, state2 = trans.split('=')
            if state1 not in transitions:
                transitions[state1] = {}
            transitions[state1][symbol] = state2
        return transitions



class DFA:
    def __init__(self, Q, sigma, delta, q0, F):
        self.Q = Q  # set of states
        self.sigma = sigma  # alphabet
        self.delta = delta  # transition function
        self.q0 = q0  # initial state
        self.F = F  # set of final states


def product(dfa1, dfa2):
    # Compute the set of states of the product automaton
    Qp = {(q1, q2) for q1 in dfa1.Q for q2 in dfa2.Q}

    # Compute the alphabet of the product automaton
    sigmap = dfa1.sigma.union(dfa2.sigma)

    # Define the transition function of the product automaton
    deltap = {}
    for (q1, q2) in Qp:
        for a in sigmap:
            p1 = dfa1.delta[q1][a] if a in dfa1.delta[q1] else q1
            p2 = dfa2.delta[q2][a] if a in dfa2.delta[q2] else q2
            p = (p1, p2)
            deltap[(q1, q2), a] = p

    # Define the initial state of the product automaton
    q0p = (dfa1.q0, dfa2.q0)

    # Define the set of final states of the product automaton
    Fp = {(q1, q2) for q1 in dfa1.F for q2 in dfa2.F}

    # Construct the product automaton
    product_dfa = DFA(Qp, sigmap, deltap, q0p, Fp)

    return product_dfa



def input_dfa():
    name = input("Enter the name of the DFA: ")
    states = set(input("Enter the states separated by commas: ").split(','))
    alphabet = set(input("Enter the alphabet separated by commas: ").split(','))
    print("Enter the transitions in the format state1,a=state2;state1,b=state2 etc")
    transitions = {}
    for transition in input("Enter transitions: ").split(';'):
        state1, trans = transition.split(',')
        symbol, state2 = trans.split('=')
        if state1 not in transitions:
            transitions[state1] = {}
        transitions[state1][symbol] = state2
    initial_state = input("Enter the initial state: ")
    final_states = set(input("Enter the final states separated by commas: ").split(','))
    return DFA(states, alphabet, transitions, initial_state, final_states)




import matplotlib.pyplot as plt
import networkx as nx

def draw_product_dfa(product_dfa):
    # Create a directed graph
    G = nx.DiGraph()

    # Add nodes to the graph
    for q in product_dfa.Q:
        G.add_node(q)

    # Add edges to the graph
    for ((q1, q2), a), p in product_dfa.delta.items():
        if q1 != p:
            G.add_edge((q1, q2), p, label=a)
        else:
            G.add_edge((q1, q2), p, label=f'{a}, {a}')

    # Set the positions of the nodes
    pos = nx.spring_layout(G)

    # Draw the nodes and edges with labels
    nx.draw_networkx_nodes(G, pos, node_size=1000)
    nx.draw_networkx_labels(G, pos, font_size=16, font_family='sans-serif')
    nx.draw_networkx_edges(G, pos, arrows=True)
    labels = nx.get_edge_attributes(G, 'label')

    # Draw the labels for edges
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=16, font_family='sans-serif')

    # Show the graph
    plt.axis('off')
    plt.show()



# Define the DFAs
dfa1 = DFA(
    {'A', 'B'},
    {'a', 'b'},
    {
        'A': {'a': 'B', 'b': 'A'},
        'B': {'a': 'B', 'b': 'B'},
    },
    'A',
    {'B'}
)

dfa2 = DFA(
    {'p', 'q', 'r'},
    {'a', 'b'},
    {
        'p': {'a': 'q', 'b': 'r'},
        'q': {'a': 'q', 'b': 'r'},
        'r': {'a': 'r', 'b': 'r'}
    },
    'p',
    {'q', 'r'}
)


# Get the input for the DFAs
#dfa1 = input_dfa()
#dfa2 = input_dfa()

# Create the main window
# root = tk.Tk()

# Create the DFA input GUI
# dfa_input_gui = DFAInputGUI(root)

# Start the main event loop
# root.mainloop()

# Compute the product of the two DFAs
product_dfa = product(dfa1, dfa2)
#
draw_product_dfa(product_dfa)

# Print the resulting product DFA
print('Product DFA:')
print('-------------')
print('States (Qp):')
print(product_dfa.Q)
print('\nAlphabet (sigmap):')
print(product_dfa.sigma)
print('\nTransition Function (deltap):')
for ((q1, q2), a), p in product_dfa.delta.items():
    print(f'({q1}, {q2}), {a} -> {p}')
print('\nInitial State (q0p):')
print(product_dfa.q0)
print('\nFinal States (Fp):')
print(product_dfa.F)


