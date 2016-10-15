# parlance

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

