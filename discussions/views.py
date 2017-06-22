from django.shortcuts import render, get_object_or_404, HttpResponse, redirect

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse

from .models import Discussion, Comment, SubComment
from discussions.forms import CommentForm


# Create your views here.


def discussions(request):
    discussion_all = Discussion.objects.all().order_by('-created_date')
    page = request.GET.get('page', 1)

    paginator = Paginator(discussion_all, 4)
    try:
        discuss_list = paginator.page(page)
    except PageNotAnInteger:
        discuss_list = paginator.page(1)
    except EmptyPage:
        discuss_list = paginator.page(paginator.num_pages)

    return render(request, 'discuss.html',
                  {'discuss_list': discuss_list}
                  )


def single_discuss(request, slug):
    discussion = get_object_or_404(Discussion, slug=slug)
    comments = Comment.objects.filter(discussion=discussion)
    if request.user.is_authenticated():
        if request.method == "POST":
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment_form = comment_form.save(commit=False)
                comment_form.commenter = request.user
                comment_form.discussion = discussion
                comment_form.save()
                if request.is_ajax():
                    print("AJAX RECIEVED")
                    return render("COMMENT DONE")
                return redirect('single_discuss', slug=discussion.slug)
        comment_form = CommentForm()
    else:
        comment_form = None
    return render(request, 'single_discuss.html',
                  {'discuss': discussion, 'comments': comments,
                   'comment_form': comment_form})
