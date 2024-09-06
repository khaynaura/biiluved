from django.shortcuts import render

def show_main(request):
    context = {
        'app_name' : 'biiLUVed',
        'name': 'Khayla Naura Ulya Luqyana',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)
