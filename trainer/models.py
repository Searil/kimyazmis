from django.db import models


# Create your models here.
class Yazar(models.Model):
    yazar_adi = models.CharField(max_length=100)
    # exclamation = models.FloatField()
    exclamation_n = models.FloatField()
    exclamation_r = models.FloatField()
    # question_mark = models.FloatField()
    question_mark_n = models.FloatField()
    question_mark_r = models.FloatField()
    # coma_count = models.FloatField()
    coma_count_n = models.FloatField()
    coma_count_r = models.FloatField()
    # yan_cizgi = models.FloatField()
    yan_cizgi_n = models.FloatField()
    yan_cizgi_r = models.FloatField()
    quote_n = models.FloatField()
    quote_r = models.FloatField()
    single_quote_n = models.FloatField()
    single_quote_r = models.FloatField()
    double_dot_n = models.FloatField()
    double_dot_r = models.FloatField()
    triple_dot_n = models.FloatField()
    triple_dot_r = models.FloatField()
    stopwords_n = models.FloatField()
    stopwords_r = models.FloatField()
    # stars_n = models.FloatField()
    # stars_r = models.FloatField()
    sentence_len = models.FloatField()
    paragraph_len = models.FloatField()

    def __unicode__(self):
        return self.yazar_adi


class TestYazar(models.Model):
    yazar_adi = models.CharField(max_length=100)
    # exclamation = models.FloatField()
    exclamation_n = models.FloatField()
    exclamation_r = models.FloatField()
    # question_mark = models.FloatField()
    question_mark_n = models.FloatField()
    question_mark_r = models.FloatField()
    # coma_count = models.FloatField()
    coma_count_n = models.FloatField()
    coma_count_r = models.FloatField()
    # yan_cizgi = models.FloatField()
    yan_cizgi_n = models.FloatField()
    yan_cizgi_r = models.FloatField()
    quote_n = models.FloatField()
    quote_r = models.FloatField()
    single_quote_n = models.FloatField()
    single_quote_r = models.FloatField()
    double_dot_n = models.FloatField()
    double_dot_r = models.FloatField()
    triple_dot_n = models.FloatField()
    triple_dot_r = models.FloatField()
    # stars_n = models.FloatField()
    # stars_r = models.FloatField()
    stopwords_n = models.FloatField()
    stopwords_r = models.FloatField()
    sentence_len = models.FloatField()
    paragraph_len = models.FloatField()

    def __unicode__(self):
        return self.yazar_adi
