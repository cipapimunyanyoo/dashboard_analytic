import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.date_input("Select a date")

st.title("""Welcome to my Dashboard
This is my first time using streamlit.""")

st.image("gym.jpg", caption="Gym Dashboard Logo")

# ✅ Correctly reading your gym data
df = pd.read_csv("gym_members_exercise_tracking.csv")

# show data
st.subheader("Raw Data")
st.write(df)

# histogram
st.subheader("Histogram")
# Added key="hist_col" to prevent duplicate widget errors!
column = st.selectbox("Choose a column for the histogram", df.columns, key="hist_col")
fig, ax = plt.subplots(figsize = (10,6))
df[column].plot(kind = 'hist', ax =ax)
st.pyplot(fig)

fig = px.histogram(df, x=column)
fig.update_traces(marker = {"color": "purple", "line":{"color": "black", "width":2}})
st.plotly_chart(fig)

# Scatter chart
st.subheader("Scatter Chart")
# Added unique keys to these selectboxes too!
x_column = st.selectbox("Choose x-axis column", df.columns, key="scatter_x")
y_column = st.selectbox("Choose y-axis column", df.columns, key="scatter_y")

fig, ax = plt.subplots(figsize = (10,6))
df.plot(kind = 'scatter', x=x_column, y=y_column, ax =ax)
st.pyplot(fig)

# ✅ FIXED: Changed color='sex' to color='Gender' to match your gym data columns!
fig = px.scatter(df, x=x_column, y=y_column, color='Gender', color_discrete_sequence=['yellow', 'red'])
st.plotly_chart(fig)