## Prerequisites
- Python3
- ANTLR4

## Setup
1. Set environment variable ANTLR_JAR to the file antlr-4.9.2-complete.jar in your computer

2. Change current directory to initial/src where there is file run.py, then run below command to generate needed files

	```sh
	python3 run.py gen 
	```

3. Run 100 testcases by typing one of five below commands. 

	```sh
	python3 run.py test LexerSuite
	```
	```sh
	python3 run.py test ParserSuite
	```
	```sh
	python3 run.py test ASTGenSuite
	```
	```sh
	python3 run.py test CheckerSuite
	```
	```sh
	python3 run.py test CodeGenSuite
	```



