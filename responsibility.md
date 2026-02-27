# Adaptive AI-Driven Context-Aware Network (Roles, Responsibilities & Boundaries Matrix)
**New Network Technology (group8) - CP352005 Networks**

จัดทำขึ้นเพื่อกำหนดบทบาท หน้าที่ ความรับผิดชอบ และขอบเขตการทำงานของสมาชิกทั้ง 4 คนอย่างชัดเจน เพื่อลดความซ้ำซ้อนและเพิ่มประสิทธิภาพในการทำงานร่วมกันตลอดระยะเวลาการพัฒนาโครงงาน

## 1. Team Role Assignment Table
ตารางแสดงการแบ่งบทบาทหน้าที่หลัก อำนาจการตัดสินใจ และสายการรายงานของสมาชิกแต่ละคน 

| Role | Assigned To | Primary Responsibilities | Secondary Responsibilities | Decision Authority | Reporting To |
|------|-------------|--------------------------|----------------------------|--------------------|--------------|
| **Architect** | พิมพ์ลักษณ์ สกุลเจริญกิจ (พลอย)<br>643020630-5 | ออกแบบระบบในภาพรวม, กำหนด Interface ของแต่ละ Layer (Context-Aware), วางแผนรองรับอุปกรณ์ Edge/Cloud | จัดทำเอกสารสถาปัตยกรรม (Architecture Docs) | การตัดสินใจสูงสุดเกี่ยวกับสถาปัตยกรรมระบบ และการเปลี่ยนแปลง Interface | อาจารย์ผู้สอน (Instructor) |
| **Network Engineer** | ทัตพิชา วะสาร (พั้น)<br>673380584-2 | พัฒนาโปรโตคอลหลัก (AI Routing, AMAIN), เขียนโค้ดอัลกอริทึมกระจายทราฟฟิก | แก้ไขบั๊ก, สร้างโปรโตไทป์ทางเทคนิค | เลือกเทคโนโลยีและแนวทางการเขียนโค้ด (Tech Stack / Tooling) | Architect |
| **Security & Privacy Specialist** | ธันยพร เสนาโนฤทธิ์ (แบมบี้)<br>673380587-6 | ออกแบบกฎการปกปิดข้อมูล (Data Anonymization), วางระบบ Fail-safe ป้องกัน AI ตัดสินใจพลาด | จำลองสถานการณ์ Edge Cases, จัดทำเอกสารข้อกำหนดด้านความปลอดภัย | การกำหนดลอจิกและนโยบายด้านความปลอดภัยทั้งหมด | Architect |
| **DevOps & Tester** | สุชานาฏ แก้วมุงคุณ (ใบยอ)<br>643020651-7 | ตั้งค่าสภาพแวดล้อม CI/CD, วางแผนการทดสอบ (Test Strategy), สร้างสถานการณ์จำลอง (Use Cases), ตรวจสอบคุณภาพระบบ | ดูแล GitHub Repository, ออกรายงานการทดสอบ (Test Reports) | อนุมัติการนำโค้ดขึ้นระบบหลัก (Release Readiness) และความครอบคลุมของการทดสอบ | Architect / สมาชิกทุกคน |

---


## 2. Evaluation Scores Matrix
สรุปผลการประเมินตนเอง และประเมินการทำงานร่วมกันโดยสมาชิกในกลุ่ม (คะแนนเต็ม 10) สำหรับการวัดผลในทีม:

| Member Name | Self Evaluation Score | Group Evaluation Score (Average) |
|-------------|-----------------------|------------------------|
| นางสาวพิมพ์ลักษณ์ สกุลเจริญกิจ (พลอย) | 8 | 8 |
| นางสาวทัตพิชา วะสาร (พั้น) | 8 | 8 |
| นางสาวธันยพร เสนาโนฤทธิ์ (แบมบี้) | 9 | 9 |
| นางสาวสุชานาฏ แก้วมุงคุณ (ใบยอ) | 9 | 9 |

*(หมายเหตุ: อ้างอิงคะแนนจากการประเมินในเอกสารรายงานกลุ่มที่ 8)*


---

## 3. Boundaries of Responsibility (In-Scope / Out-of-Scope)
ขอบเขตการทำงานที่ชัดเจนของแต่ละบทบาท เพื่อป้องกันการทำงานทับซ้อนกัน

### Architect's Boundaries (พลอย)
* **In Scope:** ตัดสินใจเรื่องสถาปัตยกรรมระดับระบบ, กำหนดข้อตกลง (Interface) ของทุกเลเยอร์, เลือกโครงสร้างเทคโนโลยี
* **Out of Scope:** การเขียนโค้ดแบบบรรทัดต่อบรรทัด, การแก้ไขบั๊กยิบย่อย, การเขียนชุดทดสอบ (Test cases)

