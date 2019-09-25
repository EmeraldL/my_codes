S = 1
den = 1
for num in range(3,39+1,2):
    den = den*2
    S = S + (num/den)
print("%.2f" % S)
