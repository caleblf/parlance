# Parlance to C Translator
# By: Harrison Kaiser
#     Caleb Lucas-Foley
#     Chris Phifer
#
# This Python script translates a program written
# in the Parlance language into the C language.
#
# Usage: python translator.py <filename>

from sys import argv, exit
from os import path

def build_call(words):
    pass

def build_variable(words):
    pass

def build_return(words):
    pass

def build_cpp(words):
    pass

def build_if(words):
    pass

def build_else(words):
    pass

def build_loop(words):
    pass

def build_end(words):
    pass

def build_declaration(words):
    pass

statements = {
    "CALL": build_call,
    "VARIABLE": build_variable,
    "RETURN": build_return,
    "CPP": build_cpp,
    "IF": build_if,
    "ELSE": build_else,
    "LOOP": build_loop,
    "DECLARE": build_declaration,
}

def build_else(words):
    output = "else "
    word = words.pop(0)

    if word == "IF":
        return output + build_if(words)
    elif word == "BEGIN":
        return output + "{\n" + build_scope(words)
    else:
        exit(1)

def build_loop(words):
    output = ""
    word = ""
    first = ""
    condition = ""
    cycle = ""
    word = words.pop(0)
    while (word != "BEGIN"):
        if word == "FIRST":
            first = build_expression(words)
        elif word == "CONDITION":
            condition = build_expression(words)
        elif word == "CYCLE":
            cycle = build_expression(words)
        else:
            exit(1)
        word = words.pop(0)
    output = "for ( %s; %s; %s ) {\n" % (first, condition, cycle) + build_scope(words)        

def build_declaration(words):
    output = ""
    word = words.pop(0)
    if word == "FUNCTION":
        word = words.pop(0)
        params = []
        output += word
        word = words.pop(0)
        while (word != "BEGIN" and word != "END"):
            if word == "PARAM":
                pname = words.pop(0)
                word = words.pop(0)
                type_ = ""
                if word == "TYPE":
                    type_ = words.pop(0)
                else:
                    exit(1)
                params.append(type_ + " " + pname)
            else:
                exit(1)
        output += "(" + ",".join(params) + ")"
        if word == "END":
            return output + ";"
        elif word == "BEGIN":
            return output + " {\n" + build_scope(words)

def build_call(words):
    """Builds a C function call"""
    output = words.pop(0) + "("
    word = words.pop(0)
    args = []
    while True:
        if word == "ARG":
            args.append(expression(words))
        elif word == "END":
            return output + ",".join(args) + ")"

        else:
            exit(1)
        word = words.pop(0)
    
def scope(words):
    output = ""
    word = words.pop(0)
            
if len(argv) < 2:
    exit("Usage: " + argv[0] + " <filename>")

if not path.exists(argv[1]):
    exit("Error: File " + argv[1] + " not found.")

parlance_code = open(argv[1], 'r')
code_words = parlance_code.read().split()


