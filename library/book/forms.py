from django import forms

from .models import Comment

fohshaye_bad = ["احمق"]

# class CommentForm(forms.Form):
#     content = forms.CharField(widget=forms.Textarea, required=False)
#     rate = forms.IntegerField()


#     def clean_content(self):
#         content = self.cleaned_data['content']
#         for fosh in fohshaye_bad:
#             if fosh in content:
#                 raise forms.ValidationError("Moadab bash")
#         return content


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content", "rate"]