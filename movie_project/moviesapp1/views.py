from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Movie
from .forms import MoviesForm


def index(request):
    movie = Movie.objects.all()
    context = {
        "movie_list": movie
    }
    return render(request, 'index.html', context)
    # or another way is
    # return render(request, 'index.html',{'movie_list':movie})

    # Create your views here.


def details1(request, x_id):
    movie = Movie.objects.get(id=x_id)
    return render(request, 'details.html', {'movie': movie})


def add_movie(request):
    if request.method == 'POST':
        movie_name = request.POST.get('name1')
        movie_desc = request.POST.get('desc1')
        movie_year = request.POST.get('year1')
        movie_image = request.FILES['image1']
        movie_data = Movie(name=movie_name, desc=movie_desc, year=movie_year, ima=movie_image)
        movie_data.save()
    return render(request, 'add.html')


def updates(request,id):
    movie = Movie.objects.get(id=id)
    form = MoviesForm(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit1.html', {'form': form, 'movie': movie})
def delete(request,id):
    if request.method=='POST':
        movie = Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')
