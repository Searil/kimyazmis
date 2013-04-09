#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import os
import codecs


def entry_cleaner(entry):
    """
    Clear entry from noise values

    web'den okurken bunla oku, dosyadan okurken alttaki cleaner'la

    Arguments:
    - `entry`:
    """

    entry = re.sub(r"(\r\n|\n){1,10}", "\n", entry)
    entry = re.sub(u"“|”", "\"", entry, re.UNICODE)
    entry = re.sub(u"‘|’", "\'", entry, re.UNICODE)

    return entry


def cleaner(a_line):
    """
    Replaces “” to "
    Replaces ‘’ to '

    Arguments:
    - `a_line`: A line of a text
    """

    return re.sub(r"‘|’", "\'", re.sub(r"“|”", "\"", a_line))


def entry_builder(filename="", author="", from_web="", structure="train"):
    """
    gets a filename and returns a full
    cleaned entry as one string

    Arguments:
    - `filename`: Filename of the entry
    - `author`: Author of the entry
    """

    if structure is "test":
        structure = "TestYazarlar/"
    else:
        structure = "Yazarlar/"

    entry = ""
    if from_web is "":
        module_dir = os.path.dirname(__file__)  # get current directory
        file_path = os.path.join(module_dir, structure +
                                 author + '/' + filename)

        file = codecs.open(file_path, "r", "utf-8")
        lines = file.readlines()
        file.close()
    else:
        lines = from_web

    for l in lines:
        entry += "%s" % entry_cleaner(l)

    entry = re.sub(r"(\r\n|\n){2,10}", "\n", entry)
    return entry.split("\n")


def paragraph_normalizer(entry):
    """
    yapıları analiz ederken paragraf sayısına göre normalize etmek daha
    mantıklı.

    örneğin yazı 0-10 paragraf arasıysa
    kullanılan ?, -, ! karakterleri 1'e

    10-20 arasıysa aynı işaretler 2'ye
    20-30 arasıysa aynı işaretler 3'e
    .
    .
    .
    .
    (n-10) - n arasıysa aynı işaretler n/10'a

    bölünmeli.

    neden: bazı yazarların 5 paragraflık yazıları da var, 60 paragraflık
    yazıları da var.

    60 paragraflık yazıda kullanılan ? ile 10 paragraflık yazıda
    kullanılan soru işaretlerini kıyaslamak mantıksız.
    """

    normalizer = 1
    paragraph_count = len(entry)

    if paragraph_count <= 10:
        normalizer = 1
    elif paragraph_count > 10 and paragraph_count <= 20:
        normalizer = 2
    elif paragraph_count > 20 and paragraph_count <= 30:
        normalizer = 3
    elif paragraph_count > 30 and paragraph_count <= 40:
        normalizer = 4
    elif paragraph_count > 40 and paragraph_count <= 50:
        normalizer = 5
    else:
        normalizer = 6

    return normalizer


