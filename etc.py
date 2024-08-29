"""
a = int(input())
b = int(input())
c = float(input())

salary = b * c

print("NUMBER =",a,
"\nSALARY = U$",salary.__format__('.2f'))
"""

"""
lista = []

for i in range(0,5):
    a = int(input())
    lista.append(a)

print(lista)

soma = 0

for i in range (0,5):
    soma = soma + lista[i]
print(soma)
"""

"""
name = round(str(input())2)
salary = float(input())
total_solded = float(input())

def salary_with_bonus(a, b, bonus = 0.15):
    return a + b * bonus

print("TOTAL = R$", round(salary_with_bonus(salary, total_solded),2))
"""

""""
name = str(input())
salary = round(float(input()),2)
total_solded = round(float(input()),2)

total_salary = (salary + total_solded * 0.15)

print("TOTAL = R$", total_salary.__format__('.2f'))
"""

"""
n = int(input())

notes = [100, 50, 20, 10, 5, 2, 1]

count_notes = {}

print(n)

#calculando o numero de notas
for i in notes:
    if n >= i:
        count = n // i
        count_notes[i] = count
        n = n - count * i

for i in notes:
    if i in count_notes:
        
        print(count_notes[i], "nota(s) de R$", round(float(i),2))

"""

"""
m = int(input())
n = int(input())

lista_m = []
lista_n = []

soma_m = 1
soma_n = 1
if m <= 20 & m >= 0 and n <= 20 & n >= 0:
    for i in range(m, 0, -1):
        lista_m.append(i)
        soma_m = soma_m * i

    for i in range(n, 0, -1):
        lista_n.append(i)
        soma_n = soma_n * i

    soma_soma = soma_m + soma_n
    print(soma_soma)

else:
    print('digite valores entre 0 e 20')

"""

"""
n = int(input())

#função que verifica se o número é primo
def eh_primo(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True



if eh_primo(n) == True:
    print('Prime')

else:
    print('Not Prime')

"""

"""
a = int(input())
b = int(input())

list = []
count = 0

for i in range(a, b+1):
    list.append(i)
    count = count + i

print(count)
"""

"""
t = int(input())

t_blocks = int(input())

wished_area = int(input())

blocks = []

contagem = 0

count = 1

#coletando os tamanhos dos blocos e gravando em uma lista
for i in range(0, t_blocks):
    i = int(input())
    blocks.append(i)

print(blocks)

if count > 0:
    for i in blocks:
        count = wished_area - i
        contagem = contagem + 1

else:
    pass


print(contagem)
"""

"""
r = float(input())
v = (4/3.0) * 3.14159 * (r ** 3)

print(f'VOLUME =', v.__round__(3))
"""


"""
cases = int(input())


for i in range(cases):
    n = float(input())
    count = 0

    while n > 1 :
        n = n / 2
        count = count + 1

    print(count, "dias")        
"""

"""
def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 4 == 0:
        leap = True

        if year % 100 == 0:
            leap = False
    
        if year % 400 == 0:
            leap = True
    
    return leap
while True:
    year = int(input())
    print(is_leap(year))
"""

"""
n = int(input())

mystring = ''
for i in range(1, n+1):
    mystring += str(i)
    
print(mystring)
"""

