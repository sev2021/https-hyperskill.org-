from django.db import models

##  To build the whole schema, we start from the core element, the Team:

class Team(models.Model):
    name = models.CharField(max_length=64)
    
    
## Each team has players. Let's define a model for a player:

class Player(models.Model):
    height = models.FloatField()
    name = models.CharField(max_length=64)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)


##  Games:

class Game(models.Model):
    home_team = models.ForeignKey(Team, related_name='game_at_home', on_delete=models.CASCADE)
    home_team_points = models.IntegerField()
    rival_team = models.ForeignKey(Team, related_name='rival_game', on_delete=models.CASCADE)
    rival_team_points = models.IntegerField()
    date = models.DateField()
    
