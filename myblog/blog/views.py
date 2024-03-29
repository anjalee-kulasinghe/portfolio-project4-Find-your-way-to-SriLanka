from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Article


class Index(View):
    def get(self, request):
        return render(request, 'blog/index.html')

class Featured(ListView):
    # Display a list of featured articles
    model = Article
    queryset = Article.objects.filter(featured=True).order_by('-date')
    template_name = 'blog/featured.html'
    paginate_by = 1

class DetailArticleView(DetailView):
    # Display details of a single article
    model = Article
    template_name = 'blog/blog_post.html'

    def get_context_data(self, *args, **kwargs):
        # Provide additional context data for the template
        context = super(DetailArticleView, self).get_context_data(*args, **kwargs)
        context['liked_by_user'] = False
        article = Article.objects.get(id=self.kwargs.get('pk'))
        if article.likes.filter(pk=self.request.user.id).exists():
            context['liked_by_user'] = True
        return context

class LikeArticle(View):
    # Handle user liking or unliking an article
    def post(self, request, pk):
        article = Article.objects.get(id=pk)
        if article.likes.filter(pk=self.request.user.id).exists():
            article.likes.remove(request.user.id)
        else:
            article.likes.add(request.user.id)
        article.save()
        return redirect('detail_article', pk)

class DeleteArticleView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    # Handle deletion of an article
    model = Article
    template_name = 'blog/blog_delete.html'
    success_url = reverse_lazy('index')

    def test_func(self):
        # Ensure that only the author of the article can delete it
        article = Article.objects.get(id=self.kwargs.get('pk'))
        return self.request.user.id == article.author.id

class BlogView(ListView):
    # Display a list of articles on the blog page
    model = Article
    queryset = Article.objects.all().order_by('-date')
    template_name = 'blog/blog.html'
    paginate_by = 1