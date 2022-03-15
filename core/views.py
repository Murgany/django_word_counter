from django.shortcuts import render


def index(request):
    return render(request, 'index.html', )


# small word counter app
def counter(request):
    text = request.POST['text']
    word_count = len(text.split())
    return render(request, 'counter.html', {'word_count': word_count})
