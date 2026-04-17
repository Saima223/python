first_name = "Rahul"
last_name  = "Sharma"
full_name  = first_name + " " + last_name   
print(full_name)

#The input() demo
score = 45
print(score)
score = score + 10    # update
print(score)
score += 5            # shorthand
print(score)

#string
raw = "  Hello Python  "
print(raw.strip())          # "Hello World"
print(raw)
print(raw.upper())
print(raw)
#print(raw.split())
xyz = raw.split()
print(xyz)
print(len(xyz))

sentence = "my name is priya"
words = sentence.split()   
print(words)
print(len(words))

messy = "phone: 98-765-43210"
clean = messy.replace("-", " ")
print(clean)  

abc = "phone: 98-765-43=22=10"
xyy =abc.replace("-", "").replace("=", "")
#xyzz = abc.replace("-","", "=", "")
print(xyy)