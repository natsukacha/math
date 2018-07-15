s1="A cat sat on the cat mat"
s2="Cats are sitting on the mat"

s1_a=s1.split(" ")
s2_a=s2.split(" ")

#print(s1_a,s2_a)
def cnt(s1_a):
	s1_d={}
	for i in s1_a:
		if i not in s1_d:
			s1_d[i] = 1
		else:
			s1_d[i] +=1
	print(s1_d)	
cnt(s1_a)
cnt(s2_a)
#print(s1_d)		