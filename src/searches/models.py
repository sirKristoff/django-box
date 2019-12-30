from django.conf import settings
from django.db import models



class SearchQuery(models.Model):
    """Search Query history"""

    user      = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL)
    path      = models.CharField(max_length=64)
    query     = models.CharField(max_length=220)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['path', '-timestamp']

    def __repr__(self):
        return f"<SearchQuery({self.id}): '{self.timestamp}' {self.user}@{self.path}:'{self.query}'>"

    @classmethod
    def add_query(cls, request):
        user = None
        if request.user.is_authenticated:
            user = request.user
        path = request.path
        query = request.GET.get('q', None) or None
        if query:
            cls.objects.create(user=user, path=path, query=query)
