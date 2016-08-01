from django import forms

 

class PostForm(forms.Form):

    zch = forms.CharField(max_length=256)

    #qyname = forms.CharField(max_length=256)
    #zczb1 = forms.CharField(max_length=256)
    #zczb2 = forms.CharField(max_length=256)
    #djjg = forms.CharField(max_length=256)
 
    

