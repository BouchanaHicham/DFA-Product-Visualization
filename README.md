# DFA-Product-Visualization

This Python program computes the product automaton of two Deterministic Finite Automata (DFAs). It allows users to input the states, alphabet, transitions, initial state, and final states for both DFAs and generates their product automaton. The resulting automaton is visualized with clear node and edge labels.

## Example


```python
# Define the DFAs
# Define the DFA 1
dfa1 = DFA(
    states={'A', 'B'},                 # Set of states in DFA 1
    alphabet={'a', 'b'},               # Alphabet in DFA 1
    delta={
        'A': {'a': 'B', 'b': 'A'},     # Transition function for each state and input symbol in DFA 1
        'B': {'a': 'B', 'b': 'B'},
    },
    q0='A',                           # Initial state in DFA 1
    F={'B'}                           # Set of final states in DFA 1
)

# Define the DFA 2
dfa2 = DFA(
    states={'p', 'q', 'r'},           # Set of states in DFA 2
    alphabet={'a', 'b'},              # Alphabet in DFA 2
    delta={
        'p': {'a': 'q', 'b': 'r'},    # Transition function for each state and input symbol in DFA 2
        'q': {'a': 'q', 'b': 'r'},
        'r': {'a': 'r', 'b': 'r'},
    },
    q0='p',                          # Initial state in DFA 2
    F={'q', 'r'}                     # Set of final states in DFA 2
)

)
```
![Product DFA Example](https://github.com/BouchanaHicham/DFA-Product-Visualization/blob/main/DFA_Visualization_Example.png)

### Output
```python
Product DFA:
-------------
States (Qp):
{('B', 'q'), ('B', 'r'), ('A', 'r'), ('A', 'q'), ('B', 'p'), ('A', 'p')}

Alphabet (sigmap):
{'a', 'b'}

Transition Function (deltap):
(B, q), a -> ('B', 'q')
(B, q), b -> ('B', 'r')
(B, r), a -> ('B', 'r')
(B, r), b -> ('B', 'r')
(A, r), a -> ('B', 'r')
(A, r), b -> ('A', 'r')
(A, q), a -> ('B', 'q')
(A, q), b -> ('A', 'r')
(B, p), a -> ('B', 'q')
(B, p), b -> ('B', 'r')
(A, p), a -> ('B', 'q')
(A, p), b -> ('A', 'r')

Initial State (q0p):
('A', 'p')

Final States (Fp):
{('B', 'q'), ('B', 'r')}
```
## Usage

1. Open the Python script `dfa_product_calculator.py`.
2. Define the two DFAs by specifying their states, alphabet, transitions, initial state, and final states.
3. Run the script and it will compute the product DFA.
4. The product DFA will be visualized with matplotlib and networkx libraries.

## Dependencies

- Python 3.x
- matplotlib
- networkx (Optional)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**Bouchana Hicham**
