import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px
from transformers import pipeline

# Set theme colors for Credit Acceptance branding
primary_color = "#003399"  # Blue
secondary_color = "#FF6600"  # Orange
highlight_color = "#00BFFF"  # Sky Blue

# Configure Streamlit page
st.set_page_config(
    page_title="Credit Acceptance Dashboard",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Configuring header with logo on the top left
t1, t2 = st.columns((0.1, 0.8))
t1.image("index_0.png", width=200)  # Replace with your logo file path
t2.title("Exploring Credit Acceptance (CACC)")
t2.markdown(
    "This interactive dashboard provides insights into Credit Acceptance Corporation (CACC), showcasing stock trends, company details, and industry trends, while demonstrating my data visualization and AI/ML skills."
)

# Fetch and display CACC stock data
ticker = "CACC"
stock_data = yf.Ticker(ticker)
history = stock_data.history(period="1mo")  # Last 1 month of stock data
current_price = stock_data.info['currentPrice']
previous_close = stock_data.info['previousClose']

m1, m2, m3, m4 = st.columns(4)
m1.metric("Ticker Symbol", ticker)
m2.metric("Current Price", f"${current_price:.2f}")
m3.metric("Previous Close", f"${previous_close:.2f}")
m4.metric("Market Cap", f"${stock_data.info['marketCap']:,}")

# Tabs for additional insights
tab1, tab2, tab3, tab4 = st.tabs(["Q&A Tool", "About Credit Acceptance", "Stock Data", "Industry Trends"])

# Tab 1: Q&A Tool
with tab1:
    st.subheader("Credit Acceptance Q&A Tool")
    st.write("Ask a question about Credit Acceptance and get an answer based on the preloaded context.")

    # Expanded Context
    context = """
    Credit Acceptance Corporation, established in 1972, provides financing programs and related services to automobile dealers. 
    These programs enable dealers to sell vehicles to customers, including those who have difficulty obtaining financing elsewhere. 

    Key features:
    - Dealer Participation: Dealers share in the collections on consumer loans.
    - Commitment to transparency and fair practices.
    - Customer outreach programs focusing on credit improvement.

    Credit Acceptance operates with a mission to provide opportunities for credit-challenged customers while maintaining strong partnerships with auto dealers.
    """

    # User question input
    user_question = st.text_input("Enter your question about Credit Acceptance:")
    if user_question:
        qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")
        answer = qa_pipeline(question=user_question, context=context)
        st.write(f"**Answer:** {answer['answer']}")

# Tab 2: About Credit Acceptance
with tab2:
    st.subheader("About Credit Acceptance")
    st.write("""
    **Mission**: To provide financing solutions that help dealers sell cars and customers improve their credit.  
    Credit Acceptance has been recognized for its innovative auto financing solutions and its commitment to credit-challenged customers.
    """)
    st.subheader("Key Programs")
    st.write("""
    - **Dealer Service Center**: A dedicated platform for dealer support.  
    - **Customer Success Program**: Tools and resources to help customers improve credit scores and manage loans effectively.
    """)

# Tab 3: Stock Data
with tab3:
    st.subheader("CACC Stock Data")
    st.write(f"### CACC Stock Performance (Last 1 Month)")

    # Line chart for stock performance
    fig = px.line(
        history.reset_index(),
        x="Date",
        y="Close",
        title=f"CACC Stock Price - Last 1 Month",
        markers=True,
        line_shape="spline"
    )
    fig.update_traces(line_color=primary_color)
    fig.update_layout(
        title_font_color=primary_color,
        plot_bgcolor="white",
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=False)
    )
    st.plotly_chart(fig, use_container_width=True)

    st.write(f"**Current Price:** ${current_price:.2f}")
    st.write(f"**Previous Close:** ${previous_close:.2f}")
    st.write(f"**Market Cap:** ${stock_data.info['marketCap']:,}")

# Tab 4: Industry Trends
with tab4:
    st.subheader("Industry Trends")
    st.write("""
    The auto financing industry is evolving with increasing demand for alternative credit solutions.  
    **Key Trends**:  
    - Rise of digital financing platforms.  
    - Increased focus on credit improvement programs.  
    - Collaboration with dealerships for seamless financing options.
    """)

    # Mock data for market growth
    growth_data = pd.DataFrame({
        "Year": [2018, 2019, 2020, 2021, 2022],
        "Market Size (in Billion USD)": [100, 110, 120, 135, 145]
    })

    # Line chart for market growth using Plotly
    st.write("### Auto Financing Market Growth")
    fig_growth = px.line(
        growth_data,
        x="Year",
        y="Market Size (in Billion USD)",
        title="Auto Financing Market Growth",
        markers=True,
        line_shape="spline"
    )
    fig_growth.update_traces(line_color=secondary_color)
    fig_growth.update_layout(
        title_font_color=primary_color,
        plot_bgcolor="white",
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=False)
    )
    st.plotly_chart(fig_growth, use_container_width=True)
