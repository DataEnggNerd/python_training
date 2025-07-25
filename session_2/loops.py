# loops 

# purpose -> iteration

a = list(range(0, 10))
b = list(range(10, 20))
# print(a)
# import pdb; pdb.set_trace()

# structure of for loop
# for => keyword
# temp_variable => iterator
# in => keyword
# target iterable => list or set dict

for i in a:
    for j in b:
        # import pdb; pdb.set_trace()
        print(i, j)
        print(i*j)

# while loop
# applicable when the end point is not available

#structure 
# initiator => i =0
# while => keyword
# i < 99 => condition check
# functional statement => ...
# i+=1 => incrementing the initiator

i = 0
while i < 99:
    print(i)
    if i%2 == 0:
        print(i)
    i+=1
    print("="*10)
    
    # condition = False