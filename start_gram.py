#!python

import sys, os, re
import argparse
import lark
import pprint
def main(args):

    parser = argparse.ArgumentParser()
    parser.add_argument('gram')

    args = parser.parse_args()
    #print(args)
    with open(args.gram, 'r') as f:
    	#lark.Lark.load(f)
        g = f.read()
        #print (g)
        #print(type(f.read()))

        l=lark.Lark(g, debug=True, start="select_expression");

        p = l.parse("""
SELECT 
USER_MARKE, USER_PRODUKTART, USER_LENKUNG, USER_KATALOGUMFANG, USER_ISO, USER_REGISO, USER_EXPAND_BNB, USER_SHORT_SEARCHPATH, USER_REQUEST_SAZ, USER_SHOW_PRODDATE, USER_SUCHRAUM, USER_SHOW_PREISE, USER_SHOW_TIPPS, USER_PRIMAERMARKT_ID, USER_TABLESTRETCH, USER_FONTSIZE, USER_DFT_VERBAUMENGE 
FROM W_USER_EINSTELLUNGEN@ETK_NUTZER WHERE USER_FIRMA_ID = '111' AND USER_ID = 'ADMIN'
""")
#['__class__', '__deepcopy__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_meta', '_pretty', '_pretty_label', 'children', 'column', 'copy', 'data', 'end_column', 'end_line', 'expand_kids_by_index', 'find_data', 'find_pred', 'iter_subtrees', 'iter_subtrees_topdown', 'line', 'meta', 'pretty', 'scan_values', 'set']    
        #print(p.pretty())
        for i in p.iter_subtrees():
            print(type(i.data))
    return sys.exit(0)

if __name__ == "__main__":
    main(sys.argv)