from django import forms
from .models import Video
from user.models import meokda_user
import os

class VideoForm(forms.ModelForm):
    def clean_file(self):
        file = self.cleaned_data.get('file', None)
        if file:
            extension = os.path.splitext(file.name)[-1].lower()
            if extension not in ('.mp4', '.avi'):
                raise forms.ValidationError('비디오파일을 올려주세요')
            return file


    class Meta:
        model = Video
        fields = [
            'restaurant',
            'foodname',
            'file',
            'price',
            'status',
            'distance',
        ]
