import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_cmt(self):
        #1
        input = """
        x: integer;
        /* This is a comment */
        //This is an inline comment
        y: integer = -13;
        """
        expect = 'x,:,integer,;,y,:,integer,=,-,13,;,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 101))
        
    def test_vardecl(self):
        #2
        input = """
        _xA099: float;
        AFFF90: string;
        09fa: integer;
        """
        expect = '_xA099,:,float,;,AFFF90,:,string,;,0,9,fa,:,integer,;,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 102))
        
    def test_vardecl2(self):
        #3
        input = """ _xA099, ffgNN: float = 109, 200; """
        expect = '_xA099,,,ffgNN,:,float,=,109,,,200,;,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 103))
        
    def test_int(self):
        #4
        input = """ 1_3254 """
        expect = '13254,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 104))
        
    def test_float(self):
        #5
        input = """ 1_3254.5678 """
        expect = '13254.5678,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 105))
        
    def test_float2(self):
        #6
        input = "1_3254.e5678"
        expect = "13254.e5678,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 106))
        
    def test_vardecl3(self):
        #7
        input = "check: boolean = true;"
        expect = "check,:,boolean,=,true,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 107))
        
    def test_str(self):
        #8
        input = """ "hello abc \\*" """
        expect = 'Illegal Escape In String: hello abc \\*'
        self.assertTrue(TestLexer.test(input, expect, 108))
        
    def test_str2(self):
        #9
        input = """ "Hello Hello \\f" """
        expect = 'Hello Hello \\f,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 109))
        
    def test_vardecl4(self):
        #10
        input = """ arr: array[10] of integer; """
        expect = 'arr,:,array,[,10,],of,integer,;,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 110))
        
    def test_arrlit(self):
        #11
        input = """ {"AOT","JOJO","JJK","CSM"} """
        expect = '{,AOT,,,JOJO,,,JJK,,,CSM,},<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 111))
        
    def test_arrlit2(self):
        #12
        input = """ {1,2,4,5,123} """
        expect = '{,1,,,2,,,4,,,5,,,123,},<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 112))
        
    def test_arrlit3(self):
        #13
        input = """ {1.2314,2_324,4_000.1e19,5E-5,123.6} """
        expect = '{,1.2314,,,2324,,,4000.1e19,,,5E-5,,,123.6,},<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 113))
        
    def test_arrlit4(self):
        #14
        input = """ {1.2314,2_324,4_000.1e19,5E-5,123.6} """
        expect = '{,1.2314,,,2324,,,4000.1e19,,,5E-5,,,123.6,},<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 114))
    
    def test_arrlit5(self):    
        #15
        input = """ {true, false, false, true, true} """
        expect = '{,true,,,false,,,false,,,true,,,true,},<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 115))
        
    def test_cmt2(self):
        #16
        input = """ "This is a \\t" """
        expect = 'This is a \\t,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 116))
        
    def test_cmt3(self):
        #17
        input = """ "This is a \\f" """
        expect = 'This is a \\f,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 117))
        
    def test_cmt4(self):
        #18
        input = """ "This is a \\r \\n" """
        expect = 'This is a \\r \\n,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 118))
        
    def test_cmt5(self):
        #19
        input = """ "Hello \\'I wanna play a game\\'" """
        expect = "Hello \\'I wanna play a game\\',<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 119))
    
    def test_cmt6(self):
        #20
        input = """ "This is a \\r \\n
        abcc" """
        expect = """Unclosed String: This is a \\r \\n"""
        self.assertTrue(TestLexer.test(input, expect, 120))
        
    def test_cmt7(self):
        #21
        input = """ "This is a !@#$%^&*()" """
        expect = 'This is a !@#$%^&*(),<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 121))
        
    def test_cmt8(self):
        #22
        input = """ "EOF hereeeee"""
        expect = """Unclosed String: EOF hereeeee"""
        self.assertTrue(TestLexer.test(input, expect, 122))
        
    def test_cmt9(self):
        #23
        input = """ "He is a nice
        guy """
        expect = """Unclosed String: He is a nice"""
        self.assertTrue(TestLexer.test(input, expect, 123))
        
    def test_cmt10(self):
        #24
        input = """ ####**** """
        expect = 'Error Token #'
        self.assertTrue(TestLexer.test(input, expect, 124))
        
    def test_expr1(self):
        #25
        input = """ x = 19 * 23 -  y + 7; """
        expect = 'x,=,19,*,23,-,y,+,7,;,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 125))
    
    def test_stmt1(self):    
        #26
        input = """ if (x == 15) return "this is a return stmt" """
        expect = 'if,(,x,==,15,),return,this is a return stmt,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 126))
        
    def test_stmt2(self):    
        #27
        input = """ print(x != 90) """
        expect = 'print,(,x,!=,90,),<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 127))
        
    def test_expr2(self):
        #28
        input = """ x: integer = 123 % 12 / 14; """
        expect = 'x,:,integer,=,123,%,12,/,14,;,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 128))
        
    def test_expr3(self):
        #29
        input = """ x: boolean = 188 >= (123 % (12 / 14)); """
        expect = 'x,:,boolean,=,188,>=,(,123,%,(,12,/,14,),),;,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 129))
        
    def test_expr4(self):
        #30
        input = """ x: boolean = 290 != (46 % (12 <= 14)); """
        expect = 'x,:,boolean,=,290,!=,(,46,%,(,12,<=,14,),),;,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 130))
        
    def test_expr5(self):
        #31
        input = """ y: boolean """
        expect = 'y,:,boolean,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 131))
        
    def test_vardecl5(self):
        #32
        input = """ y,yy: boolean """
        expect = 'y,,,yy,:,boolean,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 132))
        
    def test_func1(self):
        #33
        input = """ 
            foo: function void(f: integer) {
                return f + 10;
            } """
        expect = 'foo,:,function,void,(,f,:,integer,),{,return,f,+,10,;,},<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 133))
        
    def test_func2(self):
        #34
        input = """ 
            foo: function void(f: integer) {
                return f + 10;
            } """
        expect = 'foo,:,function,void,(,f,:,integer,),{,return,f,+,10,;,},<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 134))
        
    def test_func3(self):
        #35
        input = """ 
            foo: function integer(f: integer) {
                if (x == 5)
                    return 0;
                return f + 10;
            } """
        expect = 'foo,:,function,integer,(,f,:,integer,),{,if,(,x,==,5,),return,0,;,return,f,+,10,;,},<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 135))
        
    def test_func4(self):
        #36
        input = """ 
            foo: function void(f: void) {
                if (xfff == 5)
                    return 0;
                return f + 10;
            } """
        expect = 'foo,:,function,void,(,f,:,void,),{,if,(,xfff,==,5,),return,0,;,return,f,+,10,;,},<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 136))
        
    def test_func5(self):
        #37
        input = """ 
            foo(12);
            print(foo(40));"""
        expect = 'foo,(,12,),;,print,(,foo,(,40,),),;,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 137))
        
    def test_func6(self):
        #38
        input = """ 
            main: function integer () {
                x: integer = 3;
                foo(x);
                print(x);
                return 90 % 5;    
            }"""
        expect = 'main,:,function,integer,(,),{,x,:,integer,=,3,;,foo,(,x,),;,print,(,x,),;,return,90,%,5,;,},<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 138))
        
    def test_func7(self):
        #39
        input = """
            x: integer = 15;
            main: function integer () {
                x: integer = 3;
                foo(x);
                print(x);
                return 90 % 5;    
            }"""
        expect = 'x,:,integer,=,15,;,main,:,function,integer,(,),{,x,:,integer,=,3,;,foo,(,x,),;,print,(,x,),;,return,90,%,5,;,},<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 139))
    
    def test_func8(self):
        #40
        input = """ 
            main: function integer () {
                x: integer = 3;
                foo(x);
                print(x);
                return 90 % 5;    
            }
            z = 190;"""
        expect = 'main,:,function,integer,(,),{,x,:,integer,=,3,;,foo,(,x,),;,print,(,x,),;,return,90,%,5,;,},z,=,190,;,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 140))
        
    def test_stmt3(self):    
        #41
        input = """ 
            print(xyyy,1090,true);
            add(i,p);"""
        expect = 'print,(,xyyy,,,1090,,,true,),;,add,(,i,,,p,),;,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 141))
        
    def test_stmt4(self):    
        #42
        input = """ 
            s1 = "str1";
            s2 = "str2";
            s: string = s1 :: s2; 
            """
        expect = 's1,=,str1,;,s2,=,str2,;,s,:,string,=,s1,::,s2,;,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 142))
        
    def test_stmt5(self):    
        #43
        input = """ 
            "str
            1";
            s2 = "str2";
            s: string = s1 :: s2; 
            """
        expect = 'Unclosed String: str'
        self.assertTrue(TestLexer.test(input, expect, 143))
        
    def test_stmt6(self):    
        #44
        input = """ 
            arr: array[4] of integer;
            """
        expect = """arr,:,array,[,4,],of,integer,;,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 144))
        
    def test_stmt7(self):    
        #45
        input = """ 
            arr: array[4, 10] of integer;
            """
        expect = """arr,:,array,[,4,,,10,],of,integer,;,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 145))
        
    def test_stmt8(self):    
        #46
        input = """ 
            arr: array[4] of integer = {1,2,3,4};
            """
        expect = """arr,:,array,[,4,],of,integer,=,{,1,,,2,,,3,,,4,},;,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 146))
        
    def test_stmt9(self):    
        #47
        input = """ 
            x: auto = 20;
            """
        expect = """x,:,auto,=,20,;,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 147))
        
    def test_func9(self):
        #48
        input = """ 
            main: function integer (inherit out g: integer) {
                x: integer = 3;
                foo(x);
                print(x);
                return 90 % 5;    
            }
            z = 190;"""
        expect = 'main,:,function,integer,(,inherit,out,g,:,integer,),{,x,:,integer,=,3,;,foo,(,x,),;,print,(,x,),;,return,90,%,5,;,},z,=,190,;,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 148))
        
    def test_float20(self):
        #48
        input = """98E-902"""
        expect = '98E-902,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 148))
        
    def test_func10(self):
        #50
        input = """ 
            main: function integer (inherit  g: integer) {
                x: integer = 3;
                foo(x);
                print(x);
                return 90 % 5;    
            }
            z = 190;"""
        expect = 'main,:,function,integer,(,inherit,g,:,integer,),{,x,:,integer,=,3,;,foo,(,x,),;,print,(,x,),;,return,90,%,5,;,},z,=,190,;,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 150))
        
    def test_func11(self):
        #51
        input = """ 
            main: function integer (out  g: integer) {
                x: integer = 3;
                foo(x);
                print(x);
                return 90 % 5;    
            }
            z = 190;"""
        expect = 'main,:,function,integer,(,out,g,:,integer,),{,x,:,integer,=,3,;,foo,(,x,),;,print,(,x,),;,return,90,%,5,;,},z,=,190,;,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 151))
        
    def test_expr6(self):
        #52
        input = """ 
            x= 20*3 + 9;"""
        expect = 'x,=,20,*,3,+,9,;,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 152))
        
    def test_expr7(self):
        #53
        input = """ 
            y= x*3 %12 + 9;"""
        expect = 'y,=,x,*,3,%,12,+,9,;,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 153))
        
    def test_expr8(self):
        #54
        input = """ foo(12,3)"""
        expect = 'foo,(,12,,,3,),<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 154))
        
    def test_expr9(self):
        #55
        input = """ foo(false,3)"""
        expect = 'foo,(,false,,,3,),<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 155))
        
    def test_expr10(self):
        #56
        input = """ foo(x3,3)"""
        expect = 'foo,(,x3,,,3,),<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 156))
        
    def test_expr11(self):
        #57
        input = """ foo("abz",3)"""
        expect = 'foo,(,abz,,,3,),<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 157))
        
    def test_expr12(self):
        #58
        input = """ foo(i[4],3)"""
        expect = 'foo,(,i,[,4,],,,3,),<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 158))
        
    def test_expr14(self):
        #59
        input = """ foo(true,foo(9))"""
        expect = 'foo,(,true,,,foo,(,9,),),<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 159))
        
    def test_stmt10(self):
        #60
        input = """ if (x = 5) x = 3;"""
        expect = 'if,(,x,=,5,),x,=,3,;,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 160))
        
    def test_stmt11(self):
        #61
        input = """ if (x = 5) x = 3 else x = 6;"""
        expect = 'if,(,x,=,5,),x,=,3,else,x,=,6,;,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 161))
        
    def test_stmt12(self):
        #62
        input = """ for (i = 0, i <10, i+1) {print(i)}"""
        expect = 'for,(,i,=,0,,,i,<,10,,,i,+,1,),{,print,(,i,),},<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 162))
        
    def test_stmt13(self):
        #63
        input = """ while(true) {print(i)}"""
        expect = 'while,(,true,),{,print,(,i,),},<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 163))
        
    def test_stmt14(self):
        #64
        input = """ while(i == 0) {print(i)}"""
        expect = 'while,(,i,==,0,),{,print,(,i,),},<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 164))
        
    def test_stmt15(self):
        #65
        input = """do {print(i)} while(i == 0);"""
        expect = 'do,{,print,(,i,),},while,(,i,==,0,),;,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 165))
    
    def test_stmt16(self):
        #66
        input = """ while(i * 4 == 20) {print(i)}"""
        expect = 'while,(,i,*,4,==,20,),{,print,(,i,),},<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 166))
        
    def test_stmt17(self):
        #67
        input = """ while(i == 0) {break}"""
        expect = 'while,(,i,==,0,),{,break,},<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 167))
        
    def test_stmt18(self):
        #68
        input = """ while(i == 0) {continue}"""
        expect = 'while,(,i,==,0,),{,continue,},<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 168))
        
    def test_stmt19(self):
        #69
        input = """ while(i == 0) {x=4; continue;}"""
        expect = 'while,(,i,==,0,),{,x,=,4,;,continue,;,},<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 169))
        
    def test_stmt20(self):
        #70
        input = """ if (y >= 25) x = 3;"""
        expect = 'if,(,y,>=,25,),x,=,3,;,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 170))
        
    def test_stmt21(self):
        #71
        input = """ if (y >= 25)x = 309 else x = 611;"""
        expect = 'if,(,y,>=,25,),x,=,309,else,x,=,611,;,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 171))
        
    def test_stmt22(self):        
        #72
        input = """ for (i = 0, i <n1, i+1) {print(i * 24 + y)}"""
        expect = 'for,(,i,=,0,,,i,<,n1,,,i,+,1,),{,print,(,i,*,24,+,y,),},<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 172))
        
    def test_stmt23(self):
        #73
        input = """ while(y != 5) {print(i * 5)}"""
        expect = 'while,(,y,!=,5,),{,print,(,i,*,5,),},<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 173))
        
    def test_stmt24(self):
        #74
        input = """ while(i == 0) {print(i + 9 - po)}"""
        expect = 'while,(,i,==,0,),{,print,(,i,+,9,-,po,),},<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 174))
        
    def test_stmt25(self):
        #75
        input = """
            do {
                print(i * (x + 5) - 8);
                x = 25;
            } while(i != 0);"""
        expect = 'do,{,print,(,i,*,(,x,+,5,),-,8,),;,x,=,25,;,},while,(,i,!=,0,),;,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 175))
        
    def test_stmt26(self):
        #76
        input = """ while(x && y) {print(i)}"""
        expect = 'while,(,x,&&,y,),{,print,(,i,),},<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 176))
        
    def test_stmt27(self):
        #77
        input = """ while(x && y) {break}"""
        expect = 'while,(,x,&&,y,),{,break,},<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 177))
        
    def test_stmt28(self):
        #78
        input = """ while(x && y) {continue}"""
        expect = 'while,(,x,&&,y,),{,continue,},<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 178))
        
    def test_stmt29(self):
        #79
        input = """ while(j == 0 || check) {x = 2;continue;}"""
        expect = 'while,(,j,==,0,||,check,),{,x,=,2,;,continue,;,},<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 179))
        
    def test_stmt30(self):
        #80
        input = """
        b: integer;
        /* b is an integer */
        // a is an negative number
        a: integer = -30;
        """
        expect = 'b,:,integer,;,a,:,integer,=,-,30,;,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 180))
        
    def test_vardecl6(self):
        #81
        input = """
        f: boolean;
        a: string;
        uuuuu: integer;
        """
        expect = 'f,:,boolean,;,a,:,string,;,uuuuu,:,integer,;,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 181))
        
    def test_vardecl7(self):
        #82
        input = """ _ayy89,f0_99_ab: integer = 19, 4200; """
        expect = '_ayy89,,,f0_99_ab,:,integer,=,19,,,4200,;,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 182))
    
    def test_float3(self):
        #83
        input = """ 1_325_477_000 """
        expect = '1325477000,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 183))
        
    def test_float4(self):
        #84
        input = """ 1_325_477_000.16675678 """
        expect = '1325477000.16675678,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 184))
    
    def test_float5(self):
        #85
        input = "1_3254.1E78"
        expect = "13254.1E78,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 185))
        
    def test_vardecl8(self):
        #86
        input = "tyuuu: boolean = false;"
        expect = "tyuuu,:,boolean,=,false,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 186))
    
    def test_str3(self):
        #87
        input = """ "Forever lov3 Ya \\#" """
        expect = 'Illegal Escape In String: Forever lov3 Ya \\#'
        self.assertTrue(TestLexer.test(input, expect, 187))
        
    def test_str4(self):
        #88
        input = """ "Can Cound How to get how to come \\f" """
        expect = 'Can Cound How to get how to come \\f,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 188))
        
    def test_str5(self):
        #89
        input = """ {"AOT","Kumeno alphano be 89","088","Cool and warm ha no mata"} """
        expect = '{,AOT,,,Kumeno alphano be 89,,,088,,,Cool and warm ha no mata,},<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 189))
        
    def test_empty_block(self):
        #90
        input = """ {} """
        expect = '{,},<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 190))
    
    def test_vardecl10(self):    
        #91
        input = """ abfunc: function void {} """
        expect = 'abfunc,:,function,void,{,},<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 191))
        
    
    def test_stmt31(self):    
        #92
        input = """ 
            {
                f(123,33);
                print("Halo goal");
            } """
        expect = '{,f,(,123,,,33,),;,print,(,Halo goal,),;,},<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 192))
        
    def test_vardecl11(self):
        #93
        input = """ 
            {
                a[0] = 23;
                a[1] = 45;
                f(123,33);
                print("Halo goal");
            } """
        expect = '{,a,[,0,],=,23,;,a,[,1,],=,45,;,f,(,123,,,33,),;,print,(,Halo goal,),;,},<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 193))
        
    def test_vardecl12(self):
        #94
        input = """ 
            {
                a[0] = "gun sola";
                a[1] = "minimal central lesyser";
                f(123,33);
                print("Halo goal");
            } """
        expect = '{,a,[,0,],=,gun sola,;,a,[,1,],=,minimal central lesyser,;,f,(,123,,,33,),;,print,(,Halo goal,),;,},<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 194))
        
    
    def test_vardecl13(self):
        #95
        input = """ 
            {
                foo(true,123,45);
                a[0] = "gacha";
                a[1] = "soka soyu kotoka";
            } """
        expect = '{,foo,(,true,,,123,,,45,),;,a,[,0,],=,gacha,;,a,[,1,],=,soka soyu kotoka,;,},<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 195))
    
    def test_stmt32(self):
        #96
        input = """ 
            {
                break;
                continue;
                return f(12,"ui") == g(123.4E3)
            } """
        expect = '{,break,;,continue,;,return,f,(,12,,,ui,),==,g,(,123.4E3,),},<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 196))
        
    
    def test_stmt33(self):
        #97
        input = """ 
            {
                for (j = 10, j <90, j + 1) {
                    foo(90);
                    go(12_213.123);
                }
            } """
        expect = '{,for,(,j,=,10,,,j,<,90,,,j,+,1,),{,foo,(,90,),;,go,(,12213.123,),;,},},<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 197))
        
    
    def test_vardecl15(self):
        #98
        input = """ 
            {
                x = 1902;
                y = (x * 8) / 40 % 1000;
            } """
        expect = '{,x,=,1902,;,y,=,(,x,*,8,),/,40,%,1000,;,},<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 198))
        
    def test_str6(self):
        #99
        input = """ "Im here just to say that ya code is error """
        expect = 'Unclosed String: Im here just to say that ya code is error '
        self.assertTrue(TestLexer.test(input, expect, 199))
        
    
    def test_vardecl16(self):
        #100
        input = """ 
            {
                arr[1,2] = 12_900;
                arr[1,3] = 90_877;
            } """
        expect = '{,arr,[,1,,,2,],=,12900,;,arr,[,1,,,3,],=,90877,;,},<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 200))