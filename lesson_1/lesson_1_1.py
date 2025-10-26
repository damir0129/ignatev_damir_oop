class Animal:
    color = 'green'
    paws = 4

Animal.paws = 2

cat = Animal()

cat.paws = 4

print(f"paws cat: {cat.paws}")
print(f"color cat: {cat.color}\n")

dog = Animal()
dog.color = 'white'

print(f"paws dog: {dog.paws}")
print(f"color dog: {dog.color}\n")
print(f"paws: {Animal.paws}")
# print(f"all attrs: {Animal.__dict__}")
