import math
vdd = 1.8
uncox = 300
upcox = 68
lambdan = 0.05
lambdap = 0.1
vds7 = 0.3
vds11 = 0.3
vds12 = 0.3
vds17 = 0.3
vds9 = 0.35
vds15 = 0.35
vds5 = 0.15
vds6 = 0.15
vtn = 0.4
vtp = 0.42
ip3 = 20
in0 = 40
ip0 = 40
def vds_2_wl(i, vds, ty):
    if(ty == "n"):
        return 2*i/(uncox*(vds**2))
    elif (ty == "p"):
        return 2*i/(upcox*(vds**2))



vb1 = vdd - vds7-vds9 -vtp
vb2 = vds15 +vtn + vds17
vb3 = vdd - vds7 -vtp - vds11 -vtp
vb4 = vds12 + vds17 + 2*vtn



print("W/L 7,8 = "+str(vds_2_wl((ip3+in0/2), vds7, 'p')))
print("W/L 9,10 = "+str(vds_2_wl((ip3), vds9, 'p')))
print("W/L 15,16 = "+str(vds_2_wl((ip3), vds15, 'n')))
print("W/L 17,18 = "+str(vds_2_wl((ip3), vds17, 'n')))
print("W/L 12,13 = "+str(vds_2_wl((ip3/2), vds12, 'n')))
print("W/L 11,14 = "+str(vds_2_wl((ip3/2), vds12, 'p')))




print("W/L 5 = "+str(vds_2_wl((in0), vds5, 'n')))
print("W/L 6 = "+str(vds_2_wl((ip0), vds6, 'p')))



gm1 = 250
def gm_2_wl(i, gm, ty):
    if(ty =="n"):
        return (gm**2/(2*i*uncox))
    elif(ty == "p"):
        return (gm**2/(2*i*upcox))

print("W/L 1,2 = "+str(gm_2_wl(in0/2, gm1, 'n')))
print("W/L 3,4 = "+str(gm_2_wl(in0/2, gm1, 'p')))
WL10 = vds_2_wl((ip3), vds9, 'p')
gm10 = math.sqrt(2*ip3*upcox*WL10)
ro8 = 1/(lambdap*(ip3+in0))
ro10 = 1/(lambdap*ip3)



gain = gm1 * gm10*ro8*ro10



print(gain)
