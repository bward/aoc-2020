import ast

with open("input/day18.txt") as puzzle_input:
    expressions = puzzle_input.readlines()

class Transformer(ast.NodeTransformer):
    def visit_Sub(self, node):
        return ast.Mult()

    def visit_Div(self, node):
        return ast.Add()
    

def _evaluate_expression(expression):
    tree = ast.parse(f"out={expression}")
    Transformer().visit(tree)

    g = {}
    exec(compile(tree, filename="", mode="exec"), g)

    return g['out']

    
def part_1():
    return sum(_evaluate_expression(e.replace("*", "-")) for e in expressions)

def part_2():
    return sum(_evaluate_expression(e.replace("*", "-").replace("+", "/")) for e in expressions)


if __name__ == "__main__":
    print(part_1())
    print(part_2())

