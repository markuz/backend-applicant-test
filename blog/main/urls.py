#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# -*- coding: utf-8 -*-
"""

Created on 24/09/20

@author: Marco Antonio Islas Cruz
"""
from django.urls import path

from main.views import AddComment, AddPost, BlogList, DeletePost, ViewPost

url_patterns = [
    path("blog_list/$", BlogList.as_view(), name="blog_list"),
    path("view_post/<int:post_id>", ViewPost.as_view(), name="view_post"),
    path("add_comment/<int:post_id>", AddComment.as_view(),
         name="add_comment"),
    path("add_post/", AddPost.as_view(), name="add_post"),
    path("delete_post/", DeletePost.as_view(), name="delete_post")
    ]
