import streamlit as st

# Function for the chatbot
def chatbot():
    st.subheader("Chatbot")
    user_input = st.text_input("You: ")
    
    # Simple responses for demonstration purposes
    if user_input:
        st.text("Bot: Thanks for your input! If you have any questions about uploading invoices or receipts, feel free to ask.")

# Main function
def main():

    st.set_page_config(page_title="Factura IA")

    # Sidebar with navigation
    menu = ["Upload", "Chatbot"]
    choice = st.sidebar.selectbox("Navigation", menu)

    if choice == "Upload":
        st.title("IT RISK = IT CONTROLS FAILURE")
        st.caption("🚀 powered by Streamlit using LLM")

        st.subheader("IT RISKs = IT Controls Failures.")
        st.info(
            "Use this page to perform agile controls testing ")
    elif choice == "Chatbot":
        chatbot()

if __name__ == "__main__":
    main()
