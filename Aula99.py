import sys

# Generator expression, Iterables e Iterators em Python
iterable = ['Eu', 'Tenho', '__iter__']
iterador = iter(iterable) # tem __iter__ e __next__

lista = [n for n in range(10000)]
gerenator = (n for n in range(10000))
print(sys.getsizeof(lista))
print(sys.getsizeof(gerenator))

print(gerenator)

# for n in gerenator:
#     print(n)