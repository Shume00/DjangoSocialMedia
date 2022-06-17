from django import forms
from .models import BlogPost, Author


class DateInput(forms.DateInput):
    input_type = 'date'


class BlogPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BlogPostForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = 'form-control'

    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'files']
        widgets = {
            'date': DateInput(),
            'lastChange': DateInput(),
        }
        exclude = ("author", "date", "lastChange",)


class AddingBlockedUsersForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddingBlockedUsersForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = 'form-control'

    class Meta:
        model = Author
        fields = ['blockedUser']
        exclude = ('firstName', 'lastName', 'user')
