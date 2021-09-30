#!/bin/env python

import sys, os, re
import argparse
import lark
import pprint

def main(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('gram')
    parser.add_argument('input')
    parser.add_argument("--start-token", default="select_expression", required=False)
    parser.add_argument('--parser', default="earley", required=False)
    parser.add_argument('--debug', default=False, required=False)

    args = parser.parse_args()
    with open(args.gram, 'r') as f:
        g = f.read()
        l=lark.Lark(g, debug=True, parser=args.parser, start=args.start_token, propagate_positions=True);
        with open(args.input, 'r') as inp:
            p = l.parse(inp.read())

        enum(p, 1)
        # for i in p.iter_subtrees():
        #     print(i.data)
        #     for j in i.children:
        #         print (j.type)
        #         print (j.value)
    return sys.exit(0)

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