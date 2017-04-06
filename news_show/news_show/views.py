#coding:utf-8
from models import NewsList
from models import NewsInfo
from django.shortcuts import render_to_response
from django.core.paginator import Paginator

def index(request):
	server_pages = NewsList.objects.all()
	p = Paginator(server_pages,20)
	try:
            page = int(request.GET.get('page','1'))
        except ValueError:
            page = 1
        try:
            server_pages = p.page(page)
        except (EmptyPage,InvalidPage):
            server_pages = p.page(p.num_pages)
        return render_to_response('news show.html',{'server_pages':server_pages})
#	return render_to_response('news show.html',{'news':news})

def info(request,s):
	n=int(s)
	Info_pages = NewsInfo.objects.get(num=n)
	url= NewsList.objects.get(num=n)
	return render_to_response('news Info.html',{'Info_pages':Info_pages,'url':url.url})

