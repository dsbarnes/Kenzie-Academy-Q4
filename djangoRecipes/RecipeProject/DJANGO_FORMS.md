# Django Forms.
In this project we will use the package: `from django import forms`  

In the first demo, we used models.py as a reference to build our form.  
  
Create a forms.py file and create a class:

```python
class NewAddForm(forms.Form):
    title = forms. CharField(max_length=50)
    body = forms.CharField(widget=forms.Textarea)
    # We will need to import Author from models
    # This is so we can 'spell check' author names with a dropdown.
    author = forms.ModelChoiceField(queryset=Author.objecs.all()) 

```
  
In urls.py  
we will want to hook up the new rout to the form.   
  
Make the view in views.py file:  
```python
def my_new_view(request):
    html = 'my_new_form.html'
    if request.method == "POST":
     form = MyImportedForm(request.Post)
     # ALWAYS
     if form.is_valid():
        # This is an object - it can contain database objects
        # Thats a superpower
        data = form.cleaned_data
        MyCorrespondingModel.objects.create(
            title = data['title'],
            body = data['body'],
            author = data['author']
            # Or whatever
        )
        # Handle the re-route - path( ... name='REQUIRED_FOR_THIS_STEP')
        return HttpResponseRedirect(reverse("name"))
    form = MyImportedForm()
```
And a 'generic_form' template in `/templates/project`  
the `<form action="">` is intentional. Leave it as empty double quotes.  
be sure to link to the new template on the index / home page.  
we only need one generic_template to render both forms.  

