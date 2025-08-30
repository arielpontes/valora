from django.db import models


class Inquiry(models.Model):
    id: int
    address = models.CharField(max_length=255)
    lot_size_acres = models.DecimalField(max_digits=10, decimal_places=2)
    current_property = models.TextField()
    property_goal = models.TextField()
    investment_commitment = models.TextField()
    excitement_notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Estimate(models.Model):
    inquiry = models.ForeignKey(
        Inquiry, related_name="estimates", on_delete=models.CASCADE
    )
    project_name = models.CharField(max_length=255)
    description = models.TextField()
    net_cash_flow = models.DecimalField(max_digits=12, decimal_places=2)
    revenue = models.DecimalField(max_digits=12, decimal_places=2)
    cost = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
