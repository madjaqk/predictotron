from django.db import models
from django.forms import ModelForm

class Question(models.Model):
    duck_konundrum = models.BooleanField(default=False)
    puzzle_in_two_metas = models.BooleanField(default=False)
    two_person_runaround = models.BooleanField(default=False)
    duck_soup_scavenger_hunt = models.BooleanField(default=False)
    duck_soup_end_game = models.BooleanField(default=False)
    won_before_sunday = models.BooleanField(default=False)
    theme_from_brainstorming = models.BooleanField(default=False)
    isithuntyet_info = models.BooleanField(default=False)
    recent_tv_show = models.BooleanField(default=False)
    old_tv_show = models.BooleanField(default=False)
    recent_video_game = models.BooleanField(default=False)
    trump_twitter = models.BooleanField(default=False)
    mtg_puzzle = models.BooleanField(default=False)
    pokemon_puzzle = models.BooleanField(default=False)
    supervocalic_puzzle = models.BooleanField(default=False)
    taylor_swift_puzzle = models.BooleanField(default=False)
    simpsons_puzzle = models.BooleanField(default=False)
    vocaloids_puzzle = models.BooleanField(default=False)
    data_from_old_source = models.BooleanField(default=False)
    team_name_puzzle = models.BooleanField(default=False)
    national_crossword_puzzle = models.BooleanField(default=False)
    ternary_puzzle = models.BooleanField(default=False)
    old_hunts_puzzle = models.BooleanField(default=False)
    start_of_hunt_item_puzzle = models.BooleanField(default=False)
    three_plus_cryptics = models.BooleanField(default=False)
    dan_katz_wins = models.BooleanField(default=False)
    play_video_game = models.BooleanField(default=False)

    duck_soup_solves = models.PositiveSmallIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(vars(self))

    def getattr(self, attr):
        return getattr(self, attr)

    class Meta:
        abstract = True

class Prediction(Question):
    name = models.CharField(max_length=50)

    def score(self):
        correct = CorrectAnswers.objects.first()

        if correct is None:
            return None
        
        fields = ["theme_from_brainstorming", "puzzle_in_two_metas", "won_before_sunday", "two_person_runaround", "isithuntyet_info", "data_from_old_source", "team_name_puzzle", "national_crossword_puzzle", "play_video_game", "ternary_puzzle", "old_hunts_puzzle", "start_of_hunt_item_puzzle", "three_plus_cryptics", "duck_soup_scavenger_hunt", "duck_soup_end_game", "dan_katz_wins", "duck_konundrum", "recent_tv_show", "old_tv_show", "recent_video_game", "trump_twitter", "mtg_puzzle", "pokemon_puzzle", "supervocalic_puzzle", "taylor_swift_puzzle", "simpsons_puzzle", "vocaloids_puzzle",]

        points = 0

        for field in fields:
            if getattr(self, field) == getattr(correct, field):
                points += 120 // Prediction.objects.filter(**{field: getattr(correct, field)}).count()

        return points, -abs(correct.duck_soup_solves - self.duck_soup_solves)



class CorrectAnswers(Question):
    pass

class PredictionForm(ModelForm):
    class Meta:
        model = Prediction
        fields = [
            "name", 
            "theme_from_brainstorming",
            "puzzle_in_two_metas",
            "won_before_sunday",
            "two_person_runaround",
            "isithuntyet_info",
            "data_from_old_source",
            "team_name_puzzle",
            "national_crossword_puzzle",
            "play_video_game",
            "ternary_puzzle",
            "old_hunts_puzzle",
            "start_of_hunt_item_puzzle",
            "three_plus_cryptics",
            "duck_soup_scavenger_hunt",
            "duck_soup_end_game",
            "dan_katz_wins",
            "duck_konundrum",
            "recent_tv_show",
            "old_tv_show",
            "recent_video_game",
            "trump_twitter",
            "mtg_puzzle",
            "pokemon_puzzle",
            "supervocalic_puzzle",
            "taylor_swift_puzzle",
            "simpsons_puzzle",
            "vocaloids_puzzle",
            "duck_soup_solves",
        ]
        labels = {
            "name": "Your name",
            "duck_konundrum": '"Duck Konundrum" puzzle (that is, a following instructions puzzle with clear duck theming--2013\'s "Time Conundrum" and 2015\'s "Connect The Ducks" both count)',
            "puzzle_in_two_metas": "A puzzle is part of at least two metapuzzles",
            "two_person_runaround": "A runaround puzzle that requires more than one person to complete",
            "duck_soup_scavenger_hunt": "Duck Soup completes a scavenger hunt",
            "duck_soup_end_game": "Duck Soup unlocks the end game",
            "won_before_sunday": "The Hunt is won before Sunday (MIT time)",
            "theme_from_brainstorming": "Hunt theme matches one of the ideas from our brainstorming (Greek myth, Internet, video games, Harry Potter, Marx brothers, weddings, recipes, superheroes)",
            "isithuntyet_info": "isithuntyet.info is part of the puzzle",
            "recent_tv_show": "Puzzle about a TV show that started airing in 2016 or later",
            "old_tv_show": "Puzzle about a TV show that stopped airing before 1980",
            "recent_video_game": "Puzzle about a video game that came out in 2016 or later",
            "trump_twitter": "Puzzle about Donald Trump's Twitter",
            "mtg_puzzle": "Puzzle about Magic: the Gathering",
            "pokemon_puzzle": "Puzzle about Pokémon",
            "supervocalic_puzzle": "Puzzle about supervocalics",
            "taylor_swift_puzzle": "Puzzle about Taylor Swift",
            "simpsons_puzzle": "Puzzle about The Simpsons",
            "vocaloids_puzzle": "Puzzle about Vocaloids",
            "data_from_old_source": "Puzzle data is embedded in something produced before November 1, 2017",
            "team_name_puzzle": "Puzzle relying on team names",
            "national_crossword_puzzle": "Puzzle requires solving a nationally-published crossword",
            "ternary_puzzle": "Puzzle users ternary in extraction",
            "old_hunts_puzzle": "Puzzle that references past Mystery Hunts",
            "start_of_hunt_item_puzzle": "Something given at the start of the Hunt is a puzzle",
            "three_plus_cryptics": "At least three puzzles involve solving cryptic crossword clues",
            "dan_katz_wins": "Dan Katz is on the winning team",
            "play_video_game": "A puzzle requires playing some sort of video game written specifically for the Hunt",
            "duck_soup_solves": "TIEBREAKER: How many puzzles will Duck Soup solve?",
        }