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




# Bar Chart
st.subheader("Bar Chart")

category_column = st.selectbox(
    "Choose categorical column",
    df.select_dtypes(include='object').columns
)

value_column = st.selectbox(
    "Choose numerical column",
    df.select_dtypes(include='number').columns
)

# Calculate mean values
bar_data = df.groupby(category_column)[value_column].mean()

# Matplotlib Bar Chart
fig, ax = plt.subplots(figsize=(10, 6))
bar_data.plot(kind='bar', ax=ax)

ax.set_title(f'Average {value_column} by {category_column}')
ax.set_ylabel(f'Average {value_column}')
ax.set_xlabel(category_column)

st.pyplot(fig)

# Plotly Bar Chart
fig = px.bar(
    x=bar_data.index,
    y=bar_data.values,
    labels={'x': category_column, 'y': f'Average {value_column}'},
    title=f'Average {value_column} by {category_column}'
)

st.plotly_chart(fig)

