try:
     chislo1 = int(input("Ввеите число"))
     if 100 < chislo1 < 1000:
         sum = int(str(chislo1)[0]) + int(str(chislo1)[1]) + int(str(chislo1)[2])
         print(sum)
     else:
         print("Число не трехзначное")
         print ("Введенное число " ,chislo1)
except ValueError:
     print("Введі чісло ")
#_______________________________

# c = str(input())
# if c == c[::-1]:
#     print(c + " явл поліндромом")
# else:
#     print(c + "не явл поліндромом")
