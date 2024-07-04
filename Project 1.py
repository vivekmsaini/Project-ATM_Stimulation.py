# ATM  Stimulation


name=input("plz enter your name :")
print("hello", name )

message=""""

how may i help you sir !

type 1 >>>>>>>> check balance 
type 2 >>>>>>>> deposit amount
type 3 >>>>>>>> withdrawl amount

"""""
print(message)
available_amount=10000
task=int(input("plz enter your number : "))
if task  >=1 and task <=3:
    print("welcone in your union bank :")

    #check balance
    if task==1:
        print("check your balance :" , available_amount )

        #deposit amount

    elif task==2:
            deposit_amount=int(input("plz enter your deposit amount : "))

            if deposit_amount>=500:
                     available_amount+= deposit_amount
                     print("your amount deposit sucessfully :",deposit_amount)
                     print("now your available balance is", available_amount)

            else:
                print("your deposit ammont is  less then 500 :")

                #withdrawl amount
    else:
          withdrawl_amount=int(input("plz enter your withdraw amount : "))
          if withdrawl_amount<=available_amount:
            available_amount-=withdrawl_amount
            print(" your withdrawl amount is sucessfull :",withdrawl_amount)
            print("your balance is now :", available_amount)

          else:
              print("your balance is not sufficient for withdrawl:")


else:
    print("plz enter correct option 1 to 3!")
