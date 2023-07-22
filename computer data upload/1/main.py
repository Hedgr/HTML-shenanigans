import time
num = 9186
while True:
    time.sleep(.75)
    num += 1
    fullBinary = str(bin(num))
    processedBinary = fullBinary.removeprefix("0b")
    print(str(num)+" "+str(processedBinary))