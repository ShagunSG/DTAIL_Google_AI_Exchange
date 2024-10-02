import csv
from StylishThreadsFrontend.models import User  # Adjust this to match your model
from django.conf import settings
from datetime import datetime

def run():
    User.objects.all().delete()
    file_path = settings.BASE_DIR / 'static' / 'user_attribures.csv'  # Adjust this to your CSV file path

    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Debugging: Print the raw date fields from CSV to verify the format
            print(f"Raw Dates: account_creation_date={row.get('account_creation_date')}, last_login_date={row.get('last_login_date')}, last_transaction_date={row.get('last_transaction_date')}")

            # Safely handle any missing or improperly formatted date fields
            account_creation_date = row.get('account_creation_date', '').split(' ')[0]
            last_login_date = row.get('last_login_date', '').split(' ')[0]
            last_transaction_date = row.get('last_transaction_date', '').split(' ')[0]

            try:
                # Convert to date object if valid
                if account_creation_date:
                    account_creation_date = datetime.strptime(account_creation_date, '%Y-%m-%d').date()
                if last_login_date:
                    last_login_date = datetime.strptime(last_login_date, '%Y-%m-%d').date()
                if last_transaction_date:
                    last_transaction_date = datetime.strptime(last_transaction_date, '%Y-%m-%d').date()

                # Update row with converted dates
                row['account_creation_date'] = account_creation_date
                row['last_login_date'] = last_login_date
                row['last_transaction_date'] = last_transaction_date

            except ValueError as e:
                # Print the error and continue to next row
                print(f"Error parsing date in row {row['user_id']}: {e}")
                continue

            # Debugging: Print the parsed dates to ensure they are correctly formatted
            print(f"Parsed Dates: account_creation_date={row['account_creation_date']}, last_login_date={row['last_login_date']}, last_transaction_date={row['last_transaction_date']}")

            User.objects.create(
                user_id=row['user_id'],
                name=row['name'],
                email=row['email'],
                gender=row['gender'],
                age=row['age'],
                location=row['location'],
                account_creation_date=row['account_creation_date'],
                last_login_date=row['last_login_date'],
                total_spent=row['total_spent'].replace('$', ''),
                transaction_frequency=row['transaction_frequency'],
                average_transaction_value=row['average_transaction_value'].replace('$', ''),
                last_transaction_date=row['last_transaction_date'],
                number_of_transactions=row['number_of_transactions'],
                favorite_payment_method=row['favorite_payment_method'],
                purchase_channel=row['purchase_channel'],
                preferred_device=row['preferred_device'],
                preferred_language=row['preferred_language'],
                time_on_site=row['time_on_site'],
                    page_views_per_session=row['page_views_per_session'],
                    average_cart_value=row['average_cart_value'].replace('$', ''),
                    abandoned_cart_count=row['abandoned_cart_count'],
                    product_browsing_history=row['product_browsing_history'],
                    loyalty_program_member=row['loyalty_program_member'] == 'Yes',
                    loyalty_points_balance=row['loyalty_points_balance'],
                    email_open_rate=row['email_open_rate'].replace('%', ''),
                    email_click_rate=row['email_click_rate'].replace('%', ''),
                    SMS_opt_in=row['SMS_opt_in'] == 'Yes',
                    SMS_click_rate=row['SMS_click_rate'].replace('%', ''),
                    best_time_in_the_day=row['best_time_in_the_day'],
                    best_day_in_a_week=row['best_day_in_a_week'],
                    best_week_in_a_month=row['best_week_in_a_month'],
                    coupon_usage_frequency=row['coupon_usage_frequency'].replace('%', ''),
                    social_media_engagement=row['social_media_engagement'],
                    number_of_reviews_written=row['number_of_reviews_written'],
                    average_review_rating=row['average_review_rating'],
                    referral_count=row['referral_count'],
                    customer_service_interactions=row['customer_service_interactions'],
                    live_chat_use_frequency=row['live_chat_use_frequency'],
                    marketing_segment=row['marketing_segment'],
                    campaign_engagement_score=row['campaign_engagement_score'],
                    preferred_communication_channel=row['preferred_communication_channel'],
                    click_through_rate=row['click_through_rate'].replace('%', ''),
                    conversion_rate=row['conversion_rate'].replace('%', ''),
                    discount_usage_rate=row['discount_usage_rate'].replace('%', ''),
                    preferred_brand=row['preferred_brand'],
                    brand_loyalty_index=row['brand_loyalty_index'],
                    lifetime_value_estimate=row['lifetime_value_estimate'].replace('$', ''),
                    frequency_of_visits_per_week=row['frequency_of_visits_per_week'],
                    returning_customer=row['returning_customer'] == 'Yes',
                    shopping_basket_value=row['shopping_basket_value'].replace('$', ''),
                    cart_conversion_rate=row['cart_conversion_rate'].replace('%', ''),
                    purchase_value_category=row['purchase_value_category'],
                    transaction_frequency_category=row['transaction_frequency_category'],
                    product_affinity=row['product_affinity'],
                    discount_affinity=row['discount_affinity'].replace('%', '')
            )
        print("CSV data successfully loaded into the database.")