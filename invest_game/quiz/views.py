from django.shortcuts import render

def Quiz_list(request):
    return render(
        request,
        'quiz/question.html'
    )