#Justin Walter 2/2/21

import sys
import pickle
dict = {}
def Code():
    while True:
        try:
            code = str(input("Enter a product code (four capital letters):  "))  
            if len(code) == 4 and code.isupper()==True:
                return code 
            else: 
                code = str(input("That was not a correct product code, please try again:  "))  
                #continue
        except:
            print ("An unexpected error occured")    
            
def Number():
    while True:
        try:
            number = str(input("Enter a product number (a number with a leading 0):  ")) 
            if number.startswith('0') == True and number.isnumeric() == True:  
                return number
            else:    
                number = str(input("That was not a correct product number, please try again:  "))
                #continue
        except:
            print ("An unexpected error occured")

def Choice(choice):
    if choice != "yes" and choice != 'no':
        choice = input('Invalid entry.  Do you wish to continue? (yes/no): ')
        Choice(choice)
    else: 
        choice = choice    
        return choice 
def read(namex):
     fileObject=open(namex, "rb")
     pData=pickle.load(fileObject)
     fileObject.close()
     return pData       

def main():
    choice = "yes"
    while choice.lower() == "yes":
        #code = str(input("Enter a product code (four capital letters):  "))  
        #Code(code)
        #number = str(input("Enter a product number (a number with a leading 0):  "))  
        #Number(number)
        code = Code()
        number = Number()
        dict[code] = number
        choice = input('Do you wish to continue? (yes/no): ')
        Choice(choice)
        if choice.lower == "no":
            break
    namex = str(input("Please enter a file name:  "))  
    print("File saved")
    fileObject=open(namex, "wb")
    pickle.dump(dict,fileObject)
    fileObject.close()
    data=read(namex)
    print(data)    
    #print(dict) 


if __name__== "__main__":
    main()


