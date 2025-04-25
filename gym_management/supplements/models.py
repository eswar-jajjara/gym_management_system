from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class ProductType(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=50, default='fas fa-capsule')

    def __str__(self):
        return self.name


class ProductCategory(models.Model):
    type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.type.name} - {self.name}"


class Supplement(models.Model):
    WEIGHT_GOAL_CHOICES = [
        ('gain', 'Weight Gain'),
        ('loss', 'Weight Loss'),
        ('maintain', 'Maintain'),
    ]

    name = models.CharField(max_length=200)
    type = models.ForeignKey(ProductType, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    weight_goal = models.CharField(max_length=20, choices=WEIGHT_GOAL_CHOICES, blank=True)
    is_diet_food = models.BooleanField(default=False)
    image = models.ImageField(upload_to='supplements/', blank=True, null=True)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ProductRecommendation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='supplement_recommendations')
    product = models.ForeignKey(Supplement, on_delete=models.CASCADE, related_name='user_recommendations')
    interaction_type = models.CharField(max_length=20, choices=[
        ('viewed', 'Viewed'), ('purchased', 'Purchased'), ('recommended', 'Recommended')
    ])
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'product', 'interaction_type')