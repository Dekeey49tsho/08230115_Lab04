from django.db import models

class LearningJourney(models.Model):
    title = models.CharField(max_length=100, help_text="Enter a descriptive title for your learning journey")
    description = models.TextField(help_text="Describe your learning experience, what you learned, and any insights")

    class Meta:
        verbose_name = "Learning Journey"
        verbose_name_plural = "Learning Journeys"

    def __str__(self):
        return self.title


class AboutMe(models.Model):
    name = models.CharField(max_length=100, help_text="Your full name")
    bio = models.TextField(help_text="Tell us about yourself, your background, and interests")

    class Meta:
        verbose_name = "About Me Entry"
        verbose_name_plural = "About Me Entries"

    def __str__(self):
        return self.name
