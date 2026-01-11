num = int(input("enter the number: "))
i = 2
count = 1
while(i<num):
  if num % i == 0:
     count=2
     break
  i+=1
if count == 1:
    print('prime',num)
else:
    print('not prime')
