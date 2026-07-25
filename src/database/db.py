from src.database.config import supabase
import streamlit as st
import bcrypt

def check_pass(pwd, hash_pwd) :
    return bcrypt.checkpw(pwd.encode(), hash_pwd.encode())

def hash_password(password) :
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def login_teacher(username, password) :
    if not username or not password :
        return False, 'Some fields are not filled!'
    try :
        teacher = teacher_login(username, password)
        if teacher :
            st.session_state.teacher_data = {
                "id" : teacher['teacher_id'],
                "username" : teacher['username'],
                "name" : teacher['name'],
            }
            st.session_state.user_role = 'teacher'
            st.session_state.is_logged_in = True
            return True, "Welcome back!"
    except Exception as e :
        return False, e
    

def register_teacher(teacher_name, teacher_username, teacher_password) :
    if not teacher_username or not teacher_password or not teacher_name :
        return False, 'Some fields are not filled!'

    if check_teacher_exists(teacher_username) :
        return False, 'User name already taken!'
    try :
        create_teacher(teacher_name, teacher_username, teacher_password)
        return True, 'Successfully created! '
    except Exception as e :
        return False, e

def check_teacher_exists(username) :
    response = supabase.table("teachers").select("username").eq("username", username).execute()
    return len(response.data) > 0

def create_teacher(name, username, password) :
    data = {
        "username" : username,
        "password" : hash_password(password),
        "name" : name
    }
    response = supabase.table("teachers").insert(data).execute()
    return response.data

def teacher_login(username, password) :
    response = supabase.table("teachers").select("*").eq("username", username).execute()
    if response.data :
        teacher = response.data[0]
        if check_pass(password, teacher['password']) :
            return teacher
        return None
    
def get_all_students() :
    response = supabase.table("students").select("*").execute()
    return response.data