from exp import *

def step(exp: Expression) -> Expression:
    # 1ステップの遷移を行う
    match exp:
        # expの形によって適用できる規則を判別する
        case BinExp(op, Leaf(l), Leaf(r)):
            # 両辺とも数値
            match op:
                case '+': return Leaf(l + r)
                case '-': return Leaf(l - r)
                case '*': return Leaf(l * r)
                case '/': return Leaf(l // r)
                case _: raise Exception("Unknown op: " + op)
        case BinExp(op, BinExp(_, _, _) as left, right):
            # 左辺が数値でない
            return BinExp(op, step(left), right)
        case BinExp(op, Leaf(_) as left, BinExp(_, _, _) as right):
            # 右辺が数値でない
            return BinExp(op, left, step(right))
        case _: raise Exception("No applicable rule for: " + str(exp))

def rewrite_loop(exp: Expression) -> Leaf:
    # 終了状態(全体が数値)になるまで遷移を繰り返す
    while not isinstance(exp, Leaf):
        print(str(exp) + "->")
        exp = step(exp)
    return exp