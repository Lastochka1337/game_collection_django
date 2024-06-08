import django_setup

from collection.models import Game, Genre

'''game1 = Game(
    name = "CS2",
    genre = "shooter", 
    year = "2023", 
    rating = 3.5
)

game2 = Game(
    name = "Red Dead Redemtion 2",
    genre = "adventure", 
    year = "2018", 
    rating = 4.8
)

game1.save()
game2.save()'''

'''game_to_update = Game.objects.get(id=2)
game_to_update.name = "Cyberpunk 2077"
game_to_update.genre = "adventure"
game_to_update.year = 2020
game_to_update.rating = 4.5

game_to_update.save()'''

game1 = Game.objects.get(id = 5)
genre1 = Genre.objects.get(id = 4)

game1.genres.add(genre1)