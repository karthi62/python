list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common_item = []
for item in list1:
    if item in list2:
        common_item.append(item)
print("Common items:", common_item)
only_list1 = []
only_list2 = []
for item in list1:
    if item not in list2:
        only_list1.append(item)
for item in list2:
    if item not in list1:
        only_list2.append(item)
print("Items only in List 1:", only_list1) 
print("Items only in List 2:", only_list2)