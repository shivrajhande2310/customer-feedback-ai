import streamlit as st
from google import genai

st.set_page_config(
    page_title="Customer Feedback AI",
    page_icon="🤖"
)

st.title("🤖 Customer Feedback AI")
st.write("Generate a personalized customer support email using Gemini AI.")

product = st.text_input("Product Name")

rating = st.selectbox(
    "Customer Rating",
    [1, 2, 3, 4, 5]
)

review = st.text_input("Customer Review")

summary = st.text_area("Detailed Customer Complaint")

if st.button("Generate AI Response"):

    if not product or not review or not summary:
        st.warning("Please fill in all the fields.")

    elif rating not in [1, 2]:
        st.warning("Please enter a critical rating of 1 or 2 stars.")

    else:
        prompt = f"""
You are a professional Customer Support Agent.

Write a short, personalized, and empathetic apology email for the customer based ONLY on the information provided below.

Product: {product}
Rating: {rating} star
Customer Review: {review}
Customer Complaint: {summary}

Requirements:
- Carefully understand the customer's actual situation and specific complaints.
- Identify the important problems mentioned by the customer yourself.
- Tailor the email to the actual product and circumstances described in the complaint.
- Do not assume a fixed complaint category or product type.
- Acknowledge the specific issues mentioned by the customer.
- Apologize sincerely and show empathy.
- If multiple problems are mentioned, acknowledge the important ones naturally.
- Use only facts explicitly stated in the customer review or complaint.
- Do not invent facts, problems, policies, causes, or solutions.
- Do not promise a refund, replacement, compensation, or other action unless explicitly mentioned.
- Do not use placeholders such as [Customer Name], [Order ID], or [Your Name].
- Keep the email professional, natural, concise, and personalized.
- Include a suitable subject line.
- End with "Sincerely, Customer Support Team".
"""

        client = genai.Client(
            api_key=st.secrets["GEMINI_API_KEY"]
        )

        with st.spinner("Generating personalized AI response..."):
            response = client.models.generate_content(
                model="gemini-3.5-flash-lite",
                contents=prompt
            )

        st.subheader("📧 AI-Generated Customer Response")
        st.write(response.text)