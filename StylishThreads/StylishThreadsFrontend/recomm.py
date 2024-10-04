import openai
import pandas as pd
import requests
from io import BytesIO
from PIL import Image

# Set up OpenAI API credentials
openai.api_key = "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"

# Load and preprocess user data
user_data = pd.read_csv("E:/user_attribures.csv/user_attribures.csv")
user_data = user_data.dropna()

# Define the email template
email_template = {
    "English": """
Dear {USER_NAME},

Your wardrobe deserves an upgrade! Get {DISCOUNT}% off on the latest {PRODUCT_NAME} from StylishThreads. With prices as low as {MSP}, there’s no better time to shop!

Don't miss out!

{PRODUCT_IMAGE}
""",
    "Spanish": """
Estimado {USER_NAME},

¡Tu guardarropa merece una actualización! Obtén un {DISCOUNT}% de descuento en el último {PRODUCT_NAME} de StylishThreads. ¡Con precios tan bajos como {MSP}, no hay mejor momento para comprar!

¡No te lo pierdas!

{PRODUCT_IMAGE}
""",
    # Add more languages as needed
}


# Function to generate personalized email
def generate_promotional_email(user_name, preferred_language, purchase_history, browsing_history, discount_usage_rate):
    # Combine purchase and browsing history for context
    user_context = f"User {user_name} has purchased {purchase_history} and browsed {browsing_history}."

    # Use OpenAI to generate personalized product recommendation
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"{user_context} Recommend a product for this user.",
        max_tokens=50,
    )

    product_name = response.choices[0]["text"].strip()

    # Use DALL-E to generate an image for the recommended product
    image_response = openai.Image.create(
        prompt=f"A high-quality image of a {product_name}",
        n=1,
        size="512x512"
    )

    image_url = image_response['data'][0]['url']
    image_data = requests.get(image_url).content
    image = Image.open(BytesIO(image_data))

    # Save the image to a file
    image_path = f"{user_name}_product_image.png"
    image.save(image_path)

    # Determine the discount based on the user's discount usage rate
    discount = int(discount_usage_rate * 100)  # Convert discount usage rate to percentage

    # Fill in the email template with personalized details
    email_content = email_template[preferred_language].format(
        USER_NAME=user_name,
        DISCOUNT=discount,
        PRODUCT_NAME=product_name,
        MSP=50,  # Example minimum selling price
        PRODUCT_IMAGE=f"<img src='{image_path}' alt='{product_name}'>"
    )

    return email_content


# Example usage
for index, user in user_data.iterrows():
    user_name = user["name"]
    preferred_language = user["preferred_language"]
    purchase_history = user["product_browsing_history"]
    browsing_history = user[
        "product_browsing_history"]  # Assuming browsing history is the same as purchase history for simplicity
    discount_usage_rate = user["discount_usage_rate"]

    email = generate_promotional_email(user_name, preferred_language, purchase_history, browsing_history,
                                       discount_usage_rate)
    print(email)
    print("-" * 80)