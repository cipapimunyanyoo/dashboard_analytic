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

# 📈 Histogram Section
st.subheader("Histogram Analysis")
# Added key="hist_col" to prevent duplicate widget errors!
column = st.selectbox("Choose a column for the histogram", df.columns, key="hist_col")

# Matplotlib Histogram
fig, ax = plt.subplots(figsize=(10,6))
df[column].plot(kind='hist', ax=ax)
st.pyplot(fig)

# Plotly Histogram
fig = px.histogram(df, x=column, title=f"Distribution of {column}")
fig.update_traces(marker={"color": "purple", "line":{"color": "black", "width":2}})
st.plotly_chart(fig)

#  General Scatter Chart Section
st.subheader("General Scatter Chart")
# Added unique keys to these selectboxes too!
x_column = st.selectbox("Choose x-axis column", df.columns, key="scatter_x")
y_column = st.sheet_selectbox = st.selectbox("Choose y-axis column", df.columns, key="scatter_y")



# Matplotlib Scatter
fig, ax = plt.subplots(figsize=(10,6))
df.plot(kind='scatter', x=x_column, y=y_column, ax=ax)
st.pyplot(fig)

# Plotly Scatter
#  FIXED: Changed color='sex' to color='Gender' to match your gym data columns!
fig = px.scatter(df, x=x_column, y=y_column, color='Gender', color_discrete_sequence=['yellow', 'red'], title=f"{x_column} vs {y_column}")
st.plotly_chart(fig)


# ==========================================
# INTERACTIVE SCATTER PLOTS ADDED BELOW
# ==========================================

#  Plot 1: Workout Duration vs Calories Burned Analysis
st.subheader(" Workout Duration vs. Calories Burned")
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
    title="Relationship Between Workout Duration and Calories Burned 💸",
    labels={'Session_Duration (hours)': 'Workout Duration (Hours)', 'Calories_Burned': 'Calories Burned (kcal)'},
    opacity=0.8
)
st.plotly_chart(fig_duration)


# 2️ Plot 2: Gender Fitness Characteristics Comparison
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
    title=f"Comparing {x_fitness} vs {y_fitness} by Gender ⚧️",
    hover_data=['Age', 'Workout_Type'],
    color_discrete_sequence=px.colors.qualitative.Set2,
    opacity=0.8
)
st.plotly_chart(fig_gender)



# ==========================================
#  NEW: INTERACTIVE GROUPED BAR CHART 
# ==========================================
st.subheader("Average Fitness Characteristics by Gender")
st.markdown("This bar chart displays the aggregated average values grouped by gender.")

# 1. Calculate the mean values grouped by Gender
df_avg = df.groupby('Gender')[['Fat_Percentage', 'Workout_Frequency (days/week)', 'Water_Intake (liters)']].mean().reset_index()

# 2. Add an interactive multi-select widget to filter specific features in real-time
selected_metrics = st.multiselect(
    "Select metrics to display:",
    options=['Fat_Percentage', 'Workout_Frequency (days/week)', 'Water_Intake (liters)'],
    default=['Fat_Percentage', 'Workout_Frequency (days/week)', 'Water_Intake (liters)']
)

if selected_metrics:
    # 3. Create the interactive Grouped Bar Chart using Plotly Express
    fig_bar = px.bar(
        df_avg,
        x='Gender',
        y=selected_metrics,
        barmode='group',
        title="Average Fitness Characteristics by Gender",
        labels={'value': 'Average Value', 'variable': 'Variables'},
        color_discrete_sequence=px.colors.qualitative.Plotly  # Clean, distinct professional colors
    )
    
    # Clean up layout adjustments to replicate your screenshot style
    fig_bar.update_layout(
        yaxis_title="Average Value",
        xaxis_title="Gender",
        legend_title="Variables",
        hovermode="x unified"
    )
    
    # 4. Render chart in Streamlit
    st.plotly_chart(fig_bar, use_container_width=True)
else:
    st.warning("Please select at least one metric to display the chart! ⚠️")
