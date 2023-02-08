name = input('Eneter your name: ')
print('Hello, ', name)

temp = eval(input('Enter a temperature in Celsius: '))
print('In Fahrenheit,that is', 9/5*temp+32)
num1 = eval(input('Enter the first number: '))
num2 = eval(input('Enter the second number: '))
print('the average of the numbers you entered is', (num1+num2)/2)
num = eval(input('Enter a number: '))
print('Your number squared:', num*num)
print('Hi there')
print('the value of 3+4 is', 3+4)
print('A', 1, 'XYZ' , 2)
print('On the first line' , end='') 
print('The second line')
temp = eval(input('Enter a temperature in Celsius: '))
f_temp = 9/5*temp+32
print('In Fahrenheit, that is' , f_temp)
if f_temp > 212:
    print('That temperature is above the boiling point.')
if f_temp < 32:
    print('That temperature is below the freezing point.')    
