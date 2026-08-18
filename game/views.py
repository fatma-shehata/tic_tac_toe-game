from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'game_title': 'tic tac toe',
        'player_x': 'Player X',
        'player_o': 'Player O',
        'instructions': [
            'Click any empty cell to place your mark',
            'Get three in a row to win',
            'Click Restart to play again',
        ],
    }
    return render(request,'game/index.html',context)