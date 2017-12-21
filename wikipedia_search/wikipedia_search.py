#!/usr/bin/env python2
# my attempt at making a command line driven wikipedia search program in python

#TO ADD:
# getopt module implement --lang option
# add xowa module support (offline wikipedia)
# pygtk module for when no arg passed and DISPLAY env variable is set

import wikipedia
import getopt
import sys

#set language command
#n a script, typical usage is something like this:#wikipedia.set_lang("en")
def usage():
    print str(sys.argv[0]) + ' [options] \'search term\''

def search(search_term):
    return search_term.content

def main():
    search_term = wikipedia.page(sys.argv[-1])

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hl:v", ["help", "lang="])
    except getopt.GetoptError as err:
        print str(err) 
        usage()
        sys.exit(2)
    output = None
    verbose = False
    for o, language in opts:
        if o == "-v":
            verbose = True
        elif o in ('-h', '--help'):
            usage() 
            sys.exit(2)
        elif o in ('-l', '--lang'):
            output = language
            wikipedia.set_lang(language)
        else:
            assert False, "unhandled option"
   
   # my n00b attempt at encoding everything in unicode 
    try: 
        response = search(search_term)
        print search_term
        print '\n'
        for line in response.splitlines():
            print line.encode('utf-8')
    except wikipedia.exceptions.DisambiguationError as err:
        print str(err)
        sys.exit(2)
    
if __name__ == "__main__":
    main()
