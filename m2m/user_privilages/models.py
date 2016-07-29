from django.db import models

class User_Privilage(models.Model):

    CODE_CHOICES = (
        (0, 'USER'),
        (1, 'ADMIN'),
    )
    display_name = models.CharField(max_length=250)
    code = models.IntegerField(choices=CODE_CHOICES, default=0)
    description = models.CharField(max_length=250, blank=True, null=True)

    def __unicode__(self):
        return u'name={},code={},id={}'.format(
            self.display_name,
            self.code,
            self.pk
        )
