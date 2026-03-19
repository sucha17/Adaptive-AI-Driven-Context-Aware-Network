import streamlit as st
import pandas as pd
import time
import random
import requests  # เพิ่มสำหรับส่ง API
from requests.auth import HTTPBasicAuth

# --- ส่วนที่เพิ่ม: REST API Connector สำหรับ SDN Controller ---
def send_to_sdn_controller(bw_value, scenario_name):
    """
    ฟังก์ชันส่งค่า Bandwidth ไปยัง OpenDaylight หรือ SDN Controller อื่นๆ
    """
    # URL ตัวอย่างสำหรับ RESTCONF ของ OpenDaylight
    odl_url = "http://192.168.1.100:8181/restconf/config/network-topology:network-topology/topology/flow:1"
    
    payload = {
        "input": {
            "node": "openflow:1",
            "bandwidth-limit": bw_value,
            "context": scenario_name
        }
    }
    
    try:
        # ในการพรีเซนต์จริง เราจะใช้ timeout สั้นๆ เพื่อไม่ให้หน้าเว็บค้างถ้า Controller offline
        # response = requests.put(odl_url, json=payload, auth=HTTPBasicAuth('admin', 'admin'), timeout=0.5)
        # return response.status_code
        return 200  # คืนค่า 200 เพื่อจำลองว่าส่งสำเร็จ (Simulated Success)
    except:
        return 500

# --- ตั้งค่าหน้าจอ ---
st.set_page_config(page_title="AI Network & Privacy Dashboard", layout="wide")

st.title("🧠 Adaptive AI Network & Privacy Control Center")
st.markdown("ระบบจำลองเครือข่ายอัจฉริยะพร้อมการวิเคราะห์บริบทแบบ Real-time (SDN Ready)")

# --- 1. Sidebar: การตั้งค่าระบบ ---
st.sidebar.header("🛠 การตั้งค่าระบบ")
scenario = st.sidebar.selectbox("เลือกสถานการณ์ (Scenario)", ["Smart Campus", "Smart Stadium", "Emergency"])
is_manual = st.sidebar.checkbox("ปิดระบบ AI (Manual Mode)")

st.sidebar.markdown("---")
st.sidebar.header("🔐 Security & Privacy")
is_anonymized = st.sidebar.toggle("เปิดโหมดปกปิดตัวตน (Anonymization ON)")

# แสดงสถานะ API ใน Sidebar
st.sidebar.markdown("---")
st.sidebar.header("📡 SDN API Status")
api_placeholder = st.sidebar.empty()

# --- 2. Logic สำหรับการปกปิดตัวตน (Privacy) ---
def process_user_name(name, active):
    if active:
        return "🛡️ Hidden_User_" + str(random.randint(100, 999))
    return name

mock_users = ["User_Alice", "User_Bob", "User_Charlie", "User_David", "User_Eve"]

# --- 3. Improved Adaptive AI Logic (Context-Aware Optimization) ---
def calculate_ai_decision(users, scenario):
    if scenario == "Emergency":
        priority_weight = 2.5
        capacity_threshold = 200
    elif scenario == "Smart Stadium":
        priority_weight = 1.2
        capacity_threshold = 1000
    else: # Smart Campus
        priority_weight = 1.0
        capacity_threshold = 500

    load_ratio = users / capacity_threshold
    base_bw = 150 
    allocated_bw = int(base_bw * load_ratio * priority_weight)
    allocated_bw = max(100, min(allocated_bw, 1500))

    if scenario == "Emergency":
        status = "🚨 CRITICAL"
        reason = f"AI มอบลำดับความสำคัญสูงสุดให้กู้ภัย จัดสรร Bandwidth {allocated_bw} Mbps"
    elif load_ratio > 0.85:
        status = "🔥 HIGH LOAD"
        reason = f"AI ตรวจพบความหนาแน่น {int(load_ratio*100)}% จึงขยายช่องสัญญาณเพื่อลด Latency"
    else:
        status = "✅ OPTIMIZED"
        reason = "AI อยู่ในโหมดประหยัดพลังงาน จัดสรรทรัพยากรตามปริมาณการใช้งานจริง"
        
    return status, reason, allocated_bw

# --- 4. การแสดงผลแบบ Real-time ---
if 'data_list' not in st.session_state:
    st.session_state.data_list = []

placeholder = st.empty()

for i in range(100):
    with placeholder.container():
        if scenario == "Smart Stadium":
            current_user_count = random.randint(400, 1200)
        elif scenario == "Emergency":
            current_user_count = random.randint(50, 150)
        else:
            current_user_count = random.randint(20, 450)

        status, ai_reason, bw = calculate_ai_decision(current_user_count, scenario)
        
        # --- เรียกใช้งาน SDN API Connector ---
        if not is_manual:
            api_res = send_to_sdn_controller(bw, scenario)
            if api_res == 200:
                api_placeholder.success(f"API Sent: {bw}Mbps")
            else:
                api_placeholder.error("API Connection Failed")
        else:
            ai_reason = "⚠️ Manual Override: ระบบ AI ถูกปิดการทำงานโดยผู้ดูแล"
            api_placeholder.warning("API Paused (Manual)")

        # --- ส่วนแสดง Metrics ---
        c1, c2, c3 = st.columns(3)
        c1.metric("จำนวนผู้ใช้ขณะนี้", f"{current_user_count} User")
        c2.metric("Bandwidth ที่จัดสรร", f"{bw} Mbps", delta=f"{status}")
        c3.metric("Privacy Mode", "🔒 Protected" if is_anonymized else "🔓 Public")

        st.info(f"**AI Reasoning:** {ai_reason}")

        # --- ส่วนตาราง Live Logs (Ethics/Privacy) ---
        st.subheader("👥 Live Network Access Logs")
        display_users = []
        for u in mock_users:
            display_users.append({
                "User ID": process_user_name(u, is_anonymized),
                "Access Status": "Active",
                "IP (Pseudo)": "10.0.0.XXX" if is_anonymized else f"10.0.0.{random.randint(2,254)}"
            })
        st.table(pd.DataFrame(display_users))

        # --- ส่วนกราฟประวัติ ---
        st.session_state.data_list.append({"Time": i, "Users": current_user_count, "Bandwidth": bw})
        history_df = pd.DataFrame(st.session_state.data_list).tail(20)
        
        st.subheader("📈 Network Adaptation Analytics")
        st.line_chart(history_df.set_index("Time"))
        
        time.sleep(1)
        st.write("---") # ขีดเส้นคั่นเพื่อให้ดูเป็นระเบียบ
        st.write("📌 Current Version: 2.0 (API Ready)")
