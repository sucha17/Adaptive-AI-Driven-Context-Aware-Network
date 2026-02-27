# Adaptive AI-Driven Context-Aware Network (Roles, Responsibilities & Boundaries)
**New Network Technology (group8) - CP352005 Networks**

## 1. Team Role Assignment Table
สมาชิกทั้ง 4 คน แบ่งหน้าที่ตามความเชี่ยวชาญและแนวคิดหลักที่รับผิดชอบในสถาปัตยกรรมเครือข่าย AI:

| Role | Assigned To | Student ID | Primary Responsibilities |
|------|-------------|------------|--------------------------|
| **Network Architect** | นางสาวพิมพ์ลักษณ์ สกุลเจริญกิจ (พลอย) | 643020630-5 | ออกแบบสถาปัตยกรรมเครือข่าย AI ในภาพรวม (Self-Aware, Self-Adaptive), วางแผนรองรับอุปกรณ์ Edge/Cloud |
| **Network Engineer** | นางสาวทัตพิชา วะสาร (พั้น) | 673380584-2 | พัฒนาโปรโตคอลการหาเส้นทาง (AI Routing), ออกแบบการกระจายทราฟฟิกเพื่อลดคอขวด (AMAIN) |
| **Security & Privacy Specialist** | นางสาวธันยพร เสนาโนฤทธิ์ (แบมบี้) | 673380587-6 | พัฒนาระบบปกปิดข้อมูลผู้ใช้ (Data Anonymization) และออกแบบกฎสำรองเมื่อ AI ทำงานพลาด (Fail-Safe) |
| **DevOps & Simulation Engineer** | นางสาวสุชานาฏ แก้วมุงคุณ (ใบยอ) | 643020651-7 | จำลองสภาพแวดล้อมเครือข่าย, ทดสอบ Use Cases (Campus, Stadium, Emergency) และดูแล CI/CD |

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

เพื่อให้การทำงานร่วมกันเป็นไปอย่างราบรื่นและไม่เกิดความทับซ้อน จึงได้กำหนดขอบเขตความรับผิดชอบของแต่ละตำแหน่งดังนี้:

### Network Architect (พลอย)
* **In Scope:** ออกแบบโครงสร้างเลเยอร์ Context-Aware, กำหนดทิศทางการไหลของข้อมูล, ประเมินและจัดการข้อจำกัดด้านงบประมาณและฮาร์ดแวร์เก่า
* **Out of Scope:** การเขียนโค้ดระบบจำลองสภาพแวดล้อมเครือข่ายและการทดสอบบั๊ก (เป็นหน้าที่ของ ใบยอ)

### Network Engineer (พั้น)
* **In Scope:** เขียนลอจิก AI ในการปรับเส้นทางข้อมูล (Routing), จัดการตารางเส้นทาง, ออกแบบโครงสร้างแพ็กเก็ตข้อมูล
* **Out of Scope:** การเข้ารหัสข้อมูลเพื่อป้องกันความเป็นส่วนตัว หรือการปิดบังตัวตนของผู้ใช้งาน (เป็นหน้าที่ของ แบมบี้)

### Security & Privacy Specialist (แบมบี้)
* **In Scope:** สร้างโมดูล Anonymize ข้อมูลก่อนส่งให้ AI ประมวลผล, กำหนดกฎ Emergency Override เพื่อขัดขวาง AI หากตัดสินใจบล็อกทราฟฟิกฉุกเฉิน
* **Out of Scope:** การกำหนดสถาปัตยกรรมหลักของเครือข่ายในภาพรวม (เป็นหน้าที่ของ พลอย)

### DevOps & Simulation Engineer (ใบยอ)
* **In Scope:** ติดตั้งสภาพแวดล้อมบน GitHub, จัดทำเอกสาร, สร้างเครือข่ายจำลองด้วย Python และรันการทดสอบ 3 สถานการณ์ (Smart Campus, Smart Stadium, Emergency)
* **Out of Scope:** การพัฒนากลไกการทำงานระดับโปรโตคอลหาเส้นทาง (เป็นหน้าที่ของ พั้น)



# Adaptive AI-Driven Context-Aware Network: Roles, Responsibilities & Boundaries Matrix

