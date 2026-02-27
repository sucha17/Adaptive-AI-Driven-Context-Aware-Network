# Adaptive AI-Driven Context-Aware Network (sprint plan)
**New Network Technology (group8) - CP352005 Networks**

### Week 1: Foundation Sprint (Days 1-5)
**Theme:** Architecture, Setup, and Component Design

#### Day 1: Kickoff & Environment Setup
| Time | Activity | Lead | Participants |
|------|----------|------|--------------|
| 9:00-10:00 | Sprint Planning | DevOps (ใบยอ) | All |
| 10:00-12:00 | Environment Setup | DevOps (ใบยอ) | All |
| 13:00-15:00 | Architecture Review | Architect (พลอย) | All |
| 15:00-17:00 | Role-specific tasks | Each | Individual |

**Deliverables:**
- [x] GitHub repository created (DevOps)
- [x] Development environment documented (DevOps)
- [x] Requirements installed (All)
- [x] Initial architecture diagram including Edge/Cloud integration (Architect)

**Role Tasks:**
| Role | Tasks |
|------|-------|
| Architect (พลอย) | กำหนด Interface ของแต่ละ Layer และออกแบบสถาปัตยกรรมรองรับอุปกรณ์เก่า |
| Engineer (พั้น) | ศึกษา NetworkX และทดลองสร้างกราฟเครือข่ายพื้นฐาน |
| Specialist (แบมบี้) | ค้นคว้ามาตรฐาน Data Privacy และร่างกฎการตั้งค่า AI สำรอง 5 ข้อ |
| DevOps (ใบยอ) | ตั้งค่า CI/CD (GitHub Actions) และสร้าง Project board |
| Tester/QA (ใบยอ) | สร้างเทมเพลตแผนการทดสอบ และกำหนดหมวดหมู่ Use Cases |

#### Day 2: Context Data & Edge Layer Design
**Focus:** Context-Aware format specification and link simulation

**Pair Programming:**
- Architect + Engineer: ออกแบบรูปแบบการระบุตัวตนและบริบทของผู้ใช้ (ContextNode Address)
- Specialist + Tester: จัดทำเอกสารกฎการปกปิดข้อมูล (Anonymization)

**Deliverables:**
- [ ] Context Address format specification (Architect)
- [ ] บริบท Resolution algorithm (Engineer)
- [ ] Link simulation prototype (Engineer)
- [ ] Privacy & Fail-Safe rule v0.1 (Specialist)
- [ ] Test cases สำหรับรูปแบบบริบท (Tester)

#### Day 3: AI Routing Protocol Design
**Focus:** AI Multi-metric Routing algorithm design (ลดปัญหาคอขวด)

**Deliverables:**
- [ ] AI Routing algorithm pseudo-code (Engineer)
- [ ] Cost function definition (พิจารณาจากแบนด์วิดท์, ความหน่วง, ประเภทแอป) (Architect + Specialist)
- [ ] Routing table structure (Engineer)
- [ ] Test cases for routing (Tester)

**Key Decision:** กำหนดค่าน้ำหนัก (Weighting factors) ให้ AI ใช้ประมวลผลการหาเส้นทาง

#### Day 4: Fail-Safe & Privacy Prevention Design
**Focus:** Rule engine สำหรับขัดขวาง AI กรณีฉุกเฉิน และเข้ารหัสข้อมูล

**Deliverables:**
- [ ] Complete Fail-Safe & Privacy rule set (Specialist)
- [ ] Rule engine design (Emergency Override) (Engineer)
- [ ] Validation interface สำหรับกรองข้อมูลส่วนตัว (Architect)
- [ ] Test cases สำหรับสถานการณ์ฉุกเฉิน (Tester)

#### Day 5: Week 1 Review & Integration
**Activities:**
- 14:00-15:00: Code review session
- 15:00-16:00: Integration testing (ทดสอบการทำงานเบื้องต้น)
- 16:00-17:00: Sprint review & Week 2 planning

**Week 1 Success Criteria:**
- [ ] All specifications documented
- [ ] Development environment working for all
- [ ] Basic simulation framework created
- [ ] Test framework established
- [ ] CI passing on main branch

---

### Week 2: Implementation Sprint (Days 6-10)
**Theme:** Core Protocol Implementation

#### Day 6-7: Context Setup & Edge Layer Implementation
**Lead:** Engineer (พั้น)  
**Support:** Architect (code review), Tester (test cases)

