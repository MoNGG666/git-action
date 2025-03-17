from django.http import HttpResponse

def home(request):
    return HttpResponse("""
        <h1>Добро пожаловать!</h1>
        <p>Базовый Django проект работает!</p>
    """)
