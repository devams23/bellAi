**PRODUCT REQUIREMENTS DOCUMENT**

**Bell**

*The AI That Teaches You to Think, Not Just Know*

# **Executive Summary**

Bell is a next-generation AI learning companion that fundamentally reimagines how humans interact with artificial intelligence. Where every other AI tool optimises for faster answers, Bell optimises for deeper understanding — turning every interaction into a personalised thinking exercise.

|Core Thesis The most dangerous side effect of AI is not misinformation — it is cognitive outsourcing. Humans are offloading thinking to machines and losing the muscle of independent reasoning. Bell is the antidote: an AI that refuses to think for you, and instead trains you to think better. |


## **What Bell Is**

Bell is a gamified, scenario-driven platform consisting of four deeply integrated modules: a Communication Coach, an Adulting Assistant, a Developer Arena, and a Socratic Tutor. Each module uses AI not to dispense answers, but to simulate real-world situations, ask Socratic questions, and evaluate the quality of the user's thinking — not just their final response.

## **Unique Value Proposition**

* Test understanding, not just recall — every session ends with a Thinking Score, not a completion badge
* Scenarios feel like games — category-driven, progressive, narrative-rich
* Psychological loading screens — every page opens with a quote that primes the brain for active thinking
* Shame-free failure — the system celebrates re-tries and tracks improvement over time, not just performance


# **Product Vision & Strategic Goals**

## **Vision Statement**
Bell Vision "To become a thinking partner — the platform people turn to not when they want an answer, but when they want to become the kind of person who finds answers on their own." 
## **Mission**
Build an AI companion that measures cognitive growth — not engagement time — and creates users who progressively need the app less, not more. Success is defined by users becoming more independent thinkers, not by daily active usage alone.

## **Design Principles**

1. Brain-first, AI-second — the AI's primary role is to ask, not tell. Every feature decision must serve this principle.

2. Progress should feel earned — XP, scores, and levels only mean something if they require genuine cognitive effort.

3. Failure is data, not shame — the system never punishes users for wrong answers; it uses them as coaching input.

4. Design for the long game — features should build habits, not dependencies. Graduation from topics is a product win.

| SECTION 3   —   USER PERSONAS & TARGET AUDIENCE |
| :---- |

# **User Personas**

## **Primary Personas**

### **Persona 1 — The Ambitious Graduate (Communication Coach \+ Adulting Assistant)**

| Name / Age | Aisha, 23, recent MBA graduate |
| :---- | :---- |
| **Context** | Starting first corporate job. Strong academic record but zero practice in real-world negotiation, workplace politics, or financial decisions. |
| **Frustration** | "I know the theory but I freeze in the actual conversation. I practiced in my head but never out loud." |
| **Goal** | Feel confident walking into her first salary negotiation and first apartment lease signing. |
| **Usage Pattern** | Daily 15-minute sessions during commute. Goal: unlock Salary Negotiation Level 3 before her 90-day review. |

### **Persona 2 — The Developer in Transition (Developer Arena)**

| Name / Age | Rahul, 27, mid-level software engineer |
| :---- | :---- |
| **Context** | Solving LeetCode problems daily but failing system design interviews at FAANG companies. Knows syntax; struggles with architectural thinking. |
| **Frustration** | "I can code the solution but I can't explain why it's the right approach at scale. Interviewers see through me immediately." |
| **Goal** | Land a senior role at a product company within 6 months. |
| **Usage Pattern** | Three 30-minute sessions per week. Focuses on distributed systems and API design scenario tracks. |

### **Persona 3 — The People Manager (Communication Coach)**

| Name / Age | Marcus, 34, first-time engineering manager |
| :---- | :---- |
| **Context** | Promoted from individual contributor. Technically excellent but struggling with difficult conversations, delegation, and team conflict resolution. |
| **Frustration** | "Nobody teaches you how to tell someone their work isn't good enough. I either avoid the conversation or handle it badly." |
| **Goal** | Build enough confidence to run performance reviews and resolve team conflicts without dreading them. |
| **Usage Pattern** | Scenario-based sessions twice a week. Prefers the "hard mode" scenarios where the AI character pushes back aggressively. |

### **Persona 4 — The Curious Learner (Socratic Tutor)**

| Name / Age | Meera, 19, second-year university student |
| :---- | :---- |
| **Context** | Studies computer science but learns better by discovery than by reading. Feels cheated when she looks up answers before truly trying. |
| **Frustration** | "I use ChatGPT and I get the answer but I've learned nothing. I want something that argues back at me." |
| **Goal** | Deeply understand core CS concepts through guided exploration, not memorisation. |
| **Usage Pattern** | Ad hoc sessions tied to coursework. Tracks her Thinking Score as a personal metric of academic honesty. |

## **Secondary Audiences**

* Bootcamp operators — want to add structured soft-skills training to technical curricula

* Corporate L\&D teams — looking for scalable communication training that replaces expensive coaching days

* High school seniors — preparing for college interviews and early career decisions

* Freelancers and entrepreneurs — negotiation, client communication, and financial literacy modules

| SECTION 4   —   PRODUCT ARCHITECTURE & MODULES |
| :---- |

# **Product Architecture**

## **Module 1 — Communication Coach**

The flagship module. Users select a communication category, then enter a real-world scenario where the AI plays the other person. The AI character responds authentically — it may be dismissive, aggressive, friendly, or distracted — based on the scenario difficulty setting.

### **Category Tree**

