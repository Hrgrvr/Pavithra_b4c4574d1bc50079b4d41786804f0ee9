#1.1 Implement a recursion function to calculate the factorial of a given number

def fact_rec(n):
  if n==0 or n==1:
     return 1 
  else:
    return n*fact_rec(n-2)

number =2
res=fact_rec(number )

print("factorial of {} is {}".format (number,res))
      
