from django.shortcuts import render

# Create your views here.
from article.models import Article
from django.shortcuts import redirect


def list_article(request):
    articles = Article.objects.all()
    data = {
        'articles': articles
    }
    return render(request, 'list.html', data)


def detail_article(request, pk):
    article = Article.objects.get(pk=pk)
    data = {
        'article1': article
    }
    return render(request, 'detail.html', data)


def create_article(request):
	if request.method == 'POST':
		title = request.POST.get('title', None)
		content = request.POST['content']
		article = Article.objects.create(
					title=title,
					content=content
				)
		return redirect('/')
	return render(request, 'create.html')

