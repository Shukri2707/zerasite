from .models import Feedback
from django.forms import ModelForm, TextInput, Textarea, NumberInput


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'quality', 'feedback']

        widgets = {
            "name": TextInput(attrs={
                'class': 'fb-form-name',
                'placeholder': 'Ваше имя',
            }),
            "quality": NumberInput(attrs={
                'class': 'fb-form-quality',
                'placeholder': 'Оценка работы /5',
            }),
            "feedback": Textarea(attrs={
                'class': 'fb-form-feedback',
                'placeholder': 'Отзыв',
            }),

            
        }