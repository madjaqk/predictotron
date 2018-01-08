from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from .models import Prediction, PredictionForm, CorrectAnswers

# Create your views here.
def index(request):
    return render(request, "mystery_hunt/index.html", {"form": PredictionForm()})

def process(request):
    if request.method != "POST":
        return redirect("mystery_hunt:index")

    new_prediction = PredictionForm(request.POST)
    new_prediction.save()

    return redirect("mystery_hunt:all")

def all(request):
    context = {
        "predictions": Prediction.objects.all(),
        "correct": CorrectAnswers.objects.first(),
    }

    return render(request, "mystery_hunt/show_all.html", context)

def show_one(request, pred_id):
    fields = ["theme_from_brainstorming", "puzzle_in_two_metas", "won_before_sunday", "two_person_runaround", "isithuntyet_info", "data_from_old_source", "team_name_puzzle", "national_crossword_puzzle", "play_video_game", "ternary_puzzle", "old_hunts_puzzle", "start_of_hunt_item_puzzle", "three_plus_cryptics", "duck_soup_scavenger_hunt", "duck_soup_end_game", "dan_katz_wins", "duck_konundrum", "recent_tv_show", "old_tv_show", "recent_video_game", "trump_twitter", "mtg_puzzle", "pokemon_puzzle", "supervocalic_puzzle", "taylor_swift_puzzle", "simpsons_puzzle", "vocaloids_puzzle",]

    bool_to_english = {
        True: "yes",
        False: "no"
    }

    pred = get_object_or_404(Prediction, id=pred_id)

    labels = {
        "duck_konundrum": '"Duck Konundrum" puzzle',
        "puzzle_in_two_metas": "A puzzle is part of at least two metapuzzles",
        "two_person_runaround": "A runaround puzzle that requires more than one person to complete",
        "duck_soup_scavenger_hunt": "Duck Soup completes a scavenger hunt",
        "duck_soup_end_game": "Duck Soup unlocks the end game",
        "won_before_sunday": "The Hunt is won before Sunday (MIT time)",
        "theme_from_brainstorming": "Hunt theme matches one of the ideas from our brainstorming",
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
        "play_video_game": "A puzzle requires playing a video game written for the Hunt",
    }

    correct = CorrectAnswers.objects.first()

    if correct:
        points = {field: 120 // Prediction.objects.filter(**{field: getattr(correct, field)}).count() if getattr(pred, field) == getattr(correct, field) else 0 for field in fields}
        points["duck_soup_solves"] = abs(correct.duck_soup_solves - pred.duck_soup_solves)
    else:
        points = None

    context = {
        "pred": pred,
        "fields": fields,
        "labels": labels,
        "correct": correct,
        "points": points
    }
    return render(request, "mystery_hunt/show.html", context)

def get_stats(request):
    stats = {
        "duck_soup_solves": [
            [pred.duck_soup_solves, 0, pred.name] for pred in Prediction.objects.all()
        ]
    }

    fields = ["theme_from_brainstorming", "puzzle_in_two_metas", "won_before_sunday", "two_person_runaround", "isithuntyet_info", "data_from_old_source", "team_name_puzzle", "national_crossword_puzzle", "play_video_game", "ternary_puzzle", "old_hunts_puzzle", "start_of_hunt_item_puzzle", "three_plus_cryptics", "duck_soup_scavenger_hunt", "duck_soup_end_game", "dan_katz_wins", "duck_konundrum", "recent_tv_show", "old_tv_show", "recent_video_game", "trump_twitter", "mtg_puzzle", "pokemon_puzzle", "supervocalic_puzzle", "taylor_swift_puzzle", "simpsons_puzzle", "vocaloids_puzzle",]

    english_to_bool = {
        "yes": True,
        "no": False
    }

    for field in fields:
        stats[field] = {
            english: Prediction.objects.filter(**{field: boolean}).count() for english, boolean in english_to_bool.items()
        }

    return JsonResponse(stats)