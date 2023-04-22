import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_redeclaration_1(self):
        input = """
            main: function void() {
                x: integer = 100;
                x: float = 1.1;
            }
        """
        expect = """Redeclared Variable: x"""
        self.assertTrue(TestChecker.test(input, expect, 401))
    
    
    def test_redeclaration_2(self):
        input = """
            main: function void() {
                x, y, z: integer = 100, 90, 434;
                t, u, y: float = 1.1, 1.1e2, 90;
            }
        """
        expect = """Redeclared Variable: y"""
        self.assertTrue(TestChecker.test(input, expect, 402))
    
    
    def test_redeclaration_3(self):
        input = """
            main: function void() {
                for (i = 0, i < 4, i + 1) {
                    printInteger(i);
                    i = i / 20;
                    i: integer = 4;
                }
            }"""
        expect = """Redeclared Variable: i"""
        self.assertTrue(TestChecker.test(input, expect, 403))
    
    
    def test_redeclaration_4(self):
        input = """
            foo: function integer() {
            }
            
            main: function void() {
                x: integer = foo();
            }
            
            foo: function integer() {
            }
        """
        expect = """Redeclared Function: foo"""
        self.assertTrue(TestChecker.test(input, expect, 404))
    
    
    def test_redeclaration_5(self):
        input = """
            foo: function integer(x: integer, y: float, out x: float) {
                return 12;
            }
            
            main: function void() {
                x: integer = foo(1, 1.5, 1.9);
            }
        """
        expect = """Redeclared Parameter: x"""
        self.assertTrue(TestChecker.test(input, expect, 405))
    
    
    def test_undeclaration_1(self):
        input = """
            main: function void() {
                x: integer = foo(1, 1.5);
            }
            
            k: integer = 1900;
            
            foo: function integer(x: integer, y: float) {
                if (true)
                {
                    t: integer = 2138 - 9 % 2;
                }
                
                return t;
            }
        """
        expect = """Undeclared Identifier: t"""
        self.assertTrue(TestChecker.test(input, expect, 406))
    
    
    def test_undeclaration_2(self):
        input = """
            main: function void() {
                x: integer = foo(1, 1.5);
            }
            
            foo: function integer(x: integer, y: float) {
                return foo(foo(1, 3.2), 1.4);
            }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 407))
    
    
    def test_undeclaration_3(self):
        input = """
            main: function void() {
                x: integer = foo(1, 1.5);
            }
        """
        expect = """Undeclared Function: foo"""
        self.assertTrue(TestChecker.test(input, expect, 408))
    
    
    def test_undeclaration_4(self):
        input = """
            main: function void() {
                x: integer;
                y: integer = x + z;
            }
        """
        expect = """Undeclared Identifier: z"""
        self.assertTrue(TestChecker.test(input, expect, 409))
    
    
    def test_undeclaration_5(self):
        input = """
            z: integer = 209;
            main: function void() {
                x: integer;
                y: integer = x + z;
            }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 410))
    
    
    def test_undeclaration_6(self):
        input = """
            main: function void() {
                x: integer;
                y: integer = x + z;
            }
            z: integer = 190;
        """
        expect = """Undeclared Identifier: z"""
        self.assertTrue(TestChecker.test(input, expect, 411))
    
    
    def test_undeclaration_7(self):
        input = """
            i2f: function integer(x: float) {
                return 123;
            }

            main: function void() {
                x: integer;
                y: integer = x + 78 + i2f;
            }
        """
        expect = """Undeclared Identifier: i2f"""
        self.assertTrue(TestChecker.test(input, expect, 412))
    
    
    def test_invalid_1(self):
        input = """
            main: function void() {
                x: auto = 76234;
                y: auto = "abc";
                z: auto = true;
                t: auto = 3244.e1;
            }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 413))
    
    def test_invalid_2(self):
        input = """
            main: function void() {
                x: auto = 76234;
                y: auto = "abc";
                z: auto;
                t: auto = 3244.e1;
            }
        """
        expect = """Invalid Variable: z"""
        self.assertTrue(TestChecker.test(input, expect, 414))
    
    def test_invalid_3(self):
        input = """
            bar: function integer(inherit x: integer) {
                return 100;
            }
            foo: function void() inherit bar {
                //super(20);
                // t: integer = 890;
            }
            main: function void() {
                foo();
            }
        """
        expect = """Invalid statement in function: foo"""
        self.assertTrue(TestChecker.test(input, expect, 415))
    
    
    def test_invalid_4(self):
        input = """
            bar: function integer(inherit z: integer) {
                return 100;
            }
            foo: function void() inherit bar {
                super(2.0);
                x: integer = 118;
            }
            main: function void() {
                foo();
            }
        """
        expect = """Type mismatch in expression: FloatLit(2.0)"""
        self.assertTrue(TestChecker.test(input, expect, 416))
    
    def test_invalid_5(self):
        input = """
            bar: function integer(inherit x: integer) {
                return 100;
            }
            foo: function void() inherit bar {
                super(2);
                y: boolean = true || false;
                x: integer = 18;
            }
            main: function void() {
                foo();
            }
        """
        expect = """Redeclared Variable: x"""
        self.assertTrue(TestChecker.test(input, expect, 417))
    
    def test_invalid_6(self):
        input = """
            bar: function integer(inherit x: integer) {
                return 100;
            }
            foo: function void(x: float) inherit bar {
                super(2);
                y: boolean = true || false;
                z: integer = 18;
            }
            main: function void() {
                foo(7.7);
            }
        """
        expect = """Invalid Parameter: x"""
        self.assertTrue(TestChecker.test(input, expect, 418))
    
    # TYPE MISMATCH
    def test_type_mismatch_1(self):
        input = """
            main: function void() {
                arr: array[10] of integer;
                arr[3] = 5;
            }"""
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 419))
    
    def test_type_mismatch_2(self):
        input = """
            arr: function integer() {
                
            }
            main: function void() {
                arr[3] = 5;
            }"""
        expect = """Type mismatch in expression: ArrayCell(arr, [IntegerLit(3)])"""
        self.assertTrue(TestChecker.test(input, expect, 420))
    
    def test_type_mismatch_3(self):
        input = """
            main: function void() {
                arr: integer;
                arr[3] = 5;
            }"""
        expect = """Type mismatch in expression: ArrayCell(arr, [IntegerLit(3)])"""
        self.assertTrue(TestChecker.test(input, expect, 421))
    
    def test_type_mismatch_4(self):
        input = """
            main: function void() {
                arr: array[10] of integer;
                arr[3.2] = 5;
            }"""
        expect = """Type mismatch in expression: ArrayCell(arr, [FloatLit(3.2)])"""
        self.assertTrue(TestChecker.test(input, expect, 422))
    
    def test_type_mismatch_5(self):
        input = """
            main: function void() {
                x: float = (3 + 3.e5 - 9) / 23 + 1 * 0.66;
                y: integer = 123 + 9 - 1 / 2023 % 897;
                z: boolean = (1 > 3) || (-2.5 <= 9) && true || !false;
                s: string = "abc" :: "cxyz";
            }"""
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 423))
    
    def test_type_mismatch_6(self):
        input = """
            main: function void() {
                x: float = (3 + 3.e5 - 9) / 23 + 1 * 0.66;
                y: integer = 123 + 9 - 1 / 2023 % 897;
                x = x / y + 12 % 56;
                
                check: boolean = true;
                z: boolean = (1.5 > 3) && !(-2.5 <= 9) && true || !false;
                z = z || !true && check;
                
                s: string = "abc" :: "cxyz";
                s = s :: "gogo";
            }"""
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 424))
    
    def test_type_mismatch_7(self):
        input = """
            main: function void() {
                x: float = (3 + 3.e5 - 9) / 23 + 1 * 0.66;
                y: integer = 123 + 9 - 1 / 2023 % 897;
                x = 56 - 31 + (x / y + 12) % 98;
            }"""
        expect = """Type mismatch in expression: BinExpr(%, BinExpr(+, BinExpr(/, Id(x), Id(y)), IntegerLit(12)), IntegerLit(98))"""
        self.assertTrue(TestChecker.test(input, expect, 425))
    
    def test_type_mismatch_8(self):
        input = """
            main: function void() {
                x: float = (3 + 3.e5 - 9) / 23 + 1 * 0.66;
                y: integer = 123 + 9 - 1 / 2023 % 897;
                z: boolean = (x > y) && (y <= x) != x;
            }"""
        expect = """Type mismatch in expression: BinExpr(!=, BinExpr(&&, BinExpr(>, Id(x), Id(y)), BinExpr(<=, Id(y), Id(x))), Id(x))"""
        self.assertTrue(TestChecker.test(input, expect, 426))
    
    def test_type_mismatch_9(self):
        input = """
            main: function void() {
                z: boolean = (1.5 > 3) && !(-2.5 <= 9) && true || !false;
                
                s: string = "abc" :: "cxyz";
                s = s :: "gogo";
                s = s :: z;
            }"""
        expect = """Type mismatch in expression: BinExpr(::, Id(s), Id(z))"""
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test_type_mismatch_11(self):
        input = """
            foo1: function float() {
                return 1.5;
            }
            foo2: function integer(x: boolean) {
                if (x) {
                    return 768;
                }
                return foo2(false);
            }
            foo3: function boolean () {
                return foo2(true) == 9;
            }
            foo4: function string(s: string) {
                if (1 != 0) {
                    return "";
                }
                return s :: foo4(s);
            }
            main: function void() {
            }"""
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 428))
        
    def test_type_mismatch_12(self):
        input = """
            foo1: function float() {
                return 1.5 / 6;
            }
            foo2: function integer(x: boolean) {
                if (x) {
                    return 768;
                }
                return foo2(false);
            }
            foo3: function boolean () {
                return 17 == 9;
            }
            foo4: function string(s: string) {
                t: boolean;
                if (t && true != false || t) {
                    return "";
                }
                return s :: foo4(s);
            }
            main: function void() {
                x: float = (foo2(false) + 3.e5 - 9) / foo1() + 1 * 0.66;
                y: integer = 123 + 9 - 1 / 2023 % 897;
                z: boolean = (1 > foo2(false)) || (-2.5 <= 9) && true || !false && !foo3();
                s: string = "abc" :: "cxyz";
                s = s :: foo4(foo4(foo4("this is a valid string \\t ")));
            }"""
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 429))
        
    def test_type_mismatch_13(self):
        input = """
            foo1: function auto() {
                x: string = "this is a string \\n";
            }
            main: function void() {
                x: float = (foo1() + 3.e5 - 9) / foo1() + 1 * 0.66;
                __y78: float = foo1() / 89 + foo1() - 5 + 324.E3;
                
                // type(foo1) is FloatType
                z: boolean = foo1() || true;
            }"""
        expect = """Type mismatch in expression: BinExpr(||, FuncCall(foo1, []), BooleanLit(True))"""
        self.assertTrue(TestChecker.test(input, expect, 430))
    
    def test_type_mismatch_14(self):
        input = """
            foo1: function void() {
                x: string = "this is a string \\n";
            }
            main: function void() {
                /* foo1 is void function */
                x: integer = foo1() + 20;
                return 123;
            }"""
        expect = """Type mismatch in expression: FuncCall(foo1, [])"""
        self.assertTrue(TestChecker.test(input, expect, 431))
    
    def test_type_mismatch_15(self):
        input = """
            foo1: function integer(y: boolean) {
                x: string = "this is a string \\n";
                return 13;
            }
            foo2: function integer(x: boolean) {
                if (x) {
                    x = x || true && !false;
                }
            }
            foo3: function boolean () {
            }
            foo4: function auto(s: string) {
                return "123";
            }
            foo5: function void() {
                printString("Kaka hmahmu");
                printInteger(123);
                printFloat(1.3e4);
                check: boolean = true;
                printBoolean(check);
            }
            foo6: function float() {
                return 1.e3;
            }
            main: function void() {
                s: boolean;
                // foo4 return type is function
                s = foo4("that khong the tin duoc!!");
            }"""
        expect = """Type mismatch in statement: AssignStmt(Id(s), FuncCall(foo4, [StringLit(that khong the tin duoc!!)]))"""
        self.assertTrue(TestChecker.test(input, expect, 432))
    
    def test_type_mismatch_16(self):
        input = """
            foo1: function integer(y: boolean) {
                x: string = "this is a string \\n";
                return 13;
            }
            main: function void() {
                x: integer = foo1(true, "I cant sleep") + 20;
                return 123;
            }"""
        expect = """Type mismatch in expression: """
        self.assertTrue(TestChecker.test(input, expect, 433))
    
    def test_type_mismatch_17(self):
        input = """
            foo1: function auto(y: boolean) {
            }
            main: function void() {
                x: integer = foo1(true) + 1;
                y: boolean = foo1(true) || false;
            }"""
        expect = """Type mismatch in expression: BinExpr(||, FuncCall(foo1, [BooleanLit(True)]), BooleanLit(False))"""
        self.assertTrue(TestChecker.test(input, expect, 434))
    
    def test_type_mismatch_18(self):
        input = """
            foo1: function auto(y: boolean) {
            }
            
            foo2: function auto() {}
            
            foo3: function integer(x: boolean, y: integer) {}
            
            main: function void() {
                x: boolean = !foo1(true);
                y: integer = -foo2();
                foo3(foo1(x), foo2());
                foo3(foo2(), foo1(x));
            }"""
        expect = """Type mismatch in statement: CallStmt(foo3, FuncCall(foo2, []), FuncCall(foo1, [Id(x)]))"""
        self.assertTrue(TestChecker.test(input, expect, 435))
        
    def test_type_mismatch_19(self):
        input = """
            foo: function auto(x: auto) {
                return x;
            }
            
            main: function void() {
                y: boolean = foo(78);
                z: string = foo(45);
            }"""
        expect = """Type mismatch in Variable Declaration: VarDecl(z, StringType, FuncCall(foo, [IntegerLit(45)]))"""
        self.assertTrue(TestChecker.test(input, expect, 436))
    
    def test_type_mismatch_20(self):
        input = """
            foo: function auto(x: auto) {
                return x;
            }
            
            main: function void() {
                foo(78);
                z: string = foo(4.5);
            }"""
        expect = """Type mismatch in expression: FuncCall(foo, [FloatLit(4.5)])"""
        self.assertTrue(TestChecker.test(input, expect, 437))
    
    def test_type_mismatch_21(self):
        input = """
            main: function void() {
                arr: array[2, 2] of integer = {{0, 2}, {1, 4}};
                arr1: array[2, 3] of integer = {{1, 2}, {3, 4}};
            }"""
        expect = """Type mismatch in Variable Declaration: VarDecl(arr1, ArrayType([2, 3], IntegerType), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2)]), ArrayLit([IntegerLit(3), IntegerLit(4)])]))"""
        self.assertTrue(TestChecker.test(input, expect, 438))
    
    def test_type_mismatch_22(self):
        input = """
            foo: function auto() {
                return {{2,3}};
            }
        
            main: function void() {
                for (i = 0, i == 6 * 9 - 283, i + 1) {
                    printInteger(i);
                    i = i / 20;
                    arr: array[1,2] of integer = foo();
                }
            }"""
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 439))
    
    def test_type_mismatch_23(self):
        input = """
            foo: function auto() {
                return {{2,3}};
            }
        
            main: function void() {
                for (i = 0, i == 6 * 9 - 283, i + 1.5) {
                    printInteger(i);
                    i = i / 20;
                    arr: array[1,2] of integer = foo();
                }
            }"""
        expect = """Type mismatch in statement: ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(==, Id(i), BinExpr(-, BinExpr(*, IntegerLit(6), IntegerLit(9)), IntegerLit(283))), BinExpr(+, Id(i), FloatLit(1.5)), BlockStmt([CallStmt(printInteger, Id(i)), AssignStmt(Id(i), BinExpr(/, Id(i), IntegerLit(20))), VarDecl(arr, ArrayType([1, 2], IntegerType), FuncCall(foo, []))]))"""
        self.assertTrue(TestChecker.test(input, expect, 440))
        
    def test_type_mismatch_24(self):
        input = """
            foo: function auto() {
                return {{2,3}};
            }
            
            initi: function auto() {
                return 12632423;
            }
        
            main: function void() {
                for (i = initi(), i + 5 - 3 % 12, i + 90) {
                    printInteger(i);
                    i = i / 10;
                    arr: array[1,2] of integer = foo();
                }
            }"""
        expect = """Type mismatch in statement: ForStmt(AssignStmt(Id(i), FuncCall(initi, [])), BinExpr(-, BinExpr(+, Id(i), IntegerLit(5)), BinExpr(%, IntegerLit(3), IntegerLit(12))), BinExpr(+, Id(i), IntegerLit(90)), BlockStmt([CallStmt(printInteger, Id(i)), AssignStmt(Id(i), BinExpr(/, Id(i), IntegerLit(10))), VarDecl(arr, ArrayType([1, 2], IntegerType), FuncCall(foo, []))]))"""
        self.assertTrue(TestChecker.test(input, expect, 441))
    
    def test_type_mismatch_25(self):
        input = """
            foo: function auto() {
                return true || false;
            }
        
            main: function void() {
                while (foo()) {
                    printFloat(123.e54);
                }
            }"""
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 442))
        
    def test_type_mismatch_26(self):
        input = """
            /* You cannot assign an array */
            main: function void() {
                x: array[3, 2] of integer = {{1,2},{3,4},{5,6}};
                x = {{1,2},{3,4},{5,6}};
            }"""
        expect = """Type mismatch in statement: AssignStmt(Id(x), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2)]), ArrayLit([IntegerLit(3), IntegerLit(4)]), ArrayLit([IntegerLit(5), IntegerLit(6)])]))"""
        self.assertTrue(TestChecker.test(input, expect, 443))
    
    def test_type_mismatch_28(self):
        input = """
            foo: function auto(x: integer, y: boolean, z: string) {
                x = x + 435;
                y = true || y && false;
                z = "abc" :: z;
            }
            main: function void() {
                foo(123, true);
            }"""
        expect = """Type mismatch in statement: """
        self.assertTrue(TestChecker.test(input, expect, 444))
    
    def test_type_mismatch_29(self):
        input = """
            foo: function auto(x: integer, y: boolean, z: string) {
                x = x + 435;
                y = true || y && false;
                z = "abc" :: z;
            }
            main: function void() {
                foo(123, true, "abcdefg", false);
            }"""
        expect = """Type mismatch in statement: """
        self.assertTrue(TestChecker.test(input, expect, 445))
    
    def test_type_mismatch_30(self):
        input = """
            foo: function auto(x: integer, y: boolean, z: auto) {
                x = x + 435;
                y = true || y && false;
            }
            main: function void() {
                foo(123, true, "abcdefg");
                foo(123, true, true);
            }"""
        expect = """Type mismatch in statement: CallStmt(foo, IntegerLit(123), BooleanLit(True), BooleanLit(True))"""
        self.assertTrue(TestChecker.test(input, expect, 446))
    
    def test_type_mismatch_31(self):
        input = """
            foo: function auto(x: integer, y: boolean, z: auto) {
                x = x + 435;
                y = true || y && false;
            }
            main: function void() {
                x: float;
                foo(123, true, "abcdefg");
                foo(123, x, "abcdefg");
            }"""
        expect = """Type mismatch in statement: CallStmt(foo, IntegerLit(123), Id(x), StringLit(abcdefg))"""
        self.assertTrue(TestChecker.test(input, expect, 447))
    
    def test_type_mismatch_32(self):
        input = """
            foo: function auto(x: integer, y: boolean, z: auto) {
                x = x + 435;
                y = true || y && false;
            }
            main: function void() {
                x: float;
                foo(123, true, "abcdefg");
                foo(123, x, "abcdefg");
            }"""
        expect = """Type mismatch in statement: CallStmt(foo, IntegerLit(123), Id(x), StringLit(abcdefg))"""
        self.assertTrue(TestChecker.test(input, expect, 448))
    
    def test_type_mismatch_33(self):
        input = """
            main: function void() {
                x: integer;
                x[20] = 96;
            }"""
        expect = """Type mismatch in expression: ArrayCell(x, [IntegerLit(20)])"""
        self.assertTrue(TestChecker.test(input, expect,449))
    
    def test_type_mismatch_34(self):
        input = """
            foo: function auto() {
                return true || false;
            }
        
            main: function void() {
                do {
                    printInteger(231);
                }
                while (foo());
            }"""
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect,450))
        
    
    # def test_type_mismatch_21(self):
    #     input = """
    #         foo: function auto() {
    #             return {1, {2}};
    #         }
        
    #         main: function void() {
    #             arr: array[2, 2] of integer = {{0, 2}, {1, 4}};
    #             x: array[2] of integer = foo();
    #             y: array[3] of integer = foo();
    #         }"""
    #     expect = """Type mismatch in Variable Declaration: VarDecl(y, ArrayType([3], IntegerType), FuncCall(foo, []))"""
    #     self.assertTrue(TestChecker.test(input, expect, 439))
    

    # def test_type_mismatch_20(self):
    #     input = """
    #         main: function void() {
    #             arr: array[2, 3] of integer = {{1, 2}, {3, 4, 6}};
    #         }"""
    #     expect = """Illegal array literal: ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2)]), ArrayLit([IntegerLit(3), IntegerLit(4), IntegerLit(6)])])"""
    #     self.assertTrue(TestChecker.test(input, expect, 438))
    
    # def test_type_mismatch_21(self):
    #     input = """
    #         main: function void() {
    #             arr: array[2, 3] of integer = {{1, 2, 5}, {3, 4, 6}};
    #             arr1: array[2, 3, 3] of integer = {
    #                 {{1,2,3,4}, {5,6,7,8}, {5,2,7,4}}, 
    #                 {{1,2,3,4}, {0,2,3,6}, {9,0,3,4}}
    #             };
    #         }"""
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 439))
    
    # def test_vardecl_6(self):
    #     input = """
    #         foo: function integer(x: integer, y: float, z:boolean) {
                
    #         }
    #         main: function void() {
    #             x:integer = foo(3,3.4,true);
    #         }"""
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 406))
    
    # def test_vardecl_7(self):
    #     input = """
    #         foo: function integer(x: integer, y: float, z:boolean) {
                
    #         }
    #         main: function void() {
    #             y: boolean;
    #             x: boolean = true && false || !y;
    #         }"""
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 407))
    
    # def test_vardecl_8(self):
    #     input = """
    #         foo: function float(x: integer, y: float, z:boolean) {
                
    #             return 2;
    #         }
    #         main: function void() {
    #             for (i = 0, i < 3.2, i + 1) {
    #                 z: boolean;
    #                 z = false || true;
    #             }
    #             while(true){
    #                 break;
    #             }
    #             continue;
    #         }"""
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 408))
    
    # def test_vardecl_8(self):
    #     input = """
    #         foo: function float(x: integer, y: float, z:boolean) {
                
    #             return 2.9;
    #         }
    #         main: function void() {
    #             arr: array[10] of integer;
    #             x: auto;
    #         }"""
    #     expect = """Invalid Variable: x"""
    #     self.assertTrue(TestChecker.test(input, expect, 409))
    
    # def test_vardecl_9(self):
    #     input = """
    #         foo: function float(x: integer, y: float, z:boolean) {
                
    #             return 2;
    #         }
    #         main: function void() {
    #             arr: array[10] of integer;
    #             x: auto = 5;
    #             x = 5.5;
    #         }"""
    #     expect = """Type mismatch in statement: AssignStmt(Id(x), FloatLit(5.5))"""
    #     self.assertTrue(TestChecker.test(input, expect, 410))
    
    # # def test_vardecl_4(self):
    # #     input = """main: function void() {
    # #             arr: array[10, 10] of integer = {{1,2,3},{0}};
    # #         }"""
    # #     expect = """"""
    # #     self.assertTrue(TestChecker.test(input, expect, 411))]
    
    # def test_vardecl_4(self):
    #     input = """
    #     foo: function auto() {
            
    #     }
    #     main: function void() {
    #         x: integer = foo();
    #     }"""
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 412))
