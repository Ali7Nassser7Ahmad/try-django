from django import forms
from .models import Articels
class ArticleForm(forms.ModelForm):
    class Meta:
        model=Articels
        fields=["article_title","article_content"]
    def clean(self):
        data=self.cleaned_data
        title=data.get("article_title")
        q=Articels.objects.all().filter(article_title__icontains=title)
        if q.exists():
            self.add_error("article_title",f"\"{title}\" is already in use")
        return data
class ArticleFormOld(forms.Form):
    title=forms.CharField(max_length=255)
    content=forms.CharField(max_length=255)

    # def clean_title(self):
    #     cleaned_data=self.cleaned_data
    #     title=cleaned_data.get("title")
    #     if title.lower().strip()=="the office":
    #         raise forms.ValidationError("the title is token")
    #     return title

    def clean(self):
        cleaned_data=self.cleaned_data
        title=cleaned_data.get("title")
        content=cleaned_data.get("content")
        if title=="the office":
            self.add_error("title","the title is taken")
        if "office" in content:
            self.add_error("content","the office is not allowed")