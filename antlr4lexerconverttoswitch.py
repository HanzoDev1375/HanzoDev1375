def create_java_file(class_name, file_path, input_code):
    # Create a list of case statements
    case_statements = []
    for line in input_code.split('\n'):
        # Split by ',' to get each token
        tokens = line.split(',')
        for token in tokens:
            token = token.strip()
            if '=' in token:
                name = token.split('=')[0].strip()
                case_statements.append(f"case {class_name}.{name}:")

    # Write to a Java file
    with open(file_path, 'w') as file:
        file.write(f"public class {class_name} {{\n")
        for case in case_statements:
            file.write(f"    {case}\n")
        file.write("}\n")

    print(f"File {file_path} has been created successfully! 📄✨")


# Example usage
input_text = '''ENCODING=1, INDENT=2, DEDENT=3, TYPE_COMMENT=4, FSTRING_START=5, FSTRING_MIDDLE=6, 
		FSTRING_END=7, LPAR=8, LSQB=9, LBRACE=10, RPAR=11, RSQB=12, RBRACE=13, 
		DOT=14, COLON=15, COMMA=16, SEMI=17, PLUS=18, MINUS=19, STAR=20, SLASH=21, 
		VBAR=22, AMPER=23, LESS=24, GREATER=25, EQUAL=26, PERCENT=27, EQEQUAL=28, 
		NOTEQUAL=29, LESSEQUAL=30, GREATEREQUAL=31, TILDE=32, CIRCUMFLEX=33, LEFTSHIFT=34, 
		RIGHTSHIFT=35, DOUBLESTAR=36, PLUSEQUAL=37, MINEQUAL=38, STAREQUAL=39, 
		SLASHEQUAL=40, PERCENTEQUAL=41, AMPEREQUAL=42, VBAREQUAL=43, CIRCUMFLEXEQUAL=44, 
		LEFTSHIFTEQUAL=45, RIGHTSHIFTEQUAL=46, DOUBLESTAREQUAL=47, DOUBLESLASH=48, 
		DOUBLESLASHEQUAL=49, AT=50, ATEQUAL=51, RARROW=52, ELLIPSIS=53, COLONEQUAL=54, 
		EXCLAMATION=55, FALSE=56, AWAIT=57, ELSE=58, IMPORT=59, PASS=60, NONE=61, 
		BREAK=62, EXCEPT=63, IN=64, RAISE=65, TRUE=66, CLASS=67, FINALLY=68, IS=69, 
		RETURN=70, AND=71, CONTINUE=72, FOR=73, LAMBDA=74, TRY=75, AS=76, DEF=77, 
		FROM=78, NONLOCAL=79, WHILE=80, ASSERT=81, DEL=82, GLOBAL=83, NOT=84, 
		WITH=85, ASYNC=86, ELIF=87, IF=88, OR=89, YIELD=90, NAME_OR_TYPE=91, NAME_OR_MATCH=92, 
		NAME_OR_CASE=93, NAME_OR_WILDCARD=94, NAME=95, NUMBER=96, STRING=97, NEWLINE=98, 
		COMMENT=99, WS=100, EXPLICIT_LINE_JOINING=101, ERRORTOKEN=102;'''

create_java_file('PythonLexer', '/storage/emulated/0/apktest/ANTLR4-parser-for-Python-3.13-main/port_Java/PythonLexer.java', input_text)