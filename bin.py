import numpy as np
f=open('morse.bin','w+b')
morseTree = ['\x00']*127
str=" ETIANmorseTreeSURWDKGOHVFULAPJBXCYZQ  54 3   2  +    1 6=/     7   8 90"
morseTree[75:76]='?_'
morseTree[81]='"'
morseTree[84]='.'
morseTree[89]='@'
morseTree[93]="'"
morseTree[96]='-'
morseTree[105]=';'
morseTree[106]='!'
morseTree[108]="("
morseTree[114]=','
morseTree[119]=':'
for x in range(len(str)):
    if(str[x]!=' '):
        morseTree[x]=str[x]
asciiDict = {chr(i):i  for i in range(128)}
print(morseTree)
print(asciiDict)
array=[asciiDict[i] for i in morseTree]
print(array)
binary_format=bytearray(array)
print(binary_format)
f.write(binary_format)
f.close()