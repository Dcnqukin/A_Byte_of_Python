import pickle as p
'''Python3 did not contain cPickle module'''

shoplistfile = 'shoplist.data'

shoplist = ['apple', 'mango', 'carrot']

'''f = file(shoplistfile, 'w')'''
f = open(shoplistfile, 'wb')
p.dump(shoplist, f)
f.close()

del shoplist

f = open(shoplistfile,'rb')
storedlist = p.load(f)
print(storedlist)
