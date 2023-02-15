
from dataclasses import dataclass

class Expression:
    pass

@dataclass
class BinExp(Expression):
    op: str
    left: Expression
    right: Expression
    def __str__(self):
        return "(" + str(self.left) + self.op + str(self.right) + ")"

@dataclass
class Leaf(Expression):
    value: int
    def __str__(self): return str(self.value)

# テスト用の式データ

# 2 * (6 - 2) / 4 = 2
test_exp1: Expression = BinExp('/',
                            BinExp('*', 
                                Leaf(2),
                                BinExp('-', Leaf(6), Leaf(2))),
                            Leaf(4))
# (1 + 2) * (3 + 4) = 21
test_exp2: Expression = BinExp('*', BinExp('+', Leaf(1), Leaf(2)), BinExp('+', Leaf(3), Leaf(4)))