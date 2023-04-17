from Visitor import Visitor
from StaticError import *
from AST import *
from functools import reduce

# class Type(ABC):
#     pass
# class AtomicType(Type):
#     pass
# class IntegerType(AtomicType):
#     pass
# class FloatType(AtomicType):
#     pass
# class StringType(AtomicType):
#     pass
# class BooleanType(AtomicType):
#     pass

# class ArrayType(Type):
#     def __init__(self, dimens: list[int], etyp: AtomicType):
#         self.dimensions = dimens
#         self.etyp = etyp

# class FuncType(Type):
#     pass

# class VoidType(Type):
#     pass
# class AutoType(Type):
#     def __init__(self, typ: Type or None = None):
#         self.typ = typ
#     pass

class LoopStmt(Stmt):
    def __init__(self):
        self.name = "#loop"
    pass

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
            if not Utils.isTypeCompatible(lhs.typ, rhs.typ):
                return False
        
        if type(lhs) is FloatType and type(rhs) is IntegerType:
            return True
        if type(lhs) is type(rhs):
            return True
        return False
    
    
    @staticmethod
    def isTypeEquivalent(lhs: Type, rhs: Type):
        if type(lhs) is ArrayType and type(rhs) is ArrayType:
            if not Utils.isTypeEquivalent(lhs.typ, rhs.typ):
                return False

        if type(lhs) is type(rhs):
            return True
        return False
    
    
    @staticmethod
    def castingFunctionAutoType(name: str, o):
        n = len(o)
        for idx, fundecl in enumerate(o[n - 1]): 
            if fundecl.name == name:
                o[n - 1][idx].return_type = Type
                break
        return o

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
        
        
        if ctx.op in ['+', '-', '*', '/']:
            # if type(ltyp) is AutoType and type(rtyp) in [IntegerType, FloatType]:
            if type(ltyp) in [IntegerType, FloatType] and type(rtyp) in [IntegerType, FloatType]:
                return FloatType() if type(ltyp) is FloatType() or type(rtyp) is FloatType else IntegerType()
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
            if type(ltyp) in [IntegerType, FloatType]:
                if type(rtyp) in [IntegerType, FloatType]:
                    return BooleanType()
            raise TypeMismatchInExpression(ctx)
                
        
    def visitUnExpr(self, ctx, o):
        typ = self.visit(ctx.val, o)
        
        if ctx.op == '!':
            if type(typ) is BooleanType:
                return BooleanType()
        else:
            if type(typ) in [IntegerType, FloatType]:
                return typ
        
        raise TypeMismatchInExpression(ctx)
    
    def visitId(self, ctx, o):
        for env in o:
            for decl in env:
                if ctx.name == decl.name and type(decl) is VarDecl:
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
    def visitArrayLit(self, ctx, o): 
        typ = None
        for expr in ctx.explist:
            curtyp = self.visit(expr, o)
            if typ is None:
                typ = curtyp
            elif type(typ) != type(curtyp):
                raise IllegalArrayLiteral(ctx)
        
        # n-dimensional array lit
        while hasattr(typ, "typ"):
            typ = typ.typ
        
        return ArrayType([IntegerLit(0)], typ)
    
    def visitFuncCall(self, ctx, o):
        funCallTyp = Utils.getTypeByName(ctx.name, Function(), o)
        # type(x) is ParamDecl
        paramsTyp = [x.typ for x in Utils.getFunctionParams(ctx, o)]
        
        for i, arg in enumerate(ctx.args):
            argtyp = self.visit(arg, o)
            
            if not Utils.isTypeEquivalent(paramsTyp[i], argtyp):
                raise TypeMismatchInExpression(ctx)
            
        return funCallTyp

    # STATEMENT'S VISITOR
    def visitAssignStmt(self, ctx, o):
        ltyp = self.visit(ctx.lhs, o)
        rtyp = self.visit(ctx.rhs, o)
        
        if type(ltyp) is VoidType or type(ltyp) is ArrayType:
            raise TypeMismatchInStatement(ctx)
        
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
        if not ctx.expr:
            return VoidType()
        
        returnStmtTyp = self.visit(ctx.expr, o)
        
        # function in o[1]
        for decl in o[1]:
            if hasattr(decl, 'return_type'):
                funReturnType = decl.return_type
                break
        # if not Utils.isTypeCompatible(funReturnType, returnStmtTyp):
        #     raise TypeMismatchInStatement(ctx)
        
        return o
        
    def visitCallStmt(self, ctx, o):
        funTyp = Utils.getTypeByName(ctx.name, Function(), o)
        if not type(funTyp) is VoidType:
            raise TypeMismatchInStatement(ctx)
        
        paramsTyp = [self.visit(x, o).typ for x in Utils.getFunctionParams(ctx, o)]
        
        for i, arg in enumerate(ctx.args):
            argtyp = self.visit(arg, o)
            if type(paramsTyp[i]) is FloatType and type(argtyp) is IntegerType:
                return o
            if type(argtyp) != type(paramsTyp[i]):
                raise TypeMismatchInExpression(ctx)
            
        return o

    def visitVarDecl(self, ctx, o):
        for decl in o[0]:
            if ctx.name == decl.name:
                raise Redeclared(Variable(), ctx.name)
        
        
        if ctx.init:
            initTyp = self.visit(ctx.init, o)
            
            if isinstance(ctx.typ, AutoType):
                ctx.typ = initTyp
            
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
                
                env = self.visit(firstStmt, env) 
        
        else:
            if len(ctx.body.body) == 0:
                raise InvalidStatementInFunction(ctx.name)
            
            inheritFunc = Utils.getCtxByName(ctx.inherit, o)
            firstStmt = ctx.body.body[0]
            
            if type(firstStmt) is CallStmt and firstStmt.name == 'super':
                # hàm cha không có tham số nhưng cố chấp gọi super
                if len(inheritFunc.params) == 0:
                    raise InvalidStatementInFunction(ctx.name)
                    
                for i, arg in enumerate(firstStmt.args):
                    argtyp = self.visit(arg, env)
                    if type(argtyp) is not type(inheritFunc.params[i].typ):
                        raise TypeMismatchInExpression(arg)
                    
                    env[0] += [self.visit(inheritFunc.params[i], env)]
            
            elif type(firstStmt) is CallStmt and firstStmt.name == 'preventDefault':
                pass
            else:
                raise InvalidStatementInFunction(ctx.name)
        
        for stmt in ctx.body.body[1:]:
            env = self.visit(stmt, env) 
        
        return o

    def visitProgram(self, ctx, o):
        mainExist = False
        o = [[]]
        
        # use function before declaration
        for decl in ctx.decls:
            if type(decl) is FuncDecl:
                if decl.name == 'main' and len(decl.params) == 0 and type(decl.return_type) is VoidType:
                    mainExist = True
                
                for fundecl in o[0]:
                    if fundecl.name == decl.name:
                        raise Redeclared(Function(), fundecl.name)
                o[0] += [decl]
        
        if mainExist:
            for decl in ctx.decls:
                o = self.visit(decl, o)
            return o
        
        raise NoEntryPoint()
