from django.shortcuts import render, redirect
from .models import Feedback,Service,ServiceCategory,Portfolio
from .forms import FeedbackForm
from django.http import Http404


def index(request):
    portfolio = Portfolio.objects.all()
    return render(request, 'main/index.html', {'port':portfolio})


def portfolio(request):
    portfolio = Portfolio.objects.all()
    if portfolio is not None:
        return render(request, 'main/portfolio.html', {'port':portfolio})
    else:
        raise Http404('Does not exist')


def services(request):
    service = Service.objects.all()
    service_cats = ServiceCategory.objects.all()

    context = {
        'service':service,
        'service_cats':service_cats,
    }

    return render(request, 'main/services.html', context)


def feedbacks(request):
    feedbacks = Feedback.objects.all().order_by('-id')
    return render(request, 'main/feedbacks.html', {'title': 'Отзывы', 'feedbacks': feedbacks})


def create_fb(request):
    error = ''
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedbacks')
        else:
            error = 'Оценка качества работы не должна превышать 5'

    form = FeedbackForm()

    context = {
        'form': form,
        'title': 'Написать отзыв',
        'error': error,
    }
    return render(request, 'main/create_fb.html', context)


def contacts(request):
    return render(request, 'main/contacts.html')

