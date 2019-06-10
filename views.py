from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def count(request):
    full_text = request.GET['fulltext']
    word_list = full_text.split()
    word_dictionary = {}
    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1
    #fulltext에서 나온 변수를 저장하는 것이 full_text
    return render(request,'count.html',{'fulltext':full_text, 'total': len(word_list),'dictionary': word_dictionary.items()})
# Create your views here.
