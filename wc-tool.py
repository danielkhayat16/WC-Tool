import os.path

def main():
    print("This challenge is to build your own version of the Unix command line tool wc!")
    str = ""
    commandValueError = True
    optionValueError = True
    readFileError = True
    while( commandValueError or optionValueError or readFileError):
        try:
            string = input('To use the command, please enter "ccwc -c <filename>"\n')
            commandValueError = string[0:4] != "ccwc"
            optionValueError = string[4:7] != " -c"
            

            readFileError = not os.path.isfile(string[8:])
            if(commandValueError):
                print("Wrong input try again")
            elif(optionValueError):
                print("Wrong argument, try again")
            elif(readFileError):
                print("No such file exist")
            else:
                print(f'{(os.path.getsize( string[8:]))} {string[8:]}')
                




        except ValueError:
            print("Please enter a valid value")

        
    
        # if(str[5:7] != "-c"):
            
        #     print("Wrong parameter")
        #     str = ""


if __name__ == "__main__":
    main()
