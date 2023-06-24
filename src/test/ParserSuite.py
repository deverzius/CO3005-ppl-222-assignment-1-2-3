import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    #1
    def test_vardecl(self):
        input = """ x,y,z: integer; """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))
    
    #2
    def test_vardecl_2(self):
        input = """ 
            x,y,z: boolean;
            x,y,z: float;
            x,y,z: string;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))
        
    #3
    def test_vardecl_3(self):
        input = """ x,y,z: ; """
        expect = "Error on line 1 col 8: ;"
        self.assertTrue(TestParser.test(input, expect, 203))
        
    #4
    def test_vardecl_4(self):
        input = """ x,y,z string; """
        expect = "Error on line 1 col 7: string"
        self.assertTrue(TestParser.test(input, expect, 204))
        
    #5
    def test_vardecl_5(self):
        input = """ x,y,z: void; """
        expect = "Error on line 1 col 8: void"
        self.assertTrue(TestParser.test(input, expect, 205))
    
    #6
    def test_vardecl_6(self):
        input = "a, b, c, d: integer = 3, 4, 6;"
        expect = 'Error on line 1 col 29: ;'
        self.assertTrue(TestParser.test(input, expect, 206))
    
    #7
    def test_vardecl_7(self):
        input = """ a, b, c: string = "a123", "b123","c332"; """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 207))
    
    #8
    def test_vardecl_8(self):
        input = """ x: float = 123E9 """
        expect = "Error on line 1 col 18: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 208))
        
    #9
    def test_vardecl_9(self):
        input = """ x float = 123E9; """
        expect = "Error on line 1 col 3: float"
        self.assertTrue(TestParser.test(input, expect, 209))
        
    #10
    def test_vardecl_10(self):
        input = """ x :   = 123E9; """
        expect = "Error on line 1 col 7: ="
        self.assertTrue(TestParser.test(input, expect, 210))
        
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 211))
        
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 212))
        
    #13
    def test_fundecl_3(self):
        input = """ 
            print: function integer (out inherit msg: string) {
                return 0;
            }
        """
        expect = "Error on line 2 col 41: inherit"
        self.assertTrue(TestParser.test(input, expect, 213))
        
    #14
    def test_fundecl_4(self):
        input = """ 
            print: function integer (out inherit type: integer, x: float) {
                return str(type) + str(x);
            }
        """
        expect = "Error on line 2 col 41: inherit"
        self.assertTrue(TestParser.test(input, expect, 214))
        
    #15
    def test_fundecl_5(self):
        input = """ 
            print: function integer (inherit msg: string, out type: integer, x: float) {
                return msg + str(type) + str(x);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 215))
        
    #16
    def test_fundecl_6(self):
        input = """ 
            print: function integer (inherit msg: string, out type, x: float) {
                return msg + str(type) + str(float);
            }
        """
        expect = "Error on line 2 col 66: ,"
        self.assertTrue(TestParser.test(input, expect, 216))
        
    #17
    def test_fundecl_7(self):
        input = """ 
            func: void (msg: string) {
                print(msg);
            }
        """
        expect = "Error on line 2 col 18: void"
        self.assertTrue(TestParser.test(input, expect, 217))
        
    #18
    def test_fundecl_8(self):
        input = """ 
            func: function void (msg: string) {}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 218))
    
    #19
    def test_expr_1(self):
        input = """ 
            x: integer;
            y = 5;
        """
        expect = "Error on line 3 col 14: ="
        self.assertTrue(TestParser.test(input, expect, 219))
        
    #20
    def test_expr_2(self):
        input = """ 
            main: function void() {
                x: integer;
                y = 5;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 220))
        
    #21
    def test_expr_3(self):
        input = """ 
            main: function void() {
                x: integer;
                x = ((167 - 89) + 90 * 178 / 54) % 123);
            }
        """
        expect = "Error on line 4 col 54: )"
        self.assertTrue(TestParser.test(input, expect, 221))
        
    
    #22
    def test_expr_4(self):
        input = """ 
            main: function void() {
                x: float = (((167 - 89) + 90 * 178 / 54) % 123;
            }
        """
        expect = "Error on line 3 col 62: ;"
        self.assertTrue(TestParser.test(input, expect, 222))
        
    #23
    def test_expr_5(self):
        input = """ 
            check: boolean = true && !(true || (!(false && true)) && false);
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 223))
        
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 224))
        
    #25
    def test_expr_7(self):
        input = """ 
            main: function void() {
                check1, check2: boolean
                    = 4 - (12 - 65) >= (54 + 90 / 3) % 11, (true == false) != false;
                print(check1 == check2);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 225))
        
    #26
    def test_arr_1(self):
        input = """ 
            main: function void() {
                arr: array[10] of integer;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 226))
        
    #27
    def test_arr_2(self):
        input = """ 
            main: function void() {
                arr: array[10, 30] of array;
            }
        """
        expect = "Error on line 3 col 38: array"
        self.assertTrue(TestParser.test(input, expect, 227))
    
    #28
    def test_arr_3(self):
        input = """ 
            main: function void() {
                arr: array[2, 2] of integer = {{1,3},{3,4}};
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 228))
        
    #29
    def test_arr_4(self):
        input = """ 
            main: function void() {
                arr: array[2, 2] of integer = {{1123,345214},334534};
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 229))
        
    #30
    def test_arr_5(self):
        input = """ 
            main: function void() {
                arr: array[3] of integer = {};
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 230))
        
    #31
    def test_arr_6(self):
        input = """ 
            main: function void() {
                a1,a2: array[76] of float = {12_542.3,4E-8,1.2}, {43.3e20,12.3,8_990_400.12};
                a1[3] = 129_300;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 231))
        
    #32
    def test_arr_7(self):
        input = """ 
            main: function array() {}
        """
        expect = "Error on line 2 col 32: ("
        self.assertTrue(TestParser.test(input, expect, 232))
        
    #33
    def test_arr_8(self):
        input = """ 
            main: function void() {
                arr: array[7_854] of integer = {y,z,t};
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 233))
        
    #34
    def test_arr_9(self):
        input = """ 
            main: function void() {
                arr: array[67] of integer = {y + 9,z * 8,t};
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 234))
        
    #35
    def test_func_call_1(self):
        input = """ 
            main: function void() {
                foo(x * 8, 90, 89_890.332, "Hello");
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 235))
    
    #36
    def test_stmt_1(self):
        input = """ 
            main: function void() {
                x: integer = foo(x * 8, 90, 89_890.332, "Hello");
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 236))
    
    #37
    def test_stmt_2(self):
        input = """ 
            main: function void() {
                x: integer = (foo(x * 8, 90, 89_890.332, "Hello")) * 8 - (foo(x * 18, y / 4));
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 237))
    
    #38
    def test_stmt_3(self):
        input = """ 
            main: function auto() {
                if (x == 3) {
                    print("Hello");
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 238))
        
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 239))
        
    #40
    def test_stmt_5(self):
        input = """ 
            main: function auto() {
                if (x = 8) {
                    print("Hello");
                }
                else print("olleHh dsjakhfjk !!!lsadhkljfdsh");
            }
        """
        expect = "Error on line 3 col 22: ="
        self.assertTrue(TestParser.test(input, expect, 240))
        
    #41
    def test_stmt_6(self):
        input = """ 
            main: function auto() {
                if (x == (8 == 9) && (9 != 10 - 2)) {
                    print("Hello");
                }
                else {
                    print("olleH");
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 241))
        
    #42
    def test_stmt_7(self):
        input = """ 
            main: function float() {
                if (x == (true == "Hel world") && (9 != 10 - 2)) {
                    print("Hello");
                }
                else if (x == 3) {
                    print("olleH");
                }
                else print ("Else statement is executed");
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 242))
    
    #43
    def test_stmt_8(self):
        input = """ 
            main: function float() {
                if (x == (true == "Hel world") && (9 != 10 - 2)) {
                    print("Hello");
                }
                else if (x == 3 - o + fjk / 89) {
                    print("olleH");
                }
                else print ("Else statement is executed");
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 243))
    
    #44
    def test_stmt_9(self):
        input = """ 
            main: function float() {
                if (x == (true == "Hel world") || !(x >= y) && y > z) {
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 244))
        
    #45
    def test_stmt_10(self):
        input = """ 
            main: function float() {
                if (x == (true == "Hel world") || !(x >= y) && y > z) {
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 245))
    
    #46
    def test_stmt_11(self):
        input = """ 
            main: function float() {
                if (x == (true == "Hel world") || !(x >= y) && y > z) {
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 246))
    
    #47
    def test_stmt_12(self):
        input = """ 
            main: function float() {
                else if (x == 3) {
                    print("olleH 3");
                    x: integer = 12;
                }
                else print ("Else statement is executed");
            }
        """
        expect = "Error on line 3 col 16: else"
        self.assertTrue(TestParser.test(input, expect, 247))
    
    #48
    def test_stmt_13(self):
        input = """ 
            if (x == 3) {
                print("olleH 3");
                x: integer = 12;
            }
            else print ("Else statement is executed");
        """
        expect = "Error on line 2 col 12: if"
        self.assertTrue(TestParser.test(input, expect, 248))
    
    
    #49
    def test_stmt_14(self):
        input = """ 
            main: function float() {
                for (i = 0, i < 10, i + 1) {
                    print(i);
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 249))
    
    #50
    def test_stmt_15(self):
        input = """ 
            main: function void() {
                for (i = 0, i < 10 * 8 - 0 / 2 + "huhuuuuhihi" && "hihi:::", i + 1)
                    print(i);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 250))
    
    #51
    def test_stmt_16(self):
        input = """ 
            main: function float() {
                for (i == 0, i < 80, i + 3) {
                    print(i);
                }
            }
        """
        expect = "Error on line 3 col 23: =="
        self.assertTrue(TestParser.test(input, expect, 251))
    
    #52
    def test_stmt_17(self):
        input = """ 
            main: function float() {
                for (i = -20.908; i < 17_000; i * 8) {
                    print(i);
                }
            }
        """
        expect = "Error on line 3 col 32: ;"
        self.assertTrue(TestParser.test(input, expect, 252))
    
    #53
    def test_stmt_18(self):
        input = """ 
            main: function void() {
                for (i = (87 - 90) / 3 + (1 % 20) - 8, i < 100, i * 2) {
                    print(i);
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 253))
    
    #54
    def test_stmt_19(self):
        input = """ 
            main: function void() {
                for (i = false && (true || false) && foo(1,2,3,4), i != true, !i) {
                    print(i);
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 254))
    
    #55
    def test_stmt_20(self):
        input = """ 
            main: function void() {
                for (,,,) {
                    print(i);
                }
            }
        """
        expect = "Error on line 3 col 21: ,"
        self.assertTrue(TestParser.test(input, expect, 255))
    
    #56
    def test_stmt_21(self):
        input = """ 
            main: function void() {
                while() {
                    print("Hello");
                }
            }
        """
        expect = "Error on line 3 col 22: )"
        self.assertTrue(TestParser.test(input, expect, 256))
        
    
    #57
    def test_stmt_22(self):
        input = """ 
            main: function void() {
                while(true) {
                    print("Hello");
                    x: string = "Hello I " :: "wanna play" :: "a game";
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 257))
    
    #58
    def test_stmt_23(self):
        input = """ 
            main: function void() {
                while(true)
                    print("Hello");
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 258))
    
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 259))
    
    #60
    def test_stmt_25(self):
        input = """ 
            main: function void() {
                while(true) {
                    print("Hello");
                    sum: integer = func(2,3);
            }
            
            func: function integer(a:integer, b:integer) {
                return a + b;
            }
        """
        expect = "Error on line 8 col 18: function"
        self.assertTrue(TestParser.test(input, expect, 260))
    
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 261))
    
    #62
    def test_stmt_27(self):
        input = """ 
            main: function void() {
                do {
                    print("Hello");
                    sum: integer = func(2,3);
                }
                while ();
            }
        """
        expect = "Error on line 7 col 23: )"
        self.assertTrue(TestParser.test(input, expect, 262))
    
    #63
    def test_stmt_28(self):
        input = """ 
            main: function void() {
                do {
                    prod: float = mul(8_987, 45.233);
                }
                while (x)
            }
        """
        expect = "Error on line 7 col 12: }"
        self.assertTrue(TestParser.test(input, expect, 263))
        
    #64
    def test_stmt_29(self):
        input = """ 
            main: function void() {
                do {
                    prod: float = mul(8_987, 45.233);
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 264))
        
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 265))
    
    #66
    def test_stmt_31(self):
        input = """ 
            break;
            continue;
        """
        expect = "Error on line 2 col 12: break"
        self.assertTrue(TestParser.test(input, expect, 266))
        
    #67
    def test_stmt_32(self):
        input = """ 
            main: function void() {
                foo(1,2,3,4,5);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 267))
    
    #68
    def test_stmt_33(self):
        input = """ 
            main: function void() {
                foo(2 * x, 7 + y,3 + z, true,"abczys");
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 268))
    
    #69
    def test_stmt_34(self):
        input = """ 
            main: function void() {
                foo(2 * x, true, "abczys", foo(5_900, !false, "Hello\\nXin chao"));
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 269))
    
    #70
    def test_stmt_35(self):
        input = """ 
            main: function void() {
                callFunction();
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 270))
    
    #71
    def test_stmt_36(self):
        input = """ 
            main: function void() {
                a, b: string = "abc", "\\n Hello";
                print(a,c,b);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 271))
    
    #72
    def test_stmt_37(self):
        input = """ 
            main: function void() {
                {
                    {
                        a, b: string = "abc", "\\n Hello";
                        print(a,c,b);
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 272))
    
    #73
    def test_stmt_38(self):
        input = """ 
            main: function void() {
                {
                    x, y: integer;
                    {
                        a, b: string = "abc", "\\n Hello";
                        print(a,c,b);
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 273))
    
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
                    z, t: integer;
                    {
                        f, u: integer;
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 274))
    
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 275))
    
    #76
    def test_stmt_41(self):
        input = """ 
            main: function void() {
                while (true)
                    x: integer = 5;
            }
        """
        expect = "Error on line 4 col 21: :"
        self.assertTrue(TestParser.test(input, expect, 276))
    
    #77
    def test_cmt_1(self):
        input = """ 
            main: function void() {
                /* Hello world */ x:integer = 13; */
            }
        """
        expect = "Error on line 3 col 50: *"
        self.assertTrue(TestParser.test(input, expect, 277))
    
    #78
    def test_cmt_2(self):
        input = """ 
            /*  Hello world 
                x:integer = 13;
                y: float
                while
                $$$$
                ####
            */
            main: function void() {
                /*  Hello world 
                    x:integer = 13;
                    y: float
                    while
                    $$$$
                    ####
                */
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 278))
    
    #79
    def test_cmt_3(self):
        input = """
            //  Hello world 
            //  x:integer = 13;
            //  y: float
            //  while
            //  $$$$
            //  ####
            main: function void() {
                //  Hello world 
                //  x:integer = 13;
                //  y: float
                //  while
                //  $$$$
                //  ####
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 279))
        
    #80
    def test_cmt_4(self):
        input = """ 
            main: function void() {
                /////
                /* /**/ */
            }
        """
        expect = "Error on line 4 col 24: *"
        self.assertTrue(TestParser.test(input, expect, 280))
    
    #81
    def test_cmt_5(self):
        input = """ 
            main: function void() {
                ///// Toi da rot, ban thi sao
                /* world /* Hello*/
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 281))
    
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 282))
    
    #83
    def test_mix_2(self):
        input = """ 
            fun: function integer(out i: integer) {
                do
                    xyz = 0;
                while(x == 3);
                
                return 9 * x + 8 * y;
            }
        
            main: function void() {
                t: integer = 990_000;
                x: float = fun(t);
                print(x);
            }
        """
        expect = "Error on line 4 col 20: xyz"
        self.assertTrue(TestParser.test(input, expect, 283))
    
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 284))
    
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 285))
    
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 286))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 287))
    
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 288))
    
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 289))
    
    #90
    def test_mix_9(self):
        input = """ 
			x,y: integer;
			a,b,c: float;
			_f1: function array[1,9,111] of integer(inherit z: array[10] of boolean, jklasd: string) {
				do {
					if (x == 90) {
                        0 - 80 + (((das * hj) -dsf) :: "abcxyz");
					}
				}
				while (true != a - 90 + (bjnka / fhg - 23))
			}
            main: function void() {
                _f1(90, {"ds",1,4,{abc,34,"string"}});
            }
            _bakd: array;
            _ds_12: boolean;
        """
        expect = "Error on line 7 col 24: 0"
        self.assertTrue(TestParser.test(input, expect, 290))
    
    #91
    def test_mix_10(self):
        input = """ 
            main: function void() {
                _jnkandf, _____: boolean=
					"Hello \\n" || bo && !cal,
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 291))
        
    
    #92
    def test_mix_11(self):
        input = """ 
            main: function void() {
                while (true)
					while (true)
						while (true)
							while if (x ==0)
								return (((((((((f(90 - p) * true - false)))))))));
            }
        """
        expect = "Error on line 6 col 13: if"
        self.assertTrue(TestParser.test(input, expect, 292))
    
    
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 293))
    
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 294))
    
    #95
    def test_mix_14(self):
        input = """ 
            main: function void() {
                while (true) {
					break;
					x: integer = hjk_90 + jksd, jdflk || hjdksah * yuid - !kslj;
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
        expect = "Error on line 5 col 31: ,"
        self.assertTrue(TestParser.test(input, expect, 295))
        
        
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 296))
    
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 297))
    
    
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 298))
    
    #99
    def test_mix_18(self):
        input = """ 
            main: function void(check: boolean) inherit main {
                arrayy: array[100] of integer = {};
                do {
					if (true) {}
					else if (true) {}
				} while (true)
                float: integer;
            }
        """
        expect = "Error on line 8 col 16: float"
        self.assertTrue(TestParser.test(input, expect, 299))
    
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
                arr: boolean = {integer, float, boolean};
            }
        """
        expect = "Error on line 26 col 32: integer"
        self.assertTrue(TestParser.test(input, expect, 300))