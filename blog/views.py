from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Currency
from .forms import PostForm
from django.utils import timezone
from django.shortcuts import redirect
from blog.mod import anyparsing
from .count import *
from datetime import timedelta, datetime

aa = ''
bb = ''
summ5 = 0
summ6 = 0

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(archive__in=[False])
    today = datetime.now()
    delta = timedelta(30)
    date = today - delta
    if date > today:
        a = 'Оплачено'
    else:
        a = 'Выставить счет'
    return render(request, 'blog/post_list.html', {'posts': posts, 'count': count, 'a': a})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    active = True
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form, 'active': active})

def post_edit(request, pk):
    active = True
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def post_archive(request):
    posts = Post.objects.filter(archive__in=[True])
    return render(request, 'blog/post_archive.html', {'posts': posts})

def post_in_archive(request, pk):
    post = Post.objects.get(pk=pk)
    post.archive = True
    post.save()
    return redirect('post_list')

def post_un_archive(request, pk):
    post = Post.objects.get(pk=pk)
    post.archive = False
    post.save()
    return redirect('post_list')

def post_delete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('post_list')

def start(request):
    anyparsing.parsing()
    return redirect('post_list')

def index(request):
    return render(request, "blog/index.html")

def parsing_time(request):
    url = request.POST.get('url')
    good = anyparsing.parsing(url)
    with open('aa.txt', 'w', encoding='utf8') as f:
        f.write(str(good))
    return HttpResponse(f'{good}')

def percent_step1(request):
    active2 = True
    posts = Post.objects.filter(archive__in=[False])
    return render(request, 'blog/percent_step1.html', {'posts': posts, 'active2': active2})

def percent_step2(request):
    active2 = True
    posts = Post.objects.filter(archive__in=[False])
    global aa
    aa = request.POST.get('product')
    for i in posts:
        if str(i) == str(aa):
            balance_users = i.balance_users
            balance_reserve_fund = i.balance_reserve_fund
    profile = Post.objects.get(product=aa)
    published_date = profile.published_date.strftime("%d/%m/%Y в %H:%M:%S")
    return render(request, 'blog/percent_step2.html', {'posts': posts, 'active2': active2, 'aa': aa, 'published_date': published_date, 'balance_users': balance_users, 'balance_reserve_fund': balance_reserve_fund})

def percent_step3(request):
    active2 = True
    global aa, bb
    posts = Post.objects.filter(archive__in=[False])
    for i in posts:
        if str(i) == str(aa):
            balance_users = i.balance_users
            balance_reserve_fund = i.balance_reserve_fund
    bb = request.POST.get('plus_or_minus')
    if bb == 'plus':
        bb = 'plus'
    elif bb == 'minus':
        bb = 'minus'
    else:
        bb = 'withdraw'
    profile = Post.objects.get(product=aa)
    published_date = profile.published_date.strftime("%d/%m/%Y в %H:%M:%S")
    if request.method == 'POST':
        return render(request, 'blog/percent_step3.html', {'aa': aa, 'active2': active2, 'bb': bb, 'published_date': published_date, 'balance_users': balance_users, 'balance_reserve_fund': balance_reserve_fund})

def percent_step4(request):
    active2 = True
    global aa, bb, summ5, summ6
    posts = Post.objects.filter(archive__in=[False])

    for i in posts:
        if str(i) == str(aa):
            balance_users = i.balance_users
            balance_reserve_fund = i.balance_reserve_fund
            summ5 = balance_users
            summ6 = balance_reserve_fund
    summ = int(request.POST.get('summ'))
    percent = request.POST.get('percent')
    if summ > 0:
        ok = True
        if bb == 'plus':
            summ2 = summ - (summ / 100 * int(percent))
            summ3 = summ - summ2
            summ4 = 0
            summ5 = summ5 + summ2
            summ6 = summ6 + summ3
            txt = 'ПРИБАВИТЬ НА БАЛАНС'
        elif bb == 'minus':
            summ2 = summ - (summ / 100 * int(percent))
            summ3 = summ - summ2
            summ4 = 0
            summ5 = summ5 - summ2
            summ6 = summ6 - summ3
            txt = 'ОТБАВИТЬ С БАЛАНСА'
    return render(request, 'blog/percent_step4.html', {'ok': ok, 'active2': active2, 'summ': summ, 'summ2': summ2, 'summ3': summ3, 'summ4': summ4, 'percent': percent, 'txt': txt, 'balance_users': balance_users, 'balance_reserve_fund': balance_reserve_fund, 'aa': aa, 'bb': bb, 'summ5': summ5, 'summ6': summ6})

def percent_step5(request):
    active2 = True
    global aa, bb, summ5, summ6
    posts = Post.objects.filter(archive__in=[False])
    for i in posts:
        if str(i) == str(aa):
            balance_users = i.balance_users
            balance_reserve_fund = i.balance_reserve_fund
    profile = Post.objects.get(product=aa)
    profile.balance_users = summ5
    profile.balance_reserve_fund = summ6
    profile.save()
    profile = Post.objects.get(product=aa)
    profile.published_date = datetime.now()
    profile.save()
    profile = Post.objects.get(product=aa)
    published_date = profile.published_date.strftime("%d/%m/%Y в %H:%M:%S")
    return render(request, 'blog/percent_step5.html', {'summ5': summ5, 'active2': active2, 'summ6': summ6, 'aa': aa, 'balance_users': balance_users, 'balance_reserve_fund': balance_reserve_fund, 'bb': bb, 'published_date': published_date})