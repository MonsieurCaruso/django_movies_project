import csv
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Movie
from .forms import MovieForm, CSVUploadForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

@login_required(login_url='/accounts/login')
def watchlist_view(request):
    movies = Movie.objects.filter(user=request.user)
    
    return render(request, 'movies/movies.html', {'movies': movies})

@login_required(login_url='/accounts/login')
def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.user = request.user
            movie.save()
        return redirect('movies:watchlist')
    else:
        form = MovieForm()
    return render(request, 'movies/add_movie.html', {'form': form})

def upload_csv(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES.get('file')

            # Prüfen, ob die Datei tatsächlich eine CSV ist
            if not csv_file.name.endswith('.csv'):
                messages.error(request, 'Bitte laden Sie eine CSV-Datei hoch.')
                return render(request, 'upload_csv.html', {'form': form})

            # Dekodieren und Zeilen einlesen
            try:
                decoded_file = csv_file.read().decode('utf-8').splitlines()
                reader = csv.DictReader(decoded_file)

                # Daten in die Datenbank speichern
                for row in reader:
                        Movie.objects.create(
                            user=request.user,
                            title=row['title'],
                            director=row['director'],
                            release_year=row['release_year'],
                            genre=row['genre'],
                            imdb_url=row.get('imdb_url', '')  # Optionales Feld
                        )

                messages.success(request, 'Die Datei wurde erfolgreich hochgeladen und verarbeitet.')
                return redirect('movies:watchlist')
            except Exception as e:
                messages.error(request, f'Fehler beim Verarbeiten der Datei: {str(e)}')

    else:
        form = CSVUploadForm()

    return render(request, 'movies/upload_csv.html', {'form': form})