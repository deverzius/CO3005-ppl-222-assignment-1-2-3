from Visitor import Visitor
from StaticError import *
from AST import *
from functools import reduce


class LoopStmt(Stmt):
    def __init__(self):
        self.name = "#loop"
    pass

class UnknownType(AtomicType):
    def __str__(self):
        return self.__class__.__name__

class Utils:
    @staticmethod
    def getTypeByName(name, kind: Kind, o):
        for env in o:
            for decl in env:
                if name == decl.name:
                    if hasattr(decl, 'return_type'):
                        return decl.return_type
                    return decl.typ
        raise Undeclared(kind, name)
    
    @staticmethod
    def getCtxByName(name, o):
        for env in o:
            for decl in env:
                if name == decl.name:
                    return decl
        return None

    @staticmethod
    def getFunctionParams(ctx, o):
        name = ctx.name
        for env in o:
            for decl in env:
                if name == decl.name and hasattr(decl, 'return_type'):
                    return decl.params
                # variable case
                elif name == decl.name:
                    raise TypeMismatchInExpression(ctx)
        raise Undeclared(Function(), name)
    

    @staticmethod
    def isTypeCompatible(lhs: Type, rhs: Type):
        # if type(lhs) is ArrayType:
        #     if type(rhs) is ArrayLit:
        #         if not Utils.isTypeCompatible(lhs.typ, rhs.typ):
        #             return False
        if type(lhs) is ArrayType and type(rhs) is ArrayType:
            if not Utils.compareArrayType(lhs, rhs):
                return False
        
        if type(lhs) is FloatType and type(rhs) is IntegerType:
            return True
        if type(lhs) is type(rhs):
            return True
        return False
    
    @staticmethod
    def compareArrayType(at1, at2):
        if not (type(at1.typ) is type(at2.typ)):
            return False
        
        if len(at1.dimensions) != len(at2.dimensions):
            return False
                
        for i in range(len(at1.dimensions)):
            if at1.dimensions[i] != at2.dimensions[i]:
                return False
        
        return True
    
    # @staticmethod
    # def isTypeEquivalent(lhs: Type, rhs: Type):
    #     if type(lhs) is ArrayType and type(rhs) is ArrayType:
    #         if not Utils.isTypeEquivalent(lhs.typ, rhs.typ):
    #             return False

    #     if type(lhs) is type(rhs):
    #         return True
    #     return False
    
    
    @staticmethod
    def castFunctionAutoType(name: str, typ: Type, o):
        for idx, fundecl in enumerate(o[-1]): 
            if fundecl.name == name:
                o[-1][idx].return_type = typ
                break
        return o
    
    @staticmethod
    def castParamAutoType(param_name: str, func_name: str, typ: Type, o):
        for i, fundecl in enumerate(o[-1]): 
            if fundecl.name == func_name:
                for j, param in enumerate(fundecl.params):
                    if param.name == param_name:
                        o[-1][i].params[j].typ = typ
        return o
    
    @staticmethod
    def printObjectList(o):
        print('=======================================')
        for i, env in enumerate(o):
            print('** Scope ' + str(i))
            for decl in env:
                print(decl.name + ' ' + str(type(decl.typ)) if decl.typ else str(type(decl.return_type)))
            print('** End scope ' + str(i))
        print('=======================================')

