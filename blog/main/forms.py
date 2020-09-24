#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# -*- coding: utf-8 -*-
"""

Created on 24/09/20

@author: Marco Antonio Islas Cruz
"""
from main.models import Post


class AddPost(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ["published_date"]

class AddComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["title", "comment"]
