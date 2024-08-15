# Introduction
The proposal is to develop a Code Analyzer for the Imperative Programming Language (IPL) defined at the beginning of the semester. 
The IPL should allow the declaration of atomic and structured variables (such as sets, lists, tuples, and dictionaries, similar to Python), selection instructions (conditionals), and three types of loops.
In the third assignment, we were tasked with creating Control Flow Graphs (CFG) related to our grammar.

# Grammatic
The grammar includes terminal and non-terminal attributes. 
Initially, the syntactic rules state that the code can be defined by a function or just by lines. 
These lines include different types of instructions, such as assignments, loops, input/output operations, variable creation, and conditionals. 
The data structures created encompass dictionaries, arrays, tuples, and lists.

## Lark

To traverse the grammar that we previously wrote, we used the Interpreter from the Lark module.
To do this, we need to decide how to visit the children of each node. Terminal symbols will be processed in the expressions, so there is no need for a special function for them. Unlike terminal symbols, non-terminal symbols require defining how each expression will traverse its children. 
To visit all the children, we mostly used the self.visit_children function, which visits all the children indiscriminately, as there is no need to process their values. 
However, there are some expressions that require special attention. 
These include expressions related to loop instructions, conditionals, assignments, and input/output operations.

### 2.2 Global Variables

To accomplish the tasks required in this project, we had to define several variables within the class. These variables serve different functions. Some act as counters:

- **"counter_tipo"**: A dictionary that stores the number of variables of each type present in the code being analyzed.
- **"ciclo"**: An integer that indicates the number of loops (while, for, do-while) present in the code being analyzed.
- **"condicional"**: An integer that indicates the number of conditional statements (if, elif, else) present in the code being analyzed.
- **"aninhado"**: An integer that indicates the number of nested if statements present in the code being analyzed.
- **"aninhadoIF"**: An integer that indicates the number of nested if statements present in the code being analyzed.
- **"print"**: An integer that indicates the number of print statements present in the code being analyzed.
- **"input"**: An integer that indicates the number of input operations present in the code being analyzed.

Others function as arrays that store associated values:

- **"funcoes"**: Stores the names of all defined or used functions.
- **"not_defined"**: Stores the names of all variables or functions that were not previously initialized or defined.
- **"repetido"**: Stores the names of all variables that were defined more than once.
- **"mencionado"**: Stores the names of all variables that were used, whether in assignments or function calls, in the code being analyzed.
- **"no_value"**: Stores the names of all variables that were declared but never assigned a value.
- **"variaveisTotais"**: Stores only the names of all variables used in the program.

Some are used as control mechanisms:

- **"variaveis"**: A dictionary where the keys are the levels to which the variables belong. A global variable is stored at level zero, while a variable declared within a for loop will be at level one. Each level will then have a dictionary where the keys are the names of the variables, and their values are the associated value and type. If no value has been assigned, it will be `None`. This is useful for determining whether a variable has already been defined at the level in which we are operating, thus helping to identify cases of redeclaration, non-declaration, and variables used but not initialized.
- **"strut_controlo"**: An array that stores the types of control structures the interpreter encounters as it reads the provided code. When it exits one of these structures, it pops it from the array, enabling the verification of nested control structures.
- **"nivel"**: An integer that indicates the level at which we are currently working.

Some variables were used exclusively for the second phase of the project:

- **"counter"**: Indicates which instruction is being executed at the moment.
- **"temp"**: Stores the value of the counter when there are conditional instructions (such as while and if).
- **"temp_if"**: Stores the current instruction value (self.counter) as the key and the levels in which the instruction is located as the value.
- **"graph"**: The start of the graph that will be created.

