from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from output.i2t import img2text
from output.p2t import main
def output(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        result = ''
        if '.pdf' in uploaded_file_url:
            result = main.extract(uploaded_file_url)
        else:
            result = img2text.detect_text(uploaded_file_url)
        #return HttpResponse(result)
        return render(request,'output.html',{'result':result})
