from django.shortcuts import render
from . import sentimentAnalysis
from sentiment.forms import *
from . import models
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




def showTweets(request):
    positiveList=list(models.positiveTweets.objects.all())
    negativeList=list(models.negativeTweets.objects.all())
    context={'positive':positiveList,'negative':negativeList}
    return render(request,'sentiment/displayTweets.html',context)

