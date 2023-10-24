import os.path

def checkInput(string):

    commandValueError = string[0] != "ccwc"
    optionValueError = string[1] != "-c" and string[1] != "-l" and string[1] != "-w" and string[1] != string[-1]
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
    match string[1]:
        case "-c":
            print(f'{(os.path.getsize( string[-1]))} {string[-1]}')
        case "-l":
            
            with(open(string[-1], "r") as f):
                print(f"{len(f.readlines())} {string[-1]}")
                f.close()
        case "-w":
            with(open(string[-1], "r") as f):
                print(f"{len(f.readlines())} {string[-1]}")
                f.close()
            

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
