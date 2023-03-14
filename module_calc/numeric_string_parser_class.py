from __future__ import division
from .matrix_class import Matrix
import module_calc.calculator_specific_functions as csf
import functools
import numpy as np
from scipy import linalg
import sympy as sp
sp.init_printing(use_unicode=True)
from pyparsing import (Literal, CaselessLiteral, Word, Combine, Group, Optional,
                       ZeroOrMore, Forward, nums, alphas, oneOf)
import math
import operator

class NumericStringParser:
    '''
    This parser is based on the parser created by Paul McGuire
    version = $Revision: 0.0 $
    date = $Date: 2009-03-20 $
    source= http://pyparsing.wikispaces.com/file/view/fourFn.py
    http://pyparsing.wikispaces.com/message/view/home/15549426

    Most of this code comes from the fourFn.py pyparsing example

    It's been modified to be used with the classes and functions in this project

    '''

    def push_first(self, strg, loc, toks):
        self.expr_stack.append(toks[0])

    def push_u_minus(self, strg, loc, toks):
        if toks and toks[0] == '-':
            self.expr_stack.append('unary -')

    def __init__(self,*args):
        """
        expop   :: '^'
        multop  :: '*' | '/'
        addop   :: '+' | '-'
        integer :: ['+' | '-'] '0'..'9'+
        atom    :: π | ℇ | real | fn '(' expr ')' | '(' expr ')'
        factor  :: atom [ expop factor ]*
        term    :: factor [ multop factor ]*
        expr    :: term [ addop term ]*
        """
        self.previous_answer = None
        point = Literal(".")
        e = CaselessLiteral("ℇ")
        fnumber = Combine(Word("+-" + nums, nums) +
                          Optional(point + Optional(Word(nums))) +
                          Optional(e + Word("+-" + nums, nums)))
        ident = Word(alphas, alphas + nums + "_$")
        plus = Literal("+")
        minus = Literal("-")
        mult = Literal("*")
        div = Literal("/")
        dotprod=Literal("@")
        crossprod=Literal("&")
        lpar = Literal("(").suppress()
        rpar = Literal(")").suppress()
        addop = plus | minus
        multop = mult | div | dotprod | crossprod
        expop = Literal("^")
        pi = CaselessLiteral("π")
        ans = CaselessLiteral("Ans")

        list_of_string_literals = []
        for arg in args:
            for arg_key in reversed(arg.keys()):
                list_of_string_literals.append(CaselessLiteral(arg_key))


        expr = Forward()
        atom = ((Optional(oneOf("- +")) +
                (ident + lpar + expr + rpar | pi | e | fnumber | ans | 
                functools.reduce(lambda x, y: x | y, list_of_string_literals) 
                ).setParseAction(self.push_first))
                | Optional(oneOf("- +")) + Group(lpar + expr + rpar)
                ).setParseAction(self.push_u_minus)
        # by defining exponentiation as "atom [ ^ factor ]..." instead of
        # "atom [ ^ atom ]...", we get right-to-left exponents, instead of left-to-right
        # that is, 2^3^2 = 2^(3^2), not (2^3)^2.
        factor = Forward()
        factor << atom + \
            ZeroOrMore((expop + factor).setParseAction(self.push_first))
        term = factor + \
            ZeroOrMore((multop + factor).setParseAction(self.push_first))
        expr << term + \
            ZeroOrMore((addop + term).setParseAction(self.push_first))
        # addop_term = ( addop + term ).setParseAction( self.push_first )
        # general_term = term + ZeroOrMore( addop_term ) | OneOrMore( addop_term)
        # expr <<  general_term
        self.bnf = expr
        # map operator symbols to corresponding arithmetic operations
        epsilon = 1e-12
        self.opn = {"+": operator.add,
                    "-": operator.sub,
                    "*": operator.mul,
                    "/": operator.truediv,
                    "^": operator.pow,
                    "@": operator.matmul,
                    "&": operator.and_}
        self.fn = {"sin":       csf.sin,
                   "arcsin":    csf.arcsin,
                   "cos":       csf.cos,
                   "arccos":    csf.arccos,
                   "tan":       csf.tan,
                   "arctan":    csf.arctan,
                   "sinh":      csf.sinh,
                   "arcsinh":   csf.arcsinh,
                   "cosh":      csf.cosh,
                   "arccosh":   csf.arccosh,
                   "tanh":      csf.tanh,
                   "arctanh":   csf.arctanh,
                   "Log":       csf.logarithm_base_ten,
                   "absolute":  csf.absolute,
                   "In":        csf.logarithm_base_e,
                   "norm":      csf.norm,
                   "det":       csf.det,
                   "tr":        csf.tr,
                   "root":      csf.root,
                   "exp":       math.exp,
                   "abs":       abs,
                   "trunc":     lambda a: int(a),
                   "round":     round,
                   "sgn":       lambda a: abs(a) > epsilon and cmp(a, 0) or 0}
        self.obj_var = {"π":    np.pi,
                        "ℇ":    np.e,}
        self.obj_var.update({k:v for d in (args) for k,v in d.items()})

    def evaluate_stack(self, s):
        op = s.pop()
        if op == 'unary -':
            return -self.evaluate_stack(s)
        if op in "+-*/^@&":
            op2 = self.evaluate_stack(s)
            op1 = self.evaluate_stack(s)
            return self.opn[op](op1, op2)
        elif op in self.obj_var:
            return self.obj_var[op]
        elif op == "Ans":  
            return self.previous_answer
        elif op in self.fn:
            return self.fn[op](self.evaluate_stack(s))
        elif op[0].isalpha():
            return 0
        else:
            return float(op)

    def parse(self, num_string, parseAll=True, update_previous_answer=False):
        self.expr_stack = []
        results = self.bnf.parseString(num_string, parseAll)
        val = self.evaluate_stack(self.expr_stack[:])
        if update_previous_answer: 
            self.previous_answer = val
        return val

