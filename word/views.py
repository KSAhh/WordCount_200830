from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def count(request):
    text = request.GET['fulltext']
    text_split = text.split(' ')

    word_dic = {}                   # 비어있는 word dictionary 생성
    for word in text_split:
        if word in word_dic.keys(): # word가 word_dic.keys()값에 있으면
            word_dic[word] += 1     # 단어 개수에 하나 추가
        else:
            word_dic[word] =1       # keys값에 없으면 word_dic[]에 1을 넣음. 즉 생성


    return render(request, 'count.html', {
        'length':len(text_split),
        'full' : text_split,
        'text' : text,
        'dic' : word_dic.items(),
        })