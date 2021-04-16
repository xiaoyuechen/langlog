# USAGE
# The script takes input from the standard input and outputs to the standard output
# You can pip the input to this script, for example:
# cat example.simple | python3 lexical_analyzer.py
# The script would then print the output to your shell

import sys
import re


class Func:
    def __init__(self):
        self.block = None
        self.name = None
        self.args = []
        self.content = None
        self.variables = []
        self.calls = []
        self.for_loops = []
        self.while_loops = []
        self.ites = []


class ForLoop:
    def __init__(self):
        self.initialization = None
        self.condition = None
        self.iteration = None
        self.content = None

    def print(self):
        print("For loop:")
        print(f"Initialization: {self.initialization}")
        print(f"Condition: {self.condition}")
        print(f"Iteration: {self.iteration}")
        print("Content:")
        print(self.content)


class WhileLoop:
    def __init__(self):
        self.condition = None
        self.content = None

    def print(self):
        print("While loop:")
        print(f"Condition: {self.condition}")
        print("Content:")
        print(self.content)


class IfThenElse:
    def __init__(self):
        self.condition = None
        self.content = None

    def print(self):
        print("If-then-else")
        print(f"Condition: {self.condition}")
        print("Content:")
        print(self.content)


def print_func(func):
    print(f"Function: {func.name}")
    print("Arguments: ", end="")
    for i, arg in enumerate(func.args):
        print(arg, end="")
        if i != len(func.args) - 1:
            print(", ", end="")
    print()
    print("Content:")
    print(func.content)
    print("Variables:")
    for type, name in func.variables:
        print(f"Type, Name: {type}, {name}")
    print("Function calls:")
    for call in func.calls:
        print(call)
    for for_loop in func.for_loops:
        for_loop.print()
    for while_loop in func.while_loops:
        while_loop.print()
    for ite in func.ites:
        ite.print()

    print()


src = sys.stdin.read()

func_blocks = re.split(r"(^\})", src, flags=re.MULTILINE)
funcs = []
for i in range(0, len(func_blocks) - 1, 2):
    func = Func()
    func.block = func_blocks[i] + func_blocks[i + 1]
    funcs.append(func)

for func in funcs:
    def_line = re.search(r"^(void|int|long|char) .*", func.block,
                         re.MULTILINE).group()
    words = re.findall(r"\w+", def_line)
    func.name = words[1]
    args = re.findall(r"((int|long|char) (\w+)(\[\])?)", def_line)
    for arg in args:
        func.args.append(arg[0])
        func.variables.append((arg[1] + arg[3], arg[2]))
    # content
    func.content = re.search(r"^\{.*^\}", func.block,
                             re.DOTALL | re.MULTILINE).group()
    # variables
    var_lines = re.findall(r"((int|long|char) (.*))", func.content)
    for var_line in var_lines:
        variables = re.findall(r"(((int|long|char)|,)\s?(\w+)(\[(\d)\])?)",
                               var_line[0])
        t = var_line[1]
        for var in variables:
            if var[4] != "":
                t = t + "[]"
            name = var[3]
            func.variables.append((t, name))
    # function calls
    calls = re.findall(r"((\w+)(\(.*\)))", func.content)
    for call in calls:
        func.calls.append(call[1])

    #for loops
    for_loop_heads = re.findall(r"(for \(.*?\))\s*?( +?\{.* +\})", func.content,
                                re.DOTALL | re.MULTILINE)
    for head in for_loop_heads:
        for_statement, content = head
        specs = re.findall(r"for \((.*); (.*); (.*)\)", for_statement)[0]

        fl = ForLoop()
        func.for_loops.append(fl)
        fl.initialization = specs[0]
        fl.condition = specs[1]
        fl.iteration = specs[2]
        fl.content = content

#     while_loops = re.findall(r"( *while \(.*\).*\{.* +\})", func.content,
#                              re.DOTALL)
#     for while_loop in while_loops:
#         wl = WhileLoop()
#         func.while_loops.append(wl)
#         head = re.findall(r"while \((.*)\)", while_loop)
#         wl.condition = head[0]
#         wl.content = re.sub(r".*\n", "", while_loop, 1)

    ites = re.findall(r"if \((.*)\).*(\{.*\})", func.content, re.DOTALL)
    for condition, content in ites:
        iteobj = IfThenElse()
        func.ites.append(iteobj)
        iteobj.condition = condition
        iteobj.content = content

for func in funcs:
    print_func(func)
