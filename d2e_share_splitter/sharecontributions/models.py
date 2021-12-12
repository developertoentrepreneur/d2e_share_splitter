from django.db import models

contribution_type_choices = (
    ("time", "Time"),
    ("expenses", "Expenses"),
)


class Contribution(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    contribType = models.CharField(
        max_length=1024, choices=contribution_type_choices
    )
    projectType = models.ForeignKey(
        "shareconf.Project", on_delete=models.CASCADE
    )
    value = models.FloatField(default=0, blank=True, null=True)
    hours = models.FloatField(blank=True, null=True)
    date = models.DateField()
    details = models.CharField(max_length=1024)
    slices = models.FloatField(default=0)

    @classmethod
    def get_users(cls):
        users = []
        contribs = cls.objects.all()
        for contribution in contribs:
            users.append(contribution.user)
        return users


class ContribLog(models.Model):
    date = models.DateField()
    type = models.CharField(max_length=1024, default="creation")
    user = models.CharField(max_length=1024)
    details = models.CharField(max_length=1024)
