# Create your views here.
# from wp.models import Post, Category
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.db.models import Q
from .models import Yazar, TestYazar

from trainer import parse_one_entry, entry_builder, entry_cleaner
from predictor import build_features, predict_author, get_score

import os
import pickle


def build_traindata(request):
    c = {}
    c.update(csrf(request))

    Yazar.objects.all().delete()

    module_dir = os.path.dirname(__file__)  # get current directory
    os.chdir(module_dir)

    yazar_arr = [
        "AyseArman", "AhmetHakan", "YilmazOzdil",
        "MehmetAliBirand", "MehmetBaransu", "TahaAkyol",
        "MehmetBarlas", "NazliIlicak", "CuneytOzdemir",
        "AhmetAltan", "HincalUluc", "NihalBengisuKaraca",
        "PerihanMagden", "RuhatMengi", "YaseminCongar",
        "BekirCoskun", "CengizCandar", "EnginArdic",
        "MutluTonbekici", "SuleymanOzisik"
    ]

    for yazar in yazar_arr:
        file_path = os.path.join(module_dir, 'Yazarlar/' + yazar)
        print "[DEBUG] " + str(file_path)

        for file in os.listdir(file_path):
            avgs = parse_one_entry(entry_builder(file, yazar))

            y = Yazar(yazar_adi=yazar,
                      # exclamation=avgs["exclamation"],
                      exclamation_n=avgs["exclamation_n"],
                      exclamation_r=avgs["exclamation_r"],
                      # question_mark=avgs["question_mark"],
                      question_mark_n=avgs["question_mark_n"],
                      question_mark_r=avgs["question_mark_r"],
                      # coma_count=avgs["coma"],
                      coma_count_n=avgs["coma_n"],
                      coma_count_r=avgs["coma_r"],
                      # yan_cizgi=avgs["yan_cizgi"],
                      yan_cizgi_n=avgs["yan_cizgi_n"],
                      yan_cizgi_r=avgs["yan_cizgi_r"],
                      quote_n=avgs["quote_n"],
                      quote_r=avgs["quote_r"],
                      single_quote_n=avgs["single_quote_n"],
                      single_quote_r=avgs["single_quote_r"],
                      double_dot_n=avgs["double_dot_n"],
                      double_dot_r=avgs["double_dot_r"],
                      triple_dot_n=avgs["triple_dot_n"],
                      triple_dot_r=avgs["triple_dot_r"],
                      stopwords_n=avgs["stopwords_n"],
                      stopwords_r=avgs["stopwords_r"],
                      # stars_n=avgs["stars_n"],
                      # stars_r=avgs["stars_r"],
                      sentence_len=avgs["sentence_len"],
                      paragraph_len=avgs["paragraph_len"])
            y.save()

    return render_to_response('trainer/index.html', c)


def build_pickled_array(request):
    """
    The generated array used by matplotlib
    to draw plots

    Arguments:
    - `request`:
    """
    c = {}
    c.update(csrf(request))

    module_dir = os.path.dirname(__file__)  # get current directory
    os.chdir(module_dir)
    file_path_data = os.path.join(module_dir, 'PickledDataArrays/data.pkl')
    file_path_target = os.path.join(module_dir, 'PickledDataArrays/target.pkl')

    five_authors = Yazar.objects.filter(
        Q(yazar_adi="AhmetHakan") |
        Q(yazar_adi="BekirCoskun") |
        Q(yazar_adi="TahaAkyol") |
        Q(yazar_adi="CuneytOzdemir") |
        Q(yazar_adi="YaseminCongar")
    )
    data_arr = []
    target_arr = []

    for yazar in five_authors:
        data_arr.append([yazar.paragraph_len] + [yazar.sentence_len])
        if yazar.yazar_adi == u"AhmetHakan":
            target_arr.append(0)
        elif yazar.yazar_adi == u"BekirCoskun":
            target_arr.append(1)
        elif yazar.yazar_adi == u"TahaAkyol":
            target_arr.append(2)
        elif yazar.yazar_adi == u"CuneytOzdemir":
            target_arr.append(3)
        else:
            target_arr.append(4)

    pickled_file = open(file_path_data, "wb")
    pickle.dump(data_arr, pickled_file)
    pickled_file.close()

    pickled_file = open(file_path_target, "wb")
    pickle.dump(target_arr, pickled_file)
    pickled_file.close()

    return render_to_response('trainer/index.html', c)


