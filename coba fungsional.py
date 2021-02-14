#fungsi biasa
def polynominal(x):
    return x*2 + 5*x + 4
print(polynominal(-4))

#lambda
print ((lambda x: x*2 + 5*x + 4) (-4))


#iter
# list huruf vokal
vokal = ['a', 'i', 'u', 'e', 'o']

vokal_iter = iter(vokal)
# print 'a'
print(next(vokal_iter))
# print 'i'
print(next(vokal_iter))
# print 'u'
print(next(vokal_iter))
# print 'e'
print(next(vokal_iter))
# print 'o'
print(next(vokal_iter))
#https://www.pythonindo.com/fungsi-iter/#:~:text=Fungsi%20iter()%20berfungsi%20menghasilkan,di%20iterasikan%20satu%20persatu%20elemen.&text=Fungsi%20iter()%20memiliki%20dua,set%2C%20dan%20lain%2Dlain)
