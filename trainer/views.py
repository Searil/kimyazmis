# Create your views here.
# from wp.models import Post, Category
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
import trainer_lib


def home(request):
    print "home"
    c = {}
    c.update(csrf(request))
    return render_to_response('trainer/index.html', c)


def get_data(request):
    p = request.POST
    yazilar = []
    yazar_adi = p['yazar_adi']

    yazilar.append(p['yazi1_name'])
    yazilar.append(p['yazi2_name'])
    yazilar.append(p['yazi3_name'])
    yazilar.append(p['yazi4_name'])
    yazilar.append(p['yazi5_name'])

    # print request.POST['yazi1_name']

    avgs = trainer_lib.parse(yazar_adi, yazilar)
    c = {}
    c.update(csrf(request))
    c.update(avgs)
    c.update({"yazar": yazar_adi})
    return render_to_response('trainer/results.html', c)
