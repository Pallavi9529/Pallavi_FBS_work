#WAP to convert time entered in hh,min,and sec into seconds
hrs=int(input("enter the no of hrs:"))
min=int(input("enter the no of min:"))
sec=int(input("enter the no of sec:"))
tosec=(hrs*3600+min*60,sec+30)
print("tsec:",tosec)
