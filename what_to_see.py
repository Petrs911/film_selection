import random

with open ("Films.txt", "r") as list1:
    film_list = list1.read().split('\n')  
     
def movie_search(some_list):
    i = 0
    for n in some_list:
        if '@' in n:
            i += 1
    if i == len(some_list):
        return "Вы видели все фильмы!"
    else:
        while True:
            film = random.choice(some_list)
            if '@' in film:
                i = True
            else:
                return film
                break
           
def change_list(some_film):
    index_element = film_list.index(some_film)
    film_list[index_element] = some_film + '@'
    changed_film_list = "\n".join(film_list)
    return changed_film_list    

a = movie_search(film_list)
if a == "Вы видели все фильмы!":
    print(a)
else:
    b = change_list(a)
    print('Выпал этот фильм: ', a)
    with open ("Films.txt", "w") as film:
        film.write(b)  
     





