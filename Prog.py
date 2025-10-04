import random
import time

Name=input("Enter your name: ")
print("Welcome,",Name)
Random_Password=["Hello_Worldd_2973","HiLD@85392739","I_Am_Not_A_Robot!","HeL0","WASD_is_MY_password","P4ssw0rD"]
time.sleep(2)
print("Your password is...")
time.sleep(2)
print(random.choice(Random_Password))
input("Press Enter to save your password!")
print("Your password is saved!")
