def countWordsFromFile():
    fileName= input("Enter The File Name")
    numberOfWords= 0
    file= open(fileName,"r")
    for line in file: 
        words= line.split()
        numberOfWords=numberOfWords+len(words)
    print("Number Of Words")
    print(numberOfWords)
countWordsFromFile()