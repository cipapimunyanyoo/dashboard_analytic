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
fig = px.histogram(df, x=column)
fig.update_traces( marker = {"color": "purple", "line":{"color": "black", "width":2}})
st.plotly_chart(fig)

#Scatter chart
st.subheader("Scatter Chart")
x_column = st.selectbox("Choose x-axis column", df.columns)
y_column = st.selectbox("Choose y-axis column", df.columns)
fig, ax = plt.subplots(figsize = (10,6))
df.plot(kind = 'scatter', x=x_column, y=y_column, ax =ax)
st.pyplot(fig)

fig = px.scatter(df, x=x_column, y = y_column,color ='sex' , color_discrete_sequence= ['yellow', 'red'])
st.plotly_chart(fig)

#bar chart
import pandas as pd
import matplotlib.pyplot as plt

# Create DataFrame
df = pd.DataFrame(data)

# Calculate means by gender
gender_means = df.groupby('Gender')[
    ['Fat Percentage',
     'Workout Frequency (days/week)',
     'Water Intake (liters)']
].mean()

# Plot
gender_means.plot(kind='bar', figsize=(10,6))

plt.title('Average Fitness Characteristics by Gender')
plt.ylabel('Average Value')
plt.xticks(rotation=0)
plt.legend(title='Variables')
plt.show()
