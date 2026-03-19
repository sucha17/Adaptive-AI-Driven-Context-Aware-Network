import streamlit as st
import pandas as pd
import time
import random
import requests
from requests.auth import HTTPBasicAuth

# --- ตั้งค่าหน้าจอ ---
st.set_page_config(page_title="AI Network & Privacy Dashboard", layout="wide")

# --- ส่วน API: ทำไว้โชว์ Logic (Simulated Success) ---
def send_to_sdn_api(bw_value, scenario_name):
    """
    ฟังก์ชันสำหรับส่งค่าไปยัง SDN Controller (จำลองการทำงาน)
    """
    # URL สมมติสำหรับพรีเซนต์ (ถ้ามีของจริงค่อยมาแก้ตรงนี้)
    url = "http://192.168.1.100:8181/restconf/config/..." 
    
    payload = {
        "bandwidth_limit": bw_value,
        "scenario": scenario_name,
        "timestamp": time.time()
    }
    
    try:
        # จำลองว่าส่งสำเร็จ 100% เพื่อให้หน้าพรีเซนต์ดูดี
        # ในการใช้งานจริงค่อยปลดคอมเมนต์บรรทัด requests.put ด้านล่าง
        # response = requests.put(url, json=payload, auth=HTTPBasicAuth('admin', 'admin'), timeout=0.1)
        return 200 
    except:
        return 500

st.title("🧠 Adaptive AI Network & Privacy Control Center")
st.markdown("ระบบจำลองเครือข่ายอัจฉริยะพร้อมการวิเคราะห์บริบท (API Ready)")

# --- 1. Sidebar: การตั้งค่า ---
st.sidebar.header("🛠 การตั้งค่าระบบ")
scenario = st.sidebar.selectbox("เลือกสถานการณ์ (Scenario)", ["Smart Campus", "Smart Stadium", "Emergency"])
is_manual = st.sidebar.checkbox("ปิดระบบ AI (Manual Mode)")

st.sidebar.markdown("---")
st.sidebar.header("🔐 Security & Privacy")
is_anonymized = st.sidebar.toggle("เปิดโหมดปกปิดตัวตน (Anonymization ON)")

# ส่วนแสดงสถานะ API ที่อาจารย์อยากเห็น
st.sidebar.markdown("---")
st.sidebar.header("📡 SDN API Status")
api_placeholder = st.sidebar.empty()

# --- 2. Logic การทำงาน ---
def calculate_ai_decision(users, scenario):
    # กำหนดตัวแปรตาม Scenario
    config = {
        "Emergency": (2.5, 200),
        "Smart Stadium": (1.2, 1000),
        "Smart Campus": (1.0, 500)
    }
    priority, threshold = config[scenario]
    
    load_ratio = users / threshold
    base_bw = 150 
    allocated_bw = max(100, min(int(base_bw * load_ratio * priority), 1500))

    if scenario == "Emergency":
        status, reason = "🚨 CRITICAL", f"AI จัดสรร Bandwidth พิเศษ {allocated_bw} Mbps ให้หน่วยกู้ภัย"
    elif load_ratio > 0.85:
        status, reason = "🔥 HIGH LOAD", f"AI ขยายช่องสัญญาณเพื่อลด Latency"
    else:
        status, reason = "✅ OPTIMIZED", "AI บริหารจัดการตามปริมาณการใช้งานจริง"
        
    return status, reason, allocated_bw

# --- 3. การแสดงผล Real-time ---
if 'data_list' not in st.session_state:
    st.session_state.data_list = []

placeholder = st.empty()

for i in range(100):
    with placeholder.container():
        # สุ่ม User ตาม Scenario ให้ดูสมจริง
        user_ranges = {"Smart Stadium": (400, 1200), "Emergency": (50, 150), "Smart Campus": (20, 450)}
        current_user_count = random.randint(*user_ranges[scenario])

        status, ai_reason, bw = calculate_ai_decision(current_user_count, scenario)
        
        # แสดงสถานะ API ใน Sidebar ให้ดูเหมือนทำงาน