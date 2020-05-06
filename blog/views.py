from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import CommentForm
from katalog.models import katalog
def post_list(request):
    posts = Post.objects.all()
    
    context = {
        'posts': posts,
    }
    return render(request, 'blog.html', context)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.filter(active=True)
    new_comment = None
    posty = Post.objects.all()
    firmy = katalog.objects.all()[:6]
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    context = {
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form,
                                           'post': post,
                                           'posty': posty,
                                           'firmy': firmy}
    return render(request, 'blog_detail.html', context)
