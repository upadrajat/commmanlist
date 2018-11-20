def common_member(a, b): 
	a_set = set(a) 
	b_set = set(b) 
	if (a_set & b_set): 
		print(a_set & b_set) 
	else: 
		print("No common elements") 
		

a = ['a','b','c'] 
b = ['b','d'] 
common_member(a, b) 

a = ['a','b','c'] 
b = ['b','d'] 
common_member(a, b) 
