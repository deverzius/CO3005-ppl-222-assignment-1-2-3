# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2;")
        buf.write("\u01bc\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\3\2\3\2\3\2\3\2\3")
        buf.write("\3\3\3\3\3\3\3\7\3\u008a\n\3\f\3\16\3\u008d\13\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\7\4\u0098\n\4\f\4\16\4")
        buf.write("\u009b\13\4\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3")
        buf.write("\t\3\t\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\r")
        buf.write("\3\16\3\16\3\16\3\17\3\17\3\20\3\20\3\20\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26")
        buf.write("\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34")
        buf.write("\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3 ")
        buf.write("\3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3")
        buf.write("#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3%\3&\3")
        buf.write("&\3&\3&\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3")
        buf.write(")\3)\3)\3)\3)\3)\3)\3)\3*\3*\3*\3*\3*\3*\3*\3+\3+\3+\3")
        buf.write("+\3+\3+\3+\3,\3,\3,\3,\3,\3-\3-\3-\3-\3-\3-\3.\3.\3.\3")
        buf.write(".\3.\3/\3/\3/\3/\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3")
        buf.write("\60\3\60\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3\62\3\62")
        buf.write("\3\62\3\62\3\63\3\63\3\63\3\63\3\63\3\63\3\64\3\64\7\64")
        buf.write("\u0157\n\64\f\64\16\64\u015a\13\64\3\65\6\65\u015d\n\65")
        buf.write("\r\65\16\65\u015e\3\66\3\66\7\66\u0163\n\66\f\66\16\66")
        buf.write("\u0166\13\66\3\67\3\67\5\67\u016a\n\67\3\67\3\67\38\3")
        buf.write("8\38\78\u0171\n8\f8\168\u0174\138\38\38\78\u0178\n8\f")
        buf.write("8\168\u017b\138\38\58\u017e\n8\39\39\39\39\39\59\u0185")
        buf.write("\n9\39\39\39\39\39\59\u018c\n9\39\39\3:\3:\7:\u0192\n")
        buf.write(":\f:\16:\u0195\13:\3:\3:\3:\3;\3;\3;\3<\3<\5<\u019f\n")
        buf.write("<\3=\3=\7=\u01a3\n=\f=\16=\u01a6\13=\3=\5=\u01a9\n=\3")
        buf.write("=\3=\3>\3>\3>\3?\3?\7?\u01b2\n?\f?\16?\u01b5\13?\3?\3")
        buf.write("?\3?\3@\3@\3@\4\u008b\u0193\2A\3\3\5\4\7\5\t\6\13\7\r")
        buf.write("\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!")
        buf.write("\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67")
        buf.write("\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61")
        buf.write("a\62c\63e\64g\65i\2k\2m\2o\66q\67s8u\2w\2y9{\2}:\177;")
        buf.write("\3\2\r\5\2\13\f\17\17\"\"\4\2\f\f\17\17\5\2C\\aac|\6\2")
        buf.write("\62;C\\aac|\3\2\62;\4\2GGgg\4\2--//\3\2\63;\n\2$$))^^")
        buf.write("ddhhppttvv\6\2\f\f$$))^^\3\3\f\f\2\u01c5\2\3\3\2\2\2\2")
        buf.write("\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3")
        buf.write("\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2")
        buf.write("\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2")
        buf.write("\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3")
        buf.write("\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61")
        buf.write("\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2")
        buf.write("\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3")
        buf.write("\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M")
        buf.write("\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2")
        buf.write("W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2")
        buf.write("\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2o\3\2\2")
        buf.write("\2\2q\3\2\2\2\2s\3\2\2\2\2y\3\2\2\2\2}\3\2\2\2\2\177\3")
        buf.write("\2\2\2\3\u0081\3\2\2\2\5\u0085\3\2\2\2\7\u0093\3\2\2\2")
        buf.write("\t\u009e\3\2\2\2\13\u00a0\3\2\2\2\r\u00a2\3\2\2\2\17\u00a4")
        buf.write("\3\2\2\2\21\u00a6\3\2\2\2\23\u00a8\3\2\2\2\25\u00aa\3")
        buf.write("\2\2\2\27\u00ad\3\2\2\2\31\u00b0\3\2\2\2\33\u00b3\3\2")
        buf.write("\2\2\35\u00b6\3\2\2\2\37\u00b8\3\2\2\2!\u00bb\3\2\2\2")
        buf.write("#\u00bd\3\2\2\2%\u00c0\3\2\2\2\'\u00c3\3\2\2\2)\u00c5")
        buf.write("\3\2\2\2+\u00c7\3\2\2\2-\u00c9\3\2\2\2/\u00cb\3\2\2\2")
        buf.write("\61\u00cd\3\2\2\2\63\u00cf\3\2\2\2\65\u00d1\3\2\2\2\67")
        buf.write("\u00d3\3\2\2\29\u00d5\3\2\2\2;\u00d7\3\2\2\2=\u00d9\3")
        buf.write("\2\2\2?\u00de\3\2\2\2A\u00e4\3\2\2\2C\u00ec\3\2\2\2E\u00ef")
        buf.write("\3\2\2\2G\u00f4\3\2\2\2I\u00fa\3\2\2\2K\u0100\3\2\2\2")
        buf.write("M\u0104\3\2\2\2O\u010d\3\2\2\2Q\u0110\3\2\2\2S\u0118\3")
        buf.write("\2\2\2U\u011f\3\2\2\2W\u0126\3\2\2\2Y\u012b\3\2\2\2[\u0131")
        buf.write("\3\2\2\2]\u0136\3\2\2\2_\u013a\3\2\2\2a\u0143\3\2\2\2")
        buf.write("c\u0146\3\2\2\2e\u014e\3\2\2\2g\u0154\3\2\2\2i\u015c\3")
        buf.write("\2\2\2k\u0160\3\2\2\2m\u0167\3\2\2\2o\u017d\3\2\2\2q\u018b")
        buf.write("\3\2\2\2s\u018f\3\2\2\2u\u0199\3\2\2\2w\u019e\3\2\2\2")
        buf.write("y\u01a0\3\2\2\2{\u01ac\3\2\2\2}\u01af\3\2\2\2\177\u01b9")
        buf.write("\3\2\2\2\u0081\u0082\t\2\2\2\u0082\u0083\3\2\2\2\u0083")
        buf.write("\u0084\b\2\2\2\u0084\4\3\2\2\2\u0085\u0086\7\61\2\2\u0086")
        buf.write("\u0087\7,\2\2\u0087\u008b\3\2\2\2\u0088\u008a\13\2\2\2")
        buf.write("\u0089\u0088\3\2\2\2\u008a\u008d\3\2\2\2\u008b\u008c\3")
        buf.write("\2\2\2\u008b\u0089\3\2\2\2\u008c\u008e\3\2\2\2\u008d\u008b")
        buf.write("\3\2\2\2\u008e\u008f\7,\2\2\u008f\u0090\7\61\2\2\u0090")
        buf.write("\u0091\3\2\2\2\u0091\u0092\b\3\2\2\u0092\6\3\2\2\2\u0093")
        buf.write("\u0094\7\61\2\2\u0094\u0095\7\61\2\2\u0095\u0099\3\2\2")
        buf.write("\2\u0096\u0098\n\3\2\2\u0097\u0096\3\2\2\2\u0098\u009b")
        buf.write("\3\2\2\2\u0099\u0097\3\2\2\2\u0099\u009a\3\2\2\2\u009a")
        buf.write("\u009c\3\2\2\2\u009b\u0099\3\2\2\2\u009c\u009d\b\4\2\2")
        buf.write("\u009d\b\3\2\2\2\u009e\u009f\7-\2\2\u009f\n\3\2\2\2\u00a0")
        buf.write("\u00a1\7/\2\2\u00a1\f\3\2\2\2\u00a2\u00a3\7,\2\2\u00a3")
        buf.write("\16\3\2\2\2\u00a4\u00a5\7\61\2\2\u00a5\20\3\2\2\2\u00a6")
        buf.write("\u00a7\7\'\2\2\u00a7\22\3\2\2\2\u00a8\u00a9\7#\2\2\u00a9")
        buf.write("\24\3\2\2\2\u00aa\u00ab\7(\2\2\u00ab\u00ac\7(\2\2\u00ac")
        buf.write("\26\3\2\2\2\u00ad\u00ae\7~\2\2\u00ae\u00af\7~\2\2\u00af")
        buf.write("\30\3\2\2\2\u00b0\u00b1\7?\2\2\u00b1\u00b2\7?\2\2\u00b2")
        buf.write("\32\3\2\2\2\u00b3\u00b4\7#\2\2\u00b4\u00b5\7?\2\2\u00b5")
        buf.write("\34\3\2\2\2\u00b6\u00b7\7>\2\2\u00b7\36\3\2\2\2\u00b8")
        buf.write("\u00b9\7>\2\2\u00b9\u00ba\7?\2\2\u00ba \3\2\2\2\u00bb")
        buf.write("\u00bc\7@\2\2\u00bc\"\3\2\2\2\u00bd\u00be\7@\2\2\u00be")
        buf.write("\u00bf\7?\2\2\u00bf$\3\2\2\2\u00c0\u00c1\7<\2\2\u00c1")
        buf.write("\u00c2\7<\2\2\u00c2&\3\2\2\2\u00c3\u00c4\7*\2\2\u00c4")
        buf.write("(\3\2\2\2\u00c5\u00c6\7+\2\2\u00c6*\3\2\2\2\u00c7\u00c8")
        buf.write("\7]\2\2\u00c8,\3\2\2\2\u00c9\u00ca\7_\2\2\u00ca.\3\2\2")
        buf.write("\2\u00cb\u00cc\7}\2\2\u00cc\60\3\2\2\2\u00cd\u00ce\7\177")
        buf.write("\2\2\u00ce\62\3\2\2\2\u00cf\u00d0\7\60\2\2\u00d0\64\3")
        buf.write("\2\2\2\u00d1\u00d2\7.\2\2\u00d2\66\3\2\2\2\u00d3\u00d4")
        buf.write("\7=\2\2\u00d48\3\2\2\2\u00d5\u00d6\7<\2\2\u00d6:\3\2\2")
        buf.write("\2\u00d7\u00d8\7?\2\2\u00d8<\3\2\2\2\u00d9\u00da\7c\2")
        buf.write("\2\u00da\u00db\7w\2\2\u00db\u00dc\7v\2\2\u00dc\u00dd\7")
        buf.write("q\2\2\u00dd>\3\2\2\2\u00de\u00df\7d\2\2\u00df\u00e0\7")
        buf.write("t\2\2\u00e0\u00e1\7g\2\2\u00e1\u00e2\7c\2\2\u00e2\u00e3")
        buf.write("\7m\2\2\u00e3@\3\2\2\2\u00e4\u00e5\7d\2\2\u00e5\u00e6")
        buf.write("\7q\2\2\u00e6\u00e7\7q\2\2\u00e7\u00e8\7n\2\2\u00e8\u00e9")
        buf.write("\7g\2\2\u00e9\u00ea\7c\2\2\u00ea\u00eb\7p\2\2\u00ebB\3")
        buf.write("\2\2\2\u00ec\u00ed\7f\2\2\u00ed\u00ee\7q\2\2\u00eeD\3")
        buf.write("\2\2\2\u00ef\u00f0\7g\2\2\u00f0\u00f1\7n\2\2\u00f1\u00f2")
        buf.write("\7u\2\2\u00f2\u00f3\7g\2\2\u00f3F\3\2\2\2\u00f4\u00f5")
        buf.write("\7h\2\2\u00f5\u00f6\7c\2\2\u00f6\u00f7\7n\2\2\u00f7\u00f8")
        buf.write("\7u\2\2\u00f8\u00f9\7g\2\2\u00f9H\3\2\2\2\u00fa\u00fb")
        buf.write("\7h\2\2\u00fb\u00fc\7n\2\2\u00fc\u00fd\7q\2\2\u00fd\u00fe")
        buf.write("\7c\2\2\u00fe\u00ff\7v\2\2\u00ffJ\3\2\2\2\u0100\u0101")
        buf.write("\7h\2\2\u0101\u0102\7q\2\2\u0102\u0103\7t\2\2\u0103L\3")
        buf.write("\2\2\2\u0104\u0105\7h\2\2\u0105\u0106\7w\2\2\u0106\u0107")
        buf.write("\7p\2\2\u0107\u0108\7e\2\2\u0108\u0109\7v\2\2\u0109\u010a")
        buf.write("\7k\2\2\u010a\u010b\7q\2\2\u010b\u010c\7p\2\2\u010cN\3")
        buf.write("\2\2\2\u010d\u010e\7k\2\2\u010e\u010f\7h\2\2\u010fP\3")
        buf.write("\2\2\2\u0110\u0111\7k\2\2\u0111\u0112\7p\2\2\u0112\u0113")
        buf.write("\7v\2\2\u0113\u0114\7g\2\2\u0114\u0115\7i\2\2\u0115\u0116")
        buf.write("\7g\2\2\u0116\u0117\7t\2\2\u0117R\3\2\2\2\u0118\u0119")
        buf.write("\7t\2\2\u0119\u011a\7g\2\2\u011a\u011b\7v\2\2\u011b\u011c")
        buf.write("\7w\2\2\u011c\u011d\7t\2\2\u011d\u011e\7p\2\2\u011eT\3")
        buf.write("\2\2\2\u011f\u0120\7u\2\2\u0120\u0121\7v\2\2\u0121\u0122")
        buf.write("\7t\2\2\u0122\u0123\7k\2\2\u0123\u0124\7p\2\2\u0124\u0125")
        buf.write("\7i\2\2\u0125V\3\2\2\2\u0126\u0127\7v\2\2\u0127\u0128")
        buf.write("\7t\2\2\u0128\u0129\7w\2\2\u0129\u012a\7g\2\2\u012aX\3")
        buf.write("\2\2\2\u012b\u012c\7y\2\2\u012c\u012d\7j\2\2\u012d\u012e")
        buf.write("\7k\2\2\u012e\u012f\7n\2\2\u012f\u0130\7g\2\2\u0130Z\3")
        buf.write("\2\2\2\u0131\u0132\7x\2\2\u0132\u0133\7q\2\2\u0133\u0134")
        buf.write("\7k\2\2\u0134\u0135\7f\2\2\u0135\\\3\2\2\2\u0136\u0137")
        buf.write("\7q\2\2\u0137\u0138\7w\2\2\u0138\u0139\7v\2\2\u0139^\3")
        buf.write("\2\2\2\u013a\u013b\7e\2\2\u013b\u013c\7q\2\2\u013c\u013d")
        buf.write("\7p\2\2\u013d\u013e\7v\2\2\u013e\u013f\7k\2\2\u013f\u0140")
        buf.write("\7p\2\2\u0140\u0141\7w\2\2\u0141\u0142\7g\2\2\u0142`\3")
        buf.write("\2\2\2\u0143\u0144\7q\2\2\u0144\u0145\7h\2\2\u0145b\3")
        buf.write("\2\2\2\u0146\u0147\7k\2\2\u0147\u0148\7p\2\2\u0148\u0149")
        buf.write("\7j\2\2\u0149\u014a\7g\2\2\u014a\u014b\7t\2\2\u014b\u014c")
        buf.write("\7k\2\2\u014c\u014d\7v\2\2\u014dd\3\2\2\2\u014e\u014f")
        buf.write("\7c\2\2\u014f\u0150\7t\2\2\u0150\u0151\7t\2\2\u0151\u0152")
        buf.write("\7c\2\2\u0152\u0153\7{\2\2\u0153f\3\2\2\2\u0154\u0158")
        buf.write("\t\4\2\2\u0155\u0157\t\5\2\2\u0156\u0155\3\2\2\2\u0157")
        buf.write("\u015a\3\2\2\2\u0158\u0156\3\2\2\2\u0158\u0159\3\2\2\2")
        buf.write("\u0159h\3\2\2\2\u015a\u0158\3\2\2\2\u015b\u015d\t\6\2")
        buf.write("\2\u015c\u015b\3\2\2\2\u015d\u015e\3\2\2\2\u015e\u015c")
        buf.write("\3\2\2\2\u015e\u015f\3\2\2\2\u015fj\3\2\2\2\u0160\u0164")
        buf.write("\7\60\2\2\u0161\u0163\t\6\2\2\u0162\u0161\3\2\2\2\u0163")
        buf.write("\u0166\3\2\2\2\u0164\u0162\3\2\2\2\u0164\u0165\3\2\2\2")
        buf.write("\u0165l\3\2\2\2\u0166\u0164\3\2\2\2\u0167\u0169\t\7\2")
        buf.write("\2\u0168\u016a\t\b\2\2\u0169\u0168\3\2\2\2\u0169\u016a")
        buf.write("\3\2\2\2\u016a\u016b\3\2\2\2\u016b\u016c\5i\65\2\u016c")
        buf.write("n\3\2\2\2\u016d\u017e\7\62\2\2\u016e\u0172\t\t\2\2\u016f")
        buf.write("\u0171\t\6\2\2\u0170\u016f\3\2\2\2\u0171\u0174\3\2\2\2")
        buf.write("\u0172\u0170\3\2\2\2\u0172\u0173\3\2\2\2\u0173\u0179\3")
        buf.write("\2\2\2\u0174\u0172\3\2\2\2\u0175\u0176\7a\2\2\u0176\u0178")
        buf.write("\5i\65\2\u0177\u0175\3\2\2\2\u0178\u017b\3\2\2\2\u0179")
        buf.write("\u0177\3\2\2\2\u0179\u017a\3\2\2\2\u017a\u017c\3\2\2\2")
        buf.write("\u017b\u0179\3\2\2\2\u017c\u017e\b8\3\2\u017d\u016d\3")
        buf.write("\2\2\2\u017d\u016e\3\2\2\2\u017ep\3\2\2\2\u017f\u0180")
        buf.write("\5o8\2\u0180\u0181\5k\66\2\u0181\u018c\3\2\2\2\u0182\u0184")
        buf.write("\5o8\2\u0183\u0185\5k\66\2\u0184\u0183\3\2\2\2\u0184\u0185")
        buf.write("\3\2\2\2\u0185\u0186\3\2\2\2\u0186\u0187\5m\67\2\u0187")
        buf.write("\u018c\3\2\2\2\u0188\u0189\5k\66\2\u0189\u018a\5m\67\2")
        buf.write("\u018a\u018c\3\2\2\2\u018b\u017f\3\2\2\2\u018b\u0182\3")
        buf.write("\2\2\2\u018b\u0188\3\2\2\2\u018c\u018d\3\2\2\2\u018d\u018e")
        buf.write("\b9\4\2\u018er\3\2\2\2\u018f\u0193\7$\2\2\u0190\u0192")
        buf.write("\5w<\2\u0191\u0190\3\2\2\2\u0192\u0195\3\2\2\2\u0193\u0194")
        buf.write("\3\2\2\2\u0193\u0191\3\2\2\2\u0194\u0196\3\2\2\2\u0195")
        buf.write("\u0193\3\2\2\2\u0196\u0197\7$\2\2\u0197\u0198\b:\5\2\u0198")
        buf.write("t\3\2\2\2\u0199\u019a\7^\2\2\u019a\u019b\t\n\2\2\u019b")
        buf.write("v\3\2\2\2\u019c\u019f\n\13\2\2\u019d\u019f\5u;\2\u019e")
        buf.write("\u019c\3\2\2\2\u019e\u019d\3\2\2\2\u019fx\3\2\2\2\u01a0")
        buf.write("\u01a4\7$\2\2\u01a1\u01a3\5w<\2\u01a2\u01a1\3\2\2\2\u01a3")
        buf.write("\u01a6\3\2\2\2\u01a4\u01a2\3\2\2\2\u01a4\u01a5\3\2\2\2")
        buf.write("\u01a5\u01a8\3\2\2\2\u01a6\u01a4\3\2\2\2\u01a7\u01a9\t")
        buf.write("\f\2\2\u01a8\u01a7\3\2\2\2\u01a9\u01aa\3\2\2\2\u01aa\u01ab")
        buf.write("\b=\6\2\u01abz\3\2\2\2\u01ac\u01ad\7^\2\2\u01ad\u01ae")
        buf.write("\n\n\2\2\u01ae|\3\2\2\2\u01af\u01b3\7$\2\2\u01b0\u01b2")
        buf.write("\5w<\2\u01b1\u01b0\3\2\2\2\u01b2\u01b5\3\2\2\2\u01b3\u01b1")
        buf.write("\3\2\2\2\u01b3\u01b4\3\2\2\2\u01b4\u01b6\3\2\2\2\u01b5")
        buf.write("\u01b3\3\2\2\2\u01b6\u01b7\5{>\2\u01b7\u01b8\b?\7\2\u01b8")
        buf.write("~\3\2\2\2\u01b9\u01ba\13\2\2\2\u01ba\u01bb\b@\b\2\u01bb")
        buf.write("\u0080\3\2\2\2\23\2\u008b\u0099\u0158\u015e\u0164\u0169")
        buf.write("\u0172\u0179\u017d\u0184\u018b\u0193\u019e\u01a4\u01a8")
        buf.write("\u01b3\t\b\2\2\38\2\39\3\3:\4\3=\5\3?\6\3@\7")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    WS = 1
    COMMENT = 2
    INLINE_COMMENT = 3
    PLUS = 4
    MINUS = 5
    MULT = 6
    DIV = 7
    MOD = 8
    NOT = 9
    AND = 10
    OR = 11
    EQ = 12
    NEQ = 13
    LT = 14
    LTEQ = 15
    GT = 16
    GTEQ = 17
    STRCON = 18
    LP = 19
    RP = 20
    LS = 21
    RS = 22
    LB = 23
    RB = 24
    DOT = 25
    COMMA = 26
    SEMI = 27
    COL = 28
    ASSIGN = 29
    AUTO = 30
    BREAK = 31
    BOOLEAN = 32
    DO = 33
    ELSE = 34
    FALSE = 35
    FLOAT = 36
    FOR = 37
    FUNCTION = 38
    IF = 39
    INTEGER = 40
    RETURN = 41
    STRING = 42
    TRUE = 43
    WHILE = 44
    VOID = 45
    OUT = 46
    CONTINUE = 47
    OF = 48
    INHERIT = 49
    ARRAY = 50
    ID = 51
    INTLIT = 52
    FLOATLIT = 53
    STRINGLIT = 54
    UNCLOSE_STRING = 55
    ILLEGAL_ESCAPE = 56
    ERROR_CHAR = 57

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", 
            "'!='", "'<'", "'<='", "'>'", "'>='", "'::'", "'('", "')'", 
            "'['", "']'", "'{'", "'}'", "'.'", "','", "';'", "':'", "'='", 
            "'auto'", "'break'", "'boolean'", "'do'", "'else'", "'false'", 
            "'float'", "'for'", "'function'", "'if'", "'integer'", "'return'", 
            "'string'", "'true'", "'while'", "'void'", "'out'", "'continue'", 
            "'of'", "'inherit'", "'array'" ]

    symbolicNames = [ "<INVALID>",
            "WS", "COMMENT", "INLINE_COMMENT", "PLUS", "MINUS", "MULT", 
            "DIV", "MOD", "NOT", "AND", "OR", "EQ", "NEQ", "LT", "LTEQ", 
            "GT", "GTEQ", "STRCON", "LP", "RP", "LS", "RS", "LB", "RB", 
            "DOT", "COMMA", "SEMI", "COL", "ASSIGN", "AUTO", "BREAK", "BOOLEAN", 
            "DO", "ELSE", "FALSE", "FLOAT", "FOR", "FUNCTION", "IF", "INTEGER", 
            "RETURN", "STRING", "TRUE", "WHILE", "VOID", "OUT", "CONTINUE", 
            "OF", "INHERIT", "ARRAY", "ID", "INTLIT", "FLOATLIT", "STRINGLIT", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "WS", "COMMENT", "INLINE_COMMENT", "PLUS", "MINUS", "MULT", 
                  "DIV", "MOD", "NOT", "AND", "OR", "EQ", "NEQ", "LT", "LTEQ", 
                  "GT", "GTEQ", "STRCON", "LP", "RP", "LS", "RS", "LB", 
                  "RB", "DOT", "COMMA", "SEMI", "COL", "ASSIGN", "AUTO", 
                  "BREAK", "BOOLEAN", "DO", "ELSE", "FALSE", "FLOAT", "FOR", 
                  "FUNCTION", "IF", "INTEGER", "RETURN", "STRING", "TRUE", 
                  "WHILE", "VOID", "OUT", "CONTINUE", "OF", "INHERIT", "ARRAY", 
                  "ID", "INTPART", "DECPART", "EXPPART", "INTLIT", "FLOATLIT", 
                  "STRINGLIT", "ESC_CHAR", "STRING_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_CHAR", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[54] = self.INTLIT_action 
            actions[55] = self.FLOATLIT_action 
            actions[56] = self.STRINGLIT_action 
            actions[59] = self.UNCLOSE_STRING_action 
            actions[61] = self.ILLEGAL_ESCAPE_action 
            actions[62] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INTLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace('_', '')
     

    def FLOATLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace('_', '')
     

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text = self.text[1:]; self.text = self.text[:-1]
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            s = str(self.text)
            if s[-1] == '\n': 
            	raise UncloseString(s[1:-2]) 
            else: 
            	raise UncloseString(s[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            raise IllegalEscape(self.text[1:])
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            raise ErrorToken(self.text)
     


