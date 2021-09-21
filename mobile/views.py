from django.shortcuts import render

# Create your views here.



def carougeBachet(request):
    return render(request, 'mobile/CarougeBachet.html')

def carougeBachetMap(request):
    return render(request, 'mobile/CarougeBachetMap.html')



def champelHopital(request):
    return render(request, 'mobile/ChampelHopital.html')

def champelHopitalMap(request):
    return render(request, 'mobile/ChampelHopitalMap.html')



def cheneBourg(request):
    return render(request, 'mobile/CheneBourg.html')

def cheneBourgMap(request):
    return render(request, 'mobile/CheneBourgMap.html')


def cornavin(request):
    return render(request, 'mobile/Cornavin.html')

def cornavinMap(request):
    return render(request, 'mobile/CornavinMap.html')

def geneveEauxVives(request):
    return render(request, 'mobile/geneveEauxVives.html')

def geneveEauxVivesMap(request):
    return render(request, 'mobile/geneveEauxVivesMap.html')


def lancyPontRouge(request):
    return render(request, 'mobile/lancyPontRouge.html')

def lancyPontRougeMap(request):
    return render(request, 'mobile/lancyPontRougeMap.html')