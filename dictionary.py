def amtpaid(obj): 
      
     sum = 0
     for i in obj: 
           sum = sum + obj[i] 
       
     return sum
  
# Driver Function 
obj = {'Rick': 85, 'Amit':42, 'George':53, 'Tanya':60, 'Linda':35} 
print("Sum :", amtpaid(obj)) 

    
    
    
        
    
