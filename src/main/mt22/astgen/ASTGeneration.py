from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *
from functools import reduce

class ASTGeneration(MT22Visitor):
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        # program: decl* EOF;
        if ctx.getChildCount() == 1:
            return Program([])
        
        decl = reduce(lambda prev, cur: prev + self.visit(cur), ctx.decl(), [])
        return Program(decl)
        
        
    def visitDecl(self, ctx: MT22Parser.DeclContext):
        #decl: funcDecl | varDecl;
        return self.visit(ctx.getChild(0))
    
    def visitFuncDecl(self, ctx: MT22Parser.FuncDeclContext):
        # funcDecl: 
        #     ID COL FUNCTION (VOID | typ) LP paramlist RP (INHERIT ID)? 
        #     blockStmt;
        name = ctx.ID(0).getText()
        returnTyp = VoidType() if ctx.VOID() else self.visit(ctx.typ())
        params = self.visit(ctx.paramlist())
        inheritFunc = ctx.ID(1).getText() if ctx.ID(1) else None
        body = self.visit(ctx.blockStmt())
        return [FuncDecl(name, returnTyp, params, inheritFunc, body)]

    def visitVarDecl(self, ctx: MT22Parser.VarDeclContext):
        #varDecl: idlist COL typ SEMI | varDeclFull SEMI
        if ctx.getChildCount() == 2:
            tuples = self.visit(ctx.varDeclFull())
            typ = tuples[len(tuples) - 1][1]
            inits = [x[2] for x in tuples][::-1]
            return [VarDecl(tuples[i][0], typ, inits[i]) for i in range(len(tuples))]
        
        idlist = self.visit(ctx.idlist())
        typ = self.visit(ctx.typ())
        
        return list(map(lambda x: VarDecl(x, typ), idlist))
    
    def visitVarDeclFull(self, ctx: MT22Parser.VarDeclFullContext):
        # varDeclFull: 
        #     ID COMMA varDeclFull COMMA expr 
        #     | ID COL typ ASSIGN expr;
        id = ctx.ID().getText()
        expr = self.visit(ctx.expr())
        
        if ctx.typ():
            return [(id, self.visit(ctx.typ()), expr)]
        else:
            return [(id, 'null', expr)] + self.visit(ctx.varDeclFull())
    
    def visitIdlist(self, ctx: MT22Parser.IdlistContext):
        # idlist: ID COMMA idlist | ID;
        if ctx.getChildCount() == 1:
            return [ctx.ID().getText()]
        
        return [ctx.ID().getText()] + self.visit(ctx.idlist())
    
    def visitParam(self, ctx: MT22Parser.ParamContext):
        # param: INHERIT? OUT? ID COL typ;
        name = ctx.ID().getText()
        typ = self.visit(ctx.typ())
        out = True if ctx.OUT() else False
        inherit = True if ctx.INHERIT() else False
        
        return ParamDecl(name, typ, out, inherit)
    
    def visitParamPrime(self, ctx: MT22Parser.ParamPrimeContext):
        # paramPrime: param COMMA paramPrime | param;
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.param())]
    
        return [self.visit(ctx.param())] + self.visit(ctx.paramPrime())

    def visitParamlist(self, ctx: MT22Parser.ParamlistContext):
        # paramlist: paramPrime |
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.paramPrime())
    

    def visitArglist(self, ctx: MT22Parser.ArglistContext):
        # arglist: exprlist |;
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.exprlist())

    def visitFuncCall(self, ctx: MT22Parser.FuncCallContext):
        # funcCall: ID LP arglist RP
        name = ctx.ID().getText()
        args = self.visit(ctx.arglist())
        return FuncCall(name, args)
    
    def visitDimensionlist(self, ctx: MT22Parser.DimensionlistContext):
        # dimensionlist: INTLIT COMMA dimensionlist | INTLIT;
        if ctx.getChildCount() == 1:
            return [int(ctx.INTLIT().getText())]
        return [int(ctx.INTLIT().getText())] + self.visit(ctx.dimensionlist())

    def visitAtomicTyp(self, ctx: MT22Parser.AtomicTypContext):
        # atomicTyp: INTEGER | FLOAT | BOOLEAN | STRING;
        if ctx.INTEGER():
            return IntegerType()
        if ctx.FLOAT():
            return FloatType()
        if ctx.BOOLEAN():
            return BooleanType()
        if ctx.STRING():
            return StringType()

    def visitArrayTyp(self, ctx: MT22Parser.ArrayTypContext):
        # arrayTyp: ARRAY LS dimensionlist RS OF atomicTyp;
        dmslist = self.visit(ctx.dimensionlist())
        atomicTyp = self.visit(ctx.atomicTyp())
        return ArrayType(dmslist, atomicTyp)

    def visitTyp(self, ctx: MT22Parser.TypContext):
        # typ: atomicTyp | AUTO | arrayTyp;
        if ctx.AUTO():
            return AutoType()
        return self.visit(ctx.getChild(0))
    
    def visitOperand(self, ctx: MT22Parser.OperandContext):
        # operand: typelit | ID | funcCall;
        if ctx.ID():
            return Id(ctx.ID().getText())
        return self.visit(ctx.getChild(0))

    def visitIndexOp(self, ctx: MT22Parser.IndexOpContext):
        # indexOp: ID LS exprlist RS;
        return ArrayCell(ctx.ID().getText(), self.visit(ctx.exprlist()))

    def visitSignOp(self, ctx: MT22Parser.SignOpContext):
        # signOp: MINUS;
        return ctx.getChild(0).getText()
    
    def visitLogicalOp(self, ctx: MT22Parser.LogicalOpContext):
        # logicalOp: NOT;
        return ctx.getChild(0).getText()
    
    def visitMultiplyingOp(self, ctx: MT22Parser.MultiplyingOpContext):
        # multiplyingOp:  DIV | MULT | MOD;
        return ctx.getChild(0).getText()
    
    def visitAddingOp(self, ctx: MT22Parser.AddingOpContext):
        # addingOp: MINUS | PLUS;
        return ctx.getChild(0).getText()

    def visitLogicalBinaryOp(self, ctx: MT22Parser.LogicalBinaryOpContext):
        # logicalBinaryOp: AND | OR;
        return ctx.getChild(0).getText()

    def visitRelationalOp(self, ctx: MT22Parser.RelationalOpContext):
        # relationalOp: EQ | NEQ | LT | LTEQ | GT | GTEQ;
        return ctx.getChild(0).getText()

    def visitStringOp(self, ctx: MT22Parser.StringOpContext):
        # stringOp: STRCON;
        return ctx.getChild(0).getText()

    def visitExpr(self, ctx: MT22Parser.ExprContext):
        # expr
        #     : <assoc=left> indexOp
        #     | <assoc=right> signOp expr
        #     | <assoc=right> logicalOp expr
        #     | <assoc=left> expr multiplyingOp expr
        #     | <assoc=left> expr addingOp expr
        #     | <assoc=left> expr logicalBinaryOp expr
        #     | expr relationalOp expr // none-assoc
        #     | expr stringOp expr //none-assoc
        #     | operand
        #     | LP expr RP
        if ctx.indexOp():
            return self.visit(ctx.indexOp())
        if ctx.operand():
            return self.visit(ctx.operand())
        if ctx.LP():
            return self.visit(ctx.expr(0))
        
        if ctx.signOp():
            return UnExpr(self.visit(ctx.signOp()), self.visit(ctx.expr(0)))
        if ctx.logicalOp():
            return UnExpr(self.visit(ctx.logicalOp()), self.visit(ctx.expr(0)))
        
        # Binary Expression
        expr1 = self.visit(ctx.expr(0))
        expr2 = self.visit(ctx.expr(1))
        op = self.visit(ctx.getChild(1))
        return BinExpr(op, expr1, expr2)
    
    def visitExprlist(self, ctx: MT22Parser.ExprlistContext):
        # exprlist: expr COMMA exprlist | expr;
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expr())]
        return [self.visit(ctx.expr())] + self.visit(ctx.exprlist())
    
    def visitStmt(self, ctx: MT22Parser.StmtContext):
        # stmt: 
        #     assignmentStmt 
        #     | ifStmt 
        #     | forStmt 
        #     | whileStmt 
        #     | doWhileStmt 
        #     | breakStmt 
        #     | continueStmt 
        #     | returnStmt 
        #     | callStmt
        #     | blockStmt;
        stmt = ctx.getChild(0)
        return self.visit(stmt)
    
    def visitBlockStmtElement(self, ctx: MT22Parser.BlockStmtElementContext):
        # blockStmtElement: stmt | varDecl;
        blockElement = self.visit(ctx.getChild(0))
        return [blockElement] if ctx.stmt() else blockElement
    
    def visitBlockStmtElements(self, ctx: MT22Parser.BlockStmtElementsContext):
        # blockStmtElements: blockStmtElement blockStmtElements |;
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.blockStmtElement()) + self.visit(ctx.blockStmtElements())

    def visitBlockStmt(self, ctx: MT22Parser.BlockStmtContext):
        # blockStmt: LB blockStmtElements RB;
        return BlockStmt(self.visit(ctx.blockStmtElements()))

    def visitAssignmentStmt(self, ctx: MT22Parser.AssignmentStmtContext):
        # (indexOp | ID) ASSIGN expr SEMI;
        if ctx.ID():
            lhs = Id(ctx.ID().getText())
        else:
            lhs = self.visit(ctx.indexOp())
        
        rhs = self.visit(ctx.expr())
        
        return AssignStmt(lhs, rhs)
	
    def visitIfStmt(self, ctx: MT22Parser.StmtContext):
        # ifStmt: IF LP expr RP stmt elseStmt?;
        cond = self.visit(ctx.expr())
        tstmt = self.visit(ctx.stmt())
        
        if ctx.elseStmt():
            return IfStmt(cond, tstmt, self.visit(ctx.elseStmt()))
        return IfStmt(cond, tstmt)
	
    def visitElseStmt(self, ctx: MT22Parser.ElseStmtContext):
        # elseStmt: ELSE stmt;
        return self.visit(ctx.stmt())
    
    def visitForStmt(self, ctx: MT22Parser.ForStmtContext):
        # forStmt: FOR LP ID ASSIGN expr COMMA expr COMMA expr RP stmt;
        init = AssignStmt(Id(ctx.ID().getText()), self.visit(ctx.expr(0)))
        cond = self.visit(ctx.expr(1))
        upd = self.visit(ctx.expr(2))
        stmt = self.visit(ctx.stmt())
        
        return ForStmt(init, cond, upd, stmt)
    
    def visitWhileStmt(self, ctx: MT22Parser.WhileStmtContext):
        # whileStmt: WHILE LP expr RP stmt
        expr = self.visit(ctx.expr())
        stmt = self.visit(ctx.stmt())
        return WhileStmt(expr, stmt)

    def visitDoWhileStmt(self, ctx: MT22Parser.DoWhileStmtContext):
        # doWhileStmt:
		#   DO blockStmt
		#   WHILE LP expr RP SEMI;
        expr = self.visit(ctx.expr())
        blockStmt = self.visit(ctx.blockStmt())
        return DoWhileStmt(expr, blockStmt)

    def visitBreakStmt(self, ctx: MT22Parser.BreakStmtContext):
        # breakStmt: BREAK SEMI;
        return BreakStmt()
    
    def visitContinueStmt(self, ctx: MT22Parser.ContinueStmtContext):
        # continueStmt: CONTINUE SEMI;
        return ContinueStmt()
    
    def visitReturnStmt(self, ctx: MT22Parser.ReturnStmtContext):
        # returnStmt: RETURN expr SEMI | RETURN SEMI;
        expr = self.visit(ctx.expr()) if ctx.getChildCount() == 3 else None
        return ReturnStmt(expr)
    
    def visitCallStmt(self, ctx: MT22Parser.CallStmtContext):
        # callStmt: funcCall SEMI;
        funcCall = self.visit(ctx.funcCall())
        return CallStmt(funcCall.name, funcCall.args)
    
    def visitTypelit(self, ctx: MT22Parser.TypelitContext):
        # typelit: INTLIT | FLOATLIT | STRINGLIT | arraylit | TRUE | FALSE;
        if ctx.arraylit():
            return self.visit(ctx.arraylit())

        val = ctx.getChild(0).getText()
        if ctx.INTLIT():
            return IntegerLit(int(val))
        if ctx.FLOATLIT():
            if val[0] == '.':
                if val[1] in ['e','E']:
                    val = 0
            return FloatLit(float(val))
        if ctx.STRINGLIT():
            return StringLit(str(val))
        if ctx.FALSE():
            return BooleanLit(False)
        if ctx.TRUE():
            return BooleanLit(True)
    
    def visitArraylit(self, ctx: MT22Parser.ArraylitContext):
        # arraylit: 
		# LB exprlist RB 
		# | LB RB;

        if ctx.getChildCount() == 2:
            return ArrayLit([])
        return ArrayLit(self.visit(ctx.exprlist()))