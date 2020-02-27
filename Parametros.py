import sys
print("Número de parâmetros: %d" % len(sys.argv))
for n, p in enumerate(sys.argv):
    print("Parâmetro %d = %s" % (n, p))