[cite_start]เอกสารฉบับนี้จัดทำขึ้นเพื่อกำหนดบทบาท หน้าที่ ความรับผิดชอบ และขอบเขตการทำงานของสมาชิกทั้ง 4 คนอย่างชัดเจน เพื่อลดความซ้ำซ้อนและเพิ่มประสิทธิภาพในการทำงานร่วมกันตลอดระยะเวลาการพัฒนาโครงงาน [cite: 309]

## 1. Team Role Assignment Table
[cite_start]ตารางแสดงการแบ่งบทบาทหน้าที่หลัก อำนาจการตัดสินใจ และสายการรายงานของสมาชิกแต่ละคน [cite: 310]

| Role | Assigned To | Primary Responsibilities | Secondary Responsibilities | Decision Authority | Reporting To |
|------|-------------|--------------------------|----------------------------|--------------------|--------------|
| **Architect** | พิมพ์ลักษณ์ สกุลเจริญกิจ (พลอย)<br>643020630-5 | ออกแบบระบบในภาพรวม, กำหนด Interface ของแต่ละ Layer (Context-Aware), วางแผนรองรับอุปกรณ์ Edge/Cloud | จัดทำเอกสารสถาปัตยกรรม (Architecture Docs) | การตัดสินใจสูงสุดเกี่ยวกับสถาปัตยกรรมระบบ และการเปลี่ยนแปลง Interface | อาจารย์ผู้สอน (Instructor) |
| **Network Engineer** | ทัตพิชา วะสาร (พั้น)<br>673380584-2 | พัฒนาโปรโตคอลหลัก (AI Routing, AMAIN), เขียนโค้ดอัลกอริทึมกระจายทราฟฟิก | แก้ไขบั๊ก, สร้างโปรโตไทป์ทางเทคนิค | เลือกเทคโนโลยีและแนวทางการเขียนโค้ด (Tech Stack / Tooling) | Architect |
| **Security & Privacy Specialist** | ธันยพร เสนาโนฤทธิ์ (แบมบี้)<br>673380587-6 | ออกแบบกฎการปกปิดข้อมูล (Data Anonymization), วางระบบ Fail-safe ป้องกัน AI ตัดสินใจพลาด | จำลองสถานการณ์ Edge Cases, จัดทำเอกสารข้อกำหนดด้านความปลอดภัย | การกำหนดลอจิกและนโยบายด้านความปลอดภัยทั้งหมด | Architect |
| **DevOps & Tester** | สุชานาฏ แก้วมุงคุณ (ใบยอ)<br>643020651-7 | ตั้งค่าสภาพแวดล้อม CI/CD, วางแผนการทดสอบ (Test Strategy), สร้างสถานการณ์จำลอง (Use Cases), ตรวจสอบคุณภาพระบบ | ดูแล GitHub Repository, ออกรายงานการทดสอบ (Test Reports) | อนุมัติการนำโค้ดขึ้นระบบหลัก (Release Readiness) และความครอบคลุมของการทดสอบ | Architect / สมาชิกทุกคน |

---

## 2. Evaluation Scores Matrix
[cite_start]ตารางสรุปคะแนนประเมินตนเองและประเมินกลุ่ม (คะแนนเต็ม 10) อ้างอิงจากรายงานสรุป [cite: 302, 303, 306, 307]

| Member Name | Student ID | Self Evaluation Score | Group Evaluation Score (Average) |
|-------------|------------|-----------------------|----------------------------------|
| นางสาวทัตพิชา วะสาร (พั้น) | 673380584-2 | [cite_start]8 [cite: 305] | [cite_start]9.11 [cite: 308] |
| นางสาวธันยพร เสนาโนฤทธิ์ (แบมบี้)| 673380587-6 | [cite_start]9 [cite: 305] | [cite_start]9.44 [cite: 308] |
| นางสาวพิมพ์ลักษณ์ สกุลเจริญกิจ (พลอย)| 643020630-5 | [cite_start]8 [cite: 305] | [cite_start]8.56 [cite: 308] |
| นางสาวสุชานาฏ แก้วมุงคุณ (ใบยอ) | 643020651-7 | [cite_start]9 [cite: 305] | [cite_start]9.44 [cite: 308] |

---

## 3. Boundaries of Responsibility (In-Scope / Out-of-Scope)
[cite_start]ขอบเขตการทำงานที่ชัดเจนของแต่ละบทบาท เพื่อป้องกันการทำงานทับซ้อนกัน [cite: 336, 337]

