a = float(input('a= '))
b = float(input('b= '))
area = a * b

print(f'area= {area}')

n = int(input('Enter n: '))

if (n <= 1):
    print("n should be greater than 1")
    exit()

print("value of n: ", n)
print(f'numbers from {1} to {n} are:')

for i in range(1, n + 1, 1):
    print(i)

print("\"az\" + 'sam'")
