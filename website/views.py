from django.core.mail import send_mail,BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

# Create your views here.
from website.models import Questionnaire ,Questionnaire_affiche


def home(request):
    qa = Questionnaire_affiche.objects.first()
    print(qa)
    return render(request, 'website/accueil.html',{"objet": qa})

def lynch_explication(request):
    return render(request, 'website/lynch/explication.html')

def lynch_limites(request):
    return render(request, 'website/lynch/limites.html')

def lynch_noeuds(request):
    return render(request, 'website/lynch/noeuds.html')

def lynch_points_repere(request):
    return render(request, 'website/lynch/points_repere.html')

def lynch_quartiers(request):
    return render(request, 'website/lynch/quartiers.html')

def lynch_voies(request):
    return render(request, 'website/lynch/voies.html')

def cornavinM(request):
    return render(request, 'website/gare/cornavinMap.html')

def cornavinP(request):
    return render(request, 'website/gare/cornavinP.html')

def cornavinD(request):
    return render(request, 'website/gare/cornavinD.html')

def cornavinDM(request):
    return render(request, 'website/gare/cornavinDM.html')

def pontRougeM(request):
    return render(request, 'website/gare/pontrougeMap.html')

def pontRougeP(request):
    return render(request, 'website/gare/pontrougeP.html')

def pontRougeD(request):
    return render(request, 'website/gare/pontrougeD.html')

def pontRougeDM(request):
    return render(request, 'website/gare/pontrougeDM.html')

def bachetM(request):
    return render(request, 'website/gare/bachetMap.html')

def bachetP(request):
    return render(request, 'website/gare/bachetP.html')

def bachetD(request):
    return render(request, 'website/gare/bachetD.html')

def bachetDM(request):
    return render(request, 'website/gare/bachetDM.html')

def champelM(request):
    return render(request, 'website/gare/champelMap.html')

def champelP(request):
    return render(request, 'website/gare/champelP.html')

def champelD(request):
    return render(request, 'website/gare/champelD.html')

def champelDM(request):
    return render(request, 'website/gare/champelDM.html')

def eauxVivesM(request):
    return render(request, 'website/gare/eauxVivesMap.html')

def eauxVivesP(request):
    return render(request, 'website/gare/eauxVivesP.html')

def eauxVivesD(request):
    return render(request, 'website/gare/eauxVivesD.html')

def eauxVivesDM(request):
    return render(request, 'website/gare/eauxVivesDM.html')

def cheneBourgM(request):
    return render(request, 'website/gare/cheneBourgMap.html')

def cheneBourgP(request):
    return render(request, 'website/gare/cheneBourgP.html')

def cheneBourgD(request):
    return render(request, 'website/gare/cheneBourgD.html')

def cheneBourgDM(request):
    return render(request, 'website/gare/cheneBourgDM.html')

def formulaire(request):
    if request.method == 'GET':
        return render(request, 'website/formulaire.html',{})
    elif request.method == 'POST':
        nom = request.POST['nom']
        quartier=request.POST['quartier_1']
        quartier_futur=request.POST['quartier_1']
        org_ville_demain=request.POST['ville_1']
        hum_ville_demain=request.POST['ville_2']
        questionnaire_item = Questionnaire(nom=nom,quartier=quartier,quartier_futur=quartier_futur,org_ville_demain=org_ville_demain,hum_ville_demain=hum_ville_demain)
        questionnaire_item.save()
        try:
            html_message = loader.render_to_string(
                'website/mail/email_form.html',
                {
                    'nom': nom,
                    'quartier': quartier,
                    'quartier_futur': quartier_futur,
                    'org_ville_demain': org_ville_demain,
                    'hum_ville_demain': hum_ville_demain,
                }
            )
            send_mail("Reponse Questionnaire UEN", "", 'jerministephane@gmail.com', ['stephane-alain.jermini@hesge.ch'],
                      fail_silently=False, html_message=html_message)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return render(request, 'website/formulaire.html', {"succes":"yes"})

