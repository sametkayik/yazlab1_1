from django.shortcuts import render
from .models import Notebook
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import psycopg2
from django.db.models import Q

def getConnection():
    conn = psycopg2.connect(
        host="localhost",
        database="notebookdb",
        user="postgres",
        password="s"
    )
    return conn
# Create your views here.

def index(request):
    obj = Notebook.objects.all()
    #obj = Notebook.objects.raw('SELECT 1 as id, p2.model_name, p2.price, p2.site, c2.model_name, c2.price, c2.site  FROM teknosa AS p2  LEFT JOIN n11 AS c2  ON p2.model_name = c2.model_name  WHERE c2.model_name IS NOT NULL ')
    #obj = Notebook.objects.raw('SELECT * FROM notebookapi_notebook WHERE model_name IN (SELECT model_name FROM notebookapi_notebook GROUP BY model_name HAVING COUNT(*) > 1)')
    print(obj)
    marka = obj.distinct('marka')
    islemci = obj.distinct('cpu_type')
    ram = obj.distinct('memory_capacity')
    ekran = obj.distinct('screen_size')
    isletim = obj.distinct('dos')
    disk_tipi = obj.distinct('disc_type')
    disk = obj.distinct('disc_capacity')
    query = request.GET.getlist('q')
    if query:
        obj = obj.filter(
            Q(marka__in=query) |
            Q(title__in=query) |
            Q(cpu_type__in=query) |
            Q(memory_capacity__in=query) |
            Q(screen_size__in=query) |
            Q(dos__in=query) |
            Q(disc_capacity__in=query) |
            Q(disc_type__in=query)
            )

    paginator = Paginator(obj, 10)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    
    context = {
        'posts': posts,
        'obj': obj,
        'marka': marka,
        'len': len(obj),
        'islemci': islemci,
        'ram': ram,
        'ekran': ekran,
        'isletim' : isletim,
        'disk' : disk,
        'disk_tipi' : disk_tipi,
    }

    return render(request, "index.html", context)


def pagination(obj, request):
    paginator = Paginator(obj, 5)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return posts