**Tasks:**
1. เขียนคลาส `ContextNodeAddress` เพื่อแยกแยะผู้ใช้/แอป/ตำแหน่ง
2. สร้างโมดูลวิเคราะห์และคัดกรองข้อมูลก่อนส่งให้ AI (ลดภาระทรัพยากร)
3. สร้างลิงก์เครือข่ายจำลองพร้อมค่าหน่วงเวลา (Latency metrics)
4. เขียน Unit tests (minimum 80% coverage)

**Definition of Done:**
- [ ] สร้างและตรวจสอบข้อมูลบริบทได้สำเร็จ
- [ ] โหนดส่งผ่านข้อมูลพร้อมบริบทได้ถูกต้อง
- [ ] ลิงก์จำลองคำนวณความหน่วงเครือข่ายได้
- [ ] All tests passing

#### Day 8-9: AI Routing Implementation
**Lead:** Engineer (พั้น)  
**Support:** Specialist (routing metrics), Tester (test scenarios)

**Tasks:**
1. Implement ระบบตาราง Routing แบบปรับแต่งอัตโนมัติ
2. โค้ดอัลกอริทึม Modified Dijkstra ที่ใช้ AI ประเมินค่าน้ำหนัก
3. สร้างระบบ Load balancing กระจายทราฟฟิกเมื่อคนหนาแน่น
4. เพิ่มกลไกการจำเส้นทาง (Route caching) เพื่อประหยัดทรัพยากรประมวลผล

**Critical Path Item:** Must be completed by Day 9 EOD

#### Day 10: Privacy & Fail-Safe Implementation
**Lead:** Specialist (แบมบี้) + Engineer (พั้น)  
**Support:** Tester (validation)

**Tasks:**
1. เขียนโค้ดระบบปกปิดข้อมูลตัวตน (Data Anonymization Pipeline)
2. สร้าง Rule engine ตรวจสอบเพื่อกันไม่ให้ AI บล็อกทราฟฟิกกู้ภัย
3. เพิ่มระบบ Logging เก็บประวัติเมื่อ AI ตัดสินใจพลาด
4. ทดสอบกับสถานการณ์จำลอง AI False Positive

**Week 2 Success Criteria:**
- [ ] All core protocols implemented
- [ ] Unit tests passing (>80% coverage)
- [ ] Individual components run independently
- [ ] Documentation updated

---

### Week 3: Integration Sprint (Days 11-15)
**Theme:** Integration, Testing, and Refinement

#### Day 11: Component Integration - Phase 1
**Integration Order:**
1. Context Layer + Edge Simulation
2. Add AI Routing Protocol
3. Add Privacy & Fail-Safe Module

**Integration Lead:** DevOps (ใบยอ)  
**Testing Lead:** Tester (ใบยอ)

**Activities:**
- Morning: เชื่อมต่อชั้น Context กับระบบจำลองโครงข่าย
- Afternoon: นำ AI Routing มาใช้หาเส้นทาง
- Evening: Run integration tests เบื้องต้น

#### Day 12: Component Integration - Phase 2
**Integration Tasks:**
1. เชื่อมระบบ Fail-Safe เข้ากับทราฟฟิกข้อมูล
2. สร้างการจำลองการไหลของข้อมูลแบบ End-to-end (ตั้งแต่ต้นทางถึงปลายทาง)
3. สร้างโครงสร้างพื้นฐานสำหรับรันสคริปต์การทดสอบ

**Milestone:** ส่งแพ็กเก็ตข้อมูลแบบ End-to-end สำเร็จเป็นครั้งแรก ภายใน EOD

#### Day 13: System Testing & Bug Fixes
**Testing Activities:**

| Test Suite | Owner | Target |
|------------|-------|--------|
| Unit Tests | Engineer (พั้น) | Re-run all |
| Integration Tests | Tester (ใบยอ) | 20 scenarios |
| Performance Tests | DevOps (ใบยอ) | Response time < 1s (ลดจุดคอขวด AI) |
| Fail-Safe Scenarios | Specialist (แบมบี้)| 10 edge cases (Emergency Mode) |

#### Day 14: Visualization & Demo Development
**Lead:** Engineer (พั้น)  
**Support:** All

**Visualization Requirements:**
- Network topology graph (แสดงโหนดติดคอขวด และ AI ปรับเส้นทาง)
- Packet flow animation
- แสดงผลการตัดสินใจของ AI (Routing decision display)
- แจ้งเตือนเมื่อเข้าสู่โหมดฉุกเฉิน (Emergency alert display)

#### Day 15: Week 3 Review & Dry Run
**Activities:**
- 10:00-12:00: Full system test (Smart Campus, Stadium)
- 13:00-15:00: Bug fixing
- 15:00-17:00: Internal demo dry run

