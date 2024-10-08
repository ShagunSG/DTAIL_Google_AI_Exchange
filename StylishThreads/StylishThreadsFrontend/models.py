from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length=50, unique=True, db_index=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    gender = models.CharField(max_length=10, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    account_creation_date = models.DateField(null=True, blank=True)
    last_login_date = models.DateField(null=True, blank=True)
    total_spent = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    transaction_frequency = models.IntegerField(null=True, blank=True)
    average_transaction_value = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    last_transaction_date = models.DateField(null=True, blank=True)
    number_of_transactions = models.IntegerField(null=True, blank=True)
    favorite_payment_method = models.CharField(max_length=50, null=True, blank=True)
    purchase_channel = models.CharField(max_length=50, null=True, blank=True)
    preferred_device = models.CharField(max_length=50, null=True, blank=True)
    preferred_language = models.CharField(max_length=50, null=True, blank=True)
    time_on_site = models.CharField(max_length=50, null=True, blank=True)
    page_views_per_session = models.IntegerField(null=True, blank=True)
    average_cart_value = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    abandoned_cart_count = models.IntegerField(null=True, blank=True)
    product_browsing_history = models.TextField(null=True, blank=True)
    loyalty_program_member = models.BooleanField(default=False)
    loyalty_points_balance = models.IntegerField(null=True, blank=True)
    email_open_rate = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    email_click_rate = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    SMS_opt_in = models.BooleanField(default=False)
    SMS_click_rate = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    best_time_in_the_day = models.IntegerField(null=True, blank=True)
    best_day_in_a_week = models.CharField(max_length=20, null=True, blank=True)
    best_week_in_a_month = models.IntegerField(null=True, blank=True)
    coupon_usage_frequency = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    social_media_engagement = models.CharField(max_length=50, null=True, blank=True)
    number_of_reviews_written = models.IntegerField(null=True, blank=True)
    average_review_rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    referral_count = models.IntegerField(null=True, blank=True)
    customer_service_interactions = models.IntegerField(null=True, blank=True)
    live_chat_use_frequency = models.CharField(max_length=50, null=True, blank=True)
    marketing_segment = models.CharField(max_length=50, null=True, blank=True)
    campaign_engagement_score = models.IntegerField(null=True, blank=True)
    preferred_communication_channel = models.CharField(max_length=50, null=True, blank=True)
    click_through_rate = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    conversion_rate = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    discount_usage_rate = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    preferred_brand = models.CharField(max_length=100, null=True, blank=True)
    brand_loyalty_index = models.IntegerField(null=True, blank=True)
    lifetime_value_estimate = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    frequency_of_visits_per_week = models.IntegerField(null=True, blank=True)
    returning_customer = models.BooleanField(default=False)
    shopping_basket_value = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    cart_conversion_rate = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    purchase_value_category = models.CharField(max_length=50, null=True, blank=True)
    transaction_frequency_category = models.CharField(max_length=50, null=True, blank=True)
    product_affinity = models.TextField(null=True, blank=True)
    discount_affinity = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name