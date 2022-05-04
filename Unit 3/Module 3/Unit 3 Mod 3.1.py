#Will C.
#Python 1
#Unit 2, Mod 3.1

# [ ] Use the variables `F` and `C` to generate the following print outputs
'''
75 Fahrenheit = 23.888900 Celsius
75 Fahrenheit = 23.89 Celsius
75 Fahrenheit = 000023.889 Celsius
75 Fahrenheit = 23.889     Celsius
75 Fahrenheit =     23.889 Celsius
75 Fahrenheit = 2.389E+01 Celsius
75 Fahrenheit = 2.389e+01 Celsius
'''
F = 75
C = 23.8889
print("%d Fahrenheit = %f Celcius"%(F,C))
print("%d Fahrenheit = %3.2F Celcius"%(F,C))
print("%d Fahrenheit = %010.3F Celcius"%(F,C))
print("%d Fahrenheit = %9.2f Celcius"%(F,C))