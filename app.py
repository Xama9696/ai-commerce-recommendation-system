import streamlit as st
from recommendation_engine import recommend_products
from ai_assistant import generate_ai_response

st.title("AI-Powered Personalized Commerce Recommendation System")

category = st.selectbox(
    "Choose Category",
    ["Shoes", "Fashion", "Electronics"]
)

budget = st.slider(
    "Select Budget",
    1000,
    100000,
    5000
)

query = st.text_input(
    "What are you looking for?"
)

if st.button("Get Recommendations"):

    recommendations = recommend_products(category, budget)

    st.subheader("Recommended Products")
    st.dataframe(recommendations)

    ai_response = generate_ai_response(
        query,
        recommendations.to_string()
    )

    st.subheader("AI Shopping Assistant")
    st.write(ai_response)