### [cite_start]Architect's Boundaries (พลอย) [cite: 338]
* [cite_start]**In Scope:** ตัดสินใจเรื่องสถาปัตยกรรมระดับระบบ, กำหนดข้อตกลง (Interface) ของทุกเลเยอร์, เลือกโครงสร้างเทคโนโลยี [cite: 339, 340, 341, 342]
* [cite_start]**Out of Scope:** การเขียนโค้ดแบบบรรทัดต่อบรรทัด, การแก้ไขบั๊กยิบย่อย, การเขียนชุดทดสอบ (Test cases) [cite: 344, 345, 346, 347]

### [cite_start]Engineer's Boundaries (พั้น) [cite: 348]
* [cite_start]**In Scope:** พัฒนาอัลกอริทึมและโค้ดหลักทั้งหมด (AI Routing, Mesh Logic), ปรับปรุงประสิทธิภาพ (Optimization) [cite: 349, 350]
* [cite_start]**Out of Scope:** การตัดสินใจเปลี่ยนสถาปัตยกรรมหลัก, การดูแล CI/CD Pipeline, กำหนดกลยุทธ์การทดสอบระบบ [cite: 351, 352, 354, 355]

### [cite_start]Specialist's Boundaries (แบมบี้) [cite: 356]
* [cite_start]**In Scope:** กำหนดกฎเกณฑ์ความปลอดภัย, วางลอจิก Emergency Override, ค้นคว้าโมเดลความเป็นส่วนตัว, รวบรวมข้อมูล Edge cases [cite: 357, 358, 360, 361]
* [cite_start]**Out of Scope:** พัฒนาโค้ดหาเส้นทางหลัก, ตั้งค่าเซิร์ฟเวอร์, เขียนโค้ดระบบอัตโนมัติ (Test automation) [cite: 363, 364, 365, 366]

### [cite_start]DevOps & Tester's Boundaries (ใบยอ) [cite: 368, 380]
* [cite_start]**In Scope:** ดูแล CI/CD และ Version Control, สร้างสถานการณ์ทดสอบ, ตรวจสอบคุณภาพระบบ (Quality Metrics), ติดตามบั๊ก [cite: 369, 371, 372, 381, 383, 384, 385]
* [cite_start]**Out of Scope:** ออกแบบอัลกอริทึมหาเส้นทาง, พัฒนาโปรโตคอล, กำหนดนโยบายความเป็นส่วนตัวหลัก [cite: 376, 377, 388, 389, 391]

---


## 4. RACI Matrix (Responsible, Accountable, Consulted, Informed)
[cite_start]ตารางแสดงความรับผิดชอบในแต่ละกิจกรรมหลัก [cite: 399]
[cite_start]*(R = ผู้ปฏิบัติงาน, A = ผู้รับผิดชอบผลลัพธ์, C = ผู้ให้คำปรึกษา, I = ผู้รับทราบข้อมูล)* [cite: 402, 403, 404, 405]

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
[cite_start]จุดส่งมอบงานสำคัญที่ต้องมีความชัดเจนระหว่างตำแหน่ง [cite: 394]

| Handoff | From | To | Deliverable | Acceptance Criteria |
|---------|------|----|-------------|---------------------|
| **Architecture → Implementation** | Architect | Engineer | Interface specs & System Logic | เอกสาร Interface ทั้งหมดได้รับการอนุมัติ |
| **Domain Rules → Implementation** | Specialist | Engineer | Privacy logic & Emergency Rules | กำหนดเงื่อนไขที่พร้อมเขียนโค้ดได้อย่างน้อย 5 ข้อ |
| **Code → Testing** | Engineer | Tester | โค้ดที่พร้อมทดสอบ | โค้ดต้องทำงานได้ (Unit tests passing เบื้องต้น) |
| **Integrated System → Delivery** | DevOps | All | โค้ดทั้งหมดพร้อมใช้งาน | ผ่านการทดสอบ Use cases ทั้งหมดครบถ้วน |

---

## 6. Role Boundaries Quick Reference Card
[cite_start]ตารางสรุปแบบกระชับ (Cheat Sheet) เพื่อป้องกันความสับสนในการทำงาน [cite: 407]

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
