def Thaphanoi(n , vt1, vt2, a): 
    if n==1: 
        print ("Chuyển đĩa 1 từ vị trí",vt1,"đến vị trí",vt2 )
        return
    Thaphanoi(n-1, vt1, a, vt2) 
    print ("Chuyển đĩa",n,"tự vị trí",vt1,"đến vị trí",vt2 )
    Thaphanoi(n-1, a, vt2, vt1) 
          

n = 4
Thaphanoi(n,'A','B','C')