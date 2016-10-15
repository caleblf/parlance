# parlance

##Purpose

Right now, there is a severe lack of truly accessible options for programmers with physical disabilities. If you can't type, you basically can't code--but we hope to change that.

Modern and old-fashioned languages alike tend to be very symbol-heavy. Even languages that seem very close to natural language (like Python) often rely on strict formatting rules to function, which isn't feasible for people with screen readers, or anyone who operates computers with speech-recognition tools.

##Overview

The Parlance language is an open-source, C-based language designed for accessibility. Parlance's syntax is as close to natural language as possible, so that it can be easily recognized by speech-to-text applications. It uses an easy-to-learn set of dictionary words to build a true, powerful programming language focused on readability and speakability. Parlance is directly converted to standard ANSI C code, so users who know C can easily begin using Parlance.
Current Features

- Unambiguous syntax, not dependent on finnicky formatting
- Compiles directly to C code
- Easy to understand when read aloud
- Painless to learn with a foundation in C or its relatives
- Potential for easy integration with speech-to-text and/or text-to-speech tools

##Language Features

###CALL
        CALL <name> ARG <argument> etc... 
                Calls the function with the given arguments, which may be 
                statements.

###LOOP
        FIRST <statement>
                Runs the statement on the first time through the loop.
        CONDITION <statement>
                Checks at the end of each loop, exits loop if evaluates false.
        CYCLE <statement>
                Executes at the end of each time through the loop.


###DECLARE {VARIABLE|FUNCTION} TYPE <type>

###VARIABLE <name>
        References the variable with name name.

###LITERAL <type> <value> END LITERAL
        Defines and string or integer literal.

###IF <statement>
        Defines the beginning of an if statement.

###ELSE [IF <statement>]
        Defines the beginning of an else block.

###MODULO, ADD, SUBTRACT, LESSTHAN, AND etc...
        Define basic integer operators comparisons and logical operators

