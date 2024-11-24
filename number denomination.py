Amount =int(input("Please Enter Amount for Withdraw :"))
note1 = Amount//100
note2 = (Amount%100)//50
note3 = ((Amount%100)%50)//10
print("Notes of 100 rupees", note1)
print("Notes of 50 rupees", note2)
print("Notes of 10 rupees", note3)