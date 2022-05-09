import random




randomNumber = random.randint(0,10)
print(str(randomNumber) + "start")



while randomNumber != 7:
    randomNumber = random.randint(0,10)
    print(str(randomNumber) + "inside")
print(str(randomNumber) + "End")