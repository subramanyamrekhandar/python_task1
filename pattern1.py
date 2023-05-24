r = int(input("Enter the row : "))
#k = (2*r)-2   #k = some value
for i in range (r):      # for (i=r, i>=1 , --1) # 
    for j in range (r-i-1):
        print(end=" ")
    #k = k+1
    for j in range ((i+1)):  # 
        print("$", end=' ')
    print(" ")