# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MT22Parser import MT22Parser
else:
    from MT22Parser import MT22Parser

# This class defines a complete generic visitor for a parse tree produced by MT22Parser.

class MT22Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by MT22Parser#program.
    def visitProgram(self, ctx:MT22Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#decl.
    def visitDecl(self, ctx:MT22Parser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#funcDecl.
    def visitFuncDecl(self, ctx:MT22Parser.FuncDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#varDecl.
    def visitVarDecl(self, ctx:MT22Parser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#varDeclFull.
    def visitVarDeclFull(self, ctx:MT22Parser.VarDeclFullContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#idlist.
    def visitIdlist(self, ctx:MT22Parser.IdlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#param.
    def visitParam(self, ctx:MT22Parser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#paramPrime.
    def visitParamPrime(self, ctx:MT22Parser.ParamPrimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#paramlist.
    def visitParamlist(self, ctx:MT22Parser.ParamlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arglist.
    def visitArglist(self, ctx:MT22Parser.ArglistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#funcCall.
    def visitFuncCall(self, ctx:MT22Parser.FuncCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#dimensionlist.
    def visitDimensionlist(self, ctx:MT22Parser.DimensionlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#atomicTyp.
    def visitAtomicTyp(self, ctx:MT22Parser.AtomicTypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arrayTyp.
    def visitArrayTyp(self, ctx:MT22Parser.ArrayTypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#typ.
    def visitTyp(self, ctx:MT22Parser.TypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#operand.
    def visitOperand(self, ctx:MT22Parser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#indexOp.
    def visitIndexOp(self, ctx:MT22Parser.IndexOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#signOp.
    def visitSignOp(self, ctx:MT22Parser.SignOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#logicalOp.
    def visitLogicalOp(self, ctx:MT22Parser.LogicalOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#multiplyingOp.
    def visitMultiplyingOp(self, ctx:MT22Parser.MultiplyingOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#addingOp.
    def visitAddingOp(self, ctx:MT22Parser.AddingOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#logicalBinaryOp.
    def visitLogicalBinaryOp(self, ctx:MT22Parser.LogicalBinaryOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#relationalOp.
    def visitRelationalOp(self, ctx:MT22Parser.RelationalOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stringOp.
    def visitStringOp(self, ctx:MT22Parser.StringOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr.
    def visitExpr(self, ctx:MT22Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exprlist.
    def visitExprlist(self, ctx:MT22Parser.ExprlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stmt.
    def visitStmt(self, ctx:MT22Parser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#blockStmtElement.
    def visitBlockStmtElement(self, ctx:MT22Parser.BlockStmtElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#blockStmtElements.
    def visitBlockStmtElements(self, ctx:MT22Parser.BlockStmtElementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#blockStmt.
    def visitBlockStmt(self, ctx:MT22Parser.BlockStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#assignmentStmt.
    def visitAssignmentStmt(self, ctx:MT22Parser.AssignmentStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#ifStmt.
    def visitIfStmt(self, ctx:MT22Parser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#elseStmt.
    def visitElseStmt(self, ctx:MT22Parser.ElseStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#forStmt.
    def visitForStmt(self, ctx:MT22Parser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#whileStmt.
    def visitWhileStmt(self, ctx:MT22Parser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#doWhileStmt.
    def visitDoWhileStmt(self, ctx:MT22Parser.DoWhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#breakStmt.
    def visitBreakStmt(self, ctx:MT22Parser.BreakStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#continueStmt.
    def visitContinueStmt(self, ctx:MT22Parser.ContinueStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#returnStmt.
    def visitReturnStmt(self, ctx:MT22Parser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#callStmt.
    def visitCallStmt(self, ctx:MT22Parser.CallStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#typelit.
    def visitTypelit(self, ctx:MT22Parser.TypelitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arraylit.
    def visitArraylit(self, ctx:MT22Parser.ArraylitContext):
        return self.visitChildren(ctx)



del MT22Parser