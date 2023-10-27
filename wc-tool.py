import os.path

def checkInput(string):

    commandValueError = string[0] != "ccwc"
    optionValueError = string[1] != "-c" and string[1] != "-l" and string[1] != "-w" and string[1] != "-m" and string[1] != string[-1]
    readFileError = not os.path.isfile(string[-1])
    if(commandValueError):
        print("Wrong input try again")
    elif(optionValueError):
        print("Wrong option, try again")
    elif(readFileError):
        print("No such file exist")
    else: 
        checkArgument(string)
        
        

def checkArgument(string):
    
    fileName = string[-1]
    fileSize = (os.path.getsize( fileName))
    
    
    with(open(fileName, "r") as f):
        numOfWords = 0
        numOfCharacters = 0
        lines = f.readlines()
        numOfLines = len(lines)
        for line in lines:
            words = line.split()
            numOfWords += len(words)
            numOfCharacters += sum(len(word) for word in words)
        
        f.close() 

    match string[1]:
        case "-c":
            print(f'{fileSize} {fileName}')
        case "-l":
            print(f"{numOfLines} {fileName}")      
        case "-w":
            print(f"{numOfWords} {fileName}")
        case "-m":
            print(f"{numOfCharacters} {fileName}")
        case fileName:
            print(f'{fileSize} {numOfLines} {numOfWords} {fileName}')
                
            

def main():
    print("This challenge is to build your own version of the Unix command line tool wc!")
    
    commandValueError = True
    optionValueError = True
    readFileError = True
    while( commandValueError or optionValueError or readFileError):
        try:
            string = input('To use the command, please enter "ccwc -c <filename>"\n').split()
            checkInput(string)
            break
                
        except ValueError:
            print("Please enter a valid value")

if __name__ == "__main__":
    main()
