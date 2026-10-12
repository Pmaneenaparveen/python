number=list(map(int,input("enter integers separated by space:").split()))
for i in range(len(number)):
 if number[i]>100:
    number[i]="over"
print(number)
