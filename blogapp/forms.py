from django import forms
from blogapp.models import Blogs


class AddBlogForm(forms.ModelForm):
    class Meta:
        model=Blogs
        fields=["title","body","blog_image"]

class UpdateBlogForm(forms.ModelForm):
    class Meta:
        model=Blogs
        fields=["title","body","blog_image"]


