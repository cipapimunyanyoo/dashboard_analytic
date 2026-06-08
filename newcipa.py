import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.date_input("Select a date")

st.title("""Welcome to Liyana's and Syifa's Dashboard
This is ourfirst time using streamlit.""")

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

# 1️⃣ Plot 1: Workout Duration vs Calories Burned Analysis
st.subheader("Workout Duration vs. Calories Burned")
st.markdown("Analyze whether longer exercise sessions result in a higher calorie expenditure.")

# Interactive option to see how different factors influence this relationship
color_option = st.selectbox(
    "Color points by:", 
    ['Workout_Type', 'Gender', 'Experience_Level'], 
    key="duration_color"
)

fig_duration = px.scatter(
    df, 
    x='Session_Duration (hours)', 
    y='Calories_Burned', 
    color=color_option,
    hover_data=['Age', 'BMI'],
    title="Relationship Between Workout Duration and Calories Burned ",
    labels={'Session_Duration (hours)': 'Workout Duration (Hours)', 'Calories_Burned': 'Calories Burned (kcal)'},
    opacity=0.8
)
st.plotly_chart(fig_duration)


# 2️⃣ Plot 2: Gender Fitness Characteristics Comparison
st.subheader("Gender Fitness Characteristics Comparison")
st.markdown("Compare key exercise and fitness features across different genders.")

# Restricting options to the variables you specified
fitness_vars = ['Fat_Percentage', 'Workout_Frequency (days/week)', 'Water_Intake (liters)']

x_fitness = st.selectbox("Select X-axis Variable:", fitness_vars, index=0, key="fitness_x")
y_fitness = st.selectbox("Select Y-axis Variable:", fitness_vars, index=1, key="fitness_y")

fig_gender = px.scatter(
    df,
    x=x_fitness,
    y=y_fitness,
    color='Gender',
    symbol='Gender', # Uses different shapes for Male and Female points
    title=f"Comparing {x_fitness} vs {y_fitness} by Gender ",
    hover_data=['Age', 'Workout_Type'],
    color_discrete_sequence=px.colors.qualitative.Set2,
    opacity=0.8
)
st.plotly_chart(fig_gender)
