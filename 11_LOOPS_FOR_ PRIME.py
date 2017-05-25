for x in range(5):  #to iterate between 10 to 20
   for i in range(2,x): #to iterate on the factors of the number
      if x%i == 0:      #to determine the first factor
         j=x/i          #to calculate the second factor
         print ("%d equals %d * %d" % (x,i,j))
         break #to move to the next number, the #first FOR
   else:                  # else part of the loop
      print (x, 'is a prime number')
