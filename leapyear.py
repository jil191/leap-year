fh = open('leapyear.txt','w')
a = int(input("Enter an year: ")) 
if(a%2==0): 
    fh.write("It's a leap year.") 
else: 
    fh.write("It's not a leap year")
fh.close()