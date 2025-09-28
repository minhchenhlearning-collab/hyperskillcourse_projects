This project, overall, is about sorting words, numbers or lines by counting appearances, following lexicographic order or numeric order.
This project involves:
1/ 3 data types: long(number), word, line
2/ 2 sorting types: count(appearance), natural(lexico for word and line, numeric for long)
3/ Print out result if no output file was given, else output on that file
4/ Read from input if no input file was given, else read from that file
5/ 4 parameters from terminal: dataType, sortingType, inputFile and outputFile
6/ Error checking: 
If dataType or sortingType is mentioned but no values passed, raise error
If string inputs in long data type: remove and print a message
If unknown arguments are given: print a message and skip them
