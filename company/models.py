from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.widgets import CKEditorWidget
# Create your models here.
class top3post(models.Model):
	title = models.CharField(max_length=100)
	ContentTitle = models.CharField(max_length=100)
	content = RichTextUploadingField()
	backimage =	 models.ImageField(upload_to='back_pics/')

class totalpost(models.Model):
	title = models.CharField(max_length=100)
	ContentTitle = models.CharField( max_length=100)
	content = RichTextUploadingField()
	backimage =	 models.ImageField(upload_to='back_pics/')
	
class partner(models.Model):
	image =	 models.ImageField(upload_to='back_pics')

#class QueryMail(models.Model):
#	name = models.CharField(max_length=100, blank=True, null=True)
#	email = models.EmailField()
#	subject = models.CharField()
#	message = models.TextField(max_length=100)
#	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

	#def __str__(self):
	#	return f'{self.subject}
