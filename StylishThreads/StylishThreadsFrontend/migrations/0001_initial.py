# Generated by Django 5.1.1 on 2024-10-02 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(db_index=True, max_length=50, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(blank=True, max_length=10, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('account_creation_date', models.DateField(blank=True, null=True)),
                ('last_login_date', models.DateField(blank=True, null=True)),
                ('total_spent', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('transaction_frequency', models.IntegerField(blank=True, null=True)),
                ('average_transaction_value', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('last_transaction_date', models.DateField(blank=True, null=True)),
                ('number_of_transactions', models.IntegerField(blank=True, null=True)),
                ('favorite_payment_method', models.CharField(blank=True, max_length=50, null=True)),
                ('purchase_channel', models.CharField(blank=True, max_length=50, null=True)),
                ('preferred_device', models.CharField(blank=True, max_length=50, null=True)),
                ('preferred_language', models.CharField(blank=True, max_length=50, null=True)),
                ('time_on_site', models.CharField(blank=True, max_length=50, null=True)),
                ('page_views_per_session', models.IntegerField(blank=True, null=True)),
                ('average_cart_value', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('abandoned_cart_count', models.IntegerField(blank=True, null=True)),
                ('product_browsing_history', models.TextField(blank=True, null=True)),
                ('loyalty_program_member', models.BooleanField(default=False)),
                ('loyalty_points_balance', models.IntegerField(blank=True, null=True)),
                ('email_open_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('email_click_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('SMS_opt_in', models.BooleanField(default=False)),
                ('SMS_click_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('best_time_in_the_day', models.IntegerField(blank=True, null=True)),
                ('best_day_in_a_week', models.CharField(blank=True, max_length=20, null=True)),
                ('best_week_in_a_month', models.IntegerField(blank=True, null=True)),
                ('coupon_usage_frequency', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('social_media_engagement', models.CharField(blank=True, max_length=50, null=True)),
                ('number_of_reviews_written', models.IntegerField(blank=True, null=True)),
                ('average_review_rating', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
                ('referral_count', models.IntegerField(blank=True, null=True)),
                ('customer_service_interactions', models.IntegerField(blank=True, null=True)),
                ('live_chat_use_frequency', models.CharField(blank=True, max_length=50, null=True)),
                ('marketing_segment', models.CharField(blank=True, max_length=50, null=True)),
                ('campaign_engagement_score', models.IntegerField(blank=True, null=True)),
                ('preferred_communication_channel', models.CharField(blank=True, max_length=50, null=True)),
                ('click_through_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('conversion_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('discount_usage_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('preferred_brand', models.CharField(blank=True, max_length=100, null=True)),
                ('brand_loyalty_index', models.IntegerField(blank=True, null=True)),
                ('lifetime_value_estimate', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('frequency_of_visits_per_week', models.IntegerField(blank=True, null=True)),
                ('returning_customer', models.BooleanField(default=False)),
                ('shopping_basket_value', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('cart_conversion_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('purchase_value_category', models.CharField(blank=True, max_length=50, null=True)),
                ('transaction_frequency_category', models.CharField(blank=True, max_length=50, null=True)),
                ('product_affinity', models.TextField(blank=True, null=True)),
                ('discount_affinity', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
            ],
        ),
    ]
