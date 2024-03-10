#-----------------------------------------------
#------Calculatore of numbering system----------
#-----------------------------------------------


## Function of converting from Binary to Octal
def binary_to_octal(number): 
    octal_number=""
    while len(number) % 3 != 0:
        number="0"+number
        i=0
    while i <len(number):
      octal_digit=int(number[i:i+3],2)
      octal_number+=str(octal_digit)
      i+=3
    print(f"->Binary of given is: {octal_number}\n")

## Function of coverting from binary to decimal
def Binary_to_Decimal(number):
      Binary_Char="01"
      decimal =0
      for i in number :
           decimal =decimal*2 + Binary_Char.index(i)
      print(f"-> decimal of given is: {decimal}\n")

## Function of coverting from Decimal to Binary
def Dicimal_to_Binary(number):
    binary_list =[]
    while number!=0 :
         remender = int(number)%2 
         binary_list .append(remender)
         number = int(number)//2
    binary_list=binary_list[::-1]
    print("-> binary of given number is ", end="" )
    for num in binary_list :
       print(num ,end="")
    print("\n")

## Function of converting from Decimal to Octal 
def Decimal_to_Octal(number):
    octal_list=[]
    while number!=0 :  
        remender = int(number)%8
        octal_list .append(remender)
        number = int(number)//8
    octal_list = octal_list[::-1]
    print("-> octal of given number is: " , end='')
    for num in octal_list :
          print(num , end="")
    print("\n")  

## Function of convertig from Decimal to Hexadecimal
def Decimal_to_Hexadecimal(number):
    Hexadecimal_table ={0:"0" ,1:"1" ,2:"2", 3:"3" , 4:"4" ,5:"5",6:"6" ,7:"7", 8:"8", 9:"9" ,10:"A" , 11:"B" ,12:"C" , 13:"D" ,14:"E" ,15:"F"}
    Hexadecimal_list=[]
    while number!=0 :
        remender = int(number)%16
        Hexadecimal_list . append(Hexadecimal_table[remender])
        number = int(number)//16      
    Hexadecimal_list = Hexadecimal_list[::-1]
    Hexadecimal_number ="" .join(Hexadecimal_list)
    print(f"-> Hexadecimal of given number is: {Hexadecimal_number}\n" ) 

## Function of convrting from Octal to Decimal 
def Octal_to_Decimal(number):
     decimal=0
     i=0
     while number!=0:
         digit= int(number)%10
         decimal=decimal + digit*(8**i)
         number= int(number)//10
         i=i+1
     print(f"-> Decimal of given is: {decimal} \n")

## Function of converting from octal to binary
def Octal_to_Binary(number):
     octal_digits =["000" ,"001" ,"010" ,"011","100" ,"101" ,"110" ,"111"]
     binary_result =""
     for digit in number:
          if ord(digit) >=48 and ord(digit)<=55:
               binary_result+=octal_digits[int(digit)]
     return binary_result.lstrip("0")or "0"

## Function of converting from Octal to Hexadecimal
def Octal_to_Hexadecimal(number):
      decimal=0
      i=0
      while number!=0:
           digit= int(number)%10
           decimal=decimal + digit*(8**i)
           number= int(number)//10
           i=i+1
      Hexadecimal_table ={0:"0" ,1:"1" ,2:"2", 3:"3" , 4:"4" ,5:"5",6:"6" ,7:"7", 8:"8", 9:"9" ,10:"A" , 11:"B" ,12:"C" , 13:"D" ,14:"E" ,15:"F"}
      Hexadecimal_list=[]
      while decimal!=0 :
          remender = int(decimal)%16
          Hexadecimal_list . append(Hexadecimal_table[remender])
          decimal = int(decimal)//16      
      Hexadecimal_list = Hexadecimal_list[::-1]
      Hexadecimal_number ="" .join(Hexadecimal_list)
      print(f"-> Hexadecimal of given number is: {Hexadecimal_number}\n" ) 

## Function of converting from Hexadecimal to Decimal
def Hexadecimal_to_Decimal(number):
       Hexa_char ="0123456789ABCDEF"
       decimal=0
       for i in number:
           decimal =decimal*16 + Hexa_char.index(i)
       print(f"-> decimal of given is: {decimal}\n")

## Function of converting Hexadecimal to Binary 
def Hexadecima_to_Binary(number):
     Hexadecima_digits={"0":"0000" , "1":"0001" ,"2":"0010" ,"3":"0011" ,"4":"0100" ,"5":"0101" ,"6":"0110" ,"7":"0111" ,"8":"1000" ,"9":"1001","A":"1010", "B":"1011" ,"C":"1100" ,"D":"1101" ,"E":"1110" ,"F":"1111"}
     binary_result =""
     for digit in number:
          if digit.upper() in Hexadecima_digits:
               binary_result+= Hexadecima_digits[digit.upper()]
     return  binary_result.lstrip("0") or "0"

## Function of converting from Hexadecimal to Octal
def Hexadecimal_to_Octal(number):
             Hexa_char ="0123456789ABCDEF"  
             decimal=0
             for i in number:
                    decimal =decimal*16 + Hexa_char.index(i)
             octal_list=[]
             while decimal!=0 :  
                     remender = int(decimal)%8
                     octal_list .append(remender)
                     decimal = int(decimal)//8
             octal_list = octal_list[::-1]
             print("-> octal of given number is: " ,end="")
             for num in octal_list :
                       print(num ,end="")
             print("\n")      