### Engineer's Boundaries (พั้น)
* **In Scope:** พัฒนาอัลกอริทึมและโค้ดหลักทั้งหมด (AI Routing, Mesh Logic), ปรับปรุงประสิทธิภาพ (Optimization)
* **Out of Scope:** การตัดสินใจเปลี่ยนสถาปัตยกรรมหลัก, การดูแล CI/CD Pipeline, กำหนดกลยุทธ์การทดสอบระบบ

### Specialist's Boundaries (แบมบี้)
* **In Scope:** กำหนดกฎเกณฑ์ความปลอดภัย, วางลอจิก Emergency Override, ค้นคว้าโมเดลความเป็นส่วนตัว, รวบรวมข้อมูล Edge cases
* **Out of Scope:** พัฒนาโค้ดหาเส้นทางหลัก, ตั้งค่าเซิร์ฟเวอร์, เขียนโค้ดระบบอัตโนมัติ (Test automation)

### DevOps & Tester's Boundaries (ใบยอ)
* **In Scope:** ดูแล CI/CD และ Version Control, สร้างสถานการณ์ทดสอบ, ตรวจสอบคุณภาพระบบ (Quality Metrics), ติดตามบั๊ก
* **Out of Scope:** ออกแบบอัลกอริทึมหาเส้นทาง, พัฒนาโปรโตคอล, กำหนดนโยบายความเป็นส่วนตัวหลัก

---


## 4. RACI Matrix (Responsible, Accountable, Consulted, Informed)
ตารางแสดงความรับผิดชอบในแต่ละกิจกรรมหลัก
*(R = ผู้ปฏิบัติงาน, A = ผู้รับผิดชอบผลลัพธ์, C = ผู้ให้คำปรึกษา, I = ผู้รับทราบข้อมูล)*

| Activity | Architect (พลอย) | Engineer (พั้น) | Specialist (แบมบี้) | DevOps & Tester (ใบยอ) |
|----------|------------------|-----------------|---------------------|------------------------|
| Architecture Definition | R/A | C | C | I |
| Protocol / Core Coding | I | R/A | C | C |
| Privacy & Fail-Safe Rules | C | C | R/A | C |
| Environment & CI/CD Setup| I | C | I | R/A |
| Unit & Integration Testing| C | C | C | R/A |
| Documentation | R/A | C | C | C |

---

## 5. Critical Handoff Points
จุดส่งมอบงานสำคัญที่ต้องมีความชัดเจนระหว่างตำแหน่ง

| Handoff | From | To | Deliverable | Acceptance Criteria |
|---------|------|----|-------------|---------------------|
| **Architecture → Implementation** | Architect | Engineer | Interface specs & System Logic | เอกสาร Interface ทั้งหมดได้รับการอนุมัติ |
| **Domain Rules → Implementation** | Specialist | Engineer | Privacy logic & Emergency Rules | กำหนดเงื่อนไขที่พร้อมเขียนโค้ดได้อย่างน้อย 5 ข้อ |
| **Code → Testing** | Engineer | Tester | โค้ดที่พร้อมทดสอบ | โค้ดต้องทำงานได้ (Unit tests passing เบื้องต้น) |
| **Integrated System → Delivery** | DevOps | All | โค้ดทั้งหมดพร้อมใช้งาน | ผ่านการทดสอบ Use cases ทั้งหมดครบถ้วน |

---

## 6. Role Boundaries Quick Reference Card
ตารางสรุปแบบกระชับ (Cheat Sheet) เพื่อป้องกันความสับสนในการทำงาน


```text
┌─────────────────────────────────────────────────────────────┐
│                 TEAM BOUNDARIES CHEAT SHEET                 │
├─────────────┬───────────────────────┬───────────────────────┤
│ ROLE        │ PRIMARY ZONE          │ STAY OUT OF           │
├─────────────┼───────────────────────┼───────────────────────┤
│ ARCHITECT   │ Design, Interfaces    │ Line-by-line coding   │
├─────────────┼───────────────────────┼───────────────────────┤
│ ENGINEER    │ Core Implementation   │ Architecture decisions│
├─────────────┼───────────────────────┼───────────────────────┤
│ SPECIALIST  │ Security, Domain rules│ Core routing coding   │
├─────────────┼───────────────────────┼───────────────────────┤
│ DEVOPS/TEST │ CI/CD, QA, Validation │ Algorithm design      │
└─────────────┴───────────────────────┴───────────────────────┘