def build_testdata(request):
    c = {}
    c.update(csrf(request))

    TestYazar.objects.all().delete()

    module_dir = os.path.dirname(__file__)  # get current directory
    os.chdir(module_dir)

    yazar_arr = [
        "AyseArman", "AhmetHakan", "YilmazOzdil",
        "MehmetAliBirand", "MehmetBaransu", "TahaAkyol",
        "MehmetBarlas", "NazliIlicak", "CuneytOzdemir",
        "AhmetAltan", "HincalUluc", "NihalBengisuKaraca",
        "PerihanMagden", "RuhatMengi", "YaseminCongar",
        "BekirCoskun", "CengizCandar", "EnginArdic",
        "MutluTonbekici", "SuleymanOzisik"
    ]

    for yazar in yazar_arr:
        file_path = os.path.join(module_dir, 'TestYazarlar/' + yazar)
        print "[DEBUG] " + str(file_path)

        for file in os.listdir(file_path):
            avgs = parse_one_entry(
                entry_builder(file, yazar, structure="test"))

            y = TestYazar(yazar_adi=yazar,
                          # exclamation=avgs["exclamation"],
                          exclamation_n=avgs["exclamation_n"],
                          exclamation_r=avgs["exclamation_r"],
                          # question_mark=avgs["question_mark"],
                          question_mark_n=avgs["question_mark_n"],
                          question_mark_r=avgs["question_mark_r"],
                          # coma_count=avgs["coma"],
                          coma_count_n=avgs["coma_n"],
                          coma_count_r=avgs["coma_r"],
                          # yan_cizgi=avgs["yan_cizgi"],
                          yan_cizgi_n=avgs["yan_cizgi_n"],
                          yan_cizgi_r=avgs["yan_cizgi_r"],
                          quote_n=avgs["quote_n"],
                          quote_r=avgs["quote_r"],
                          single_quote_n=avgs["single_quote_n"],
                          single_quote_r=avgs["single_quote_r"],
                          double_dot_n=avgs["double_dot_n"],
                          double_dot_r=avgs["double_dot_r"],
                          triple_dot_n=avgs["triple_dot_n"],
                          triple_dot_r=avgs["triple_dot_r"],
                          stopwords_n=avgs["stopwords_n"],
                          stopwords_r=avgs["stopwords_r"],
                          # stars_n=avgs["stars_n"],
                          # stars_r=avgs["stars_r"],
                          sentence_len=avgs["sentence_len"],
                          paragraph_len=avgs["paragraph_len"])
            y.save()

    return render_to_response('trainer/index.html', c)


def predict(request):
    """

    Arguments:
    - `request`:
    """
    c = {}
    c.update(csrf(request))

    return render_to_response('trainer/predict.html', c)


