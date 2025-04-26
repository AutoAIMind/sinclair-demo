import streamlit as st

# Streamlit app for demonstrating AI agent demos

st.set_page_config(page_title="Sinclair AI Agent Demos", layout="centered")

st.title("Sinclair AI Agent Demos")

# Sidebar to choose demo
demo = st.sidebar.selectbox(
    "Choose a Demo",
    (
        "Appointment Scheduler Bot",
        "Review Request Bot",
        "Lead Capture Bot",
        "Missed Call Text-Back Bot",
        "Social Media Auto-Post Bot",
        "Web Chat Widget"
    )
)

if demo == "Appointment Scheduler Bot":
    st.header("📅 Appointment Scheduler Bot")
    st.write("Simulate a customer booking themselves automatically.")
    name = st.text_input("Your Name")
    date = st.date_input("Select Appointment Date")
    time_slot = st.time_input("Select Appointment Time")
    if st.button("Book Appointment"):
        st.success(f"✅ Appointment booked for {name} on {date} at {time_slot}!")
        st.write("A confirmation has been sent to your email and phone.")

elif demo == "Review Request Bot":
    st.header("⭐ Review Request Bot")
    st.write("Simulate sending an automatic review request after a service.")
    customer_name = st.text_input("Customer Name")
    service_date = st.date_input("Service Completed Date")
    contact_method = st.selectbox("Contact Method", ("Email", "SMS"))
    if st.button("Send Review Request"):
        st.success(f"✅ Review request sent to {customer_name} via {contact_method}.")
        st.write(
            f"“Thank you {customer_name} for your visit on {service_date}! "
            "If you enjoyed our service, please leave us a 5-star review!”"
        )

elif demo == "Lead Capture Bot":
    st.header("🧲 Lead Capture Bot")
    st.write("Simulate capturing visitor info via a pop-up form.")
    visitor_name = st.text_input("Visitor Name")
    visitor_email = st.text_input("Visitor Email")
    if st.button("Capture Lead"):
        st.success(f"✅ Captured lead: {visitor_name} ({visitor_email}).")
        st.write("Lead has been sent to your inbox or CRM.")

elif demo == "Missed Call Text-Back Bot":
    st.header("📱 Missed Call Text-Back Bot")
    st.write("Simulate sending an automated text when a call is missed.")
    caller_number = st.text_input("Caller Phone Number")
    if st.button("Send Text-Back"):
        st.success(f"✅ Sent automated text to {caller_number}.")
        st.write(
            "“Sorry we missed your call! Reply to this message to book an appointment now.”"
        )

elif demo == "Social Media Auto-Post Bot":
    st.header("📣 Social Media Auto-Post Bot")
    st.write("Simulate scheduling a social media post.")
    post_content = st.text_area("Post Content")
    post_date = st.date_input("Schedule Date")
    post_platform = st.selectbox("Platform", ("Facebook", "Instagram"))
    if st.button("Schedule Post"):
        st.success(f"✅ Scheduled post to {post_platform} on {post_date}.")
        st.write(f"Content: {post_content}")

elif demo == "Web Chat Widget":
    st.header("💬 Web Chat Widget")
    st.write("Simulate a visitor chatting with your AI chat widget.")
    user_message = st.text_input("Visitor Message")
    if st.button("Send Message"):
        st.success("✅ Bot Response: “Hello! How can I help you today?”")
        st.write(
            "This chat widget can book appointments or collect leads in real time."
        )

st.markdown("---")
st.markdown("""
**Instructions:**
1. Install Streamlit: `pip install streamlit`
2. Run the demo: `streamlit run demo_app.py`
3. Use the sidebar to switch between demos and interact with each simulation.
""")
