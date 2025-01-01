class Cost(models.Model):
    description = models.CharField(max_length=255)
    sum = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.description} - {self.sum}"
