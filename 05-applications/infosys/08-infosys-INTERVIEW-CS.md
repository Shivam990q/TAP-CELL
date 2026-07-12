# Infosys Interview — CS Fundamentals FULL ANSWERS (OOP · DBMS/SQL · OS · CN · GenAI)

> 🔖 **PROVENANCE:** ~95% **[AI-EXPLANATION]** — standard CS fundamentals (OOP/DBMS/OS/CN/GenAI) jo AI
> ne crisp Hinglish answers me likha. Ye universal textbook knowledge hai (kisi ek source ka nahi).
> Interview questions ke topics [WEB-VERIFIED] (faceprep/Medium 2026). Legend: `README.md` → PROVENANCE INDEX.

> Interview me DSA ke saath ye poochte hain (SP + DSE dono). Yahan **actual crisp answers** hain
> (sirf topic naam nahi) — ek baar padh ke samajh le, apne words me bol pana. Detail deep-dive
> `07-infosys-specialist-programmer-PREP.md` me. DSA solutions `06-infosys-SOLUTIONS.md` me.

---
# 1. OOP (har interview me — real example ke saath bol)

**4 Pillars:**
- **Encapsulation:** data + methods ko ek class me bind karna, aur direct access rokna (private
  fields + getters/setters). Example: `BankAccount` ka `balance` private, `deposit()` se hi change.
- **Abstraction:** implementation chhupa ke sirf zaroori interface dikhana. Example: `car.start()` —
  andar engine kaise chalu hota, user ko nahi pata.
- **Inheritance:** ek class dusri ki properties/methods reuse kare (`Dog extends Animal`). Code reuse.
- **Polymorphism:** ek naam, alag behaviour. Do type:
  - **Overloading (compile-time):** same method naam, alag parameters. `add(int,int)` vs `add(int,int,int)`.
  - **Overriding (runtime):** child class parent ka method redefine kare. `Dog.sound()` overrides `Animal.sound()`.

**Overloading vs Overriding (code):**
```java
class Animal { void sound(){ System.out.println("some sound"); } }
class Dog extends Animal { void sound(){ System.out.println("bark"); } }  // override
class Calc { int add(int a,int b){return a+b;} int add(int a,int b,int c){return a+b+c;} } // overload
```
**Abstract class vs Interface:**
- Abstract class: partial implementation + state (fields) rakh sakti hai; ek hi extend hoti hai.
- Interface: pure contract (Java 8+ me default methods); multiple implement ho sakti hain.
- Java multiple inheritance: **classes se NO** (diamond problem), **interfaces se YES**.
**Composition vs Inheritance:** "has-a" (composition) vs "is-a" (inheritance). Prefer composition — flexible, loose coupling.
**SOLID (1-line):** Single-responsibility, Open-closed, Liskov substitution, Interface-segregation, Dependency-inversion.

---
# 2. DBMS / SQL

**Normalization** (redundancy + anomalies kam karne ke liye):
- **1NF:** atomic values (har cell me ek value), no repeating groups.
- **2NF:** 1NF + no partial dependency (non-key fully depend on whole primary key).
- **3NF:** 2NF + no transitive dependency (non-key non-key pe depend na kare).
- **BCNF:** stricter 3NF (har determinant candidate key ho).

**Keys:** Primary (unique + not null), Foreign (dusri table ke PK ko refer), Candidate (PK banne ke eligible), Composite (2+ columns milke key).
**Index:** read fast (B-tree lookup), par write/space slow (index maintain karna padta).
**ACID:** Atomicity (all-or-nothing), Consistency (valid state), Isolation (transactions independent), Durability (committed = permanent).
**DELETE vs TRUNCATE vs DROP:** DELETE (rows, WHERE lagta, rollback ho sakta, DML) · TRUNCATE (saari rows, fast, no WHERE, DDL) · DROP (table hi delete).
**JOINs:** INNER (dono me match) · LEFT (left saara + match) · RIGHT · FULL (dono saara).
**WHERE vs HAVING:** WHERE rows pe (group se pehle), HAVING groups pe (GROUP BY ke baad).

**Must-know queries:**
```sql
-- 2nd highest salary
SELECT MAX(salary) FROM emp WHERE salary < (SELECT MAX(salary) FROM emp);
-- Nth highest (dense)
SELECT salary FROM emp ORDER BY salary DESC LIMIT 1 OFFSET N-1;
-- duplicates find
SELECT email, COUNT(*) FROM users GROUP BY email HAVING COUNT(*) > 1;
-- department-wise count
SELECT dept, COUNT(*) FROM emp GROUP BY dept HAVING COUNT(*) > 5;
```
**Window functions:** `ROW_NUMBER() OVER(PARTITION BY dept ORDER BY salary DESC)` — ranking per group.
**DDL/DML/DCL/TCL:** DDL (CREATE/ALTER/DROP) · DML (SELECT/INSERT/UPDATE/DELETE) · DCL (GRANT/REVOKE) · TCL (COMMIT/ROLLBACK/SAVEPOINT).

---
# 3. Operating Systems

