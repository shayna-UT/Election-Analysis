import random
random_float_0to1 = random.random()
print(random_float_0to1)

random_float_1to10 = random.uniform(1,10)
print(random_float_1to10)

random_int_1to10 = random.randint(1,10)
print(random_int_1to10)

random_even_int_0to100 = random.randrange(0,101,2)
print(random_even_int_0to100)

random_choice = random.choice('abcdefghij')
print(random_choice)

items = [1,2,3,4,5,6,7]
random.shuffle(items)
print(items)

random_sample_3elements = random.sample([1,2,3,4,5], 3)
print(random_sample_3elements)