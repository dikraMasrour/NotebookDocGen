import ast


program = """x = 1
def print_x():
    print(x)
    if False: x = 0
print_x()"""
my_tree = ast.parse(program)
print(ast.dump(my_tree))