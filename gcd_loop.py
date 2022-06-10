#Program to find the highest common factor (H.C.F) or greatest common divisor (G.C.D)

# define a function
def compute_hcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i 
    return hcf

num1 = 54 
num2 = 24

print("The H.C.F. is", compute_hcf(num1, num2))

#+ Addition
#- Sub
#* Mult
#/ Div
#% Mod
#** Exp
#// Floor division - rounds the result down to the nearest whole number