from time import sleep
def contagen_regresiva (num1):
    while num1 > 0: 
        num1 = num1 -1
        print(num1) 
        sleep(1)  

n1 = int(input("O valor da contagen e: "))

contagen_regresiva(n1)