#Justin Walter 2/2/21

import sys
import pickle
dict = {}
def Code(code):
    if len(code) != 4:
        code = str(input("That was not a correct product code, please try again:  "))  
        Code(code)
    elif code.isupper() == False:
        code = str(input("That was not a correct product code, please try again:  "))     
        Code(code) 
    else:
        
        return code
 
def Number(number):
    if number.startswith('0') == False:
        number = str(input("That was not a correct product number, please try again:  "))
        Number(number)
    if number.isnumeric() == False:
        number = str(input("That was not a correct product number, please try again:  "))
        Number(number)
    else:
        
        return number  

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
        code = str(input("Enter a product code (four capital letters):  "))  
        Code(code)
        number = str(input("Enter a product number (a number with a leading 0):  "))  
        Number(number)
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