from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import redirect, render
# Create your views here.
from django.views import View
from django.views.generic import TemplateView

from main.models import Comment, Post


class AddPost(View, LoginRequiredMixin):

    def post(self, request, post_id):
        if not request.user.is_staff:
            return JsonResponse({"error": "Permisos insuficientes"})
        title = request.POST.get("title", "")
        content = request.POST.get("content", "")
        related_tags = request.POST.get("related_tags", "")
        post = Post.objects.create(
            title=title,
            content=content,
            related_tags = related_tags
            )
        post.save()
        return redirect("view_post", (post.pk))


class DeletePost(View, LoginRequiredMixin):
    def post(self, request, post_id):
        if not request.user.is_staff:
            return JsonResponse({"error": "Permisos insuficientes"})
        try:
            post = Post.objects.get(pk=post_id)
        except Post.DoesNotExist:
            return JsonResponse({"error": "Post Inexistente"})
        post.delete()
        return JsonResponse({"msg": "Success"})


class ViewPost(View, LoginRequiredMixin):
    def get(self, request, post_id):
        post = Post.object.filter(pk=post_id).first()
        if not post:
            data = {"error": "Post no encontrado"}
        data = post.as_json()
        return JsonResponse(data)


class AddComment(View, LoginRequiredMixin):
    def post(self, request, post_id):
        """Usado para agregar un comentario al post"""
        post = Post.object.filter(pk=post_id).first()
        title = self.request.POST.get("title", "")
        comment = self.request.POST.get("comment", "")
        user = self.request.user
        if not title or not comment:
            return JsonResponse({"error": "Datos incompletos"})
        obj = Comment.objects.create(
            title=title,
            comment=comment,
            user=user,
            post=post
            )
        obj.save()
        return redirect("view_post", (self.post.pk,))


class BlogList(TemplateView, LoginRequiredMixin):
    template = "templates/blog_list.html"

    def get(self, request):
        objs = Post.objects.all().order_by("-pk")
        context = {"posts": objs}
        return render(request, self.template, context)
