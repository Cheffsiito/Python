import random

def my_shuffle(lst):
    shuffled_lst = lst[:]  
    for i in range(len(shuffled_lst)):
        j = random.randint(0, i)  
        shuffled_lst[i], shuffled_lst[j] = shuffled_lst[j], shuffled_lst[i]  
    return shuffled_lst

letters = ['a', 'b', 'c']
print(f"Original: {letters}")

shuffled_letters = my_shuffle(letters)
print(f"Shuffle: {shuffled_letters}")
