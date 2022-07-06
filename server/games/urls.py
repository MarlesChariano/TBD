from django.urls import path, include
from .views import allGameView, deleteGameView, updateGameView

urlpatterns = [

    path('games/all/',
         allGameView.as_view(), name='insert_game_view'),
    path('games/delete/',
         deleteGameView.as_view(), name='delete_game_view'),
    path('games/update/',
         updateGameView.as_view(), name='update_game_view'),
    

]