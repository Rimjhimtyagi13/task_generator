import streamlit as st

if "spec_history" not in st.session_state:
    st.session_state["spec_history"] = []
    
if "latest_output" not in st.session_state:
    st.session_state["latest_output"] = None
# Page configuration (runs once)
st.set_page_config(
    page_title="Tasks Generator",
    page_icon="📝",
    layout="wide"
)

# Sidebar navigation
st.sidebar.title("Tasks Generator")
st.sidebar.markdown("Mini planning tool")

page = st.sidebar.radio(
    "Navigate",
    ["Home", "Generate Tasks", "Status"]
)

# Route to pages
if page == "Home":
    from pages.Home import show_home
    show_home()

elif page == "Generate Tasks":
    from pages.Generator import show_generator
    show_generator()

elif page == "Status":
    from pages.Status import show_status
    show_status()


if "spec_history" not in st.session_state:
    st.session_state["spec_history"] = []

