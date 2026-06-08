import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.date_input("Select a date")

st.title("""Welcome to Liyana's and Syifa's Dashboard
This is our first time using streamlit.""")

st.image("gym.jpg", caption="Gym Dashboard Logo")

# ✅ Correctly reading your gym data
df = pd.read_csv("gym_members_exercise_tracking.csv")

# show data
st.subheader("Raw Data")
st.write(df)

#histogram
st.subheader("Histogram")
column = st.selectbox("Choose a column", df.columns)
fig, ax = plt.subplots(figsize = (10,6))
df[column].plot(kind = 'hist', ax =ax)
st.pyplot(fig)





# Plotly bar chart
fig = px.bar(
    gender_means_long,
    x='Gender',
    y='Average Value',
    color='Variable',
    barmode='group',
    title='Average Fitness Characteristics by Gender'
)

st.plotly_chart(fig, use_container_width=True)
fig = px.histogram(df, x=column)
fig.update_traces( marker = {"color": "purple", "line":{"color": "black", "width":2}})
st.plotly_chart(fig)



