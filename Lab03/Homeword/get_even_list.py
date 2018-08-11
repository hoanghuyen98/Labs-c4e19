
def get_even_list(l):
    for i in range(len(l)):
        for item in l:
            if item % 2 != 0:
                l.remove(item)
    return l
    
            
even_list = get_even_list([1, 2, 5, -10, 9, 6])
print(even_list)
if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")





# l = [1, 4, 5, -3 ,-1, 10]
# m = []
# for item in l:
#     if item % 2 == 0:
#         m.append(item)
       
    

# print(m)