## Function of converting from Binary to Hexadecimal
def Binary_to_Hexadecimal(number):
           number= number.zfill((len(number)+3) & -4)
           Hexadecima_digits={"0000": "0", "0001":"1" ,"0010":"2" ,"0011" :"3","0100":"4" ,"0101":"5" ,"0110":"6" ,"0111":"7" ,"1000":"8" ,"1001":"9","1010":"A", "1011":"B" ,"1100":"C" ,"1101":"D" ,"1110":"E" ,"1111":"F"}
           hexa_result =""
           for i in range(0,len(number),4):
                 binary_digit =number[i:i+4]
                 hexa_result+= Hexadecima_digits[binary_digit]
           return hexa_result.lstrip("0") or "0"

      

## Menu 1
while True :
  print("Menu 1 : \nA) Enter a number \nB) exite programe")
  types =input("=> Enter A or B: ").upper()
  if types == "A" :
      ## input from user a number
      number= input("\n=>please enter a number: ").upper()

    ## Menu 2
      while True:
        ## let user select the base you want to convert a number from 
        print("\nMenu 2 : \nA) base of Decimal \nB) base of Binary \nC) base of Octal \nD) base of Hexadecimal")
        input_base1= input("\n=>Please select the base you want to convert a number from: ").upper()
        if input_base1=="A" or input_base1=="B" or input_base1=="C" or input_base1=="D":
            break   
        else:
            ## if user input invalid choise print error message 
             print(" \n==>error \n=>please select a valid choice")
            

    ## Menu 3        
      while True:
        ## let user select the base you want to convert a number to
        print("\nMenu 3: \nA) base of Decimal \nB) base of Binary \nC) baseof Octal \nD) base ofHexadecimal")
        input_base2=input("\n=>Please select the base you want to convert a number to: ").upper()
        if input_base2=="A" or input_base2=="B" or input_base2=="C" or input_base2=="D":
            break
        else:
            ## If user input invalid choise print error message
            print("==>error \n=>please select a valid choice ")
            exit

      ## The result of the convert from system to system
      while True:      
        ## If user selected convert from Decimal ("A") to Binary ("B")
        if input_base1=="A" and input_base2 =="B":
                   ## Caling the function Decimal_to_Binary
                   Dicimal_to_Binary(number)
                   break   ## return to Menu 1
                    
         ## If user selected convert from Decimal ("A") to Octal("C")
        elif input_base1=="A" and input_base2=="C" :
                   
                   Decimal_to_Octal(number)
                   break   ## return to Menu 1
                   
        ## If user selected convert from Decimal ("A") to Hexadecimal ("D")
        elif input_base1=="A" and input_base2=="D":
                   ## Caling the function Decimal_to_Hexadecimal
                   Decimal_to_Hexadecimal(number)
                   break   ## return to Menu 1 

         ## If user selected convert from Octal ("C") to Dicimal ("A")
        elif input_base1=="C" and input_base2=="A" :
                    ## Caling the function Octal_to_Dicimal
                    Octal_to_Decimal(number)
                    break    ## return to Menu 1 

        ## If user selected convert from Octal ("C") to Binary("B")
        elif input_base1=="C" and input_base2=="B" :
                     ## Caling function Octal_to_Binary
                     binary_output =Octal_to_Binary(number)
                     print(f"-> Binary of given is: {binary_output}\n")
                     break   ## return to Menu 1 
                
        ## If user selected convert from Octal ("C") to Hexadecimal ("D")        
        elif input_base1=="C" and input_base2=="D" :
                     ## Caling function Octal_to_Hexadecimal  
                     Octal_to_Hexadecimal(number)
                     break  ## return to Menu 1 
        
        ## If user selected convert from Hexadecimal ("D") to Decimal ("A")
        elif input_base1=="D" and input_base2=="A":
                    ## Caling function Hexadecimal_to_decimal
                    Hexadecimal_to_Decimal(number)                    
                    break  ## return to Menu 1 
               
        ## If user selected convert from Hexadecimal ("D") to Binary ("B")
        elif input_base1=="D" and input_base2=="B":
                     binary_output=Hexadecima_to_Binary(number)
                     print(f"-> Binary of given is: {binary_output}\n")
                     break  ## return to Menu 1  
        
         ## If user selected convert from Hexadecimal ("D") to Octal ("C")
        elif input_base1=="D" and input_base2=="C":
                    Hexadecimal_to_Octal(number)
                    break  ## return to Menu 1
        
         ## If user selected convert from Binary ("B") to Decimal ("A")
        elif input_base1=="B" and input_base2=="A" :
             ## Caling the function Binary_to_Decimal
             Binary_to_Decimal(number)
             break  ## return to Menu 1
        
         ## If user selected convert from Binary ("B") to Octal ("C")
        elif input_base1=="B" and input_base2=="C":
             ## Caling the function conveting from Binary to Octal
             binary_to_octal(number)
             break   ## return to Menu 1 
        
        ## If user selected convert from Binary ("B") to Hexadecimal ("D")
        elif input_base1=="B" and input_base2=="D":
           hex_output =Binary_to_Hexadecimal(number)
           print(f"-> Hexadecimal of given is: {hex_output}\n")
        break    ## return to Menu 1

  
 ## If user selected "B" exit the programe
  elif types=="B":
       print("--> The program is closed")
       break
  else :         
     ## If user selected invalid choice print error message to select valid choice  
     print("==> erro \n-> please select a valid choice \n")
     

                
                    
