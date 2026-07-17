import streamlit as st
import hashlib
import json
import os
from datetime import datetime, timedelta

USERS_FILE = "users.json"

def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r") as f:
            return json.load(f)
    # Usuario por defecto
    default = {
        "admin": {
            "password": hashlib.sha256("admin123".encode()).hexdigest(),
            "role": "admin",
            "email": "admin@example.com"
        }
    }
    save_users(default)
    return default

def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=2)

def authenticate(username, password):
    users = load_users()
    if username in users:
        hashed = hashlib.sha256(password.encode()).hexdigest()
        if users[username]["password"] == hashed:
            return users[username]["role"]
    return None

def login():
    st.sidebar.markdown("## 🔐 Iniciar sesión")
    username = st.sidebar.text_input("Usuario")
    password = st.sidebar.text_input("Contraseña", type="password")
    if st.sidebar.button("Entrar"):
        role = authenticate(username, password)
        if role:
            st.session_state["logged_in"] = True
            st.session_state["username"] = username
            st.session_state["role"] = role
            st.rerun()
        else:
            st.sidebar.error("Credenciales incorrectas")

def logout():
    for key in ["logged_in", "username", "role"]:
        if key in st.session_state:
            del st.session_state[key]
    st.rerun()

def is_admin():
    return st.session_state.get("role") == "admin"

def admin_panel():
    if not is_admin():
        st.warning("Acceso restringido a administradores")
        return
    st.subheader("👥 Panel de administración de usuarios")
    users = load_users()
    with st.form("user_form"):
        new_user = st.text_input("Nuevo usuario")
        new_pass = st.text_input("Contraseña", type="password")
        role = st.selectbox("Rol", ["admin", "viewer"])
        if st.form_submit_button("Crear usuario"):
            if new_user and new_pass:
                users[new_user] = {
                    "password": hashlib.sha256(new_pass.encode()).hexdigest(),
                    "role": role,
                    "email": ""
                }
                save_users(users)
                st.success(f"Usuario {new_user} creado")
                st.rerun()
    st.subheader("Usuarios existentes")
    for u, data in users.items():
        cols = st.columns([2,1,1])
        cols[0].write(f"**{u}** ({data['role']})")
        if cols[1].button("Eliminar", key=f"del_{u}"):
            if u != "admin":  # prevenir borrar admin
                del users[u]
                save_users(users)
                st.rerun()
            else:
                st.warning("No se puede eliminar al admin principal")
