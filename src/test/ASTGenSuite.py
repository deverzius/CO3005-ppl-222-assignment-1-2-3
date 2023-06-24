import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
	#1
    def test_vardecl(self):
        input = """ x,y,z: integer; """
        expect = """Program([
	VarDecl(x, IntegerType)
	VarDecl(y, IntegerType)
	VarDecl(z, IntegerType)
])"""
        self.assertTrue(TestAST.test(input, expect, 301))
    
    #2
    def test_vardecl_2(self):
        input = """ 
            x,y,z: boolean;
            x,y,z: float;
            x,y,z: string;
        """
        expect = """Program([
	VarDecl(x, BooleanType)
	VarDecl(y, BooleanType)
	VarDecl(z, BooleanType)
	VarDecl(x, FloatType)
	VarDecl(y, FloatType)
	VarDecl(z, FloatType)
	VarDecl(x, StringType)
	VarDecl(y, StringType)
	VarDecl(z, StringType)
])"""
        self.assertTrue(TestAST.test(input, expect, 302))
        
    #3
    def test_vardecl_3(self):
        input = """ x,y,z: integer = 1,2,"the goat \\r"; """
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, StringLit(the goat \\r))
])"""
        self.assertTrue(TestAST.test(input, expect, 303))
        
    #4
    def test_vardecl_4(self):
        input = """ x: integer = 2 + -!i[2] :: x + 90 * y; """
        expect = """Program([
	VarDecl(x, IntegerType, BinExpr(::, BinExpr(+, IntegerLit(2), UnExpr(-, UnExpr(!, ArrayCell(i, [IntegerLit(2)])))), BinExpr(+, Id(x), BinExpr(*, IntegerLit(90), Id(y)))))
])"""
        self.assertTrue(TestAST.test(input, expect, 304))
        
    #5
    def test_vardecl_5(self):
        input = """ x: float = 7 + !-8; """
        expect = """Program([
	VarDecl(x, FloatType, BinExpr(+, IntegerLit(7), UnExpr(!, UnExpr(-, IntegerLit(8)))))
])"""
        self.assertTrue(TestAST.test(input, expect, 305))
    
    #6
    def test_vardecl_6(self):
        input = """a, b, c, d: integer = 3.5e2, 4E-2, 6_990_912, "this is a test \\t \\r \\n \\\\ ";"""
        expect = """Program([
	VarDecl(a, IntegerType, FloatLit(350.0))
	VarDecl(b, IntegerType, FloatLit(0.04))
	VarDecl(c, IntegerType, IntegerLit(6990912))
	VarDecl(d, IntegerType, StringLit(this is a test \\t \\r \\n \\\\ ))
])"""
        self.assertTrue(TestAST.test(input, expect, 306))
    
    #7
    def test_vardecl_7(self):
        input = """ a, b, c: string = "a123", "b123","c332"; """
        expect = """Program([
	VarDecl(a, StringType, StringLit(a123))
	VarDecl(b, StringType, StringLit(b123))
	VarDecl(c, StringType, StringLit(c332))
])"""
        self.assertTrue(TestAST.test(input, expect, 307))
    
    #8
    def test_vardecl_8(self):
        input = """ x: float = 123E20; """
        expect = """Program([
	VarDecl(x, FloatType, FloatLit(1.23e+22))
])"""
        self.assertTrue(TestAST.test(input, expect, 308))
        
    #9
    def test_vardecl_9(self):
        input = """ z: float = 1299002E-90; """
        expect = """Program([
	VarDecl(z, FloatType, FloatLit(1.299002e-84))
])"""
        self.assertTrue(TestAST.test(input, expect, 309))
        
    #10
    def test_vardecl_10(self):
        input = """ t: float = 3288100000000E-90; """
        expect = """Program([
	VarDecl(t, FloatType, FloatLit(3.2881e-78))
])"""
        self.assertTrue(TestAST.test(input, expect, 310))
        
    #11
    def test_fundecl_1(self):
        input = """ 
            print: function void (msg: string) {
                y = 12;
                x: string = "Result: ";
                log(msg);
                return;
            }
        """
        expect = """Program([
	FuncDecl(print, VoidType, [Param(msg, StringType)], None, BlockStmt([AssignStmt(Id(y), IntegerLit(12)), VarDecl(x, StringType, StringLit(Result: )), CallStmt(log, Id(msg)), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 311))
        
    #12
    def test_fundecl_2(self):
        input = """ 
            print: function integer (inherit out msg: string) {
                if (empty(msg) == false)
                    log(msg);
                    return 1;
                return 0;
            }
        """
        expect = """Program([
	FuncDecl(print, IntegerType, [InheritOutParam(msg, StringType)], None, BlockStmt([IfStmt(BinExpr(==, FuncCall(empty, [Id(msg)]), BooleanLit(False)), CallStmt(log, Id(msg))), ReturnStmt(IntegerLit(1)), ReturnStmt(IntegerLit(0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 312))
        
    #13
    def test_fundecl_3(self):
        input = """ 
            print: function integer (inherit out msg: string) {
                cout(msg);
                return 0;
            }
            hasCycle: function boolean (inherit head: integer, inherit headNext: integer) {
                if (!head || !headNext) {
                    return false;
                }
                tortoise: integer = head;
                hare: integer = headNext;

                while (hare && getNext(hare)) {
                    if (tortoise == hare) {
                        return true;
                    }
                    tortoise = getNext(tortoise);
                    hare = getNext(getNext(hare));
                }
                return false;
            }
        """
        expect = """Program([
	FuncDecl(print, IntegerType, [InheritOutParam(msg, StringType)], None, BlockStmt([CallStmt(cout, Id(msg)), ReturnStmt(IntegerLit(0))]))
	FuncDecl(hasCycle, BooleanType, [InheritParam(head, IntegerType), InheritParam(headNext, IntegerType)], None, BlockStmt([IfStmt(BinExpr(||, UnExpr(!, Id(head)), UnExpr(!, Id(headNext))), BlockStmt([ReturnStmt(BooleanLit(False))])), VarDecl(tortoise, IntegerType, Id(head)), VarDecl(hare, IntegerType, Id(headNext)), WhileStmt(BinExpr(&&, Id(hare), FuncCall(getNext, [Id(hare)])), BlockStmt([IfStmt(BinExpr(==, Id(tortoise), Id(hare)), BlockStmt([ReturnStmt(BooleanLit(True))])), AssignStmt(Id(tortoise), FuncCall(getNext, [Id(tortoise)])), AssignStmt(Id(hare), FuncCall(getNext, [FuncCall(getNext, [Id(hare)])]))])), ReturnStmt(BooleanLit(False))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 313))
        
    #14
    def test_fundecl_4(self):
        input = """ 
            print: function integer (inherit out type: integer, x: float) {
                return str(type) + str(x);
            }
            print: function boolean (inherit type: integer, x: float) {
                return str(type) + str(x);
            }
            print: function float (out type: integer, x: float) {
                return str(type) + str(x);
            }
            print: function string (type: integer, x: float) {
                return str(type) + str(x);
            }
            print: function void (type: integer, x: float) {
                return str(type) + str(x);
            }
        """
        expect = """Program([
	FuncDecl(print, IntegerType, [InheritOutParam(type, IntegerType), Param(x, FloatType)], None, BlockStmt([ReturnStmt(BinExpr(+, FuncCall(str, [Id(type)]), FuncCall(str, [Id(x)])))]))
	FuncDecl(print, BooleanType, [InheritParam(type, IntegerType), Param(x, FloatType)], None, BlockStmt([ReturnStmt(BinExpr(+, FuncCall(str, [Id(type)]), FuncCall(str, [Id(x)])))]))
	FuncDecl(print, FloatType, [OutParam(type, IntegerType), Param(x, FloatType)], None, BlockStmt([ReturnStmt(BinExpr(+, FuncCall(str, [Id(type)]), FuncCall(str, [Id(x)])))]))
	FuncDecl(print, StringType, [Param(type, IntegerType), Param(x, FloatType)], None, BlockStmt([ReturnStmt(BinExpr(+, FuncCall(str, [Id(type)]), FuncCall(str, [Id(x)])))]))
	FuncDecl(print, VoidType, [Param(type, IntegerType), Param(x, FloatType)], None, BlockStmt([ReturnStmt(BinExpr(+, FuncCall(str, [Id(type)]), FuncCall(str, [Id(x)])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 314))
        
    #15
    def test_fundecl_5(self):
        input = """ 
            print: function integer (inherit msg: string, out type: integer, x: float) {
                return msg + str(type) + str(x);
            }
        """
        expect = """Program([
	FuncDecl(print, IntegerType, [InheritParam(msg, StringType), OutParam(type, IntegerType), Param(x, FloatType)], None, BlockStmt([ReturnStmt(BinExpr(+, BinExpr(+, Id(msg), FuncCall(str, [Id(type)])), FuncCall(str, [Id(x)])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 315))
        
    #16
    def test_fundecl_6(self):
        input = """ 
            f1: function integer (inherit msg: string, out type: boolean, x: float) {
                return msg + str(type) + str(x);
            }
            f2: function void (inherit msg: string, inherit out type: array[2] of integer, out x: float) {
                return msg + str(type) + str(x) + .e1;
            }
        """
        expect = """Program([
	FuncDecl(f1, IntegerType, [InheritParam(msg, StringType), OutParam(type, BooleanType), Param(x, FloatType)], None, BlockStmt([ReturnStmt(BinExpr(+, BinExpr(+, Id(msg), FuncCall(str, [Id(type)])), FuncCall(str, [Id(x)])))]))
	FuncDecl(f2, VoidType, [InheritParam(msg, StringType), InheritOutParam(type, ArrayType([2], IntegerType)), OutParam(x, FloatType)], None, BlockStmt([ReturnStmt(BinExpr(+, BinExpr(+, BinExpr(+, Id(msg), FuncCall(str, [Id(type)])), FuncCall(str, [Id(x)])), FloatLit(0.0)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 316))
        
    #17
    def test_fundecl_7(self):
        input = """ 
            func: function void (msg: string) {
                x: float = 1e-2;
                x: float = 1.e2;
                x: float = .e-22;
                x: float = .E09;
                x: float = .5e2;
                x: float = 1.5E-2;
            }
        """
        expect = """Program([
	FuncDecl(func, VoidType, [Param(msg, StringType)], None, BlockStmt([VarDecl(x, FloatType, FloatLit(0.01)), VarDecl(x, FloatType, FloatLit(100.0)), VarDecl(x, FloatType, FloatLit(0.0)), VarDecl(x, FloatType, FloatLit(0.0)), VarDecl(x, FloatType, FloatLit(50.0)), VarDecl(x, FloatType, FloatLit(0.015))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 317))
        
    #18
    def test_fundecl_8(self):
        input = """ 
            func: function void (msg: string) {}
        """
        expect = """Program([
	FuncDecl(func, VoidType, [Param(msg, StringType)], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 318))
    
    #19
    def test_expr_1(self):
        input = """ 
            main: function void() {
                y: float = x + 13 / 23;
                x: boolean = (x :: "Hello World") <= __x89 / 78 + 123;
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(y, FloatType, BinExpr(+, Id(x), BinExpr(/, IntegerLit(13), IntegerLit(23)))), VarDecl(x, BooleanType, BinExpr(<=, BinExpr(::, Id(x), StringLit(Hello World)), BinExpr(+, BinExpr(/, Id(__x89), IntegerLit(78)), IntegerLit(123))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 319))
        
    #20
    def test_expr_2(self):
        input = """ 
            main: function void() {
                x: integer;
                y = 5;
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType), AssignStmt(Id(y), IntegerLit(5))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 320))
        
    #21
    def test_expr_3(self):
        input = """ 
            main: function void() {
                x: integer;
                x = (((167 - 89) + 90 * 178 / 54) % 123);
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType), AssignStmt(Id(x), BinExpr(%, BinExpr(+, BinExpr(-, IntegerLit(167), IntegerLit(89)), BinExpr(/, BinExpr(*, IntegerLit(90), IntegerLit(178)), IntegerLit(54))), IntegerLit(123)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 321))
    
    #22
    def test_expr_4(self):
        input = """ 
            main: function void() {
                x: float = ((167E1 - 66.1e4) + 90e-3 * 29.001 % 54.000) || 123.20;
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, FloatType, BinExpr(||, BinExpr(+, BinExpr(-, FloatLit(1670.0), FloatLit(661000.0)), BinExpr(%, BinExpr(*, FloatLit(0.09), FloatLit(29.001)), FloatLit(54.0))), FloatLit(123.2)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 322))
        
    #23
    def test_expr_5(self):
        input = """ 
            check: boolean = true && !(true || (!(false && true)) && false);
        """
        expect = """Program([
	VarDecl(check, BooleanType, BinExpr(&&, BooleanLit(True), UnExpr(!, BinExpr(&&, BinExpr(||, BooleanLit(True), UnExpr(!, BinExpr(&&, BooleanLit(False), BooleanLit(True)))), BooleanLit(False)))))
])"""
        self.assertTrue(TestAST.test(input, expect, 323))
        
    #24
    def test_expr_6(self):
        input = """ 
            main: function void() {
                s1: string = "Hello from ";
                s2: string = "Viet Nam";
                s = s1 :: s2;
                print(s);
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(s1, StringType, StringLit(Hello from )), VarDecl(s2, StringType, StringLit(Viet Nam)), AssignStmt(Id(s), BinExpr(::, Id(s1), Id(s2))), CallStmt(print, Id(s))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 324))
        
    #25
    def test_expr_7(self):
        input = """ 
            main: function void() {
                check1, check2: boolean
                    = 4 - (12 - 65) >= (54 + 90 / 3) % 11, (true == false) != false;
                print(check1 == check2);
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(check1, BooleanType, BinExpr(>=, BinExpr(-, IntegerLit(4), BinExpr(-, IntegerLit(12), IntegerLit(65))), BinExpr(%, BinExpr(+, IntegerLit(54), BinExpr(/, IntegerLit(90), IntegerLit(3))), IntegerLit(11)))), VarDecl(check2, BooleanType, BinExpr(!=, BinExpr(==, BooleanLit(True), BooleanLit(False)), BooleanLit(False))), CallStmt(print, BinExpr(==, Id(check1), Id(check2)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 325))
        
    #26
    def test_arr_1(self):
        input = """ 
            main: function void() {
                arr: array[10] of integer;
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(arr, ArrayType([10], IntegerType))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 326))
        
    #27
    def test_arr_2(self):
        input = """ 
            main: function void() {
                array27: array[4] of float = {1.002, 1e3, 12.567, 9E-0, 10.2, 123_456.9, 2_000.9};
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(array27, ArrayType([4], FloatType), ArrayLit([FloatLit(1.002), FloatLit(1000.0), FloatLit(12.567), FloatLit(9.0), FloatLit(10.2), FloatLit(123456.9), FloatLit(2000.9)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 327))
    
    #28
    def test_arr_3(self):
        input = """ 
            main: function void() {
                arr: array[2, 2] of integer = {{1,3},{3,4}};
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(arr, ArrayType([2, 2], IntegerType), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(3)]), ArrayLit([IntegerLit(3), IntegerLit(4)])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 328))
        
    #29
    def test_arr_4(self):
        input = """ 
            main: function void() {
                arr: array[2, 2] of integer = {{1123,345214},334534};
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(arr, ArrayType([2, 2], IntegerType), ArrayLit([ArrayLit([IntegerLit(1123), IntegerLit(345214)]), IntegerLit(334534)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 329))
        
    #30
    def test_arr_5(self):
        input = """ 
            main: function void() {
                arr: array[3] of integer = {};
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(arr, ArrayType([3], IntegerType), ArrayLit([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 330))
        
    #31
    def test_arr_6(self):
        input = """ 
            main: function void() {
                a1,a2: array[76] of float = {12_542.3,4E-8,1.2}, {43.3e20,12.3,8_990_400.12};
                a1[3] = 129_300;
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a1, ArrayType([76], FloatType), ArrayLit([FloatLit(12542.3), FloatLit(4e-08), FloatLit(1.2)])), VarDecl(a2, ArrayType([76], FloatType), ArrayLit([FloatLit(4.33e+21), FloatLit(12.3), FloatLit(8990400.12)])), AssignStmt(ArrayCell(a1, [IntegerLit(3)]), IntegerLit(129300))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 331))
        
    #32
    def test_arr_7(self):
        input = """ 
            main: function array[200_19] of float() {}
        """
        expect = """Program([
	FuncDecl(main, ArrayType([20019], FloatType), [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 332))
        
    #33
    def test_arr_8(self):
        input = """ 
            main: function void() {
                arr: array[7_854] of integer = {y,z,t};
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(arr, ArrayType([7854], IntegerType), ArrayLit([Id(y), Id(z), Id(t)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 333))
        
    #34
    def test_arr_9(self):
        input = """ 
            main: function void() {
                arr: array[67] of integer = {y + 9,z * 8,t};
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(arr, ArrayType([67], IntegerType), ArrayLit([BinExpr(+, Id(y), IntegerLit(9)), BinExpr(*, Id(z), IntegerLit(8)), Id(t)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 334))
        
    #35
    def test_func_call_1(self):
        input = """ 
            main: function void() {
                foo(x * 8, 90, 89_890.332, "Hello");
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(foo, BinExpr(*, Id(x), IntegerLit(8)), IntegerLit(90), FloatLit(89890.332), StringLit(Hello))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 335))
    
    #36
    def test_stmt_1(self):
        input = """ 
            main: function void() {
                x: integer = foo(x * 8, 90, 89_890.332, "Hello");
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType, FuncCall(foo, [BinExpr(*, Id(x), IntegerLit(8)), IntegerLit(90), FloatLit(89890.332), StringLit(Hello)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 336))
    
    #37
    def test_stmt_2(self):
        input = """ 
            main: function void() {
                x: integer = (foo(x * 8, 90, 89_890.332, "Hello")) * 8 - (foo(x * 18, y / 4));
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType, BinExpr(-, BinExpr(*, FuncCall(foo, [BinExpr(*, Id(x), IntegerLit(8)), IntegerLit(90), FloatLit(89890.332), StringLit(Hello)]), IntegerLit(8)), FuncCall(foo, [BinExpr(*, Id(x), IntegerLit(18)), BinExpr(/, Id(y), IntegerLit(4))])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 337))
    
    #38
    def test_stmt_3(self):
        input = """ 
            main: function auto() {
                if (x == 3) {
                    print("Hello");
                }
            }
        """
        expect = """Program([
	FuncDecl(main, AutoType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(x), IntegerLit(3)), BlockStmt([CallStmt(print, StringLit(Hello))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 338))
        
    #39
    def test_stmt_4(self):
        input = """ 
            main: function auto() {
                if (x == 3) {
                    print("Hello");
                }
                else print("olleH");
            }
        """
        expect = """Program([
	FuncDecl(main, AutoType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(x), IntegerLit(3)), BlockStmt([CallStmt(print, StringLit(Hello))]), CallStmt(print, StringLit(olleH)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 339))
        
    #40
    def test_stmt_5(self):
        input = """ 
            main: function auto() {
                if (x >= 8) {
                    a[20] = 100;
                    print("Hello");
                }
                else print("olleHh dsjakhfjk !!!lsadhkljfdsh");
            }
        """
        expect = """Program([
	FuncDecl(main, AutoType, [], None, BlockStmt([IfStmt(BinExpr(>=, Id(x), IntegerLit(8)), BlockStmt([AssignStmt(ArrayCell(a, [IntegerLit(20)]), IntegerLit(100)), CallStmt(print, StringLit(Hello))]), CallStmt(print, StringLit(olleHh dsjakhfjk !!!lsadhkljfdsh)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 340))
        
    #41
    def test_stmt_6(self):
        input = """ 
            main: function auto() {
                if (x == (8 == 9) && (9 != 10 - 2)) {
                    print("Hello");
                }
                else if (f(x) == 10 && 7 - -8 + 90) {
                    print("olleHvft");
                }
                else {
                    print("olleH");
                }
            }
        """
        expect = """Program([
	FuncDecl(main, AutoType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(x), BinExpr(&&, BinExpr(==, IntegerLit(8), IntegerLit(9)), BinExpr(!=, IntegerLit(9), BinExpr(-, IntegerLit(10), IntegerLit(2))))), BlockStmt([CallStmt(print, StringLit(Hello))]), IfStmt(BinExpr(==, FuncCall(f, [Id(x)]), BinExpr(&&, IntegerLit(10), BinExpr(+, BinExpr(-, IntegerLit(7), UnExpr(-, IntegerLit(8))), IntegerLit(90)))), BlockStmt([CallStmt(print, StringLit(olleHvft))]), BlockStmt([CallStmt(print, StringLit(olleH))])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 341))
        
    #42
    def test_stmt_7(self):
        input = """ 
            main: function float() {
                if (x + (true == "Hel world") && (9 != 10 - 2)) {
                    print("Hello");
                }
                else if (x == 3) {
                    print("olleH");
                }
                else print ("Else statement is executed");
            }
        """
        expect = """Program([
	FuncDecl(main, FloatType, [], None, BlockStmt([IfStmt(BinExpr(&&, BinExpr(+, Id(x), BinExpr(==, BooleanLit(True), StringLit(Hel world))), BinExpr(!=, IntegerLit(9), BinExpr(-, IntegerLit(10), IntegerLit(2)))), BlockStmt([CallStmt(print, StringLit(Hello))]), IfStmt(BinExpr(==, Id(x), IntegerLit(3)), BlockStmt([CallStmt(print, StringLit(olleH))]), CallStmt(print, StringLit(Else statement is executed))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 342))
    
    #43
    def test_stmt_8(self):
        input = """ 
            getMonth: function string(x: integer) {
                if (x == 1 % 5) {
                    return "January";
                }
                else if (x == 12 * 8.6 - 10 / 5_0_9_8 * 2_0 * 2.5) {
                    return "February";
                }
                else if (x == 3 || 8 :: "hello") {
                    return "March";
                }
                else if (x == (4) - ((988-m) / 9) / so_9xss ) {
                    return "April";
                }
                else if (x == 5 + (__90 / 87) + (4_0) - o) {
                    return "May";
                }
                return x :: ("u" :: 9) - 90 * __iox9;
            }
            
            main: function void() {
                x: integer = 13 / 6 - 4;
                print(getMonth(x));
            }
        """
        expect = """Program([
	FuncDecl(getMonth, StringType, [Param(x, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(x), BinExpr(%, IntegerLit(1), IntegerLit(5))), BlockStmt([ReturnStmt(StringLit(January))]), IfStmt(BinExpr(==, Id(x), BinExpr(-, BinExpr(*, IntegerLit(12), FloatLit(8.6)), BinExpr(*, BinExpr(*, BinExpr(/, IntegerLit(10), IntegerLit(5098)), IntegerLit(20)), FloatLit(2.5)))), BlockStmt([ReturnStmt(StringLit(February))]), IfStmt(BinExpr(::, BinExpr(==, Id(x), BinExpr(||, IntegerLit(3), IntegerLit(8))), StringLit(hello)), BlockStmt([ReturnStmt(StringLit(March))]), IfStmt(BinExpr(==, Id(x), BinExpr(-, IntegerLit(4), BinExpr(/, BinExpr(/, BinExpr(-, IntegerLit(988), Id(m)), IntegerLit(9)), Id(so_9xss)))), BlockStmt([ReturnStmt(StringLit(April))]), IfStmt(BinExpr(==, Id(x), BinExpr(-, BinExpr(+, BinExpr(+, IntegerLit(5), BinExpr(/, Id(__90), IntegerLit(87))), IntegerLit(40)), Id(o))), BlockStmt([ReturnStmt(StringLit(May))])))))), ReturnStmt(BinExpr(::, Id(x), BinExpr(-, BinExpr(::, StringLit(u), IntegerLit(9)), BinExpr(*, IntegerLit(90), Id(__iox9)))))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType, BinExpr(-, BinExpr(/, IntegerLit(13), IntegerLit(6)), IntegerLit(4))), CallStmt(print, FuncCall(getMonth, [Id(x)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 343))
    
    #44
    def test_stmt_9(self):
        input = """ 
            main: function float() {
                if ((x == (true == "Hel world")) || !(x >= y) && (y > z)) {
                    print("Hello");
                }
                else if (x == 3) {
                    print("olleH 3");
                }
                else if (x == 4) {
                    print("olleH 4");
                }
                else if (x == 5) {
                    print("olleH 5");
                }
                else if (x == 6) {
                    print("olleH 6");
                }
                else print ("Else statement is executed");
            }
        """
        expect = """Program([
	FuncDecl(main, FloatType, [], None, BlockStmt([IfStmt(BinExpr(&&, BinExpr(||, BinExpr(==, Id(x), BinExpr(==, BooleanLit(True), StringLit(Hel world))), UnExpr(!, BinExpr(>=, Id(x), Id(y)))), BinExpr(>, Id(y), Id(z))), BlockStmt([CallStmt(print, StringLit(Hello))]), IfStmt(BinExpr(==, Id(x), IntegerLit(3)), BlockStmt([CallStmt(print, StringLit(olleH 3))]), IfStmt(BinExpr(==, Id(x), IntegerLit(4)), BlockStmt([CallStmt(print, StringLit(olleH 4))]), IfStmt(BinExpr(==, Id(x), IntegerLit(5)), BlockStmt([CallStmt(print, StringLit(olleH 5))]), IfStmt(BinExpr(==, Id(x), IntegerLit(6)), BlockStmt([CallStmt(print, StringLit(olleH 6))]), CallStmt(print, StringLit(Else statement is executed)))))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 344))
        
    #45
    def test_stmt_10(self):
        input = """ 
            main: function float() {
                if ((true == "Hel world") || !(x >= y) && y + z) {
                    print("Hello");
                    x: integer = 12;
                    y: array[1] of string;
                }
                else if (x == 3) {
                    print("olleH 3");
                    x: integer = 12;
                }
                else if (x == 4) {
                    print("olleH 4");
                    x: integer = 12;
                }
                else if (x == 5) {
                    print("olleH 5");
                    y: array[2,3,4,1] of string;
                }
                else if (x == 6) {
                    print("olleH 6");
                    y: array[213] of string;
                }
                else print ("Else statement is executed");
                
                y: array[19] of string;
            }
        """
        expect = """Program([
	FuncDecl(main, FloatType, [], None, BlockStmt([IfStmt(BinExpr(&&, BinExpr(||, BinExpr(==, BooleanLit(True), StringLit(Hel world)), UnExpr(!, BinExpr(>=, Id(x), Id(y)))), BinExpr(+, Id(y), Id(z))), BlockStmt([CallStmt(print, StringLit(Hello)), VarDecl(x, IntegerType, IntegerLit(12)), VarDecl(y, ArrayType([1], StringType))]), IfStmt(BinExpr(==, Id(x), IntegerLit(3)), BlockStmt([CallStmt(print, StringLit(olleH 3)), VarDecl(x, IntegerType, IntegerLit(12))]), IfStmt(BinExpr(==, Id(x), IntegerLit(4)), BlockStmt([CallStmt(print, StringLit(olleH 4)), VarDecl(x, IntegerType, IntegerLit(12))]), IfStmt(BinExpr(==, Id(x), IntegerLit(5)), BlockStmt([CallStmt(print, StringLit(olleH 5)), VarDecl(y, ArrayType([2, 3, 4, 1], StringType))]), IfStmt(BinExpr(==, Id(x), IntegerLit(6)), BlockStmt([CallStmt(print, StringLit(olleH 6)), VarDecl(y, ArrayType([213], StringType))]), CallStmt(print, StringLit(Else statement is executed))))))), VarDecl(y, ArrayType([19], StringType))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 345))
    
    #46
    def test_stmt_11(self):
        input = """ 
            main: function float() {
                if (!!!!!(true == "Hel world") || !(x >= y) && (!!!y <= !z)) {
                    print("Hello");
                    x: integer = 12;
    
                    if (y == 90 && uy || z) {
                        foo("string",23);
                        yu: string = "Met moi qua tr";
                        yu = yu :: s;
                    }
                }
                else if (x == 3) {
                    print("olleH 3");
                    x: integer = 12;
                }
                else print ("Else statement is executed");
            }
        """
        expect = """Program([
	FuncDecl(main, FloatType, [], None, BlockStmt([IfStmt(BinExpr(&&, BinExpr(||, UnExpr(!, UnExpr(!, UnExpr(!, UnExpr(!, UnExpr(!, BinExpr(==, BooleanLit(True), StringLit(Hel world))))))), UnExpr(!, BinExpr(>=, Id(x), Id(y)))), BinExpr(<=, UnExpr(!, UnExpr(!, UnExpr(!, Id(y)))), UnExpr(!, Id(z)))), BlockStmt([CallStmt(print, StringLit(Hello)), VarDecl(x, IntegerType, IntegerLit(12)), IfStmt(BinExpr(==, Id(y), BinExpr(||, BinExpr(&&, IntegerLit(90), Id(uy)), Id(z))), BlockStmt([CallStmt(foo, StringLit(string), IntegerLit(23)), VarDecl(yu, StringType, StringLit(Met moi qua tr)), AssignStmt(Id(yu), BinExpr(::, Id(yu), Id(s)))]))]), IfStmt(BinExpr(==, Id(x), IntegerLit(3)), BlockStmt([CallStmt(print, StringLit(olleH 3)), VarDecl(x, IntegerType, IntegerLit(12))]), CallStmt(print, StringLit(Else statement is executed))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 346))
    
    #47
    def test_stmt_12(self):
        input = """ 
            main: function float() {
                if (x == 3) {
                    print("olleH 3");
                    x: integer = 12;
                }
                else if (true) print ("Else if statement is executed");
                else print ("Else statement is executed");
            }
            main: function float() {
                if (x == 3) {
                    print("olleH 3");
                    x: integer = 12;
                }
                else if (true) print ("Else if statement is executed");
                else print ("Else statement is executed");
            }
        """
        expect = """Program([
	FuncDecl(main, FloatType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(x), IntegerLit(3)), BlockStmt([CallStmt(print, StringLit(olleH 3)), VarDecl(x, IntegerType, IntegerLit(12))]), IfStmt(BooleanLit(True), CallStmt(print, StringLit(Else if statement is executed)), CallStmt(print, StringLit(Else statement is executed))))]))
	FuncDecl(main, FloatType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(x), IntegerLit(3)), BlockStmt([CallStmt(print, StringLit(olleH 3)), VarDecl(x, IntegerType, IntegerLit(12))]), IfStmt(BooleanLit(True), CallStmt(print, StringLit(Else if statement is executed)), CallStmt(print, StringLit(Else statement is executed))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 347))
    
    #48
    def test_stmt_13(self):
        input = """ 
        main: function boolean() {
            if (x == 3) {
                log("x == 3");
                x: integer = 12;
                while (yyy != true - false) {
                    x = x + 1;
                    y: boolean = true / 123_900;
                    break;
                }
                return false;
            }
            else print ("pjhalksdf____hkjalshdf");
            return true;
        }
        """
        expect = """Program([
	FuncDecl(main, BooleanType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(x), IntegerLit(3)), BlockStmt([CallStmt(log, StringLit(x == 3)), VarDecl(x, IntegerType, IntegerLit(12)), WhileStmt(BinExpr(!=, Id(yyy), BinExpr(-, BooleanLit(True), BooleanLit(False))), BlockStmt([AssignStmt(Id(x), BinExpr(+, Id(x), IntegerLit(1))), VarDecl(y, BooleanType, BinExpr(/, BooleanLit(True), IntegerLit(123900))), BreakStmt()])), ReturnStmt(BooleanLit(False))]), CallStmt(print, StringLit(pjhalksdf____hkjalshdf))), ReturnStmt(BooleanLit(True))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 348))
    
    
    #49
    def test_stmt_14(self):
        input = """ 
            main: function float() {
                for (i = 0, i < 10, i + 1) {
                    print(i);
                }
            }
        """
        expect = """Program([
	FuncDecl(main, FloatType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(print, Id(i))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 349))
    
    #50
    def test_stmt_15(self):
        input = """ 
            main: function void() {
                for (i = 0, i < 10 * 8 - 0 / 2 + "huhuuuuhihi" && "hihi:::", i + 1)
                    print(i);
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), BinExpr(&&, BinExpr(+, BinExpr(-, BinExpr(*, IntegerLit(10), IntegerLit(8)), BinExpr(/, IntegerLit(0), IntegerLit(2))), StringLit(huhuuuuhihi)), StringLit(hihi:::))), BinExpr(+, Id(i), IntegerLit(1)), CallStmt(print, Id(i)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 350))
    
    #51
    def test_stmt_16(self):
        input = """ 
            main: function float() {
                for (j = 0, i < (80 :: "alpha beta gamma"), i + 3 / 1) {
                    print(i);
                    x = 90 - fun(30);
                    y = y + 1;
                }
            }
        """
        expect = """Program([
	FuncDecl(main, FloatType, [], None, BlockStmt([ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(i), BinExpr(::, IntegerLit(80), StringLit(alpha beta gamma))), BinExpr(+, Id(i), BinExpr(/, IntegerLit(3), IntegerLit(1))), BlockStmt([CallStmt(print, Id(i)), AssignStmt(Id(x), BinExpr(-, IntegerLit(90), FuncCall(fun, [IntegerLit(30)]))), AssignStmt(Id(y), BinExpr(+, Id(y), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 351))
    
    #52
    def test_stmt_17(self):
        input = """ 
            main: function float() {
                for (i = -20_34_3.908, i < 17_000, i * 8.0000 + 10.00300) {
                    print(i);
                }
            }
        """
        expect = """Program([
	FuncDecl(main, FloatType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), UnExpr(-, FloatLit(20343.908))), BinExpr(<, Id(i), IntegerLit(17000)), BinExpr(+, BinExpr(*, Id(i), FloatLit(8.0)), FloatLit(10.003)), BlockStmt([CallStmt(print, Id(i))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 352))
    
    #53
    def test_stmt_18(self):
        input = """ 
            main: function void() {
                for (i = (87 - 90) / 3 + (1 % 20) - 8, i < 100, i * 2) {
                    print(i);
                }
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), BinExpr(-, BinExpr(+, BinExpr(/, BinExpr(-, IntegerLit(87), IntegerLit(90)), IntegerLit(3)), BinExpr(%, IntegerLit(1), IntegerLit(20))), IntegerLit(8))), BinExpr(<, Id(i), IntegerLit(100)), BinExpr(*, Id(i), IntegerLit(2)), BlockStmt([CallStmt(print, Id(i))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 353))
    
    #54
    def test_stmt_19(self):
        input = """ 
            main: function void() {
                for (i = false && (true || false) && foo(1,2,3,4), i != true, !i) {
                    print(i);
                }
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), BinExpr(&&, BinExpr(&&, BooleanLit(False), BinExpr(||, BooleanLit(True), BooleanLit(False))), FuncCall(foo, [IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4)]))), BinExpr(!=, Id(i), BooleanLit(True)), UnExpr(!, Id(i)), BlockStmt([CallStmt(print, Id(i))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 354))
    
    #55
    def test_stmt_20(self):
        input = """ 
            main: function void() {
                for (x = foo(90 / 4) % 100 && false , x / y == 9 - 100 + a99 + ____6 <= 10, x + 0-9 + -1000 + 20) {
                    print(ippp);
                }
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(x), BinExpr(&&, BinExpr(%, FuncCall(foo, [BinExpr(/, IntegerLit(90), IntegerLit(4))]), IntegerLit(100)), BooleanLit(False))), BinExpr(<=, BinExpr(==, BinExpr(/, Id(x), Id(y)), BinExpr(+, BinExpr(+, BinExpr(-, IntegerLit(9), IntegerLit(100)), Id(a99)), Id(____6))), IntegerLit(10)), BinExpr(+, BinExpr(+, BinExpr(-, BinExpr(+, Id(x), IntegerLit(0)), IntegerLit(9)), UnExpr(-, IntegerLit(1000))), IntegerLit(20)), BlockStmt([CallStmt(print, Id(ippp))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 355))
    
    #56
    def test_stmt_21(self):
        input = """ 
            main: function void() {
                return 0;
                while(true && false) {
                    print("Hello1");
                    while(false) {
                        print("Hello2");
                            while(__u7A12) {
                                print("Hello3");
                            }
                    }
                    while(x == 90 + 8 > 65) {
                        print("Hello4");
                    }
                }
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ReturnStmt(IntegerLit(0)), WhileStmt(BinExpr(&&, BooleanLit(True), BooleanLit(False)), BlockStmt([CallStmt(print, StringLit(Hello1)), WhileStmt(BooleanLit(False), BlockStmt([CallStmt(print, StringLit(Hello2)), WhileStmt(Id(__u7A12), BlockStmt([CallStmt(print, StringLit(Hello3))]))])), WhileStmt(BinExpr(>, BinExpr(==, Id(x), BinExpr(+, IntegerLit(90), IntegerLit(8))), IntegerLit(65)), BlockStmt([CallStmt(print, StringLit(Hello4))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 356))
        
    
    #57
    def test_stmt_22(self):
        input = """ 
            main: function void() {
                while(true) {
                    print("Hello");
                    x: string = ("Hello I " :: "wanna play") :: "a game";
                }
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BooleanLit(True), BlockStmt([CallStmt(print, StringLit(Hello)), VarDecl(x, StringType, BinExpr(::, BinExpr(::, StringLit(Hello I ), StringLit(wanna play)), StringLit(a game)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 357))
    
    #58
    def test_stmt_23(self):
        input = """ 
            main: function void() {
                while(true)
                    print("Hello");
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BooleanLit(True), CallStmt(print, StringLit(Hello)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 358))
    
    #59
    def test_stmt_24(self):
        input = """ 
            main: function void() {
                while(true) {
                    print("Hello");
                    sum: integer = func(2,3);
                }
            }
            
            func: function integer(a:integer, b:integer) {
                return a + b;
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BooleanLit(True), BlockStmt([CallStmt(print, StringLit(Hello)), VarDecl(sum, IntegerType, FuncCall(func, [IntegerLit(2), IntegerLit(3)]))]))]))
	FuncDecl(func, IntegerType, [Param(a, IntegerType), Param(b, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(+, Id(a), Id(b)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 359))
    
    #60
    def test_stmt_25(self):
        input = """ 
            main: function void() {
                while(true) {
                    print("Hello");}
                    
                    sum: integer = func(2,3);
            }
            
            func: function integer(a:integer, b:integer) {
                return a + b;
            }
            gcd: function integer (a: integer, b: integer)
            {
                if (a == 0)
                    return b;
                return gcd(b % a, a);
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BooleanLit(True), BlockStmt([CallStmt(print, StringLit(Hello))])), VarDecl(sum, IntegerType, FuncCall(func, [IntegerLit(2), IntegerLit(3)]))]))
	FuncDecl(func, IntegerType, [Param(a, IntegerType), Param(b, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(+, Id(a), Id(b)))]))
	FuncDecl(gcd, IntegerType, [Param(a, IntegerType), Param(b, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(0)), ReturnStmt(Id(b))), ReturnStmt(FuncCall(gcd, [BinExpr(%, Id(b), Id(a)), Id(a)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 360))
    
    #61
    def test_stmt_26(self):
        input = """ 
            main: function void() {
                do {
                    print("Hello");
                    sum: integer = func(2,3);
                }
                while (true);
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BooleanLit(True), BlockStmt([CallStmt(print, StringLit(Hello)), VarDecl(sum, IntegerType, FuncCall(func, [IntegerLit(2), IntegerLit(3)]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 361))
    
    #62
    def test_stmt_27(self):
        input = """ 
            main: function void() {
                do {
                    print("Hello \\t");
                    x: float = 1e3;
                }
                while (1.333e2);
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(FloatLit(133.3), BlockStmt([CallStmt(print, StringLit(Hello \\t)), VarDecl(x, FloatType, FloatLit(1000.0))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 362))
    
    #63
    def test_stmt_28(self):
        input = """ 
            main: function void() {
                do {
                    prod: float = mul(8_987, 45.233);
                }
                while (x);
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(Id(x), BlockStmt([VarDecl(prod, FloatType, FuncCall(mul, [IntegerLit(8987), FloatLit(45.233)]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 363))
        
    #64
    def test_stmt_29(self):
        input = """ 
            main: function void() {
                do {
                    prod: float = mul(8_987, 45.2e33);
                    continue;
                    continue;
                    continue;
                    continue;
                    continue;
                    continue;
                }
                while (x);
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(Id(x), BlockStmt([VarDecl(prod, FloatType, FuncCall(mul, [IntegerLit(8987), FloatLit(4.52e+34)])), ContinueStmt(), ContinueStmt(), ContinueStmt(), ContinueStmt(), ContinueStmt(), ContinueStmt()]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 364))
        
    #65
    def test_stmt_30(self):
        input = """ 
            main: function void() {
                do {
                    prod: float = mul(8_987, 45.233);
                    break;
                    break;
                    break;
                    break;
                    break;
                    break;
                }
                while (x);
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(Id(x), BlockStmt([VarDecl(prod, FloatType, FuncCall(mul, [IntegerLit(8987), FloatLit(45.233)])), BreakStmt(), BreakStmt(), BreakStmt(), BreakStmt(), BreakStmt(), BreakStmt()]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 365))
    
    #66
    def test_stmt_31(self):
        input = """ 
            foo: function array[10] of string() {
                break;
                continue;
                break;
                continue;
                while (false)
                    while (false)
                        while (false)
                            return;
            }
        """
        expect = """Program([
	FuncDecl(foo, ArrayType([10], StringType), [], None, BlockStmt([BreakStmt(), ContinueStmt(), BreakStmt(), ContinueStmt(), WhileStmt(BooleanLit(False), WhileStmt(BooleanLit(False), WhileStmt(BooleanLit(False), ReturnStmt())))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 366))
        
    #67
    def test_stmt_32(self):
        input = """ 
            main: function void() {
                foo(1,2,3,4,5);
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(foo, IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 367))
    
    #68
    def test_stmt_33(self):
        input = """ 
            main: function void() {
                foo(2 * x, 7 + y,3 + z, true,"abczys");
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(foo, BinExpr(*, IntegerLit(2), Id(x)), BinExpr(+, IntegerLit(7), Id(y)), BinExpr(+, IntegerLit(3), Id(z)), BooleanLit(True), StringLit(abczys))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 368))
    
    #69
    def test_stmt_34(self):
        input = """ 
            main: function void() {
                foo(2 * x, true, "abczys", foo(5_900, !false, "Hello\\nXin chao"));
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(foo, BinExpr(*, IntegerLit(2), Id(x)), BooleanLit(True), StringLit(abczys), FuncCall(foo, [IntegerLit(5900), UnExpr(!, BooleanLit(False)), StringLit(Hello\\nXin chao)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 369))
    
    #70
    def test_stmt_35(self):
        input = """ 
            main: function void() {
                callFunction();
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(callFunction, )]))
])"""
        self.assertTrue(TestAST.test(input, expect, 370))
    
    #71
    def test_stmt_36(self):
        input = """ 
            main: function void() {
                a, b: string = "abc", "\\t Hello";
                print(a,c,b);
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, StringType, StringLit(abc)), VarDecl(b, StringType, StringLit(\\t Hello)), CallStmt(print, Id(a), Id(c), Id(b))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 371))
    
    #72
    def test_stmt_37(self):
        input = """ 
            main: function void() {
                {
                    {
                        a, b: string = "abc", "\\n Hello";
                        print(a,c,b);
                        a, b: string = "abc", "\\n Hello";
                        print(a,c,b);
                    }
                    a, b: string = "abc", "\\n Hello";
                    print(a,c,b);
                }
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([BlockStmt([BlockStmt([VarDecl(a, StringType, StringLit(abc)), VarDecl(b, StringType, StringLit(\\n Hello)), CallStmt(print, Id(a), Id(c), Id(b)), VarDecl(a, StringType, StringLit(abc)), VarDecl(b, StringType, StringLit(\\n Hello)), CallStmt(print, Id(a), Id(c), Id(b))]), VarDecl(a, StringType, StringLit(abc)), VarDecl(b, StringType, StringLit(\\n Hello)), CallStmt(print, Id(a), Id(c), Id(b))])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 372))
    
    #73
    def test_stmt_38(self):
        input = """ 
            main: function void() {
                {
                    x, y: integer;
                    {
                        a, b: string = "abc", "\\n worldHello";
                        print(a,c,b);
                    }
                }
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([BlockStmt([VarDecl(x, IntegerType), VarDecl(y, IntegerType), BlockStmt([VarDecl(a, StringType, StringLit(abc)), VarDecl(b, StringType, StringLit(\\n worldHello)), CallStmt(print, Id(a), Id(c), Id(b))])])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 373))
    
    #74
    def test_stmt_39(self):
        input = """ 
            main: function void() {
                {
                    x, y: integer;
                    {
                        a, b: string = "abc", "\\n Hello";
                        print(a,c,b);
                    }
                    {
                        z, t: integer;
                        {
                            f, u: integer;
                        }
                    }
                    jkalsdf, asdf: boolean = true, false;
                }
                {{{
                    x = x - 9_000;
                }}}
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([BlockStmt([VarDecl(x, IntegerType), VarDecl(y, IntegerType), BlockStmt([VarDecl(a, StringType, StringLit(abc)), VarDecl(b, StringType, StringLit(\\n Hello)), CallStmt(print, Id(a), Id(c), Id(b))]), BlockStmt([VarDecl(z, IntegerType), VarDecl(t, IntegerType), BlockStmt([VarDecl(f, IntegerType), VarDecl(u, IntegerType)])]), VarDecl(jkalsdf, BooleanType, BooleanLit(True)), VarDecl(asdf, BooleanType, BooleanLit(False))]), BlockStmt([BlockStmt([BlockStmt([AssignStmt(Id(x), BinExpr(-, Id(x), IntegerLit(9000)))])])])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 374))
    
    #75
    def test_stmt_40(self):
        input = """ 
            main: function void() {
                {
                    x, y: integer;
                    {
                        print(a,c,b);
                        {
                            f, u: integer;
                        }
                    }
                    z, t: integer;
                    {
                        {
                            f, u: integer;
                        }
                        {
                            f, u: integer;
                        }
                    }
                }
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([BlockStmt([VarDecl(x, IntegerType), VarDecl(y, IntegerType), BlockStmt([CallStmt(print, Id(a), Id(c), Id(b)), BlockStmt([VarDecl(f, IntegerType), VarDecl(u, IntegerType)])]), VarDecl(z, IntegerType), VarDecl(t, IntegerType), BlockStmt([BlockStmt([VarDecl(f, IntegerType), VarDecl(u, IntegerType)]), BlockStmt([VarDecl(f, IntegerType), VarDecl(u, IntegerType)])])])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 375))
    
    #76
    def test_stmt_41(self):
        input = """ 
            main: function void() {
                while (true) {
                    x: integer = 5;
                    x: integer = 5;
                    while (true) {
                        x: integer = 5;
                        x: integer = 5;
                        while (true) {
                            x: integer = 5;
                            x: integer = 5;
                            break;
                        }   
                        continue;
                    }
                    return;
                }
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BooleanLit(True), BlockStmt([VarDecl(x, IntegerType, IntegerLit(5)), VarDecl(x, IntegerType, IntegerLit(5)), WhileStmt(BooleanLit(True), BlockStmt([VarDecl(x, IntegerType, IntegerLit(5)), VarDecl(x, IntegerType, IntegerLit(5)), WhileStmt(BooleanLit(True), BlockStmt([VarDecl(x, IntegerType, IntegerLit(5)), VarDecl(x, IntegerType, IntegerLit(5)), BreakStmt()])), ContinueStmt()])), ReturnStmt()]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 376))
    
    #77
    def test_cmt_1(self):
        input = """ 
            main: function void() {
                ///* Hello world */ x:integer = 13; */
                // $#$*&^*(&_)__+_()*^^&%$^$&^*
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 377))
    
    #78
    def test_cmt_2(self):
        input = """ 
            // Recursive function to return gcd of a and b in single line
            gcd: function integer   (a: integer, b: integer)
            {
                if (b == 0)
                    return a;
                return gcd(b, a % b);   
            }
            
            main: function void() {
                ///* Hello world */ x:integer = 13; */
                f: float = .e390;
                // $#$*&^*(&_)__+_()*^^&%$^$&^*
            }
        """
        expect = """Program([
	FuncDecl(gcd, IntegerType, [Param(a, IntegerType), Param(b, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(b), IntegerLit(0)), ReturnStmt(Id(a))), ReturnStmt(FuncCall(gcd, [Id(b), BinExpr(%, Id(a), Id(b))]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(f, FloatType, FloatLit(0.0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 378))
    
    #79
    def test_cmt_3(self):
        input = """ 
        // cmt cmt cmt cmt
        /*
            cmt ctm ctm
        */
        main: function void() {
            while (true) {
                // cmt
                while (true) {
                    /*
                        cmt cmt cmt
                    */
                    x: integer = 5;
                    while (true) {
                        x: integer = 5;
                        y: integer = 5;
                        break;
                    }   
                    continue;
                    /*
                        cmt2 cmt2 cmt2
                    */
                }
                return;
                // cmt3 cmt3 cmt3 cmt3
            }
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BooleanLit(True), BlockStmt([WhileStmt(BooleanLit(True), BlockStmt([VarDecl(x, IntegerType, IntegerLit(5)), WhileStmt(BooleanLit(True), BlockStmt([VarDecl(x, IntegerType, IntegerLit(5)), VarDecl(y, IntegerType, IntegerLit(5)), BreakStmt()])), ContinueStmt()])), ReturnStmt()]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 379))

    #80
    def test_cmt_4(self):
        input = """ 
            main: function void() {
                /////
                /* /*
                    $#$*&^*(&_)__+_()*^^&%$^$&^*
                    $#$*&^*(&_)__+_()*^^&%$^$&^*
                */
                /*
                    mon nay co toi 4BTL lan
                    Khong hoc cam thi rang chiu
                */
                /*
                    fun: function integer(out i: integer) {
                        while (i >= 0)
                            if (x == 5)
                                return 5 * (i + 1);
                        
                        return 9 * x + 8 * y;
                    }
                */
                ////
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 380))
    
    #81
    def test_cmt_5(self):
        input = """ 
            main: function void() {
                ///// Toi da rot, ban thi sao
                /* world /* Hello*/
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 381))
    
    #82
    def test_mix_1(self):
        input = """ 
            fun: function integer(out i: integer) {
                while (i >= 0)
                    if (x == 5)
                        return 5 * (i + 1);
                
                return 9 * x + 8 * y;
            }
        
            main: function void() {
                t: integer = 100_000;
                x: float = fun(t);
                print(x);
            }
        """
        expect = """Program([
	FuncDecl(fun, IntegerType, [OutParam(i, IntegerType)], None, BlockStmt([WhileStmt(BinExpr(>=, Id(i), IntegerLit(0)), IfStmt(BinExpr(==, Id(x), IntegerLit(5)), ReturnStmt(BinExpr(*, IntegerLit(5), BinExpr(+, Id(i), IntegerLit(1)))))), ReturnStmt(BinExpr(+, BinExpr(*, IntegerLit(9), Id(x)), BinExpr(*, IntegerLit(8), Id(y))))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(t, IntegerType, IntegerLit(100000)), VarDecl(x, FloatType, FuncCall(fun, [Id(t)])), CallStmt(print, Id(x))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 382))
    
    #83
    def test_mix_2(self):
        input = """ 
            fun: function integer(out i: integer) {
                do {
                    xyz = 0;
                }
                while(x == 3);
                
                return 9 * x + 8 * y;
            }
        
            main: function void() {
                t: integer = 990_000;
                x: float = fun(t);
                print(x);
            }
            
            telmewhy: function void(out i: integer) {
                if (i == 90)
                    return;
                else return 90 / l;
            }
        """
        expect = """Program([
	FuncDecl(fun, IntegerType, [OutParam(i, IntegerType)], None, BlockStmt([DoWhileStmt(BinExpr(==, Id(x), IntegerLit(3)), BlockStmt([AssignStmt(Id(xyz), IntegerLit(0))])), ReturnStmt(BinExpr(+, BinExpr(*, IntegerLit(9), Id(x)), BinExpr(*, IntegerLit(8), Id(y))))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(t, IntegerType, IntegerLit(990000)), VarDecl(x, FloatType, FuncCall(fun, [Id(t)])), CallStmt(print, Id(x))]))
	FuncDecl(telmewhy, VoidType, [OutParam(i, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(i), IntegerLit(90)), ReturnStmt(), ReturnStmt(BinExpr(/, IntegerLit(90), Id(l))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 383))
    
    #84
    def test_mix_3(self):
        input = """ 
            fun: function integer(out i: integer) inherit funParent {
                return 9 * x + 8 * y;
            }
        
            main: function void() {
                t: integer = lp - 8_3.1e1;
                x: float = fun(t);
                print(x);
            }
        """
        expect = """Program([
	FuncDecl(fun, IntegerType, [OutParam(i, IntegerType)], funParent, BlockStmt([ReturnStmt(BinExpr(+, BinExpr(*, IntegerLit(9), Id(x)), BinExpr(*, IntegerLit(8), Id(y))))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(t, IntegerType, BinExpr(-, Id(lp), FloatLit(831.0))), VarDecl(x, FloatType, FuncCall(fun, [Id(t)])), CallStmt(print, Id(x))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 384))
    
    #85
    def test_mix_4(self):
        input = """ 
            fun: function array[5,6] of float (out i: integer) inherit funParent {
                return 9 * x + 8 * y;
            }
        
            main: function void() {
                x,y,z: array[1,2,3] of boolean;
            }
        """
        expect = """Program([
	FuncDecl(fun, ArrayType([5, 6], FloatType), [OutParam(i, IntegerType)], funParent, BlockStmt([ReturnStmt(BinExpr(+, BinExpr(*, IntegerLit(9), Id(x)), BinExpr(*, IntegerLit(8), Id(y))))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, ArrayType([1, 2, 3], BooleanType)), VarDecl(y, ArrayType([1, 2, 3], BooleanType)), VarDecl(z, ArrayType([1, 2, 3], BooleanType))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 385))
    
    #86
    def test_mix_5(self):
        input = """ 
            fun: function array[5,6] of float (out i: integer) inherit funParent {
                return 9 * x + 8 * y;
            }
        
            main: function void() {
                x,y,z: array[1,2,3] of string = "nm,", {{},{}}, {};
            }
        """
        expect = """Program([
	FuncDecl(fun, ArrayType([5, 6], FloatType), [OutParam(i, IntegerType)], funParent, BlockStmt([ReturnStmt(BinExpr(+, BinExpr(*, IntegerLit(9), Id(x)), BinExpr(*, IntegerLit(8), Id(y))))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, ArrayType([1, 2, 3], StringType), StringLit(nm,)), VarDecl(y, ArrayType([1, 2, 3], StringType), ArrayLit([ArrayLit([]), ArrayLit([])])), VarDecl(z, ArrayType([1, 2, 3], StringType), ArrayLit([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 386))

    #87
    def test_mix_6(self):
        input = """ 
            fun: function array[5,6] of float (out i: integer) inherit funParent {
                for (i = 0, i < bool + 123 * 89 - 90, x + bo + _a90 -1) {
					while (x == 0) {
						fx = (90-o) + ((8709 - i) - 9 + u) - (asdnf + jl0);
						fun(fun(fun(func(100))));
					}
					g: boolean = f(90) - 90 + fun(80) || 8 :: "dnasfjkbadslfhgsd";
				}
                
                return 9 * x + 8 * y;
            }
        
            main: function void() {
                x,y,z: array[1,5,6] of boolean;
                fun(sf);
            }
        """
        expect = """Program([
	FuncDecl(fun, ArrayType([5, 6], FloatType), [OutParam(i, IntegerType)], funParent, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), BinExpr(-, BinExpr(+, Id(bool), BinExpr(*, IntegerLit(123), IntegerLit(89))), IntegerLit(90))), BinExpr(-, BinExpr(+, BinExpr(+, Id(x), Id(bo)), Id(_a90)), IntegerLit(1)), BlockStmt([WhileStmt(BinExpr(==, Id(x), IntegerLit(0)), BlockStmt([AssignStmt(Id(fx), BinExpr(-, BinExpr(+, BinExpr(-, IntegerLit(90), Id(o)), BinExpr(+, BinExpr(-, BinExpr(-, IntegerLit(8709), Id(i)), IntegerLit(9)), Id(u))), BinExpr(+, Id(asdnf), Id(jl0)))), CallStmt(fun, FuncCall(fun, [FuncCall(fun, [FuncCall(func, [IntegerLit(100)])])]))])), VarDecl(g, BooleanType, BinExpr(::, BinExpr(||, BinExpr(+, BinExpr(-, FuncCall(f, [IntegerLit(90)]), IntegerLit(90)), FuncCall(fun, [IntegerLit(80)])), IntegerLit(8)), StringLit(dnasfjkbadslfhgsd)))])), ReturnStmt(BinExpr(+, BinExpr(*, IntegerLit(9), Id(x)), BinExpr(*, IntegerLit(8), Id(y))))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, ArrayType([1, 5, 6], BooleanType)), VarDecl(y, ArrayType([1, 5, 6], BooleanType)), VarDecl(z, ArrayType([1, 5, 6], BooleanType)), CallStmt(fun, Id(sf))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 387))
    
    #88
    def test_mix_7(self):
        input = """ 
            fun: function string (out i: integer) inherit funParent {
                for (i = 0, i < bool + 123 * 89 - 90, x + bo + _a90 -1) {
					if (fx == (90-o) + ((8709 - i) - 9 + u) - (asdnf + jl0))
						fun(fun(fun(func(100))));
					else {
						uuu34=fun(g(x), f(x), k(x79823), _89324hkjhfds, kljdsafl) + fun(g(x), f(x), k(x79823), _89324hkjhfds, kljdsafl) * fun(g(x), f(x), k(x79823), _89324hkjhfds, kljdsafl);
					}
				}
                
                return fun(g(x), f(x)) - 90 * k % 2 / fds;
            }
        
            main: function void() {
                x,y,z: array[1,5,6] of boolean;
                fun(sf);
            }
        """
        expect = """Program([
	FuncDecl(fun, StringType, [OutParam(i, IntegerType)], funParent, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), BinExpr(-, BinExpr(+, Id(bool), BinExpr(*, IntegerLit(123), IntegerLit(89))), IntegerLit(90))), BinExpr(-, BinExpr(+, BinExpr(+, Id(x), Id(bo)), Id(_a90)), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, Id(fx), BinExpr(-, BinExpr(+, BinExpr(-, IntegerLit(90), Id(o)), BinExpr(+, BinExpr(-, BinExpr(-, IntegerLit(8709), Id(i)), IntegerLit(9)), Id(u))), BinExpr(+, Id(asdnf), Id(jl0)))), CallStmt(fun, FuncCall(fun, [FuncCall(fun, [FuncCall(func, [IntegerLit(100)])])])), BlockStmt([AssignStmt(Id(uuu34), BinExpr(+, FuncCall(fun, [FuncCall(g, [Id(x)]), FuncCall(f, [Id(x)]), FuncCall(k, [Id(x79823)]), Id(_89324hkjhfds), Id(kljdsafl)]), BinExpr(*, FuncCall(fun, [FuncCall(g, [Id(x)]), FuncCall(f, [Id(x)]), FuncCall(k, [Id(x79823)]), Id(_89324hkjhfds), Id(kljdsafl)]), FuncCall(fun, [FuncCall(g, [Id(x)]), FuncCall(f, [Id(x)]), FuncCall(k, [Id(x79823)]), Id(_89324hkjhfds), Id(kljdsafl)]))))]))])), ReturnStmt(BinExpr(-, FuncCall(fun, [FuncCall(g, [Id(x)]), FuncCall(f, [Id(x)])]), BinExpr(/, BinExpr(%, BinExpr(*, IntegerLit(90), Id(k)), IntegerLit(2)), Id(fds))))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, ArrayType([1, 5, 6], BooleanType)), VarDecl(y, ArrayType([1, 5, 6], BooleanType)), VarDecl(z, ArrayType([1, 5, 6], BooleanType)), CallStmt(fun, Id(sf))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 388))
    
    #89
    def test_mix_8(self):
        input = """ 
			x,y: integer;
			a,b,c: float;
			_f1: function array[1,23,8] of integer(out x: integer, z: array[10] of boolean, jklasd: string) {
				do {
					if (x == 90) {
						x = 0 - 80 + (((das * hj) -dsf) :: "abcxyz");
					}
				}
				while (true != a - 90 + (bjnka / fhg - 23));
			}
			_bakd: string;
			_ds_12: boolean;
            main: function void() {
                _f1(90, {"ds",1,4,{abc,34,"string"}});
            }
            _bakd: string;
            _ds_12: boolean;
        """
        expect = """Program([
	VarDecl(x, IntegerType)
	VarDecl(y, IntegerType)
	VarDecl(a, FloatType)
	VarDecl(b, FloatType)
	VarDecl(c, FloatType)
	FuncDecl(_f1, ArrayType([1, 23, 8], IntegerType), [OutParam(x, IntegerType), Param(z, ArrayType([10], BooleanType)), Param(jklasd, StringType)], None, BlockStmt([DoWhileStmt(BinExpr(!=, BooleanLit(True), BinExpr(+, BinExpr(-, Id(a), IntegerLit(90)), BinExpr(-, BinExpr(/, Id(bjnka), Id(fhg)), IntegerLit(23)))), BlockStmt([IfStmt(BinExpr(==, Id(x), IntegerLit(90)), BlockStmt([AssignStmt(Id(x), BinExpr(+, BinExpr(-, IntegerLit(0), IntegerLit(80)), BinExpr(::, BinExpr(-, BinExpr(*, Id(das), Id(hj)), Id(dsf)), StringLit(abcxyz))))]))]))]))
	VarDecl(_bakd, StringType)
	VarDecl(_ds_12, BooleanType)
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(_f1, IntegerLit(90), ArrayLit([StringLit(ds), IntegerLit(1), IntegerLit(4), ArrayLit([Id(abc), IntegerLit(34), StringLit(string)])]))]))
	VarDecl(_bakd, StringType)
	VarDecl(_ds_12, BooleanType)
])"""
        self.assertTrue(TestAST.test(input, expect, 389))
    
    #90
    def test_mix_9(self):
        input = """ 
			merge: function void (arr: array[100] of integer, left: integer, mid: integer, right: integer)
            {
                subArrayOne: auto = mid - left + 1;
                subArrayTwo: auto = right - mid;
            
                // Create temp arrays
                leftArray: array [100] of integer;
                rightArray: array [100] of integer;
            
                // Copy data to temp arrays leftArray[] and rightArray[]
                for (i = 0, i < subArrayOne, i + 1)
                    leftArray[i] = arr[left + i];
                for (j = 0, j < subArrayTwo, j+1)
                    rightArray[j] = arr[mid + 1 + j];
            
                indexOfSubArrayOne: auto = 0; // Initial index of first sub-array
                indexOfSubArrayTwo: auto = 0; // Initial index of second sub-array
                indexOfMergedArray: integer
                    = left; // Initial index of merged array
            
                // Merge the temp arrays back into array[left..right]
                while ((indexOfSubArrayOne < subArrayOne)
                    && (indexOfSubArrayTwo < subArrayTwo)) {
                    if (leftArray[indexOfSubArrayOne]
                        <= rightArray[indexOfSubArrayTwo]) {
                        arr[indexOfMergedArray]
                            = leftArray[indexOfSubArrayOne];
                        indexOfSubArrayOne = indexOfSubArrayOne + 1;
                    }
                    else {
                        arr[indexOfMergedArray]
                            = rightArray[indexOfSubArrayTwo];
                        indexOfSubArrayTwo = indexOfSubArrayTwo + 1;
                    }
                    indexOfMergedArray = indexOfMergedArray + 1;
                }
                // Copy the remaining elements of
                // left[], if there are any
                while (indexOfSubArrayOne < subArrayOne) {
                    arr[indexOfMergedArray]
                        = leftArray[indexOfSubArrayOne];
                    indexOfSubArrayOne = indexOfSubArrayOne + 1;
                    indexOfMergedArray=indexOfMergedArray + 1;
                }
                // Copy the remaining elements of
                // right[], if there are any
                while (indexOfSubArrayTwo < subArrayTwo) {
                    arr[indexOfMergedArray]
                        = rightArray[indexOfSubArrayTwo];
                    indexOfSubArrayTwo=indexOfSubArrayTwo+1;
                    indexOfMergedArray=indexOfMergedArray+1;
                }
                delete(leftArray);
                delete(rightArray);
            }
        """
        expect = """Program([
	FuncDecl(merge, VoidType, [Param(arr, ArrayType([100], IntegerType)), Param(left, IntegerType), Param(mid, IntegerType), Param(right, IntegerType)], None, BlockStmt([VarDecl(subArrayOne, AutoType, BinExpr(+, BinExpr(-, Id(mid), Id(left)), IntegerLit(1))), VarDecl(subArrayTwo, AutoType, BinExpr(-, Id(right), Id(mid))), VarDecl(leftArray, ArrayType([100], IntegerType)), VarDecl(rightArray, ArrayType([100], IntegerType)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(subArrayOne)), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(ArrayCell(leftArray, [Id(i)]), ArrayCell(arr, [BinExpr(+, Id(left), Id(i))]))), ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), Id(subArrayTwo)), BinExpr(+, Id(j), IntegerLit(1)), AssignStmt(ArrayCell(rightArray, [Id(j)]), ArrayCell(arr, [BinExpr(+, BinExpr(+, Id(mid), IntegerLit(1)), Id(j))]))), VarDecl(indexOfSubArrayOne, AutoType, IntegerLit(0)), VarDecl(indexOfSubArrayTwo, AutoType, IntegerLit(0)), VarDecl(indexOfMergedArray, IntegerType, Id(left)), WhileStmt(BinExpr(&&, BinExpr(<, Id(indexOfSubArrayOne), Id(subArrayOne)), BinExpr(<, Id(indexOfSubArrayTwo), Id(subArrayTwo))), BlockStmt([IfStmt(BinExpr(<=, ArrayCell(leftArray, [Id(indexOfSubArrayOne)]), ArrayCell(rightArray, [Id(indexOfSubArrayTwo)])), BlockStmt([AssignStmt(ArrayCell(arr, [Id(indexOfMergedArray)]), ArrayCell(leftArray, [Id(indexOfSubArrayOne)])), AssignStmt(Id(indexOfSubArrayOne), BinExpr(+, Id(indexOfSubArrayOne), IntegerLit(1)))]), BlockStmt([AssignStmt(ArrayCell(arr, [Id(indexOfMergedArray)]), ArrayCell(rightArray, [Id(indexOfSubArrayTwo)])), AssignStmt(Id(indexOfSubArrayTwo), BinExpr(+, Id(indexOfSubArrayTwo), IntegerLit(1)))])), AssignStmt(Id(indexOfMergedArray), BinExpr(+, Id(indexOfMergedArray), IntegerLit(1)))])), WhileStmt(BinExpr(<, Id(indexOfSubArrayOne), Id(subArrayOne)), BlockStmt([AssignStmt(ArrayCell(arr, [Id(indexOfMergedArray)]), ArrayCell(leftArray, [Id(indexOfSubArrayOne)])), AssignStmt(Id(indexOfSubArrayOne), BinExpr(+, Id(indexOfSubArrayOne), IntegerLit(1))), AssignStmt(Id(indexOfMergedArray), BinExpr(+, Id(indexOfMergedArray), IntegerLit(1)))])), WhileStmt(BinExpr(<, Id(indexOfSubArrayTwo), Id(subArrayTwo)), BlockStmt([AssignStmt(ArrayCell(arr, [Id(indexOfMergedArray)]), ArrayCell(rightArray, [Id(indexOfSubArrayTwo)])), AssignStmt(Id(indexOfSubArrayTwo), BinExpr(+, Id(indexOfSubArrayTwo), IntegerLit(1))), AssignStmt(Id(indexOfMergedArray), BinExpr(+, Id(indexOfMergedArray), IntegerLit(1)))])), CallStmt(delete, Id(leftArray)), CallStmt(delete, Id(rightArray))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 390))
    
    #91
    def test_mix_10(self):
        input = """ 
            main: function void() {
                _jnkandf, _____: boolean=
					"Hello world com \\n" || bo && !cal,
					{1,2,3,"jkljlk"} / nh % jlkas__;
				for 
                (i = 0, i < 90, i + 9) 
                {
					va: integer = 1900 + {9,3,41,2};
					while(dshj) {
						dshj = dfh - 9 - p2;
					}
				}
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(_jnkandf, BooleanType, BinExpr(&&, BinExpr(||, StringLit(Hello world com \\n), Id(bo)), UnExpr(!, Id(cal)))), VarDecl(_____, BooleanType, BinExpr(%, BinExpr(/, ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), StringLit(jkljlk)]), Id(nh)), Id(jlkas__))), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(90)), BinExpr(+, Id(i), IntegerLit(9)), BlockStmt([VarDecl(va, IntegerType, BinExpr(+, IntegerLit(1900), ArrayLit([IntegerLit(9), IntegerLit(3), IntegerLit(41), IntegerLit(2)]))), WhileStmt(Id(dshj), BlockStmt([AssignStmt(Id(dshj), BinExpr(-, BinExpr(-, Id(dfh), IntegerLit(9)), Id(p2)))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 391))
        
    
    #92
    def test_mix_11(self):
        input = """ 
            main: function void() {
                while (true)
					while (true)
						while (true)
							while (true) if (x ==0)
								return (((((((((f(90 - p) * true - false)))))))));
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BooleanLit(True), WhileStmt(BooleanLit(True), WhileStmt(BooleanLit(True), WhileStmt(BooleanLit(True), IfStmt(BinExpr(==, Id(x), IntegerLit(0)), ReturnStmt(BinExpr(-, BinExpr(*, FuncCall(f, [BinExpr(-, IntegerLit(90), Id(p))]), BooleanLit(True)), BooleanLit(False))))))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 392))
    
    
    #93
    def test_mix_12(self):
        input = """ 
            main: function void() {
                while (true)
					while (true)
						for (i = 0, i * dss - f + vnm :: ((((yu + __f - lk)))), kl - 9 + f +{1,2,3} :: "empty")
							return true || false - fay;
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BooleanLit(True), WhileStmt(BooleanLit(True), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(::, BinExpr(+, BinExpr(-, BinExpr(*, Id(i), Id(dss)), Id(f)), Id(vnm)), BinExpr(-, BinExpr(+, Id(yu), Id(__f)), Id(lk))), BinExpr(::, BinExpr(+, BinExpr(+, BinExpr(-, Id(kl), IntegerLit(9)), Id(f)), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)])), StringLit(empty)), ReturnStmt(BinExpr(||, BooleanLit(True), BinExpr(-, BooleanLit(False), Id(fay)))))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 393))
    
    #94
    def test_mix_13(self):
        input = """ 
            main: function void() {
                while (true) {
					break;
					break;
					break;
					break;
					break;
					continue;
					continue;
					continue;
					while (true)
						break;
						break;
						continue;
						continue;
						for (i = 0, i * dss - f + vnm :: ((((yu + __f - lk)))), kl - 9 + f +{1,2,3} :: "empty")
							return true || false - fay;
				}
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BooleanLit(True), BlockStmt([BreakStmt(), BreakStmt(), BreakStmt(), BreakStmt(), BreakStmt(), ContinueStmt(), ContinueStmt(), ContinueStmt(), WhileStmt(BooleanLit(True), BreakStmt()), BreakStmt(), ContinueStmt(), ContinueStmt(), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(::, BinExpr(+, BinExpr(-, BinExpr(*, Id(i), Id(dss)), Id(f)), Id(vnm)), BinExpr(-, BinExpr(+, Id(yu), Id(__f)), Id(lk))), BinExpr(::, BinExpr(+, BinExpr(+, BinExpr(-, Id(kl), IntegerLit(9)), Id(f)), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)])), StringLit(empty)), ReturnStmt(BinExpr(||, BooleanLit(True), BinExpr(-, BooleanLit(False), Id(fay)))))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 394))
    
    #95
    def test_mix_14(self):
        input = """ 
            main: function void() {
                while (true) {
					break;
					x: integer = hjk_90 + jksd % jdflk || hjdksah * yuid - !kslj;
					continue;
					while (true)
						break;
						break;
						continue;
						continue;
						for (i = 0, i  < 90, kl - 9 + f +{1,2,3} :: "empty")
							return true || (false - fay + 9999 ) / {1,2,34,5, "abc"};
				}
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BooleanLit(True), BlockStmt([BreakStmt(), VarDecl(x, IntegerType, BinExpr(||, BinExpr(+, Id(hjk_90), BinExpr(%, Id(jksd), Id(jdflk))), BinExpr(-, BinExpr(*, Id(hjdksah), Id(yuid)), UnExpr(!, Id(kslj))))), ContinueStmt(), WhileStmt(BooleanLit(True), BreakStmt()), BreakStmt(), ContinueStmt(), ContinueStmt(), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(90)), BinExpr(::, BinExpr(+, BinExpr(+, BinExpr(-, Id(kl), IntegerLit(9)), Id(f)), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)])), StringLit(empty)), ReturnStmt(BinExpr(||, BooleanLit(True), BinExpr(/, BinExpr(+, BinExpr(-, BooleanLit(False), Id(fay)), IntegerLit(9999)), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(34), IntegerLit(5), StringLit(abc)])))))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 395))
        
        
    #96
    def test_mix_15(self):
        input = """ 
            main: function void() {
                while (true) {
					if (x * 78 + 9 - foo(9,0))
                        while (x == (0 - k + lkll) - __ldf) return f(g("io",{9,0,0},{}));
                    else for (i = 0, i<0 + __9 - jkl + {{{}}}, i+0) {}
				}
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BooleanLit(True), BlockStmt([IfStmt(BinExpr(-, BinExpr(+, BinExpr(*, Id(x), IntegerLit(78)), IntegerLit(9)), FuncCall(foo, [IntegerLit(9), IntegerLit(0)])), WhileStmt(BinExpr(==, Id(x), BinExpr(-, BinExpr(+, BinExpr(-, IntegerLit(0), Id(k)), Id(lkll)), Id(__ldf))), ReturnStmt(FuncCall(f, [FuncCall(g, [StringLit(io), ArrayLit([IntegerLit(9), IntegerLit(0), IntegerLit(0)]), ArrayLit([])])]))), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), BinExpr(+, BinExpr(-, BinExpr(+, IntegerLit(0), Id(__9)), Id(jkl)), ArrayLit([ArrayLit([ArrayLit([])])]))), BinExpr(+, Id(i), IntegerLit(0)), BlockStmt([])))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 396))
    
    #97
    def test_mix_16(self):
        input = """ 
            main: function void(check: boolean) inherit main {
                while (true) {
					if (x * 78 + 9 - foo(9,0))
                        while (x == (0 - k + lkll) - __ldf) {
                            return f(g("io",{9,0,0},{}));
							return callf("90909090");
						}
                    else for (i = 0, i<0 + __9 - jkl + {{{}}}, i+0) {
						if (x__f__f == 9)
							return !!!!!!!!!!!!!!!!!!true;
					}
				}
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [Param(check, BooleanType)], main, BlockStmt([WhileStmt(BooleanLit(True), BlockStmt([IfStmt(BinExpr(-, BinExpr(+, BinExpr(*, Id(x), IntegerLit(78)), IntegerLit(9)), FuncCall(foo, [IntegerLit(9), IntegerLit(0)])), WhileStmt(BinExpr(==, Id(x), BinExpr(-, BinExpr(+, BinExpr(-, IntegerLit(0), Id(k)), Id(lkll)), Id(__ldf))), BlockStmt([ReturnStmt(FuncCall(f, [FuncCall(g, [StringLit(io), ArrayLit([IntegerLit(9), IntegerLit(0), IntegerLit(0)]), ArrayLit([])])])), ReturnStmt(FuncCall(callf, [StringLit(90909090)]))])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), BinExpr(+, BinExpr(-, BinExpr(+, IntegerLit(0), Id(__9)), Id(jkl)), ArrayLit([ArrayLit([ArrayLit([])])]))), BinExpr(+, Id(i), IntegerLit(0)), BlockStmt([IfStmt(BinExpr(==, Id(x__f__f), IntegerLit(9)), ReturnStmt(UnExpr(!, UnExpr(!, UnExpr(!, UnExpr(!, UnExpr(!, UnExpr(!, UnExpr(!, UnExpr(!, UnExpr(!, UnExpr(!, UnExpr(!, UnExpr(!, UnExpr(!, UnExpr(!, UnExpr(!, UnExpr(!, UnExpr(!, UnExpr(!, BooleanLit(True)))))))))))))))))))))])))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 397))
    
    
    #98
    def test_mix_17(self):
        input = """ 
			fun1: function integer() {
			}
			fun2: function array[100] of integer() {				
			}
			fun: function array[100] of integer() {
			}
			fun: function  array[100] of integer() {}
            main: function void(check: boolean) inherit main {
            }
        """
        expect = """Program([
	FuncDecl(fun1, IntegerType, [], None, BlockStmt([]))
	FuncDecl(fun2, ArrayType([100], IntegerType), [], None, BlockStmt([]))
	FuncDecl(fun, ArrayType([100], IntegerType), [], None, BlockStmt([]))
	FuncDecl(fun, ArrayType([100], IntegerType), [], None, BlockStmt([]))
	FuncDecl(main, VoidType, [Param(check, BooleanType)], main, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 398))
    
    #99
    def test_mix_18(self):
        input = """ 
            f: function integer() {
                return 1 + (90 - og + __89 / 40) - iu + u3;
            }
            f2: function string() {
                return des :: ("no non" :: "its me") + "hey" || "n0";
            }
            main: function void(check: boolean) inherit main {
                arrayy: array[100] of integer = {};
                do {
					if (true) {}
					else if (true) {}
				} while (true);
                floatin: integer;
            }
        """
        expect = """Program([
	FuncDecl(f, IntegerType, [], None, BlockStmt([ReturnStmt(BinExpr(+, BinExpr(-, BinExpr(+, IntegerLit(1), BinExpr(+, BinExpr(-, IntegerLit(90), Id(og)), BinExpr(/, Id(__89), IntegerLit(40)))), Id(iu)), Id(u3)))]))
	FuncDecl(f2, StringType, [], None, BlockStmt([ReturnStmt(BinExpr(::, Id(des), BinExpr(||, BinExpr(+, BinExpr(::, StringLit(no non), StringLit(its me)), StringLit(hey)), StringLit(n0))))]))
	FuncDecl(main, VoidType, [Param(check, BooleanType)], main, BlockStmt([VarDecl(arrayy, ArrayType([100], IntegerType), ArrayLit([])), DoWhileStmt(BooleanLit(True), BlockStmt([IfStmt(BooleanLit(True), BlockStmt([]), IfStmt(BooleanLit(True), BlockStmt([])))])), VarDecl(floatin, IntegerType)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 399))
    
    #100
    def test_mix_19(self):
        input = """ 
            main: function void(check: boolean) inherit main {
                if (true) {if (true) {if (true) {if (true) {if (true) {if (true) {}}}}}}
                while (true){if (true) {if (true) {if (true) {if (true) {}}}}}
                for (i = 0, i ==0, i + 0) {
					if (true) {if (true) {while (true){if (true) {if (true) {if (true) {if (true) {}}}}}}}
				}
				{
					x: integer;
					{
						{{}}{{{}}}{}{}{}{}
					}
					x: integer;
					{
						x: integer;
						{
							{}{}{}
						}
					}
						x: integer;
					{
						{}{}{}{}
					}
					y: float;
				}
                arr: boolean = {"integer", "float", "boolean"};
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [Param(check, BooleanType)], main, BlockStmt([IfStmt(BooleanLit(True), BlockStmt([IfStmt(BooleanLit(True), BlockStmt([IfStmt(BooleanLit(True), BlockStmt([IfStmt(BooleanLit(True), BlockStmt([IfStmt(BooleanLit(True), BlockStmt([IfStmt(BooleanLit(True), BlockStmt([]))]))]))]))]))])), WhileStmt(BooleanLit(True), BlockStmt([IfStmt(BooleanLit(True), BlockStmt([IfStmt(BooleanLit(True), BlockStmt([IfStmt(BooleanLit(True), BlockStmt([IfStmt(BooleanLit(True), BlockStmt([]))]))]))]))])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(==, Id(i), IntegerLit(0)), BinExpr(+, Id(i), IntegerLit(0)), BlockStmt([IfStmt(BooleanLit(True), BlockStmt([IfStmt(BooleanLit(True), BlockStmt([WhileStmt(BooleanLit(True), BlockStmt([IfStmt(BooleanLit(True), BlockStmt([IfStmt(BooleanLit(True), BlockStmt([IfStmt(BooleanLit(True), BlockStmt([IfStmt(BooleanLit(True), BlockStmt([]))]))]))]))]))]))]))])), BlockStmt([VarDecl(x, IntegerType), BlockStmt([BlockStmt([BlockStmt([])]), BlockStmt([BlockStmt([BlockStmt([])])]), BlockStmt([]), BlockStmt([]), BlockStmt([]), BlockStmt([])]), VarDecl(x, IntegerType), BlockStmt([VarDecl(x, IntegerType), BlockStmt([BlockStmt([]), BlockStmt([]), BlockStmt([])])]), VarDecl(x, IntegerType), BlockStmt([BlockStmt([]), BlockStmt([]), BlockStmt([]), BlockStmt([])]), VarDecl(y, FloatType)]), VarDecl(arr, BooleanType, ArrayLit([StringLit(integer), StringLit(float), StringLit(boolean)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 400))