#!python

import sys, os, re
import argparse
import lark
import pprint
def main(args):

    s_ex1 = """
SELECT TIPP_ID ID, TIPP_FILENAME FILENAME, TIPP_ART ART, DECODE(USERT_TIPP_ID, USERT_TIPP_ID, 'J', 'N') GELESEN  FROM W_TIPP@ETK_NUTZER     LEFT JOIN W_USER_TIPPS@ETK_NUTZER ON (USERT_FIRMA_ID = '111'  AND USERT_ID ='ADMIN' AND USERT_TIPP_ID = TIPP_ID) WHERE TIPP_ID > 0 AND TIPP_WICHTIG = 'N' ORDER BY TIPP_POS
"""

    s_ex4 = "SELECT A FA, DECODE ( TCP_SACHNR, TCP_SACHNR, 'C', NULL) TEIL_TC FROM T"
    
    s_ex5 = """SELECT A FROM T LEFT JOIN B ON (F<=22)"""

    parser = argparse.ArgumentParser()
    parser.add_argument('gram')
    parser.add_argument('input')
    parser.add_argument('--parser', default="earley", required=False)
    parser.add_argument('--debug', default=False, required=False)

    args = parser.parse_args()
    #print(args)
    with open(args.gram, 'r') as f:
    	#lark.Lark.load(f)
        g = f.read()
        #print (g)
        #print(type(f.read()))

        #l=lark.Lark(g, debug=True, parser='lalr', start="select_expression");
        #l=lark.Lark(g, debug=True, parser='lalr');
        l=lark.Lark(g, debug=True, parser=args.parser, start="select_expression", propagate_positions=True);
        with open(args.input, 'r') as inp:
            p = l.parse(inp.read())

#['__class__', '__deepcopy__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_meta', '_pretty', '_pretty_label', 'children', 'column', 'copy', 'data', 'end_column', 'end_line', 'expand_kids_by_index', 'find_data', 'find_pred', 'iter_subtrees', 'iter_subtrees_topdown', 'line', 'meta', 'pretty', 'scan_values', 'set']    
        #print(p.pretty())
        enum(p, 1)
        # for i in p.iter_subtrees():
        #     print(i.data)
        #     for j in i.children:
        #         print (j.type)
        #         print (j.value)
    return sys.exit(0)

#"from_clause, *, ""
def enum(t, s=0):
    for i in t.children:
        if isinstance(i, lark.Tree):
            print(s*' ', "Nonterm [%s]" % i.data)
            #print( '{0:{fill}{align}{width}}'.format("Nonterm %s" % i.data, fill=" ", align="<", width=s))
            #print("Nonterm %s" % i.data)
            enum(i, s+4)
        else:
            print(s*' ', "Term [%s, %s]" % (i.type, i.value))
            #print( '{0:{fill}{align}{width}}'.format("Term %s, %s" % (i.type, i.value), fill=" ", align="<", width=s))
            #print("Term %s, %s" % (i.type, i.value))


if __name__ == "__main__":
    main(sys.argv)