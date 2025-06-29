#WAp distance given in feet and inches into metter and centimeter
feet=int(input("enter the distance in feet:"))
inches=int(input("enter the distance in inches:"))
total_meter=(feet*0.3048)+(inches*0.0254)
total_centimeter=total_meter*100
print("distance in meter:",total_meter)
print("distance in centimeter:",total_centimeter)