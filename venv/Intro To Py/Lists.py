print('hello')

baselist = ['liz','vicky','cory']
slicedlist = baselist[1:] #End integer here is TO not THROUGH!

print(slicedlist)

# changing elements
baselist[1] = 'victoria'

# add remove elements
baselist + slicedlist # = 1 list pasted together
fam_ext = ['joey']

#add joey
baselist = baselist + fam_ext
print(baselist)

#delete joey
del(baselist[3])
print(baselist)

#copy list
x = [1,2,3,4]
y = x[:]
y = list(x)