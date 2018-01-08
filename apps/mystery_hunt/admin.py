from django.contrib import admin

from .models import Prediction, CorrectAnswers

admin.site.register(Prediction)
admin.site.register(CorrectAnswers)