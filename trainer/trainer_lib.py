#!/usr/bin/python
# -*- coding: utf-8 -*-

import re


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


def parse_one_entry(entry):
    """

    Arguments:
    - `entry`: The entry array of the author
    splitted with paragraphs
    """

    normalizer = paragraph_normalizer(entry)
    normalizer = float(normalizer)

    # total_length is used to calculate paragraph length
    total_length = 0

    # counters
    exclamation = 0
    question_mark = 0
    coma = 0
    yan_cizgi = 0

    for line in entry:
        # stripped.append(line.strip())
        total_length += len(line)
        exclamation += line.count('!')
        question_mark += line.count('?')
        coma += line.count(',')
        yan_cizgi += line.count('-')

    parsed = {}
    parsed['exclamation_count'] = exclamation
    parsed['exclamation_count_n'] = exclamation / normalizer
    parsed['question_mark_count'] = question_mark
    parsed['question_mark_count_n'] = question_mark / normalizer
    parsed['coma_count'] = coma
    parsed['coma_count_n'] = coma / normalizer
    parsed['yan_cizgi_count'] = yan_cizgi
    parsed['yan_cizgi_count_n'] = yan_cizgi / normalizer
    parsed['paragraph_len'] = float(total_length) / len(entry)
    return parsed


def parse(yazar_adi, yazilar):
    sonuclar = []
    for yazi in yazilar:
        yeni_yazi = re.sub(r"(\r\n){2,10}", "\r\n", yazi)
        sonuclar.append(parse_one_entry(yeni_yazi.split("\r\n")))

    avg_exclamation = 0
    avg_exclamation_n = 0
    avg_question_mark = 0
    avg_question_mark_n = 0
    avg_coma = 0
    avg_coma_n = 0
    avg_yan_cizgi = 0
    avg_yan_cizgi_n = 0
    avg_paragraph_len = 0

    for sonuc in sonuclar:
        avg_exclamation += sonuc['exclamation_count']
        avg_exclamation_n += sonuc['exclamation_count_n']
        avg_question_mark += sonuc['question_mark_count']
        avg_question_mark_n += sonuc['question_mark_count_n']
        avg_coma += sonuc['coma_count']
        avg_coma_n += sonuc['coma_count_n']
        avg_yan_cizgi += sonuc['yan_cizgi_count']
        avg_yan_cizgi_n += sonuc['yan_cizgi_count_n']
        avg_paragraph_len += sonuc['paragraph_len']

    l = float(len(sonuclar))
    avg_exclamation /= l
    avg_exclamation_n /= l
    avg_question_mark /= l
    avg_question_mark_n /= l
    avg_coma /= l
    avg_coma_n /= l
    avg_yan_cizgi /= l
    avg_yan_cizgi_n /= l
    avg_paragraph_len /= l

    avgs = {}
    avgs["exclamation"] = avg_exclamation
    avgs["exclamation_n"] = avg_exclamation_n
    avgs["question_mark"] = avg_question_mark
    avgs["question_mark_n"] = avg_question_mark_n
    avgs["coma"] = avg_coma
    avgs["coma_n"] = avg_coma_n
    avgs["yan_cizgi"] = avg_yan_cizgi
    avgs["yan_cizgi_n"] = avg_yan_cizgi_n
    avgs["paragraph_len"] = avg_paragraph_len

    return avgs