**Week 3 Success Criteria:**
- [ ] All components integrated
- [ ] End-to-end packet flow working
- [ ] 3 demo scenarios functional (Campus, Stadium, Emergency)
- [ ] Visualization displays correctly
- [ ] Test coverage >80%

---

### Week 4: Delivery Sprint (Days 16-20)
**Theme:** Finalization, Documentation, and Presentation

#### Day 16: Documentation Sprint
| Document | Owner | Template |
|----------|-------|----------|
| User Guide | DevOps (ใบยอ) | `docs/user_guide.md` |
| API Reference | Engineer (พั้น) | `docs/api.md` |
| Test Report | Tester (ใบยอ) | `docs/test_report.md` |
| Architecture Final | Architect (พลอย) | `architecture_spec.md` |
| Implementation Summary | All | `README.md` |

#### Day 17: Polish & Optimization
**Focus Areas:**
- Code cleanup and comments
- ปรับแต่งการใช้ทรัพยากรประมวลผลเพื่อแก้ไขข้อจำกัดอุปกรณ์เก่า
- Edge case handling (เมื่อ AI ประมวลผลล้มเหลว)
- Visualization enhancement

#### Day 18: Presentation Development
**Tasks:**
1. Create slide deck (All)
2. Record demo video (Engineer - พั้น)
3. Prepare live demo script (Tester - ใบยอ)
4. Rehearse presentation (All)

**Presentation Structure:**
| Section | Duration | Presenter |
|---------|----------|-----------|
| Introduction & Constraints | 2 min | Architect (พลอย) |
| Architecture & Solutions | 3 min | Architect (พลอย) |
| AI Routing Implementation | 4 min | Engineer (พั้น) |
| Privacy & Fail-Safe | 3 min | Specialist (แบมบี้) |
| Demo (3 Use Cases) | 5 min | Engineer (พั้น) |
| Testing Results | 2 min | Tester (ใบยอ) |
| Conclusion | 1 min | DevOps (ใบยอ) |

#### Day 19: Final Review & Rehearsal
**Schedule:**
- 9:00-11:00: Final code review
- 11:00-12:00: Documentation review
- 13:00-15:00: Presentation rehearsal
- 15:00-16:00: Feedback & fixes
- 16:00-17:00: Final adjustments

#### Day 20: Submission Day
**Final Checklist:**

**Code:**
- [ ] All code pushed to main branch
- [ ] Tagged as `v1.0.0`
- [ ] README updated with setup instructions
- [ ] Requirements.txt complete

**Documentation:**
- [ ] Architecture specification
- [ ] Implementation plan
- [ ] User guide
- [ ] API documentation
- [ ] Test report

**Presentation:**
- [ ] Slide deck (PDF)
- [ ] Demo video (MP4)
- [ ] Live demo ready

**Submission Package:**
- [ ] GitHub repository link
- [ ] All deliverables zipped
- [ ] Team contribution statement
- [ ] Peer evaluations

---


## Part 3: Role-Specific Implementation Analysis

### 3.1 Architect's Implementation Analysis (พลอย)

**Key Concerns:**
- ความเสถียรของ Interface ระหว่างเลเยอร์
- การผสานการทำงานเพื่อลดภาระอุปกรณ์รุ่นเก่า (Edge offloading)
- ความยืดหยุ่นในการรองรับปริมาณทราฟฟิก (Scalability)

**Implementation Checklist:**
- [ ] Documented Interfaces ระหว่างระบบเครือข่ายและ AI โมดูล
- [ ] ตรวจสอบรูปแบบ Context data ด้วย Test cases
- [ ] กำหนดรูปแบบข้อความและแพ็กเก็ต
- [ ] บันทึกการตัดสินใจทางสถาปัตยกรรม (Architecture decisions logged)

**Risk Mitigation:**
- สร้าง Mock Interface เพื่อให้เขียนโค้ดคู่ขนานกันได้
- ตรวจสอบโค้ดทั้งหมดเพื่อให้ตรงกับข้อกำหนดสถาปัตยกรรม
- Track architectural drift

### 3.2 Engineer's Implementation Analysis (พั้น)

**Core Implementation Tasks:**

Priority 1 (Must Have):
├── ContextNodeAddress class
├── RoutingTable management
├── AI-Weighted Dijkstra
├── Packet structure
└── Basic simulation

Priority 2 (Should Have):
├── Route caching (เพื่อลดการประมวลผล AI)
├── Load balancing (สำหรับ Smart Stadium)
├── Visualization
└── Performance optimization

