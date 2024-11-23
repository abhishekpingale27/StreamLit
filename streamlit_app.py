import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set the page configuration
st.set_page_config(page_title="CSV Data Visualizer", layout="wide")

# Application Title
st.title("CSV Data Visualizer")
st.write("Upload a CSV file to explore and visualize your data!")

# File Upload Section
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    # Read the uploaded CSV file
    data = pd.read_csv(uploaded_file)

    # Display dataset shape and basic information
    st.sidebar.header("Dataset Information")
    st.sidebar.write(f"**Rows:** {data.shape[0]}")
    st.sidebar.write(f"**Columns:** {data.shape[1]}")

    st.write("### Dataset Preview")
    st.dataframe(data.head(10))

    # Select Chart Type
    st.sidebar.header("Visualization Settings")
    chart_type = st.sidebar.selectbox("Select Chart Type", ["Line Chart", "Bar Chart", "Histogram", "Scatter Plot"])
    column1 = st.sidebar.selectbox("Select First Column", data.columns)
    column2 = st.sidebar.selectbox("Select Second Column (Optional)", ["None"] + list(data.columns))

    # Generate Chart
    st.write(f"### {chart_type}")
    if chart_type == "Line Chart":
        st.line_chart(data[column1])
    elif chart_type == "Bar Chart":
        st.bar_chart(data[column1])
    elif chart_type == "Histogram":
        plt.figure(figsize=(8, 6))
        sns.histplot(data[column1], kde=True, bins=20, color="blue")
        st.pyplot(plt)
    elif chart_type == "Scatter Plot":
        if column2 != "None":
            plt.figure(figsize=(8, 6))
            sns.scatterplot(data=data, x=column1, y=column2, color="green")
            plt.title(f"Scatter Plot: {column1} vs {column2}")
            st.pyplot(plt)
        else:
            st.warning("Please select a second column for the scatter plot.")

    # Summary Statistics
    st.write("### Summary Statistics")
    st.write(data.describe())

else:
    st.info("Please upload a CSV file to begin.")
