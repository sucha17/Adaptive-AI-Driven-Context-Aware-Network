import streamlit as st
import pandas as pd
import time
import random

# --- ตั้งค่าหน้าจอ ---
st.set_page_config(page_title="AI Network & Privacy Dashboard", layout="wide")

st.title("🧠 Adaptive AI Network & Privacy Control Center")
st.markdown("ระบบจำลองเครือข่ายอัจฉริยะพร้อมโหมดปกปิดตัวตน")

# --- 1. Sidebar: เพิ่มปุ่ม Anonymization ---
st.sidebar.header("🛠 การตั้งค่าระบบ")
scenario = st.sidebar.selectbox("เลือกสถานการณ์", ["Smart Campus", "Smart Stadium", "Emergency"])
is_manual = st.sidebar.checkbox("ปิดระบบ AI (Manual Mode)")

st.sidebar.markdown("---")
st.sidebar.header("🔐 Security & Privacy")
# ปุ่ม Toggle สำหรับการปกปิดตัวตน
is_anonymized = st.sidebar.toggle("เปิดโหมดปกปิดตัวตน (Anonymization ON)")

# --- 2. Logic สำหรับการจัดการชื่อผู้ใช้ ---
def process_user_name(name, active):
    if active:
        return "🛡️ Hidden_User_" + str(random.randint(100, 999))
    return name

# รายชื่อผู้ใช้จำลอง
mock_users = ["User_Alice", "User_Bob", "User_Charlie", "User_David", "User_Eve"]

# --- 3. Logic จำลอง AI Network ---
def get_network_status(users, scenario):
    if scenario == "Emergency":
        return "CRITICAL", "🚨 โหมดฉุกเฉิน: ให้ความสำคัญกับกู้ภัย", 1000
    if users > 300:
        return "HIGH LOAD", "🔥 คนหนาแน่น: ขยายช่องสัญญาณอัตโนมัติ", 500
    return "NORMAL", "✅ สถานะปกติ: จัดสรรทรัพยากรแบบประหยัดพลังงาน", 100

# --- 4. ส่วนแสดงผล Real-time ---
if 'data_list' not in st.session_state:
    st.session_state.data_list = []

placeholder = st.empty()

for i in range(100):
    with placeholder.container():
        # สุ่มจำนวนผู้ใช้ตาม Scenario
        current_user_count = random.randint(300, 800) if scenario == "Smart Stadium" else random.randint(20, 150)
        status, msg, bw = get_network_status(current_user_count, scenario)
        
        if is_manual:
            msg = "⚠️ ควบคุมโดยมนุษย์ (AI ถูกระงับ)"

        # --- ส่วน Metrics หลัก ---
        c1, c2, c3 = st.columns(3)
        c1.metric("จำนวนผู้ใช้ทั้งหมด", f"{current_user_count} คน")
        c2.metric("Bandwidth ที่จัดสรร", f"{bw} Mbps")
        c3.metric("สถานะความเป็นส่วนตัว", "🔒 ปกปิด" if is_anonymized else "🔓 เปิดเผย")

        st.info(msg)

        # --- ส่วนตารางผู้ใช้ที่เชื่อมต่อ (Privacy Demo) ---
        st.subheader("👥 ผู้ใช้งานที่กำลังเชื่อมต่อ (Live Access Log)")
        display_users = []
        for u in mock_users:
            display_users.append({
                "User ID": process_user_name(u, is_anonymized),
                "Status": "Connected",
                "IP Address": "192.168.1.xxx" if is_anonymized else f"192.168.1.{random.randint(10,99)}"
            })
        st.table(pd.DataFrame(display_users))

        # --- ส่วนกราฟประวัติ ---
        st.session_state.data_list.append({"Time": i, "Users": current_user_count, "Bandwidth": bw})
        history_df = pd.DataFrame(st.session_state.data_list)
        
        if not history_df.empty:
            st.subheader("📈 กราฟการปรับตัวของเครือข่าย")
            st.line_chart(history_df.set_index("Time"))
        
        time.sleep(1)