class StaticChecker(Visitor):
    def __init__(self, ast):
        self.ast = ast
    
    def check(self):
        return self.visit(self.ast, [[]])
    
    def visitIntegerType(self, ctx, o): pass
    def visitFloatType(self, ctx, o): pass
    def visitBooleanType(self, ctx, o): pass
    def visitStringType(self, ctx, o): pass
    def visitArrayType(self, ctx, o):
        return ArrayType(ctx.dimensions, ctx.typ)
            
    def visitAutoType(self, ctx, o): pass
    def visitVoidType(self, ctx, o): pass

    # EXPRESSION'S VISITOR
    def visitBinExpr(self, ctx, o):        
        ltyp = self.visit(ctx.left, o)
        rtyp = self.visit(ctx.right, o)
        
        if type(ltyp) is AutoType and type(ctx.left) is FuncCall:
            o = Utils.castFunctionAutoType(ctx.left.name, rtyp, o)
            ltyp = rtyp
        
        if type(rtyp) is AutoType and type(ctx.right) is FuncCall:
            o = Utils.castFunctionAutoType(ctx.right.name, ltyp, o)
            rtyp = ltyp
        
        if ctx.op in ['+', '-', '*', '/']:
            # if type(ltyp) is AutoType and type(rtyp) in [IntegerType, FloatType]:
            if type(ltyp) in [IntegerType, FloatType] and type(rtyp) in [IntegerType, FloatType]:
                return IntegerType() if (type(ltyp) is IntegerType and type(rtyp) is IntegerType) else FloatType()
            raise TypeMismatchInExpression(ctx)
        
        if ctx.op == '%':
            if type(ltyp) is IntegerType and type(rtyp) is IntegerType:
                return IntegerType()
            raise TypeMismatchInExpression(ctx)
        
        if ctx.op in ['!', '&&', '||']:
            if type(ltyp) is BooleanType and type(rtyp) is BooleanType:
                return BooleanType()
            raise TypeMismatchInExpression(ctx)
        
        if ctx.op == '::':
            if type(ltyp) is StringType and type(rtyp) is StringType:
                return StringType()
            raise TypeMismatchInExpression(ctx)
        
        if ctx.op in ['==','!=']:
            if type(ltyp) is type(rtyp):
                if type(ltyp) in [IntegerType, BooleanType]:
                    return BooleanType()
            raise TypeMismatchInExpression(ctx)
        
        if ctx.op in ['>','>=','<','<=']:
            # if type(ltyp) is type(rtyp):
            #     if type(ltyp) in [IntegerType, FloatType]:
            if type(ltyp) in [IntegerType, FloatType]:
                if type(rtyp) in [IntegerType, FloatType]:
                    return BooleanType()
            raise TypeMismatchInExpression(ctx)
                
        
    def visitUnExpr(self, ctx, o):
        typ = self.visit(ctx.val, o)
        
        if ctx.op == '!':
            if type(typ) is BooleanType:
                return BooleanType()
            if type(typ) is AutoType and type(ctx.val) is FuncCall:
                o = Utils.castFunctionAutoType(ctx.val.name, BooleanType(), o)
                return BooleanType()
        else:
            if type(typ) in [IntegerType, FloatType]:
                return typ
            if type(typ) is AutoType and type(ctx.val) is FuncCall:
                o = Utils.castFunctionAutoType(ctx.val.name, IntegerType(), o)
                return IntegerType()
        
        raise TypeMismatchInExpression(ctx)
    
    def visitId(self, ctx, o):
        for env in o:
            for decl in env:
                if ctx.name == decl.name and type(decl) is not FuncDecl:
                    return decl.typ
        raise Undeclared(Identifier(), ctx.name)
        
    def visitArrayCell(self, ctx, o):
        arrayTyp = Utils.getTypeByName(ctx.name, Identifier(), o)
        # id is not array type
        if not hasattr(arrayTyp, 'dimensions'):
            raise TypeMismatchInExpression(ctx)
        
        for expr in ctx.cell:
            typ = self.visit(expr, o)
            if not type(typ) is IntegerType:
                raise TypeMismatchInExpression(ctx)
        
        # return atomic type
        return arrayTyp.typ
        
    def visitIntegerLit(self, ctx, o):
        return IntegerType()
    def visitFloatLit(self, ctx, o):
        return FloatType()
    def visitStringLit(self, ctx, o):
        return StringType()
    def visitBooleanLit(self, ctx, o): 
        return BooleanType()
    
    
    def getArrayLitAtomicTyp(self, ctx, o):
        if not hasattr(ctx, 'explist'):
            return self.visit(ctx, o) 
        if len(ctx.explist) == 0:
            return UnknownType()
        return self.getArrayLitAtomicTyp(ctx.explist[0], o)
    
    def getArrayLitType(self, ctx, atomictyp, root_ctx, o):
        # atomic type
        if not hasattr(ctx.explist[0], "explist"):
            return ArrayType([len(ctx.explist)], atomictyp)
        
        curTyp = None
        for expr in ctx.explist:
            exprTyp = self.getArrayLitType(expr, atomictyp, root_ctx, o)
            
            if curTyp is None:
                curTyp = exprTyp
            elif not Utils.compareArrayType(exprTyp, curTyp):
                raise IllegalArrayLiteral(root_ctx)
        
        return ArrayType([len(ctx.explist)] + exprTyp.dimensions, atomictyp)
        
    def visitArrayLit(self, ctx, o):
        atomictyp = self.getArrayLitAtomicTyp(ctx, o)
        arrayType = self.getArrayLitType(ctx, atomictyp, ctx, o)
        # print(arrayType)
        return arrayType
    
    
    
    def visitFuncCall(self, ctx, o):
        params = Utils.getFunctionParams(ctx, o)
        
        # if len(ctx.args) < len(params):
        #     raise TypeMismatchInExpression()
        # if len(ctx.args) > len(params):
        #     errIdx = len(params)
        #     raise TypeMismatchInExpression(ctx.args[errIdx])
        if len(ctx.args) != len(params):
            raise TypeMismatchInExpression()
        
        paramsTypList = [x.typ for x in params]
        
        for i, arg in enumerate(ctx.args):
            argtyp = self.visit(arg, o)
            
            if type(paramsTypList[i]) is AutoType:
                Utils.castParamAutoType(params[i].name, ctx.name, argtyp, o)
                continue
            
            if not Utils.isTypeCompatible(paramsTypList[i], argtyp):
                raise TypeMismatchInExpression(ctx)
        
        funCallTyp = Utils.getTypeByName(ctx.name, Function(), o)
        if type(funCallTyp) is VoidType:
            raise TypeMismatchInExpression(ctx)
        # type(x) is ParamDecl
            
        return funCallTyp

    # STATEMENT'S VISITOR
    def visitAssignStmt(self, ctx, o):
        ltyp = self.visit(ctx.lhs, o)
        rtyp = self.visit(ctx.rhs, o)
        
        if type(ltyp) is VoidType or type(ltyp) is ArrayType:
            raise TypeMismatchInStatement(ctx)
        
        if type(rtyp) is AutoType and type(ctx.rhs) is FuncCall:
            o = Utils.castFunctionAutoType(ctx.rhs.name, ltyp, o)
            return o

        if Utils.isTypeCompatible(ltyp, rtyp):
            return o
        raise TypeMismatchInStatement(ctx)
        
    def visitBlockStmt(self, ctx, o):
        # Block Statement creates new scope
        env = [[]] + o
        for stmt in ctx.body:
            env = self.visit(stmt, env)
        return o
        
    def visitIfStmt(self, ctx, o):
        cond = self.visit(ctx.cond, o)
        if not (type(cond) is BooleanType):
            raise TypeMismatchInStatement(ctx)
        
        o = self.visit(ctx.tstmt, o)
        if ctx.fstmt:
            o = self.visit(ctx.fstmt, o)
        return o
        
    def visitForStmt(self, ctx, o):
        initLhsName = ctx.init.lhs.name
        initRhsTyp = self.visit(ctx.init.rhs, o)
        
        if not type(initRhsTyp) is IntegerType:
            raise TypeMismatchInStatement(ctx)
        
        # change here
        env = [[VarDecl(initLhsName, IntegerType(), ctx.init.rhs), LoopStmt()]] + o
        
        condTyp = self.visit(ctx.cond, env)
        if not (type(condTyp) is BooleanType):
            raise TypeMismatchInStatement(ctx)
        
        updtyp = self.visit(ctx.upd, env)
        if not (type(updtyp) is IntegerType):
            raise TypeMismatchInStatement(ctx)
        
        if type(ctx.stmt) is BlockStmt:
            for stmt in ctx.stmt.body:
                env = self.visit(stmt, env)
        else:
            env = self.visit(ctx.stmt, env)
            
        return o
        
    def visitWhileStmt(self, ctx, o): 
        env = [[LoopStmt()]] + o
        cond = self.visit(ctx.cond, env)
        if not (type(cond) is BooleanType):
            raise TypeMismatchInStatement(ctx)
        
        env = self.visit(ctx.stmt, env)
        return o
        
    def visitDoWhileStmt(self, ctx, o):
        env = [[LoopStmt()]] + o
        cond = self.visit(ctx.cond, env)
        if not (type(cond) is BooleanType):
            raise TypeMismatchInStatement(ctx)
        
        env = self.visit(ctx.stmt, env)
        return o
        
    def visitBreakStmt(self, ctx, o):
        for env in o:
            for decl in env:
                if type(decl) is LoopStmt:
                    return o
        raise MustInLoop(ctx)
    
    def visitContinueStmt(self, ctx, o):
        for env in o:
            for decl in env:
                if type(decl) is LoopStmt:
                    return o
        raise MustInLoop(ctx)
    
    def visitReturnStmt(self, ctx, o):
        # stmt duy nhat k return o
        returnStmtTyp = self.visit(ctx.expr, o)
        return returnStmtTyp

    def visitCallStmt(self, ctx, o):
        funTyp = Utils.getTypeByName(ctx.name, Function(), o)
        # if not type(funTyp) is VoidType:
        #     raise TypeMismatchInStatement(ctx)
        params = Utils.getFunctionParams(ctx, o)
        paramsTypList = [x.typ for x in params]
        
        if len(ctx.args) != len(params):
            raise TypeMismatchInStatement()
        
        for i, arg in enumerate(ctx.args):
            argtyp = self.visit(arg, o)
            
            if type(paramsTypList[i]) is AutoType:
                Utils.castParamAutoType(params[i].name, ctx.name, argtyp, o)
                continue
            
            if not Utils.isTypeCompatible(argtyp, paramsTypList[i]):
                raise TypeMismatchInStatement(ctx)
            
        return o

    def visitVarDecl(self, ctx, o):
        for decl in o[0]:
            if ctx.name == decl.name:
                raise Redeclared(Variable(), ctx.name)
        
        
        if ctx.init:
            initTyp = self.visit(ctx.init, o)
            
            if isinstance(ctx.typ, AutoType):
                ctx.typ = initTyp
            
            elif type(initTyp) is AutoType and type(ctx.init) is FuncCall:
                o = Utils.castFunctionAutoType(ctx.init.name, ctx.typ, o)
            
            elif not Utils.isTypeCompatible(ctx.typ, initTyp):
                raise TypeMismatchInVarDecl(ctx)
        
        elif isinstance(ctx.typ, AutoType):
            raise Invalid(Variable(), ctx.name)
        
        o[0] += [ctx]
        return o
    def visitParamDecl(self, ctx, o):
        for decl in o[0]:
            if ctx.name == decl.name:
                if ctx.inherit == True:
                    raise Invalid(Parameter(), ctx.name)
                else:
                    raise Redeclared(Parameter(), ctx.name)
        return ctx
        
    def visitFuncDecl(self, ctx, o):
        # for decl in o[0]:
        #     if decl.name == ctx.name:
        #         raise Redeclared(Function(), ctx.name)
        # o[0] += [ctx]
        
        env = [[]] + o
        for param in ctx.params:
            env[0] += [self.visit(param, env)]
        
        # Function inherit tức là có các biến từ hàm cha mà không cần khai báo
        # cái para của hàm cha cần có từ khoá inherit
        # hàm super được gọi duy nhất ở dòng đầu tiên
        # hàm k cha k được gọi super
        # k có testcase super nằm ở dòng sau đâu nên đừng bắt
        if ctx.inherit is None:
            if len(ctx.body.body) != 0:
                firstStmt = ctx.body.body[0]
                
                if type(firstStmt) is CallStmt and firstStmt.name == 'super':
                    raise InvalidStatementInFunction(ctx.name)
                
                if type(firstStmt) is CallStmt and firstStmt.name == 'preventDefault':
                    raise InvalidStatementInFunction(ctx.name)
        
        else:
            if len(ctx.body.body) == 0:
                raise InvalidStatementInFunction(ctx.name)
            
            inheritFunc = Utils.getCtxByName(ctx.inherit, o)
            firstStmt = ctx.body.body[0]
            
            if type(firstStmt) is CallStmt and firstStmt.name == 'super':
                # hàm cha không có tham số nhưng cố chấp gọi super
                if len(inheritFunc.params) == 0:
                    raise InvalidStatementInFunction(ctx.name)
                
                if len(firstStmt.args) > len(inheritFunc.params):
                    errIdx = len(inheritFunc.params)
                    raise TypeMismatchInExpression(firstStmt.args[errIdx])
                if len(firstStmt.args) < len(inheritFunc.params):
                    raise TypeMismatchInExpression()
                    
                for i, arg in enumerate(firstStmt.args):
                    argtyp = self.visit(arg, env)
                    if type(argtyp) is not type(inheritFunc.params[i].typ):
                        raise TypeMismatchInExpression(arg)
                    
                    env[0] += [self.visit(inheritFunc.params[i], env)]
            
            elif type(firstStmt) is CallStmt and firstStmt.name == 'preventDefault':
                pass
            else:
                raise InvalidStatementInFunction(ctx.name)
        
        for stmt in ctx.body.body:
            if type(stmt) is CallStmt:
                if stmt.name == 'super' or stmt.name == 'preventDefault':
                    continue
            
            if type(stmt) is ReturnStmt:
                returnStmtTyp = self.visit(stmt, env)
                
                if type(ctx.return_type) is AutoType:
                    Utils.castFunctionAutoType(ctx.name, returnStmtTyp, o)
                    Utils.castFunctionAutoType(ctx.name, returnStmtTyp, env)
                elif type(ctx.return_type) is not type(returnStmtTyp):
                    raise TypeMismatchInStatement(stmt)
                continue
                
            env = self.visit(stmt, env) 
        
        return o

    def visitProgram(self, ctx, o):
        mainExist = False
        
        o = [[
            FuncDecl('readInteger', IntegerType(), [], None, BlockStmt([])),
            FuncDecl('printInteger', VoidType(), [ParamDecl('anArg', IntegerType())], None, BlockStmt([])),
            
            FuncDecl('readFloat', FloatType(), [], None, BlockStmt([])),
            FuncDecl('printFloat', VoidType(), [ParamDecl('anArg', FloatType())], None, BlockStmt([])),
            
            FuncDecl('readBoolean', BooleanType(), [], None, BlockStmt([])),
            FuncDecl('printBoolean', VoidType(), [ParamDecl('anArg', BooleanType())], None, BlockStmt([])),
            
            FuncDecl('readString', StringType(), [], None, BlockStmt([])),
            FuncDecl('printString', VoidType(), [ParamDecl('anArg', StringType())], None, BlockStmt([])),
            
            FuncDecl('super', VoidType(), [], None, BlockStmt([])),
            FuncDecl('preventDefault', VoidType(), [], None, BlockStmt([])),
        ]]
        
        # use function before declaration
        for decl in ctx.decls:
            if type(decl) is FuncDecl:
                if decl.name == 'main' and len(decl.params) == 0 and type(decl.return_type) is VoidType:
                    mainExist = True
                
                for fundecl in o[0]:
                    if fundecl.name == decl.name:
                        raise Redeclared(Function(), fundecl.name)
                o[0] += [decl]

        # print("======")
        # for x in o[0]:
        #     print(x.name)
        # print("======")
        
        for decl in ctx.decls:
            o = self.visit(decl, o)
        
        if mainExist == False:
            raise NoEntryPoint()
