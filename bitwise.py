a,b=5,4
print(a&b) 
#bitwise and
"""5=0 1 0 1
   4=0 1 0 0
ans= 0 1 0 0 =4
"""
print(a|b)
#bitwise or
"""5=0 1 0 1
   4=0 1 0 0
ans= 0 1 0 1 =5
"""
print(a^b)
#bitwise x-or
""" 5=0 1 0 1
    4=0 1 0 0
ans=  0 0 0 1 =1
"""
print(~a)
#bitwise not
"""5=0 1 0 1
2's compliment=1's compliment+1  
6=    0 1 1 0
1'sC= 1 0 0 1
+           1
      1 0 1 0
      FORMULA= (~n)=-(n+1)
"""
print(a<<2)
#bitwise left shift- gains the bits
""" 5= 0 1 0 1
     0 1 0 1 _0 _0 =20
     FORMULA =(X<<n)= X*2^n (5<<2)=5*2^2=5*4=20
"""
print(a>>2)
#bitwise right shift -looses the bits
""" 5=0 1 0 1
       0 0  0   1 =1
       FORMULA=(X>>n)=X/2^n  (5>>2)=5/2^2=5/4=1
 """
# assignment
print(26&23)
print(17|24)
print(17^24)
print(~45)
print(68<<2)
print(56>>3)