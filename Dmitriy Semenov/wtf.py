a = True
while a:
    ps = input("Напиши пароль") 
    if len(ps) < 8: 
       print("Короткий") 
    
       
    else: 
         print("OK") 
         a = False 
print("Хороший пароль") 