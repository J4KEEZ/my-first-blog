from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    remove_image = forms.BooleanField(required=False, label='Remove Image')
    remove_image2 = forms.BooleanField(required=False, label='Remove Image 2')

    class Meta:
        model = Post
        fields = ('title', 'text', 'image', 'image2')

    def save(self, commit=True):
        post = super().save(commit=False)

        if self.cleaned_data.get('remove_image'):
            post.image.delete(save=False)  # Delete the file from storage
            post.image = None

        if self.cleaned_data.get('remove_image2'):
            post.image2.delete(save=False)  # Delete the file from storage
            post.image2 = None

        if commit:
            post.save()
        return post