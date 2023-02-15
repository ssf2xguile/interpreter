from exp import *

def evaluate(exp: Expression) -> Leaf:
    match exp:
        case BinExp(op, left, right):
            l = evaluate(left).value
            r = evaluate(right).value
            match op:
                case '+': return Leaf(l + r)
                case '-': return Leaf(l - r)
                case '*': return Leaf(l * r)
                case '/': return Leaf(l // r)
                case _: raise Exception("Unknown op: " + op)
        case Leaf(value): return exp
        case _: raise Exception("Unknown expression: " + str(exp))

print(evaluate(test_exp1))