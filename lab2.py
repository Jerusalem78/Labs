# Домашнее задание по лабораторной №2 по предмету "Информационные технологии"
# БВТ2404 - Фомин Денис Владиславович

# 1
def greet(name):
    return 'здравствуйте,' + name 

def square(num):
    return num**2

def max_of_two(x,y):
    return max(x,y) 

# 2
def describe_person(name, age=30):
    print( 'имя:', name,'возраст:',age)
          
# 3
def is_prime(num):
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
    return True
    


