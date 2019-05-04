from django.shortcuts import render
from .models import Movie
from .forms import Movie_form

# Create your views here.
def movie_view(request):
    return render(request,'movieapp/home.html')




def movie_list(request):
    movie_list=Movie.objects.all()
    return render(request,'movieapp/movielist.html',{'movie_list':movie_list})




def add_movie(request):
    form=Movie_form()
    if request.method=='POST':
        form=Movie_form(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return movie_view(request)
    return render(request,'movieapp/addmovie.html',{'form':form})
