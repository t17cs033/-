from django import forms

class FclForm(forms.Form):
    fcl_a = forms.IntegerField(
        label = 'ホワイトボード',
        min_value = 0,
        max_value = 10,
        required = True,
        )
    
    fcl_b = forms.IntegerField(
        label = 'プロジェクタ',
        min_value = 0,
        max_value = 1,
        required = True,
        )
    
    