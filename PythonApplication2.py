import fractions
import math
option = int(input("1:sin,2:cos,3:tan!!!"))
def sinsqr2cos(x,y):
    xsqr=x*x
    ysqr=y*y
    cossqrx=ysqr-xsqr
    cosx=(math.sqrt(abs(cossqrx)))
    cosy=math.sqrt(ysqr)
    cosxx = int(cosx)
    cosyy = int(cosy)
    Cos=fractions.Fraction(cosxx,cosyy)
    return Cos
def tansqr2cos(a,b):
    asqr = a*a
    bsqr = b*b
    secsqrx = bsqr+asqr
    secx = int(math.sqrt(secsqrx))
    secy = int(math.sqrt(bsqr))
    sec = fractions.Fraction(secx,secy)
    cos = fractions.Fraction(1,sec)
    return cos

if option == 1:
    def main():
        x = eval(input("sin0x:"))
        y = eval(input("sin0y:"))
        xy =fractions.Fraction(x,y)
        z = sinsqr2cos(x,y)
        print("As sin0=",xy,"so cos0 is =",z,end=" ")
        Tan =fractions.Fraction(xy,z)
        print("And tan0 is =",Tan)
    main()
elif option == 3:
    a = int(input("enter tan0x:"))
    b = int(input("enter tan0y:"))
    ab =(fractions.Fraction(a,b))
    c = tansqr2cos(a,b)
    Sin = c*ab
    print("AS tan0=",ab,"then cos0=",c,'and sin0=',Sin)

else:
    exit()


    

