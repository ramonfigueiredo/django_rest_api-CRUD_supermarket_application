from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    subcategory = models.CharField(max_length=255)
    amount = models.PositiveIntegerField()

    def __str__(self):
        return 'Item: [name = {}, category = {}, subcategory = {}, amount = {}]'\
            .format(self.name, self.category, self.subcategory, self.amount)
