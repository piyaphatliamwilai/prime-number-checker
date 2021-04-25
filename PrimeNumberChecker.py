from playsound import playsound
import time

number = int(input("Welcome to my prine number checker, to use please put the number : "))

print(' ------------ 2 ------------ ')
print(number / 2)
print(' ------------ 3 ------------ ')
print(number / 3)
print(' ------------ 5 ------------ ')
print(number / 5)
print(' ------------ 7 ------------ ')
print(number / 7)

playsound("numberChecked.mp3")
print("If all of the number had decimals then it's prime number.")
while 3 > 2:
    time.sleep(1)
