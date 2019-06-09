from django.http import HttpResponse
from django.shortcuts import render
import operator

def home_page(request):
    return render(request, "home.html")

def count(request):

    fullText = request.GET["fulltext"]
    wordList = fullText.split()
    wordDictionary = {}

    for word in wordList:
        if word in wordDictionary:
            # This is awsome
            wordDictionary[word] += 1
        else:
            # Add to the dictionary
            wordDictionary[word] = 1

    sortedWords = sorted(wordDictionary.items(), key = operator.itemgetter(1), reverse = True)

    return render(request, "count.html", {"fullText": fullText, "words": len(wordList), "sortedWords": sortedWords})

def about_page(request):
    return render(request, "about.html")
