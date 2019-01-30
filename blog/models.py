from django.db import models

# Create your models here.
class Blog(models.Model):

	title = models.CharField(max_length=255)
	pub_date = models.DateTimeField(auto_now=True)
	image = models.ImageField(upload_to='blogsimage/')
	body = models.TextField(max_length=1000, default="")

	def summary(self):
		return self.body[0:100]

	def short_date(self):
		return self.pub_date.strftime('%b %e, %Y')
		
	def __str__(self):
		return self.title,self.pub_date
		
	
		