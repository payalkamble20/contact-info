import requests
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Contact App Project", 
    page_icon="📞:"
    )


st.title("Contact App Project")
st.write("This is a simple contact app project built with Streamlit. It allows users to view and manage their contacts.")
if st.button("fetch Contacts"):
    print("Button clicked!")
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    users = response.json()

    users_data=[]
    for user in users:
        users_data.append({
            "id": user["id"],
            "name": user["name"],
            "email": user["email"],
            "website": user["website"]
        })

    df = pd.DataFrame(users_data)
    st.subheader("Contacts Information")
    st.dataframe(df)