Priority 3 (Nice to Have):
├── โมเดล AI ที่ซับซ้อนและเรียนรู้ได้เอง
├── Advanced metrics
└── GUI interface

**ความท้าทายทางเทคนิค (Technical Challenges):**
- การสร้าง AI Routing ที่มีประสิทธิภาพและไม่ทำให้เกิดการประมวลผลล่าช้า (Latency)
- การประมวลผลแบบจำลองที่มีโหนดจำนวนมาก
- การเชื่อมต่อกับ Visualization แบบเรียลไทม์

---

### 3.3 การวิเคราะห์การดำเนินงานของ Specialist (แบมบี้)

**การนำกฎเกณฑ์ไปปฏิบัติใช้ (Domain Rules Implementation):**

| กฎระเบียบ (Rule) | ความซับซ้อน | วิธีการตรวจสอบ (Validation Method) |
|------------------|------------|-----------------------------------|
| **Data Anonymization** | ปานกลาง (Medium) | Unit tests กับข้อมูลจำลอง |
| **Emergency Override** | ต่ำ (Low) | ติดตามเส้นทางทราฟฟิกกู้ภัย |
| **False Positive Prevention** | สูง (High) | Timeline/Context consistency checks |
| **QoS Prioritization** | ปานกลาง (Medium)| ตรวจสอบระดับความสำคัญ (State validation) |

**ความต้องการด้านการค้นคว้า (Research Requirements):**
- [ ] ศึกษาวิธีการปิดบังตัวตนของข้อมูลแบบไม่เสียบริบท
- [ ] กำหนด 5 สถานการณ์ที่ AI มักตัดสินใจผิดพลาด
- [ ] สร้างโมเดลประเมินความเสี่ยงและตั้งเกณฑ์ความปลอดภัย
- [ ] ระบุ Edge cases สำหรับโหมดฉุกเฉิน

---

### 3.4 การวิเคราะห์การดำเนินงานของ DevOps (ใบยอ)


[Image of CI/CD pipeline architecture]


**ความต้องการด้านโครงสร้างพื้นฐาน (Infrastructure Requirements):**

| องค์ประกอบ (Component) | เทคโนโลยี (Technology) | การตั้งค่า (Configuration) |
|----------------------|-----------------------|--------------------------|
| **Version Control** | GitHub | Branch protection |
| **CI/CD** | GitHub Actions | Python 3.8+ |
| **Documentation** | MkDocs / Markdown | Material theme |
| **Testing** | pytest | Coverage reporting |
| **Dependencies** | pip | requirements.txt |

**ตัวอย่าง CI Pipeline (GitHub Actions):**

name: Adaptive-Net CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Setup Python
        uses: actions/setup-python@v2
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run tests
        run: pytest tests/ --cov=src
      - name: Check style
        run: flake8 src/

---

### 3.5 การวิเคราะห์การดำเนินงานของ Tester/QA (ใบยอ)

**กลยุทธ์การทดสอบ (Test Strategy):**

**ระดับการทดสอบ (Test Levels):**

* **Unit Tests (Week 2)**
  - Individual class testing
  - Method-level validation
  - Expected: 50+ test cases

* **Integration Tests (Week 3)**
  - Layer interaction testing (ระหว่าง AI และ Routing)
  - End-to-end packet flow
  - Expected: 20+ scenarios

* **System Tests & Use Cases (Week 4)**
  - Full simulation testing (Smart Campus, Smart Stadium, Emergency)
  - Performance benchmarks
  - Expected: 10+ test runs

**ตารางภาพรวมการทดสอบ (Test Matrix):**

| Component | Unit Tests | Integration | System | Owner |
|-----------|------------|-------------|---------|-------|
| Context Layer | 15 | 5 | 2 | Tester (ใบยอ) |
| AI Routing | 20 | 8 | 3 | Tester (ใบยอ) |
| Privacy & Fail-Safe| 15 | 5 | 3 | Tester (ใบยอ) |
| Simulation | 10 | 2 | 2 | Tester (ใบยอ) |

**แบบฟอร์มรายงานข้อผิดพลาด (Bug Tracking Template):**

## Bug Report
**ID:** ADAPTIVE-[Number]
**Severity:** Critical/High/Medium/Low
**Component:** [Context/Routing/Privacy/Sim]
**Description:** **Steps to Reproduce:**
  1. 
  2. 

**Expected Behavior:**

**Actual Behavior:**

**Assigned To:**

**Status:** Open/In Progress/Resolved/Verified
