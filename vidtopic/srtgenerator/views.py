from django.shortcuts import render
from .forms import UploadFileForm
from django.conf import settings
import subprocess as sp
# Create your views here.

MODEL_SCRIPT_PATH = "../../py-srt-generator"

def index(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            file_location = str(settings.BASE_DIR) + obj.file.url
            print(file_location)
            args = [
                "python3", 
                f"{MODEL_SCRIPT_PATH}/run.py", 
                file_location,
                f"{obj.title}.srt",
            ]
            print(" ".join(args))
            logs = sp.run(args)
            print(logs)
            with open(f'{MODEL_SCRIPT_PATH}/{obj.title}.srt', 'r') as f:
                file = f.read().split('\n')
                new_text = "<br>".join(file)
                print(file)
            return render(request, 'srtgenerator/show_srt.html', {'text': new_text})
        else:
            return render(request, 'srtgenerator/index.html', {'form': form})
        
    form = UploadFileForm()
    return render(request, 'srtgenerator/index.html', {'form': form})