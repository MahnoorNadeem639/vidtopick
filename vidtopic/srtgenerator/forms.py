from django import forms
from matplotlib import widgets
from .models import UserFiles

def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.mp4', '.wav']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')    

class UploadFileForm(forms.ModelForm):
    file = forms.FileField(
        # upload_to = 'user_files', 
        label='Upload File', 
        validators=[validate_file_extension],
        widget=forms.FileInput(attrs={
            'placeholder': 'Upload File', 
            'style': 'width: 400px;',
            'class': 'form-control'
        })
    )

    title = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'style': 'margin-top: 5px;width: 400px;',
            'placeholder': 'test',
        })
    )

    class Meta:
        model = UserFiles
        fields = '__all__'