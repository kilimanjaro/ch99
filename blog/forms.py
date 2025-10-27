from django.forms import Form, CharField

class PostSearchForm(Form):
  search_word = CharField(label='Search Word')
  
  