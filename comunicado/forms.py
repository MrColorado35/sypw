from django.forms import ModelForm
from .models import Forum, Discussion


class CreateInForum(ModelForm):
    class Meta:
        model = Forum
        fields = ('name', 'email', 'topic', 'description')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Your Name',
            'email': 'Email Address',
            'topic': 'New subject',
            'description': 'Here you can describe your idea',
        }

        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False


class CreateInDiscussion(ModelForm):
    class Meta:
        model = Discussion
        forum = Forum.id
        fields = ['forum', 'discuss', 'nick', ]

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'forum': 'Choose Forum',
            'discuss': 'Your message',
            'nick': 'Your Name',
        }

        self.fields['discuss'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            # self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False


# class EditInDiscussion(ModelForm):
#     class Meta:
#         model = Discussion
        # def __init__(self, *args, **kwargs):
        #     self.fields['nick'].widget.attrs['autofocus'] = True

