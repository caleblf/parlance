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
    return "foo"

def build_expression(words):
    pass

def build_literal(words):
    pass

def build_scope(words):
    pass

terms = {}
statements = {}
operators = {}

def build_literal(words):
    if words.pop(0) not in ("STRING", "INT"):
        exit(1)
    literal = words.pop(0)
    if words.pop(0) != "END" or words.pop(0) != "LITERAL":
        exit(1)
    return " "+literal + " "

def build_variable(words):
    return words.pop(0)

def build_expression(words):
    output = ""
    command = words.pop(0)
    # the expression is over when we read in a foreign command
    while True:
        if command in terms:
            output += " " + terms[command](words)
        elif command in operators:
            output += " " + operators[command]
        else:
            break
        command = words.pop(0)
    words.insert(0, command)
    return output
    
def build_call(words):
    """Builds a C function call"""
    output = words.pop(0) + "("
    word = words.pop(0)
    args = []
    while True:
        if word == "ARG":
            args.append(build_expression(words))
        elif word == "END":
            return output + ", ".join(args) + ")"
        else:
            exit(1)
        word = words.pop(0)

def build_return(words):
    output = "return " + build_expression(words)
    if words.pop(0) == "END" and words.pop(0) == "STATEMENT":
        output += ";"
    else:
        exit(1)
    return output

def build_cpp(words):
    output = "#"
    command = words.pop(0)
    if command == "DEFINE":
        output += "define " + words.pop(0) + "\n"
    elif command == "INCLUDES":
        output += "include " + words.pop(0) + "\n"
    elif command == "IFNDEF":
        output += "ifndef " + words.pop(0) + "\n"
    elif command == "ENDIF":
        output += "endif\n"
    return output


def build_if(words):
    output = "if (" + build_expression(words) + ")"
    if words.pop(0) != "BEGIN":
        exit(1)
    else:
        return output + " {\n" + build_scope(words)

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
        # Only want one of each, but we don't check that (yet)
        if word == "FIRST":
            first = build_expression(words)
        elif word == "CONDITION":
            condition = build_expression(words)
        elif word == "CYCLE":
            cycle = build_expression(words)
        else:
            exit(1)
        word = words.pop(0)
    output = "for (%s; %s; %s) {\n" % (first, condition, cycle) + build_scope(words)

def build_declaration(words):
    output = ""
    word = words.pop(0)
    if word == "FUNCTION":
        fname = words.pop(0)
        ftype = ""
        if words.pop(0) == "TYPE":
            ftype = words.pop(0)
        else:
            exit(1)
        params = []
        word = words.pop(0)
        while (word != "BEGIN" and word != "END"):
            if word == "PARAM":
                pname = words.pop(0)
                word = words.pop(0)
                ptype = ""
                if word == "TYPE":
                    ptype = words.pop(0)
                else:
                    exit(1)
                params.append(ptype + " " + pname)
                word = words.pop(0)
            else:
                exit(1)
        output += "%s %s(%s)" % (ftype, fname, ", ".join(params))
        if word == "END":
            if words.pop(0) != "STATEMENT":
                exit(1)
            return output + ";"
        elif word == "BEGIN":
            return output + " {\n" + build_scope(words)
    elif word == "VARIABLE":
        vname = words.pop(0)
        vtype = ""
        if words.pop(0) == "TYPE":
            vtype = words.pop(0)
        else:
            exit(1)
        word = words.pop(0)
        output += "%s %s" % (vtype, vname)
        if word == "GETS":
            output += " = " + build_expression(words)
            if words.pop(0) != "END" or words.pop(0) != "STATEMENT":
                exit(1);
            return output + ";"
        elif word == "END":
            if words.pop(0) != "STATEMENT":
                exit(1)
            return output + ";"
    else:
        exit(1)


def build_scope(words):
    output = ""
    command = words.pop(0);
    while command != "END":
        if command in statements:
            output += statements[command](words) + "\n"

        else:
            words.insert(0, command)
            output += build_expression(words)
            if words.pop(0) != "END" or words.pop(0) != "STATEMENT":
                exit(1)
            output += ";\n"
        command = words.pop(0)
    if len(words) == 0:
        return output
    elif words.pop(0) == "SCOPE":
        return output + "\n}\n"
    else:
        exit(1)
    

statements = {
    "RETURN": build_return,
    "CPP": build_cpp,
    "IF": build_if,
    "ELSE": build_else,
    "LOOP": build_loop,
    "DECLARE": build_declaration,
}

terms = {
    "VARIABLE": build_variable,
    "LITERAL": build_literal,
    "CALL": build_call
}

operators = {
    "PREINCREMENT": "++",
    "NEGATIVE": "-",
    "BITWISE NOT": "~",
    "MODULO": "%",
    "GETS": "=",
    "AND": "+",
    "EQUALS": "==",
    "LESSTHAN": "<"
}


if len(argv) < 2:
    exit("Usage: " + argv[0] + " <filename>")

if not path.exists(argv[1]):
    exit("Error: File " + argv[1] + " not found.")

parlance_code = open(argv[1], 'r')

# We assume that string literals are all one word with quotes around them
code_words = parlance_code.read().split()

print build_scope(code_words)