| Category | Scenario Sub-Types |
| :---- | :---- |
| **Negotiation** | Salary negotiation, vendor negotiation, freelance rate-setting, lease negotiation, performance bonus discussion |
| **Leadership** | Giving critical feedback, running 1:1s, addressing underperformance, setting team expectations, delivering bad news |
| **Networking** | Cold introductions, elevator pitches, conference conversations, LinkedIn follow-up, warm referral requests |
| **Public Speaking** | Impromptu answers, structured 2-minute pitches, handling hostile Q\&A, opening a presentation confidently |
| **Conflict Resolution** | Peer disputes, client complaints, family boundary-setting, managing upward (disagreeing with a boss) |
| **Emotional Intelligence** | Reading a room, de-escalating tension, demonstrating empathy under pressure, active listening practice |

### **How a Scenario Session Works**

6. User picks a category (e.g., Negotiation) and a sub-type (e.g., Salary Negotiation)

7. A psychological loading quote appears — 3 to 5 seconds — priming the brain before the scene loads

8. User sees a scene-setter: context, their role, the AI character's profile (name, mood, position)

9. Conversation begins. User types or speaks. AI responds as the character — not as a helpful assistant

10. At any point, user can spend a Hint Token for a contextual nudge (e.g., "Think about what the other person's primary concern is")

11. Scenario ends when the user reaches an outcome — positive, neutral, or failed

12. Debrief Mode activates: scoring breakdown, specific phrase analysis, what to do differently

## **Module 2 — Socratic Tutor**

A universal learning mode applicable to any subject. The AI never answers directly — it responds to every question with a guiding question, a thought experiment, or an analogy, gradually helping users construct their own understanding.

| Supported Subjects | Any — the AI is subject-agnostic. Optimised paths exist for CS, Economics, Philosophy, History, Biology, Mathematics |
| :---- | :---- |
| **Socratic Depth Levels** | Surface (what?), Structural (how?), Critical (why does this matter?), Creative (what if this were different?) |
| **Session Modes** | Concept Exploration, Exam Preparation (timed), Essay Argument Review, Debate Practice |
| **Output** | Concept Mastery Map — visual tree of what the user has genuinely understood vs. what they've only seen |

All the topic that are successfully covered and understood by the user,  these topics are shown in the user dashboard, as an brain like storage , or a visual storage, where the user can see that how many topic he has learned till now, so when he comes  , basically creating his knowledge vault, 

| SECTION 5   —   GAMIFICATION & ENGAGEMENT SYSTEM |
| :---- |

## **Psychological Loading Screens**

| Design Intention Before every scenario, a full-screen loading card appears for 3–5 seconds. It displays a single quote or micro-prompt designed to activate the prefrontal cortex — the brain's reasoning centre — before the challenge begins. This is a deliberate product decision to prime users for active thinking rather than passive consumption. |
| :---- |

### **Quote Categories & Examples**

| Quote Type | Example |
| :---- | :---- |
| **Neuroscience** | "The brain that is challenged grows. The brain that is only answered atrophies. — Bell" |
| **Philosophy** | "He who thinks he knows, doesn't know. He who knows he doesn't know, knows. — Confucius" |
| **Resilience** | "You don't rise to the level of your goals. You fall to the level of your systems. — James Clear" |
| **Cognitive Science** | "Memory is the residue of thought. Think harder, and you will remember better. — Daniel Willingham" |
| **Growth Mindset** | "The illiterate of the 21st century will not be those who cannot read; they will be those who cannot learn, unlearn, and relearn. — Alvin Toffler" |
| **Self-Challenge Prompts** | "Before this scenario: What do you already know about this situation? Try to solve it yourself first." |

## **Hint System**

Hints are scarce by design. Users receive a fixed hint budget per session (based on their level), and each hint reduces the session's maximum possible Thinking Score. Hints are contextual — they never give the answer, only redirect the user's thinking.

| Hint Type | What it Does |
| :---- | :---- |
| **Level 1 Hint** | Reframes the situation: "What is the other person's primary concern in this scenario?" |
| **Level 2 Hint** | Identifies the gap: "Your last response addressed the surface complaint. What might be underneath it?" |
| **Level 3 Hint** | Provides a framework: "In negotiation theory, BATNA refers to... how does that apply here?" |

| SECTION 7   —   UX & DESIGN LANGUAGE |
| :---- |

# **UX & Design Language**

## **Design Philosophy**

Bell's design must communicate one thing visually before a user reads a single word: this is a serious tool for serious growth. It should feel like the intersection of a premium productivity app and a well-designed game — never childish, never clinical.

### **Loading Screen — Psychological Primer**

| UX Specification Duration: 3.5 seconds (non-skippable but not perceived as waiting — it's perceived as a ritual). Full bleed dark background. Large, single quote in Fraunces italic. Subtle animated particle background (slow, meditative — not energetic). Quote category shown in small text (e.g., "NEUROSCIENCE" or "SELF-CHALLENGE"). Fades out into scenario scene with a soft dissolve. |
| :---- |

## **Mobile-First Responsive Design**

prompt the user to use the app on desktop for the best experience, and lock the app access on mobile devices, as the app is designed to be used on desktop only, due to the nature of the scenarios and the need for a larger screen to fully engage with the content. The mobile version will be a simplified version of the desktop experience, with limited functionality and a focus on providing access to the user's progress and scores. 

## **Accessibility Standards**

* WCAG 2.1 AA compliance across all interfaces

* Voice input support for scenario responses (especially valuable for public speaking practice)

* High contrast mode available without requiring OS-level settings

* All animations can be disabled for users with motion sensitivity

| SECTION 11   —   SUCCESS METRICS & KPIs |
| :---- |

# **Success Metrics & KPIs**

## **North Star Metric**

| North Star Weekly Active Thinkers (WAT) — defined as users who completed at least 2 scenario sessions in a week AND showed a positive Thinking Score trend over the past 4 weeks. This metric captures both engagement and genuine growth, which is Bell's core promise. |