**Process vs Thread:** Process = independent program (apna memory space); Thread = process ke andar lightweight unit (memory share karte). Thread switching sasta.
**Context switching:** CPU ka ek process/thread se dusre pe switch — state save/restore (overhead).
**Scheduling:** FCFS (order me) · SJF (shortest job first) · Round Robin (time-slice, fair) · Priority.
**Deadlock — 4 conditions (saari saath me):** Mutual exclusion, Hold-and-wait, No preemption, Circular wait. **Todo (prevent):** in me se koi ek break karo. **Avoid:** Banker's algorithm.
**Semaphore vs Mutex:** Mutex = lock (1 thread at a time, ownership); Semaphore = counter (N resources allow).
**Race condition:** 2 threads shared data ek saath change karein → unpredictable. Fix: lock/mutex.
**Paging vs Segmentation:** Paging = fixed-size blocks (pages); Segmentation = logical variable-size (code/stack/data).
**Virtual memory:** disk ko RAM ki tarah use karna (page in/out). **Thrashing:** zyada paging → CPU kaam se zyada swapping me busy.

---
# 4. Computer Networks

**OSI (7 layers):** Physical, Data-link, Network, Transport, Session, Presentation, Application.
**TCP/IP (4):** Link, Internet, Transport, Application.
**TCP vs UDP:** TCP = connection-oriented, reliable, ordered, slow (handshake); UDP = connectionless, fast, no guarantee (video/games).
**3-way handshake:** SYN → SYN-ACK → ACK (connection establish).
**HTTP vs HTTPS:** HTTPS = HTTP + TLS/SSL encryption (port 443).
**DNS:** domain name → IP resolve karta hai (jaise phonebook).
**"URL type karne pe kya hota hai":** DNS lookup → TCP connection (+ TLS) → HTTP request → server response → browser render.
**Status codes:** 200 OK · 301 redirect · 400 bad request · 401 unauthorized · 404 not found · 500 server error.
**Public vs Private IP:** Public = internet pe unique; Private = LAN ke andar (192.168.x.x), NAT se bahar jaata.

---
# 5. ★ ML / GenAI basics (2026 NEW — tera differentiator, ROSE/MCP/CrewAI se connect)

**ML kya hai:** data se patterns seekh ke prediction/decision (explicit rules ke bina).
**Supervised vs Unsupervised:** Supervised = labelled data (classification/regression); Unsupervised = no labels (clustering).
**Overfitting:** model training data ratt le, naye data pe fail. Fix: more data, regularization, cross-validation.
**LLM (Large Language Model):** huge text pe train kiya neural network (transformer) jo next token predict karke text generate karta (GPT, Claude).
**Generative AI:** naya content banane wali AI (text/image/code).
**AI Agent:** LLM + tools + memory + loop — khud decide karke actions leta (sirf jawab nahi deta).
**RAG (Retrieval-Augmented Generation):** LLM ko bahar se relevant docs retrieve karke context do → accurate, up-to-date jawab (hallucination kam).
**MCP (Model Context Protocol):** standard protocol jisse AI agents tools/data-sources se connect karte (tune ispe kaam kiya — ROSE, open-figma-mcp).
**CrewAI:** multi-agent orchestration framework (kai agents milke task karte).
> Interview me: "Maine ROSE banaya — ek Gen-AI agent jo MCP se tools use karta; Better Than Claude
> Skills me 16+ LLM skills likhe" — ye bolke stand out karo.

---
# 6. Language quick (jo choose karo — Java/Python)

**Java:** JDK (dev kit) > JRE (runtime) > JVM (executes bytecode). `==` (reference) vs `.equals()` (value). String immutable + string pool. `final` (constant) / `finally` (always runs) / `finalize` (GC). ArrayList (dynamic array, fast access) vs LinkedList (fast insert/delete). Checked vs unchecked exceptions.
**Python:** list vs tuple (mutable vs immutable). `is` (identity) vs `==` (value). List comprehension. GIL (one thread executes bytecode at a time). Decorators, generators (`yield`).

---
# 7. HR / Behavioral (2-3 line answers ready)
- **Tell me about yourself:** (self-intro — README/QUESTION-BANK me hai).
- **Why Infosys?** Premium tech role, enterprise-scale + latest tech (cloud, GenAI), strong learning
  culture + mentorship, PAN-India. Role jo coding skill ko reward karta hai.
- **Strengths:** fast learner (90+ projects), problem-solving, shipping real products.
- **Weakness:** (ek honest + improving waali — e.g. "pehle over-engineer karta tha, ab MVP-first").
- **Relocate PAN-India?** YES. **Any technology?** YES — naye stacks jaldi pick karta hoon.
- **5 years?** Strong engineer ban ke, complex systems + AI pe kaam, team lead karna.
- **Puzzles (practice):** bulb-switch, egg-drop, weighing balls, bridge-crossing.

---
> Ye + `06-infosys-SOLUTIONS.md` (DSA) = interview fully covered (SP + DSE dono).
> Padhna nahi, SAMAJHNA hai — apne words me bol pana. Projects (NETWORKED/Parakh/ROSE) cold yaad rakho.
