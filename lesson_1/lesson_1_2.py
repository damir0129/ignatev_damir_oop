class Animal:
    "Класс для создания животных"
    color = 'green'
    paws = 4

cat = Animal()
dog = Animal()

# cat.meal = 'fish'

setattr(cat, "meal", "fish")

print(cat.meal)
print(getattr(cat, "meal"))
print(getattr(cat, "color"))
print(getattr(cat, "color_paw", "black"))
# print(cat.__dict__)

delattr(cat, "meal")

print(Animal.__doc__)