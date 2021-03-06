# Generated by Django 2.0 on 2018-01-08 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mystery_hunt', '0006_prediction_play_video_game'),
    ]

    operations = [
        migrations.CreateModel(
            name='CorrectAnswers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duck_konundrum', models.BooleanField(default=False)),
                ('puzzle_in_two_metas', models.BooleanField(default=False)),
                ('two_person_runaround', models.BooleanField(default=False)),
                ('duck_soup_scavenger_hunt', models.BooleanField(default=False)),
                ('duck_soup_end_game', models.BooleanField(default=False)),
                ('won_before_sunday', models.BooleanField(default=False)),
                ('theme_from_brainstorming', models.BooleanField(default=False)),
                ('isithuntyet_info', models.BooleanField(default=False)),
                ('recent_tv_show', models.BooleanField(default=False)),
                ('old_tv_show', models.BooleanField(default=False)),
                ('recent_video_game', models.BooleanField(default=False)),
                ('trump_twitter', models.BooleanField(default=False)),
                ('mtg_puzzle', models.BooleanField(default=False)),
                ('pokemon_puzzle', models.BooleanField(default=False)),
                ('supervocalic_puzzle', models.BooleanField(default=False)),
                ('taylor_swift_puzzle', models.BooleanField(default=False)),
                ('simpsons_puzzle', models.BooleanField(default=False)),
                ('vocaloids_puzzle', models.BooleanField(default=False)),
                ('data_from_old_source', models.BooleanField(default=False)),
                ('team_name_puzzle', models.BooleanField(default=False)),
                ('national_crossword_puzzle', models.BooleanField(default=False)),
                ('ternary_puzzle', models.BooleanField(default=False)),
                ('old_hunts_puzzle', models.BooleanField(default=False)),
                ('start_of_hunt_item_puzzle', models.BooleanField(default=False)),
                ('three_plus_cryptics', models.BooleanField(default=False)),
                ('dan_katz_wins', models.BooleanField(default=False)),
                ('play_video_game', models.BooleanField(default=False)),
                ('duck_soup_solves', models.PositiveSmallIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
