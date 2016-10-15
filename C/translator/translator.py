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

def build_call():
    pass

def build_variable():
    pass

def build_return():
    pass

def build_cpp():
    pass

def build_if():
    pass

def build_else():
    pass

def build_loop():
    pass

def build_end():
    pass

def build_declaration():
    pass

statements = {
    "CALL": build_call,
    "VARIABLE": build_variable,
    "RETURN": build_return,
    "CPP": build_cpp,
    "IF": build_if,
    "ELSE": build_else,
    "LOOP": build_loop,
    "END": build_end, # Probably don't need this
    "DECLARE": build_declaration,
}

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


