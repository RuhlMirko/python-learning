import streamlit as st
import functions

todo_list = functions.get_todo_list()

def add_todo():

    todo_local = st.session_state['new_todo']

    todo_list.append(todo_local + '\n')
    functions.set_todo_list(todo_list)

    st.session_state['new_todo'] = ""  # Clears the text input


st.title("My todo app")
st.subheader("This is my web todo app")
st.write("This app is to increase your productivity")



for todo in todo_list:
    st.checkbox(todo.strip('\n'))

st.text_input(label="New Todo:", placeholder="Add new todo", on_change=add_todo, key='new_todo')

st.session_state
