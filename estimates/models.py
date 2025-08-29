from django.db import models


class Inquiry(models.Model):
    address = models.CharField(max_length=255)
    lot_size_acres = models.DecimalField(max_digits=10, decimal_places=2)
    user_context = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)


class Estimate(models.Model):
    inquiry = models.ForeignKey(Inquiry, related_name="estimates", on_delete=models.CASCADE)
    project_name = models.CharField(max_length=255)
    description = models.TextField()
    net_cash_flow = models.DecimalField(max_digits=12, decimal_places=2)
    revenue = models.DecimalField(max_digits=12, decimal_places=2)
    cost = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
