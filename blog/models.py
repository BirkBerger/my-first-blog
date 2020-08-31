from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):       # models.Model: We define Post in our database as a "Django Model"

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # ForeignKey is another model
    title = models.CharField(max_length=200)    # define text with a limit of 200 characters
    text = models.TextField()                   # define text with no limit
    created_date = models.DateTimeField(default=timezone.now)       # define date and time
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):      # double-underscore = dunder (mifflin)
        return self.title


# Django model: An object that is saved in the database
# We are using a SQLite database

# Your local computer will be the place where you do development and testing.
# When you're happy with the changes, you will place a copy of your program on GitHub.
# Your website will be on PythonAnywhere
# and you will update it by getting a new copy of your code from GitHub.

# Deploying a web app on PythonAnywhere involves pulling down your code from GitHub,
# and then configuring PythonAnywhere to recognise it
# and start serving it as a web application.

# The workflow in web development:
# 1) make changes locally,
# 2) push those changes to GitHub
# 3) pull your changes down to your live Web server (PythonAnywhere)