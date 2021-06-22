print('choose any operator')
print('1. Add')
print('2. Subtraction')
print('3. Multiplication')
print('4. Division')
print('5. percentage')

a=int(input('choose any option from 1,2,3,4,5 :'))
x = int(input('enter 1st number\n'))
y = int(input('enter 2nd number\n'))
if a==1:
    sum=x+y
    print('addition of given number =',sum)

elif a==2:

    sub=x-y
    print('substraction of',x, 'and',y,'=',sub)


elif a==3:

    mul=x*y
    print('multiplication of given number =',mul)

elif a==4:
    div=x/y
    print('Division of given number =',div)

elif a==5:
    x = int(input('enter a number\n'))
    y = int(input('How much percent\n'))
    per=x*(y/100)
    print('percent of given number =',per)


