# a = int(input("Enter 1st number: "))
# b = int(input("Enter 2nd number: "))



from django.http import HttpResponse

from Letsbegin import views


def jango1(a,b):
  def adj(k,p):
          for n in range(0,p-1):
            if k[n]== "1" and k[n+1]== "1":
              return mydict.update({i:'True'})
            else: 
              return mydict.update({i:'False'})   

  mydict = {}
  
  for i in range(a,b):
    
     k = bin(i)
     s= k[2:]
     p = len(s)
       
     adj(s,p)
  ans =  str(mydict) 
  return HttpResponse(ans)



