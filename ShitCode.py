
def hash(n):
   precision = 10
   point = 0

   #making number integral
   number = int(n)
   while n%number != 0 :
      n = n*10
      number = int(n)
      point = point + 1

   #making an array
   num = n
   arrNum = list()
   while num >= 1 :
      arrNum.append(int(num % precision))
      num = int(num / precision)
   
   #cheking number of precision
   arrNumCorrect = list()
   numlen = len(arrNum) 
   giveRight = arrNum[numlen - 1]
   j = 1
   while j <= giveRight :
      arrNumCorrect.append(arrNum[numlen - j])
      arrNum.pop()
      j = j + 1

   #sorting
   arrNum.sort()

   #reforming
   n = 0
   k = 0
   while k < giveRight :
      n = n + arrNumCorrect[k]*(10**(numlen - 1 - k))
      k = k + 1
   while k < numlen :
      n = n + arrNum[k - giveRight]*(10**(numlen - 1 - k))
      k = k + 1
   n = n / (10**(point))
   return n

def add(m,n): 
   decimalPoint = 0
   sum = 0.00
   n1 = int(n)
   m1 = int(m)
   if n%n1 == 0 and m%m1 == 0:
      if m**n < 10**7:
         while m**n < 10**7:
            m = m*10
            n = n*10
            decimalPoint += 1
         #addition from gandhi
      elif m**n >= 10**7:
         pass 
         #gandhi code for add
   else :
      while m*n < 10**7 :
         m *= 10
         n *= 10
      m = int(m)
      n = int(n)
      #gandhian math
   return sum
