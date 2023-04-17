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
            foo: function integer() {
            }
            foo: function void() {
            }
            main: function void() {
                x: integer = foo();
            }
        """
        expect = """Redeclared Function: foo"""
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
                return k;
            }
        """
        expect = """"""
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
