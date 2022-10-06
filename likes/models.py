from django.db import models
from django.contrib.auth.models import User
from observations.models import Observation


class Like(models.Model):
    """
    Like model, related to 'owner' and 'observation'.
    'owner' is a User instance and 'observation' is a observation instance.
    'unique_together' makes sure a user can't like the same observation twice.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    observation = models.ForeignKey(
        observation, related_name='likes', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'observation']

    def __str__(self):
        return f'{self.owner} {self.observation}'
