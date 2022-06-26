from django.shortcuts import get_object_or_404, render
from Article.models import Article
from django.views.generic.detail import DetailView

from Article.models import Comment
# Create your views here.
class ArticlesDetailView(DetailView):
    
    model = Article
    template_name = 'home/post-details.html'
    def get_object(self):

        pk = self.kwargs.get('pk')
        article = get_object_or_404(Article.objects.filter(status = 'p' , id=pk))
        ip_address = self.request.user.ip_address
        if ip_address not in article.hits.all():
            article.hits.add(ip_address)
        return article
                
                
                
def detail(request , pk):
    article = get_object_or_404(Article , id = pk)
    if request.method == 'POST':
        body = request.POST.get('body')
        parent_id = request.POST.get('parent_id')
        if parent_id :
            Comment.objects.create(body=body, article=article , user=request.user ,parent_id=int(parent_id))
        else :
            Comment.objects.create(body=body, article=article , user=request.user)
    return render(request, 'home/post-details.html', {'article': article})