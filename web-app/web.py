import streamlit as st
import functions

st.title("My todo app")
st.subheader("This is my web todo app")
st.write("This app is to increase your productivity")


todo_list = functions.get_todo_list()
for todo in todo_list:
    st.checkbox(todo.strip('\n'))

st.text_input(label="", placeholder="Add new todo")

