import pytest
# ดึงฟังก์ชันมาจากไฟล์ main.py
from main import process_user_name, calculate_ai_decision

# ==========================================
# 1. Tests for Privacy Logic (process_user_name)
# ==========================================
def test_process_user_name_privacy_on():
    original_name = "User_Alice"
    result = process_user_name(original_name, True)
    assert result.startswith("🛡️ Hidden_User_")
    assert original_name not in result

def test_process_user_name_privacy_off():
    original_name = "User_Alice"
    result = process_user_name(original_name, False)
    assert result == original_name

# ==========================================
# 2. Tests for AI Logic (calculate_ai_decision)
# ==========================================
def test_calculate_ai_decision_min_bandwidth():
    status, reason, bw = calculate_ai_decision(1, "Smart Campus")
    assert bw == 100
    assert status == "✅ OPTIMIZED"

def test_calculate_ai_decision_max_bandwidth():
    status, reason, bw = calculate_ai_decision(10000, "Smart Stadium")
    assert bw == 1500

def test_calculate_ai_decision_emergency():
    status, reason, bw = calculate_ai_decision(50, "Emergency")
    assert status == "🚨 CRITICAL"
    assert "กู้ภัย" in reason

def test_calculate_ai_decision_high_load():
    status, reason, bw = calculate_ai_decision(450, "Smart Campus")
    assert status == "🔥 HIGH LOAD"
    assert "90%" in reason

def test_calculate_ai_decision_optimized():
    status, reason, bw = calculate_ai_decision(200, "Smart Campus")
    assert status == "✅ OPTIMIZED"
    assert "ประหยัดพลังงาน" in reason