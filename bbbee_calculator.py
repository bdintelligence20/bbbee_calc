import streamlit as st

# Apply custom CSS to remove the Streamlit header and menu
st.markdown(
    """
    <style>
    .stApp {
        background-color: #a7af38;
        color: black;
    }
    .stNumberInput label, .stNumberInput input, .stMarkdown, .stTitle {
        color: black !important;
    }
    .stNumberInput input {
        background-color: #e0e0e0 !important;
        color: black !important;
    }
    .output {
        font-size: 24px;
        font-weight: bold;
        color: black;
    }
    .header {
        font-size: 36px;
        font-weight: bold;
        margin-top: 20px;
        color: black !important;
    }
    h1 {
        color: black !important;
    }
    /* Hide Streamlit header and menu */
    header, .st-emotion-cache-h4xjwg ezrtsby2 {
        display: none;
    }

    /* Hide the Streamlit menu */
.css-18ni7ap.e8zbici2 {
    visibility: hidden;
}

/* Hide the Streamlit footer */
footer {
    visibility: hidden;
}

/* Hide the top bar */
.css-164nlkn.egzxvld0 {
    visibility: hidden;
}

    </style>
    """,
    unsafe_allow_html=True
)

# Add space for the logo
logo_path = 'DigitalCampus-logo (2).png'  # Ensure the path is correct
st.image(logo_path, width=200)

st.title('B-BBEE Skills Spend Recognition Calculator')

# User inputs for the calculator
num_employees = st.number_input('Number of Employees', min_value=1, value=1, step=1)
average_salary = st.number_input('Average Monthly Salary of Designate Employee (ZAR)', value=0.0, step=1000.0)
average_duration_days = st.number_input('Average Duration of Programme (in Days)', value=0, step=1)
course_cost = st.number_input('Programme or Course Cost (ZAR)', value=0.0, step=1000.0)

# Calculation based on the provided formula using averages
spend_per_employee = ((average_salary / 21) * average_duration_days) + course_cost
total_spend_recognition = spend_per_employee * num_employees

# Display the spend per employee
st.markdown(f'<p class="header">Potential B-BBEE Skills Spend Recognition Spend per Employee:</p>', unsafe_allow_html=True)
st.markdown(f'<p class="output">R {spend_per_employee:,.2f}</p>', unsafe_allow_html=True)

# Display the total spend recognition for all employees
st.markdown(f'<p class="header">Potential Total B-BBEE Skills Spend Recognition for {num_employees} employees:</p>', unsafe_allow_html=True)
st.markdown(f'<p class="output">R {total_spend_recognition:,.2f}</p>', unsafe_allow_html=True)