def count_stopwords(line):
    counter = 0
    word_list = [
        u"acaba", u"altı", u"ama", u"ancak", u"artık",
        u"asla", u"aslında", u"az", u"bana", u"bazen",
        u"bazı", u"bazıları", u"bazısı", u"belki",
        u"ben", u"beni", u"benim", u"beş", u"bile",
        u"bir", u"birçoğu", u"birçok", u"birçokları",
        u"biri", u"birisi", u"birkaç", u"birkaçı",
        u"birşey", u"birşeyi", u"biz", u"bize", u"bizi",
        u"bizim", u"böyle", u"böylece", u"bu", u"buna",
        u"bunda", u"bundan", u"bunu", u"bunun", u"burada",
        u"bütün", u"çoğu", u"çoğuna", u"çoğunu", u"çok",
        u"çünkü", u"da", u"daha", u"de", u"değil",
        u"demek", u"diğer", u"diğeri", u"diğerleri", u"diye",
        u"dokuz", u"dolayı", u"dört", u"elbette", u"en",
        u"fakat", u"falan", u"felan", u"filan", u"gene",
        u"gibi", u"hâlâ", u"hangi", u"hangisi", u"hani",
        u"hatta", u"hem", u"henüz", u"hep", u"hepsi",
        u"hepsine", u"hepsini", u"her", u"her biuri", u"herkes",
        u"herkese", u"herkesi", u"hiç", u"hiç kiumse", u"hiçbiri",
        u"hiçbirine", u"hiçbirini", u"için", u"içinde", u"iki",
        u"ile", u"ise", u"işte", u"kaç", u"kadar",
        u"kendi", u"kendine", u"kendini", u"ki", u"kim",
        u"kime", u"kimi", u"kimin", u"kimisi", u"madem",
        u"mı", u"mı", u"mi", u"mu", u"mu",
        u"mü", u"mü", u"nasıl", u"ne", u"ne kadar",
        u"ne zauman", u"neden", u"nedir", u"nerde", u"nerede",
        u"nereden", u"nereye", u"nesi", u"neyse", u"niçin",
        u"niye", u"on", u"ona", u"ondan", u"onlar",
        u"onlara", u"onlardan", u"onların", u"onların", u"onu",
        u"onun", u"orada", u"oysa", u"oysaki", u"öbürü",
        u"ön", u"önce", u"ötürü", u"öyle", u"rağmen",
        u"sana", u"sekiz", u"sen", u"senden", u"seni",
        u"senin", u"siz", u"sizden", u"size", u"sizi",
        u"sizin", u"son", u"sonra", u"şayet", u"şey",
        u"şeyden", u"şeye", u"şeyi", u"şeyler", u"şimdi",
        u"şöyle", u"şu", u"şuna", u"şunda", u"şundan",
        u"şunlar", u"şunu", u"şunun", u"tabi", u"tamam",
        u"tüm", u"tümü", u"üç", u"üzere", u"var",
        u"ve", u"veya", u"veyahut", u"ya", u"ya da",
        u"yani", u"yedi", u"yerine", u"yine", u"yoksa",
        u"zaten", u"zira"]

    arr = line.split(" ")

    # token unicode test ettim
    for token in arr:

        if token in word_list:
            counter += 1

    return counter


def parse_one_entry(entry_arr):
    """

    Arguments:
    - `entry`: The entry array of the author
    splitted with paragraphs
    """

    normalizer = paragraph_normalizer(entry_arr)
    normalizer = float(normalizer)

    # total_length is used to calculate paragraph length
    total_length = 0

    # counters
    exclamation = 0
    question_mark = 0
    coma = 0
    yan_cizgi = 0
    quote = 0
    single_quote = 0
    sentence_count = 0
    stars = 0
    double_dot = 0
    triple_dot = 0
    stopwords = 0

    for line in entry_arr:
        # stripped.append(line.strip())
        total_length += len(line)
        exclamation += line.count('!')
        question_mark += line.count('?')
        coma += line.count(',')
        yan_cizgi += line.count('-')
        quote += line.count('"')
        single_quote += line.count("'")
        stars += line.count("*")
        double_dot += (line.count("..") - line.count("..."))
        triple_dot += line.count("...")
        stopwords += count_stopwords(line)
        sentence_count += len(line.split('.'))

    # print total_length / float(sentence_count)
    parsed = {}
    # parsed['exclamation'] = exclamation
    parsed['exclamation_n'] = exclamation / normalizer
    parsed['exclamation_r'] = exclamation / float(total_length)
    # parsed['question_mark'] = question_mark
    parsed['question_mark_n'] = question_mark / normalizer
    parsed['question_mark_r'] = question_mark / float(total_length)
    # parsed['coma'] = coma
    parsed['coma_n'] = coma / normalizer
    parsed['coma_r'] = coma / float(total_length)
    # parsed['yan_cizgi'] = yan_cizgi
    parsed['yan_cizgi_n'] = yan_cizgi / normalizer
    parsed['yan_cizgi_r'] = yan_cizgi / float(total_length)

    parsed['quote_n'] = quote / normalizer
    parsed['quote_r'] = quote / float(total_length)
    parsed['single_quote_n'] = single_quote / normalizer
    parsed['single_quote_r'] = single_quote / float(total_length)

    parsed['double_dot_n'] = double_dot / normalizer
    parsed['double_dot_r'] = double_dot / float(total_length)
    parsed['triple_dot_n'] = triple_dot / normalizer
    parsed['triple_dot_r'] = triple_dot / float(total_length)

    parsed['stopwords_n'] = stopwords / normalizer
    parsed['stopwords_r'] = stopwords / float(total_length)
    # parsed['stars_n'] = stars / normalizer
    # parsed['stars_r'] = stars / float(total_length)

    parsed['sentence_len'] = float(total_length) / sentence_count
    parsed['paragraph_len'] = float(total_length) / len(entry_arr)
    return parsed
