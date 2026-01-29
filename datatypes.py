# dynamicallu run data type so we dont have to define the 
# data type before and the interpreter is deciding the type of
# values automatically in run time.
a=23        #INTEGER
print (type(a))

b=34.44     #FLOAT
print(b)    # just for output of variable b to be shown, no other needs
print(type(b))

c="sujan"   #STRING
print(c)    # just for output of variable c to be shown no other needs
print(type(c))

d=5+7j      #COMPLEX
print(d)
print(type(d))

e=True      #BOOLEAN
print(e)
print(type(e))

f=[38,46.4,"sujan"]     #LIST []
print(e)
print(type(f))
 #LIST- list is a datatype in python which lets users store 
 # different types of values like str,int,float,etc enclosed in a "[]".

g=("ram",6,6.7)     #TUPLE ()
print(g)
print(type(g))
#TUPLE- same as LIST lets users store differnt types 
# of values but enclosed in a "()"

h={"sita",7,7.5}        #SET {}
print(h)
print(type(h))
#SET- same as LIST lets users store differnt types 
# of values but enclosed in a "{}"

i={'age':21}      #DICTIONARY {'key':value}
print(i)
print(type(i))  
#DICTIONARY-a dict type has key and value,
# in this case 'age'=key and 21=value
# the value of 'age' is 21. (so the key represents the value)
#ACCESSING THE VALUE THROUGH KEY USING get method-
print(i.get('age'))
# we printed the key-'age' but the output came 21 that is 
# because the key represents the value.
# "i." because (get) will take key form 'i'
  


#NOW THE DIFFERNCES BETWEEN LIST, TUPLE, SET, DICT-

#LIST allows the use of duplicate values and
#  TUPLE also allows the use of duplicate values
#  but they differ in the use of brackets;
# LIST uses [] but TUPLE uses () 

#  SET does not allow the use of 'duplicate values' whereas
#  DICTIONARY does not allow the use of 'duplicate keys' 
# (each key has to be unique)

# if you use duplicate values in SET 
# then the 'same value will be returned only once'
# if you use duplicate keys in DICT
# then only one key will be considered the other won't be allowed
# if you use duplicate key but with different values 
# then the value of only the latest will be considered. 