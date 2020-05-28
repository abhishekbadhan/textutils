from django.http import HttpResponse
from django.shortcuts import render


def front(request):
    return render(request, 'form.html')


def result(request):
    tx = request.POST.get('textofarea', 'NO INPUT')
    
    check = request.POST.get('box', 'off')
    
    
    up = request.POST.get('upperbox', 'off')
    
    es = request.POST.get('extraspace', 'off')

    if check == 'on':
        rs = True
        punct = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        st1 = ""
        for i in tx:
            if i not in punct:
                st1 += i
            else:
                st1 += ' '
        tx = st1
    
    if up == 'on':
        rs = True
        st2 = ''
        for index, i in enumerate(tx):
            st2 += tx[index].upper()
        tx = st2

    
    if es == 'on':
        rs = True
        st3 = ''
        for index, i in enumerate(tx):
            if not (tx[index] == ' ' and tx[index+1] == ' '):
                st3 += i 
        tx = st3
    
    if check == 'off' and up == 'off' and es == 'off':
        rs = False
        return HttpResponse('ERROR')

    if rs:
        dict = {'txt': tx}
        return render(request, 'formresult.html', dict)
