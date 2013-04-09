#!/usr/bin/python
# -*- coding: utf-8 -*-
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import GradientBoostingClassifier

from sklearn import svm, linear_model, tree


def build_features(objects, structure="train"):

    yazar_features = []             # for train data
    yazar_classes = []              # for train classes

    for yazar in objects:
        single_yazar_features = []
        # single_yazar_features.append(yazar.exclamation)
        single_yazar_features.append(yazar.exclamation_n)
        single_yazar_features.append(yazar.exclamation_r)

        # single_yazar_features.append(yazar.question_mark)
        single_yazar_features.append(yazar.question_mark_n)
        single_yazar_features.append(yazar.question_mark_r)

        # single_yazar_features.append(yazar.coma_count)
        single_yazar_features.append(yazar.coma_count_n)
        single_yazar_features.append(yazar.coma_count_r)

        # single_yazar_features.append(yazar.yan_cizgi)
        single_yazar_features.append(yazar.yan_cizgi_n)
        single_yazar_features.append(yazar.yan_cizgi_r)

        single_yazar_features.append(yazar.quote_n)
        single_yazar_features.append(yazar.quote_r)
        single_yazar_features.append(yazar.single_quote_n)
        single_yazar_features.append(yazar.single_quote_r)

        single_yazar_features.append(yazar.double_dot_n)
        single_yazar_features.append(yazar.double_dot_r)
        single_yazar_features.append(yazar.triple_dot_n)
        single_yazar_features.append(yazar.triple_dot_r)
        single_yazar_features.append(yazar.stopwords_n)
        single_yazar_features.append(yazar.stopwords_r)

        # single_yazar_features.append(yazar.stars_n)
        # single_yazar_features.append(yazar.stars_r)
        single_yazar_features.append(yazar.sentence_len)
        single_yazar_features.append(yazar.paragraph_len)

        # if structure is "test":
        #     test_yazar_features.append(single_yazar_features)
        #     test_yazar_classes.append(yazar.yazar_adi)
        # else:
        #     yazar_features.append(single_yazar_features)
        #     yazar_classes.append(yazar.yazar_adi)
        yazar_features.append(single_yazar_features)
        yazar_classes.append(yazar.yazar_adi)

    return yazar_features, yazar_classes
    # print yazar_features
    # print yazar_classes


def get_score(yazar_features, yazar_classes,
              test_yazar_features, test_yazar_classes):
    """

    Arguments:
    - `arr`:
    """
    # print "get score'a geldik"

    scores = []

    # print "Test Data Count"
    # print "Yazar Classes (len): " + str(len(yazar_classes))
    # print "Test Yazar Classes (len): " + str(len(test_yazar_classes))

    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(yazar_features, yazar_classes)
    scores.append(knn.score(test_yazar_features, test_yazar_classes))

    svc = svm.SVC(kernel='linear', degree=3)
    svc.fit(yazar_features, yazar_classes)
    scores.append(svc.score(test_yazar_features, test_yazar_classes))

    regr = linear_model.LogisticRegression()
    regr.fit(yazar_features, yazar_classes)
    scores.append(regr.score(test_yazar_features, test_yazar_classes))

    gnb = GaussianNB()
    gnb.fit(yazar_features, yazar_classes)
    scores.append(gnb.score(test_yazar_features, test_yazar_classes))

    dtc = tree.DecisionTreeClassifier()
    dtc.fit(yazar_features, yazar_classes)
    scores.append(dtc.score(test_yazar_features, test_yazar_classes))

    gbc = GradientBoostingClassifier()
    gbc.fit(yazar_features, yazar_classes)
    scores.append(gbc.score(test_yazar_features, test_yazar_classes))

    # print "scores"
    # print scores

    return scores


def predict_author(arr, yazar_features, yazar_classes):
    results = []

    print "\n[DEBUG] K-NN result (neighbors: 10)"
    knn = KNeighborsClassifier(n_neighbors=10)
    knn.fit(yazar_features, yazar_classes)
    print knn.predict(arr)
    results.append(knn.predict(arr)[0])

    print "\n[DEBUG] SVC result (linear) (degree=3)"
    svc = svm.SVC(kernel='linear', degree=3)
    svc.fit(yazar_features, yazar_classes)
    print svc.predict(arr)
    results.append(svc.predict(arr)[0])

    print "\n[DEBUG] Logistic Regression result ()"
    regr = linear_model.LogisticRegression()
    regr.fit(yazar_features, yazar_classes)
    print regr.predict(arr)
    results.append(regr.predict(arr)[0])

    print "\n[DEBUG] Gaussian Naive Bayes"
    gnb = GaussianNB()
    gnb.fit(yazar_features, yazar_classes)
    print gnb.predict(arr)
    results.append(gnb.predict(arr)[0])

    print "\n[DEBUG] Decision Tree Classifier"
    dtc = tree.DecisionTreeClassifier()
    dtc.fit(yazar_features, yazar_classes)
    print dtc.predict(arr)
    results.append(dtc.predict(arr)[0])

    print "\n[DEBUG] Gradient Boosting Classification"
    gbc = GradientBoostingClassifier()
    gbc.fit(yazar_features, yazar_classes)
    print gbc.predict(arr)
    results.append(gbc.predict(arr)[0])

    # output = open('features.pkl', 'wb')
    # pickle.dump(yazar_features, output)
    # output.close()

    # output = open('classes.pkl', 'wb')
    # pickle.dump(yazar_classes, output)
    # output.close()

    # test_yazar_features = []        # for test data
    # test_yazar_classes = []         # for test classes
    # # yazar_features = []             # for train data
    # # yazar_classes = []              # for train classes

    return results
