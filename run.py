from build.Release import example

print(example.add1())
print(example.add2(i=23, j=2))
print(example.the_answer)
print(example.what)
print(example.warning)
# print(help(example))

p = example.Pet("Dabai")
print(p)
print(p.name)
print(p.getName())
p.setName("Xiaohui")
print(p.getName())