def result(request):
    c = {}
    c.update(csrf(request))

    p = request.POST
    entry = p['yazi1_name']
    entry = entry_cleaner(entry)

    entry_features = parse_one_entry(entry_builder(from_web=entry))

    objects_all = Yazar.objects.all()
    objects_15_authors = Yazar.objects.filter(
        Q(yazar_adi="AhmetAltan") |
        Q(yazar_adi="AhmetHakan") |
        Q(yazar_adi="AyseArman") |
        Q(yazar_adi="BekirCoskun") |
        Q(yazar_adi="CengizCandar") |
        Q(yazar_adi="CuneytOzdemir") |
        Q(yazar_adi="EnginArdic") |
        Q(yazar_adi="HincalUluc") |
        Q(yazar_adi="MehmetAliBirand") |
        Q(yazar_adi="MehmetBaransu") |
        Q(yazar_adi="MehmetBarlas") |
        Q(yazar_adi="MutluTonbekici") |
        Q(yazar_adi="NazliIlicak") |
        Q(yazar_adi="NihalBengisuKaraca") |
        Q(yazar_adi="YilmazOzdil")
    )
    objects_10_authors = Yazar.objects.filter(
        Q(yazar_adi="AhmetAltan") |
        Q(yazar_adi="AhmetHakan") |
        Q(yazar_adi="AyseArman") |
        Q(yazar_adi="BekirCoskun") |
        Q(yazar_adi="CengizCandar") |
        Q(yazar_adi="CuneytOzdemir") |
        Q(yazar_adi="EnginArdic") |
        Q(yazar_adi="HincalUluc") |
        Q(yazar_adi="MehmetAliBirand") |
        Q(yazar_adi="YilmazOzdil")
    )
    objects_5_authors = Yazar.objects.filter(
        Q(yazar_adi="AhmetAltan") |
        Q(yazar_adi="AhmetHakan") |
        Q(yazar_adi="AyseArman") |
        Q(yazar_adi="BekirCoskun") |
        Q(yazar_adi="YilmazOzdil")
    )

    test_objects_all = TestYazar.objects.all()
    test_objects_15_authors = TestYazar.objects.filter(
        Q(yazar_adi="AhmetAltan") |
        Q(yazar_adi="AhmetHakan") |
        Q(yazar_adi="AyseArman") |
        Q(yazar_adi="BekirCoskun") |
        Q(yazar_adi="CengizCandar") |
        Q(yazar_adi="CuneytOzdemir") |
        Q(yazar_adi="EnginArdic") |
        Q(yazar_adi="HincalUluc") |
        Q(yazar_adi="MehmetAliBirand") |
        Q(yazar_adi="MehmetBaransu") |
        Q(yazar_adi="MehmetBarlas") |
        Q(yazar_adi="MutluTonbekici") |
        Q(yazar_adi="NazliIlicak") |
        Q(yazar_adi="NihalBengisuKaraca") |
        Q(yazar_adi="YilmazOzdil")
    )
    test_objects_10_authors = TestYazar.objects.filter(
        Q(yazar_adi="AhmetAltan") |
        Q(yazar_adi="AhmetHakan") |
        Q(yazar_adi="AyseArman") |
        Q(yazar_adi="BekirCoskun") |
        Q(yazar_adi="CengizCandar") |
        Q(yazar_adi="CuneytOzdemir") |
        Q(yazar_adi="EnginArdic") |
        Q(yazar_adi="HincalUluc") |
        Q(yazar_adi="MehmetAliBirand") |
        Q(yazar_adi="YilmazOzdil")
    )
    test_objects_5_authors = TestYazar.objects.filter(
        Q(yazar_adi="AhmetAltan") |
        Q(yazar_adi="AhmetHakan") |
        Q(yazar_adi="AyseArman") |
        Q(yazar_adi="BekirCoskun") |
        Q(yazar_adi="YilmazOzdil")
    )

    # order is important here
    entry_features_arr = [
        # entry_features['exclamation'],
        entry_features['exclamation_n'],
        entry_features['exclamation_r'],
        # entry_features['question_mark'],
        entry_features['question_mark_n'],
        entry_features['question_mark_r'],
        # entry_features['coma'],
        entry_features['coma_n'],
        entry_features['coma_r'],
        # entry_features['yan_cizgi'],
        entry_features['yan_cizgi_n'],
        entry_features['yan_cizgi_r'],
        entry_features['quote_n'],
        entry_features['quote_r'],
        entry_features['single_quote_n'],
        entry_features['single_quote_r'],
        entry_features["double_dot_n"],
        entry_features["double_dot_r"],
        entry_features["triple_dot_n"],
        entry_features["triple_dot_r"],
        entry_features["stopwords_n"],
        entry_features["stopwords_r"],
        # entry_features['stars_n'],
        # entry_features['stars_r'],
        entry_features['sentence_len'],
        entry_features['paragraph_len']
    ]

    scores_dict = {}
    # --------------------------------------------------------------- #
    print "################################################"
    y_features, y_classes = build_features(objects_5_authors)
    y_test_features, y_test_classes = build_features(test_objects_5_authors)
    print "[DEBUG] Length of Yazar-Classes (5 authors): " + \
        str(len(y_classes))
    print "[DEBUG] Length of Yazar-Test-Classes (5 authors): " + \
        str(len(y_test_classes))

    scores = get_score(y_features, y_classes,
                       y_test_features, y_test_classes)
    print "[DEBUG] Algorithm Scores with 5 authors"
    print scores
    # --------------------------------------------------------------- #
    print "------------------------------------------------"
    y_features, y_classes = build_features(objects_10_authors)
    y_test_features, y_test_classes = build_features(test_objects_10_authors)
    print "[DEBUG] Length of Yazar-Classes (10 authors): " + \
        str(len(y_classes))
    print "[DEBUG] Length of Yazar-Test-Classes (10 authors): " + \
        str(len(y_test_classes))

    scores = get_score(y_features, y_classes,
                       y_test_features, y_test_classes)
    print "[DEBUG] Algorithm Scores with 10 authors"
    print scores
    # --------------------------------------------------------------- #
    print "------------------------------------------------"
    y_features, y_classes = build_features(objects_15_authors)
    y_test_features, y_test_classes = build_features(test_objects_15_authors)
    print "[DEBUG] Len of y_classes (15 authors): " + \
        str(len(y_classes))
    print "[DEBUG] Len of y_test_classes (15 authors): " + \
        str(len(y_test_classes))

    scores = get_score(y_features, y_classes,
                       y_test_features, y_test_classes)
    print "[DEBUG] Algorithm Scores with 15 authors"
    print scores
    # --------------------------------------------------------------- #
    print "------------------------------------------------"
    y_features, y_classes = build_features(objects_all)
    y_test_features, y_test_classes = build_features(test_objects_all)
    print "[DEBUG] Length of Yazar-Classes (20 authors): " + \
        str(len(y_classes))
    print "[DEBUG] Length of Yazar-Test-Classes (20 authors): " + \
        str(len(y_test_classes))
    scores = get_score(y_features, y_classes,
                       y_test_features, y_test_classes)
    print "[DEBUG] Algorithm Scores with 20 authors"
    print scores
    print "################################################"

    print "[DEBUG] Features Array Of Web-Entry"
    print entry_features_arr

    results = predict_author(entry_features_arr, y_features, y_classes)
    results_dict = {}
    results_dict['knn'] = results[0]
    results_dict['svc'] = results[1]
    results_dict['logistic'] = results[2]
    results_dict['gnb'] = results[3]
    results_dict['dtc'] = results[4]
    results_dict['gbc'] = results[5]

    results_with_grams = (([results[0]] * 1) + ([results[1]] * 3) +
                          ([results[2]] * 4) + ([results[3]] * 3) +
                          ([results[4]] * 1) + ([results[5]] * 4))

    results_dict['total'] = max(set(results_with_grams),
                                key=results_with_grams.count)
    c.update(results_dict)

    # scores = get_score(test_objects_10_authors)
    # scores_dict['knn_score'] = (scores[0] * 100)
    # scores_dict['svc_score'] = (scores[1] * 100)
    # scores_dict['logistic_score'] = (scores[2] * 100)
    # scores_dict['gnb_score'] = (scores[3] * 100)
    # scores_dict['dtc_score'] = (scores[4] * 100)
    # scores_dict['gbc_score'] = (scores[5] * 100)

    # scores_5 = get_score(test_objects_5_authors)
    # scores_dict['knn_score_5'] = (scores_5[0] * 100)
    # scores_dict['svc_score_5'] = (scores_5[1] * 100)
    # scores_dict['logistic_score_5'] = (scores_5[2] * 100)
    # scores_dict['gnb_score_5'] = (scores_5[3] * 100)
    # scores_dict['dtc_score_5'] = (scores_5[4] * 100)
    # scores_dict['gbc_score_5'] = (scores_5[5] * 100)
    c.update(scores_dict)

    return render_to_response('trainer/predict-results.html', c)
