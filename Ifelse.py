
import time
currentTime = time.strftime('%H:%M:%S')
print(currentTime)
currentHour= int(time.strftime('%H'))
print(currentHour)
currentMinute=time.strftime('%M')
print(currentMinute)
currentSecond=time.strftime('%S')
print(currentSecond)

print("Current Hour ",currentHour,":","current Minute ", currentMinute ,":", "Current Second", currentSecond)

name=input("Enter Your Name") 


if(currentHour < 12):
    print("Goodmorning ", name)
elif(currentHour<18):
    print("Good Afternoon", name)
else:
    print("Good Night ", name)