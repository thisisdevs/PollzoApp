from django.forms import ModelForm
from .models import Question

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['question_text','interests']
        help_texts = {
            'interests':'select multiple choices by pressing CTRL'
        }
