from django.shortcuts import render
from . import sentimentAnalysis
from sentiment.forms import *
def getSearchTerm(request):
    if request.method=='POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            f=form.save()
            searchTerm=f.term
            number=f.number
            analysisObj=sentimentAnalysis.Analysis()
            args=analysisObj.DownloadData(searchTerm,number)
            return render(request,"sentiment/displayChart.html",context=args)
        else:
            args = {'form': form}
            return render(request, 'sentiment/searchForm.html', args)
    else:
        form = SearchForm()
        args = {'form': form}
        return render(request, 'sentiment/searchForm.html', args)





