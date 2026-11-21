# CSE791 – Research Methodology
## Week 4 & Week 5: Exam-Ready Notes

---

# WEEK 4: RESEARCH QUESTIONS, HYPOTHESES, AND STUDY DESIGN

## 1. What is a Problem Statement?

A problem statement is a clear description of a specific research problem, its context, its importance, and the knowledge gap that needs to be addressed.

A good problem statement should identify:
- The research context.
- The specific problem.
- Existing knowledge from previous studies.
- The research gap.
- The proposed research direction.

**Problem Statement Formula:**

Context + Specific Problem + Existing Evidence + Research Gap + Research Direction.

## 2. What is a Research Gap?

A research gap is an unanswered question, limitation, or underexplored area in existing literature that requires further investigation.

A research gap provides the justification for conducting a new study.

**Example:** Previous studies have examined AI adoption in education, but limited research has investigated how different AI scaffolding strategies influence independent problem-solving among undergraduate programming students.

## 3. What is a Research Question (RQ)?

A research question is a clear, focused, and answerable question that guides a research study.

A strong research question should:
1. Be linked to a specific literature gap.
2. Define the population or context.
3. Identify the phenomenon or variables.
4. Have a clear evidence source.
5. Be answerable using an appropriate method.
6. Be feasible within the available time and resources.

**Relationship:**

Research Gap → Research Question → Evidence → Method → Analysis.

## 4. Anatomy of a Strong Research Question

A strong RQ contains five important elements:

1. Population/Context: Who or what is being studied?
2. Phenomenon: What issue is being investigated?
3. Constructs/Variables: What concepts or measures are important?
4. Evidence: What data can answer the question?
5. Contribution: What will the findings explain or evaluate?

**General Template:**

How / To what extent / Why does [X] affect or relate to [Y] among [population/context] using [evidence or method]?

## 5. Characteristics of Weak and Strong Research Questions

| Weak RQ | Strong RQ |
|---|---|
| How can AI improve education? | How does step-by-step AI support influence independent problem-solving among undergraduate students? |
| Is online learning better? | How do learning outcomes differ between online and classroom-based instruction? |
| Why should we build an app? | To what extent does the proposed application improve task completion among target users? |
| How can we solve misinformation? | How are misinformation exposure and verification behavior related among university students? |

## 6. Types of Research Questions

| Type | Purpose | Typical Evidence/Method |
|---|---|---|
| Descriptive | Describes what is happening | Survey, logs, content analysis |
| Comparative | Compares groups | Experiment, survey, statistical tests |
| Relational | Examines relationships between variables | Correlation, regression, SEM |
| Causal | Examines whether X causes a change in Y | Experiment, quasi-experiment |
| Interpretive | Understands experiences and meanings | Interviews, observation, thematic analysis |
| Design/Evaluation | Evaluates an artifact or system | Prototype, usability testing, field study |

## 7. RQ Revision Checklist

Every revised research question should pass these six checks:

1. Gap link: Which literature gap supports this RQ?
2. Evidence: What specific data will answer it?
3. Method fit: Is the selected method appropriate?
4. Scope: Is the population, context, or dataset clearly defined?
5. Construct clarity: Are the main concepts measurable or interpretable?
6. Feasibility: Can the study be completed within the available time?

**Important:** It is better to have fewer strong RQs than many weak and unanswerable RQs.

## 8. What is a Hypothesis?

A hypothesis is a testable prediction about the expected relationship or difference between variables in a research study.

Hypotheses are mainly used in quantitative and confirmatory research.

### Types of Hypotheses

**Alternative Hypothesis (H1):**
Predicts that a relationship or difference exists between variables.

**Null Hypothesis (H0):**
Predicts that no significant relationship or difference exists between variables.

**Example:**

RQ: To what extent do provenance cues affect users' willingness to share social media posts?

- H1: Posts with visible provenance cues will produce lower sharing intention than posts without provenance cues.
- H0: There is no difference in sharing intention between posts with and without provenance cues.

### When Should We Use Hypotheses?

Use hypotheses when:
- Variables are measurable.
- Previous literature provides a theoretical basis.
- Statistical testing is planned.
- The expected relationship or difference is clear.

Avoid forcing hypotheses in exploratory, qualitative, or interpretive studies when the expected direction is unknown.

## 9. Components of a Hypothesis

A testable hypothesis should identify:

1. Independent Variable (IV): The factor that changes or differs.
2. Dependent Variable (DV): The outcome being measured.
3. Direction: Expected increase, decrease, or relationship.
4. Comparison: The condition or group being compared.

## 10. Variables and Constructs

**Construct:** An abstract concept that cannot always be directly observed, such as trust, usability, or cognitive load.

**Variable:** A measurable characteristic that can take different values.

**Dimension:** A specific aspect of a construct.

**Indicator:** An observable sign used to represent a construct.

**Measure:** The actual value or score collected.

**Operational Definition:** A precise explanation of how a construct or variable will be observed or measured in a particular study.

### Example

| Stage | Example |
|---|---|
| Construct | Trust |
| Dimension | Credibility |
| Indicator | Agreement with trust-related statements |
| Measure | 1–5 Likert-scale score |
| Analysis | Mean, regression, group comparison |

## 11. What is Study Design?

Study design is the overall plan or framework that explains how a research study will collect, measure, and analyze evidence to answer its research questions.

A good study design connects:
- Research questions.
- Variables and constructs.
- Participants or datasets.
- Data collection methods.
- Analysis techniques.
- Validity considerations.
- Feasibility.

**Important Principle:** Design follows the research question.

## 12. Types of Study Design

### A. Quantitative Research Design

Quantitative research uses numerical data and statistical analysis to measure variables, compare groups, test relationships, or make predictions.

Common types:

1. Survey: Measures attitudes, behavior, and prevalence.
2. Experiment: Tests causal effects by manipulating conditions.
3. Quasi-experiment: Compares groups or conditions without full randomization.
4. Dataset/ML study: Uses data and computational models for prediction, classification, or pattern analysis.

### B. Qualitative Research Design

Qualitative research explores experiences, opinions, meanings, behavior, and processes using non-numerical evidence.

Common methods:

1. Interviews: Collect detailed individual experiences.
2. Observation: Study actual behavior.
3. Focus groups: Explore shared opinions and group interactions.
4. Thematic analysis: Identify patterns and themes in qualitative data.

### C. Mixed-Methods Research Design

Mixed-methods research combines quantitative and qualitative methods to answer different or complementary aspects of a research problem.

Types:

1. Sequential Explanatory: QUAN → qual. Quantitative findings are followed by qualitative investigation to explain the results.
2. Sequential Exploratory: qual → QUAN. Qualitative findings are used to develop or guide quantitative investigation.
3. Convergent: QUAN + qual. Both types of data are collected in parallel and compared or integrated.

**Important:** Mixed methods should be selected because the RQs require different forms of evidence, not simply to make the study look more comprehensive.

## 13. ML, CV, and Data Science Study Design

ML and data science research requires a different design logic.

Important components:

1. Task Framing: Define the exact prediction, classification, detection, or generation task.
2. Dataset: Select data that matches the research question and target population.
3. Evaluation Protocol: Define metrics, baselines, data splits, and ablation studies.
4. Generalization Claim: Specify the population, domain, or conditions to which the model is expected to generalize.

**Mapping:**

- Task framing ↔ Research Question
- Dataset ↔ Sample
- Evaluation protocol ↔ Measurement
- Generalization claim ↔ Validity

## 14. Validity Threats

Validity refers to how accurately and reliably a research study measures, explains, and supports its conclusions.

Six important validity considerations:

1. Construct Validity: Whether the study measures the concept it claims to measure.
2. Internal Validity: Whether the observed result is actually caused by the studied factor rather than another factor.
3. External Validity: Whether the findings can be generalized to other populations, settings, or contexts.
4. Reliability: Whether the research process produces consistent results.
5. Conclusion Validity: Whether the conclusions are supported by the analysis and available evidence.
6. Ethical Validity: Whether participants' rights, safety, and privacy are protected.

## 15. Feasibility of a Research Study

Feasibility means determining whether a research study can realistically be completed with available resources and constraints.

Important factors:

- Access: Availability of participants, datasets, tools, and APIs.
- Time: Ability to finish within the deadline.
- Ethics: Whether risks, consent, and privacy can be managed.
- Skill: Whether the research team has the required technical and analytical skills.
- Scope: Whether the research questions are manageable.

## 16. Alignment Matrix

An alignment matrix is a research planning tool that connects each research question with its literature gap, evidence source, method, analysis, and validity risk.

| RQ | Gap | Evidence | Method/Analysis | Validity Risk |
|---|---|---|---|---|
| RQ1 | Literature gap A | Dataset or survey | Descriptive analysis | Recall or measurement bias |
| RQ2 | Literature gap B | Scale, logs, or labels | Regression or comparison | Construct validity |
| RQ3 | Literature gap C | Interviews or open responses | Thematic analysis | Transferability |

Evidence status should also be recorded:
- Available now.
- Likely available.
- Needs collection.
- Risky.
- Not available.

## 17. Dataset Selection and Quality Assessment

A dataset must match the research question and satisfy research, technical, and ethical requirements.

### Dataset Fit Criteria

**Research Fit:**
- Matches the RQ.
- Correct unit of analysis.
- Relevant population and context.
- Appropriate time period.
- Contains the required outcome variables.

**Technical Fit:**
- Sufficient number of records.
- Usable format and size.
- Manageable missing values.
- Duplicates can be identified.
- Suitable train/test split is possible.

**Research Quality Fit:**
- Creator and collection purpose are documented.
- Labeling process is clear.
- License permits research use.
- Bias and limitations can be identified.
- Relevant baselines are available.

### Important Dataset Quality Dimensions

1. Research Fit: Does the dataset match the RQ?
2. Temporal Fit: Is the collection period relevant?
3. Variable Fit: Are the required variables available?
4. Granularity Fit: Is the level of detail appropriate?
5. Provenance: Is the data origin documented?
6. Label Quality: Are labels reliable and consistent?
7. Completeness: Are missing values and duplicates manageable?
8. Representativeness: Does the dataset cover the target population?
9. Class Balance: Are the classes sufficiently represented?
10. Leakage Risk: Does any feature reveal the target unintentionally?
11. Ethics and License: Is the data legally and ethically usable?
12. Documentation: Are collection and preprocessing explained?

## 18. Dataset Search Strategy

A systematic dataset search follows these steps:

1. Start from the RQ.
2. Define the unit of analysis.
3. List the required fields.
4. Set region, population, time, and task boundaries.
5. Search and document candidate datasets.

### Common Dataset Sources

- Google Dataset Search
- Kaggle
- UCI Machine Learning Repository
- OpenML
- Hugging Face Datasets
- Papers with Code
- Zenodo
- Figshare
- OSF
- data.gov.bd
- Bangladesh Bureau of Statistics
- World Bank Open Data

### Dataset Candidate Log

Record:
- Dataset/source name.
- Repository or source link.
- Which RQ it supports.
- Key fields.
- License.
- Quality risks.
- Final decision.

**Week 4 Milestone:**
1. Revised problem statement.
2. Revised RQs (usually 2–4).
3. Hypotheses, if applicable.
4. Construct and variable map.
5. Study design outline.
6. Dataset or evidence source note with 2–3 candidates.

---

# WEEK 5: HUMAN-CENTERED METHODS, ETHICS, AND RESPONSIBLE DATA COLLECTION

## 1. What is Human-Centered Research?

Human-centered research focuses on understanding people's experiences, needs, behavior, and interaction with systems or technologies.

It uses methods such as surveys, interviews, focus groups, observation, and usability testing.

The goal is to collect meaningful evidence while protecting participants' rights, safety, privacy, and dignity.

## 2. Learning Outcomes of Week 5

Students should be able to:

1. Design appropriate research instruments.
2. Plan ethical data collection and recruitment.
3. Obtain informed consent.
4. Protect participants' privacy.
5. Assess dataset provenance, licensing, and PII.
6. Apply responsible AI practices.

## 3. Two Evidence Tracks

### A. Human-Participant Track

Uses evidence collected directly from people.

Examples:
- Surveys.
- Interviews.
- Focus groups.
- Observation.
- Usability testing.

Deliverables:
- Draft survey or interview protocol.
- Recruitment and consent plan.
- Ethics considerations draft.

### B. Dataset/ML Track

Uses existing datasets, scraped data, logged data, or benchmarks.

Deliverables:
- Dataset ethics note.
- Provenance and license assessment.
- PII audit.
- Bias and downstream harm assessment.
- Ethics considerations draft.

**Important:** Publicly available data does not automatically mean ethically usable data.

## 4. Selecting the Appropriate Research Method

| Method | Best For | Typical Output |
|---|---|---|
| Survey | Measuring attitudes, prevalence, and relationships | Numeric responses and scale scores |
| Interview | Understanding experiences and reasoning | Interview transcripts |
| Focus Group | Understanding shared opinions and disagreements | Group transcripts |
| Observation | Studying actual behavior | Field notes and observations |
| Usability Testing | Evaluating a system or artifact | Task success, time, errors, SUS |
| Existing Dataset Study | ML, AI, CV, and NLP research | Model performance and evaluation results |

**Method Selection Rule:**

- How much/how many? → Survey or logs.
- How/why? → Interview or observation.
- Does the system work? → Usability testing.
- Can a model learn a pattern? → Dataset study with evaluation protocol.

## 5. Survey Design

A survey is a structured data collection method used to gather information from respondents through a set of questions.

### Survey Design Process

Construct → Dimensions → Items → Response Scale → Pilot → Deployment.

### Principles of Good Survey Design

1. Use simple and clear language.
2. Each question should measure one concept.
3. Avoid leading questions.
4. Avoid double-barreled questions.
5. Keep response scales consistent.
6. Use validated scales when possible.
7. Keep the survey reasonably short.
8. Pilot-test before deployment.

### Common Survey Item Problems

| Problem | Example | Improvement |
|---|---|---|
| Double-barreled | Is the app fast and easy to use? | Ask two separate questions |
| Leading | How much do you love this feature? | Use neutral wording |
| Vague quantifier | Do you often verify news? | Specify a time period |
| Jargon | Rate the system's affordances | Use plain language |
| Absolute wording | Do you always check sources? | Use a graded response scale |

**Pilot Testing:** Test the instrument with approximately 3–5 people before the actual deployment.

## 6. Sampling and Recruitment

Sampling is the process of selecting participants from a target population for a research study.

### Types of Sampling

**1. Convenience Sampling:**
Selecting participants who are easily accessible.

Advantage: Fast and inexpensive.

Limitation: Weak generalizability.

**2. Snowball Sampling:**
Existing participants refer additional participants.

Advantage: Useful for hard-to-reach populations.

Limitation: Referral bias.

**3. Purposive Sampling:**
Selecting participants based on specific characteristics relevant to the RQ.

Advantage: Provides relevant and information-rich participants.

Limitation: Findings may not represent the wider population.

### Sample Size

- Quantitative studies: Sample size should be justified based on the planned statistical analysis.
- Qualitative studies: Sample size depends on research scope and information sufficiency; saturation may guide recruitment.
- The lecture suggests around 8–15 interviews as a realistic course-level target, not a universal rule.

### Recruitment Ethics

Participation must be voluntary. Researchers must not use grades, employment authority, favors, or pressure to force participation.

## 7. Interview Design

An interview is a qualitative data collection method used to explore participants' experiences, opinions, reasoning, and behavior in depth.

### Semi-Structured Interview

A semi-structured interview uses prepared core questions while allowing follow-up questions and probes.

### Interview Structure

1. Opening: Explain the study, reconfirm consent, and build rapport.
2. Core Questions: Ask open-ended questions linked to RQs.
3. Probes: Ask follow-up questions such as "Can you explain more?"
4. Closing: Invite additional comments, thank participants, and explain next steps.

**Good Interview Questions:**
- How do you decide whether a post is trustworthy?
- Can you describe the last time you verified information?

Avoid leading or judgmental questions.

## 8. Focus Groups

A focus group is a qualitative method in which a small group discusses a specific topic under the guidance of a moderator.

### Characteristics

- Usually 4–8 participants.
- One moderator.
- One note-taker.
- Useful for shared norms, group language, and disagreement.

### Advantages
- Generates multiple perspectives.
- Reveals group interaction.
- Helps identify shared beliefs and disagreements.

### Limitations
- Dominant participants may influence others.
- Participants may hesitate to disagree.
- Confidentiality cannot be guaranteed among participants.

**Important:** Sensitive personal topics are generally more appropriate for individual interviews.

## 9. Observation

Observation is a data collection method in which researchers systematically watch and record actual behavior in a particular setting.

### Types

**Naturalistic Observation:** Observing behavior in its natural environment with minimal interference.

**Structured Observation:** Recording predefined behaviors using a coding sheet or checklist.

### Important Considerations

- Observer effect: Participants may change their behavior because they know they are being observed.
- Field notes: Separate direct observations from researcher interpretations.
- Online observation: Public online content still requires privacy and ethical consideration.

## 10. Usability Testing

Usability testing evaluates how effectively and efficiently users can complete tasks using a system or product.

### Important Measures

1. Task Success: Whether the participant completes the task.
2. Time on Task: How long task completion takes.
3. Error Count: Number of errors made.
4. SUS: System Usability Scale score.
5. Think-Aloud: Participants explain their thoughts while performing tasks.

### Think-Aloud Method

Participants verbalize their thoughts while interacting with a system. It helps researchers understand confusion, decisions, and interaction problems.

**Important:** Test the system, not the participant.

## 11. Dataset-Track Research Methods

For AI, ML, CV, and NLP projects, the dataset and evaluation protocol function as the main research instruments.

Important steps:

1. Select a dataset that matches the RQ.
2. Check its provenance and license.
3. Inspect samples manually.
4. Identify duplicates, incorrect labels, and missing data.
5. Define train/test splits.
6. Select appropriate evaluation metrics.
7. Compare with baseline models.
8. Document transformations and limitations.

### Common Evaluation Metrics

- Accuracy.
- Precision.
- Recall.
- F1-score.
- Mean Average Precision (mAP).
- BLEU.
- Calibration metrics.

Metrics must match the research task.

### Annotation Quality

For self-collected or manually labeled datasets:
- Prepare written annotation guidelines.
- Use at least two annotators on a sample where feasible.
- Measure inter-annotator agreement, such as Cohen's kappa.

## 12. Instrument Quality and Pilot Testing

An instrument is a tool used to collect research evidence, such as a survey questionnaire or interview guide.

Pilot testing helps identify:
- Unclear questions.
- Confusing language.
- Technical issues.
- Excessive completion time.
- Problems with response options.

### Language Considerations

For Bangla and English instruments:
1. Translate the questions.
2. Back-translate to check meaning.
3. Avoid complex expressions and jargon.
4. Record the language used by each participant.

## 13. Thematic Analysis

Thematic analysis is a qualitative method used to identify, analyze, and report patterns or themes within qualitative data.

### Six Phases of Thematic Analysis

1. Familiarization: Read and understand the data.
2. Coding: Label meaningful data segments.
3. Building Themes: Group related codes into patterns.
4. Reviewing Themes: Check themes against the complete dataset.
5. Defining and Naming: Clearly define each theme.
6. Writing Up: Present findings with supporting evidence.

**Important:** Themes are developed through systematic analysis; they do not automatically emerge from data.

## 14. Research Ethics

Research ethics refers to the principles and practices that protect participants' rights, dignity, privacy, safety, and well-being during research.

### Three Fundamental Ethical Principles

**1. Respect for Persons**

- Respect individual autonomy.
- Obtain informed consent.
- Ensure voluntary participation.
- Allow withdrawal without penalty.

**2. Beneficence**

- Maximize potential benefits.
- Minimize possible harm.
- Assess and reduce research risks.

**3. Justice**

- Distribute research burdens and benefits fairly.
- Avoid exploiting vulnerable populations.
- Ensure fair participant selection.

These principles are associated with the Belmont Report.

## 15. Informed Consent

Informed consent is a process through which participants voluntarily agree to participate after receiving and understanding relevant information about the study.

### Elements of Informed Consent

1. Research purpose.
2. Procedures and estimated time.
3. Potential risks and benefits.
4. Voluntary participation.
5. Right to withdraw without penalty.
6. Data usage and storage.
7. Anonymization or confidentiality measures.
8. Separate permission for audio/video recording.
9. Contact information for questions or complaints.

**Important:** Consent means understanding and voluntary agreement, not merely signing a form.

### Ongoing Consent

Researchers should check whether participants remain comfortable during long or sensitive sessions.

## 16. Privacy and Data Protection

Privacy and data protection involve safeguarding personal information from unauthorized access, disclosure, misuse, or identification.

### Anonymization vs Pseudonymization

| Anonymization | Pseudonymization |
|---|---|
| Removes identifying information so identity cannot reasonably be recovered | Replaces direct identifiers with codes |
| No identity key is retained | A separate key may reconnect codes to identities |
| Identity is intended to be unrecoverable | Re-identification remains possible through the key |

### Data Protection Practices

- Use encrypted storage.
- Restrict access to authorized team members.
- Keep identity keys separate.
- Define retention and deletion periods.
- Avoid storing participant data in personal messaging accounts.
- Remove or generalize indirect identifiers.
- Avoid sharing identifiable data publicly.

## 17. IRB and Ethics Review

IRB stands for Institutional Review Board.

An IRB is a committee that reviews research involving human participants to ensure that ethical principles, participant rights, and safety requirements are followed.

### What Does an IRB Review?

1. Risk-benefit balance.
2. Informed consent quality.
3. Recruitment fairness.
4. Protection of vulnerable participants.
5. Privacy and data storage.
6. Researcher competence.
7. Risk mitigation procedures.

For course projects, the instructor may review instruments and ethics plans before data collection. Formal thesis research may require university ethics review.

## 18. Dataset Ethics

Dataset ethics concerns the responsible collection, selection, use, storage, and application of datasets, especially datasets containing information about people.

Important issues:

1. Provenance: Where did the dataset come from?
2. Licensing: Is research and model training permitted?
3. Consent: Under what expectations was the data collected?
4. PII: Does it contain personally identifiable information?
5. Bias: Are particular groups or regions underrepresented?
6. Downstream Harm: Could the model cause discrimination or other harm?
7. Storage: Who can access the data and when will it be deleted?

**Important:** Public availability does not automatically establish ethical permission for every type of use.

## 19. PII (Personally Identifiable Information)

PII refers to information that can directly or indirectly identify an individual.

Examples:
- Full name.
- Phone number.
- Email address.
- Face image.
- Username.
- Precise location.
- Other combinations of identifying information.

Researchers should identify and minimize unnecessary PII before analysis.

## 20. Data Provenance

Data provenance is the documented history and origin of a dataset, including who collected it, why, when, how, and what transformations were applied.

### Main Components

1. Origin: Creator, purpose, funding, and collection period.
2. Collection: How the data was obtained.
3. Labeling: Who labeled the data and what guidelines were used.
4. Transformations: Cleaning, filtering, deduplication, and rebalancing.
5. Documentation: Records of processing and limitations.

**Importance:** Provenance improves transparency, reproducibility, accountability, and trustworthiness.

## 21. Responsible AI Use in Research

Responsible AI use means using AI tools transparently, safely, and with human verification.

### Legitimate Uses

- Literature scanning.
- Transcription assistance.
- Coding assistance.
- Brainstorming coding schemes.
- Language polishing.

### Important Restrictions

- Do not upload identifiable participant information or raw transcripts to third-party AI tools without proper authorization and safeguards.
- Do not treat AI-generated synthetic participants as real research evidence.
- Do not use unverified AI-generated claims as citations.
- Verify all AI-generated outputs.
- Disclose AI tools and their purposes in the research report.

**Key Principle:** Researchers remain responsible for all findings, claims, data, and code, even when AI tools are used.

## 22. Dataset Ethics Note

A dataset ethics note is a document that explains whether a dataset can be responsibly and legally used for a research project.

It should include:

1. Source and Provenance: Who created the dataset, why, and how?
2. License: Does the license permit research and model training?
3. Consent Basis: Under what conditions was the original data collected?
4. PII Audit: What identifying information exists?
5. Bias and Coverage: Which groups or cases are missing or overrepresented?
6. Downstream Harm: What risks could result from using the dataset or model?
7. Storage and Access: Where is it stored and who can access it?

## 23. Ethics Considerations Draft

An ethics considerations draft describes the ethical risks and protection measures associated with a research project.

For human-participant studies, include:
- Participants and their context.
- Recruitment and consent.
- Voluntary participation.
- Potential risks and mitigation.
- Privacy and storage.
- Withdrawal procedure.
- AI-use disclosure.

For dataset/ML studies, include:
- Data source and provenance.
- License and consent basis.
- PII and anonymization.
- Bias and representation.
- Downstream harm.
- Access control and deletion.
- AI-use disclosure.

---

# IMPORTANT DIFFERENCES FOR EXAM

## 1. Quantitative vs Qualitative Research

| Quantitative | Qualitative |
|---|---|
| Uses numerical data | Uses non-numerical data |
| Measures variables | Explores meanings and experiences |
| Uses statistical analysis | Uses thematic or interpretive analysis |
| Often uses surveys and experiments | Often uses interviews and observations |
| Answers how much, how many, or how strongly | Answers how and why |

## 2. Interview vs Focus Group

| Interview | Focus Group |
|---|---|
| Usually one participant at a time | Multiple participants |
| Explores individual experiences | Explores group interaction and shared views |
| Better for sensitive personal topics | Better for shared norms and disagreements |
| Interviewer asks questions | Moderator manages discussion |

## 3. Survey vs Interview

| Survey | Interview |
|---|---|
| Structured questions | Structured or semi-structured conversation |
| Can reach many participants | Usually fewer participants |
| Often produces numerical data | Produces detailed verbal data |
| Useful for measuring prevalence | Useful for understanding experiences |

## 4. Anonymization vs Pseudonymization

| Anonymization | Pseudonymization |
|---|---|
| Identity cannot reasonably be recovered | Identity may be recovered using a separate key |
| No identity mapping is retained | Identity mapping may exist |
| Stronger identity protection | Requires secure key management |

## 5. H1 vs H0

| H1 – Alternative Hypothesis | H0 – Null Hypothesis |
|---|---|
| Predicts a relationship or difference | Predicts no relationship or difference |
| Represents the research expectation | Represents the null position tested statistically |

## 6. Week 4 vs Week 5

| Week 4 | Week 5 |
|---|---|
| Revises problem statement and RQs | Designs instruments and collection procedures |
| Identifies variables and constructs | Measures constructs using instruments |
| Selects study design | Implements ethical data collection planning |
| Identifies dataset candidates | Audits dataset ethics and provenance |
| Plans evidence and analysis | Protects participants and data subjects |

---

# IMPORTANT SHORT QUESTIONS AND ANSWERS

**Q1. What is a research gap?**

A research gap is an unanswered or underexplored issue in existing literature that requires further investigation.

**Q2. What is a research question?**

A research question is a focused and answerable question that guides a research study.

**Q3. What is a hypothesis?**

A hypothesis is a testable prediction about a relationship or difference between variables.

**Q4. What are H1 and H0?**

H1 is the alternative hypothesis, which predicts a relationship or difference. H0 is the null hypothesis, which predicts no relationship or difference.

**Q5. What is a construct?**

A construct is an abstract concept, such as trust, usability, or cognitive load, that researchers investigate.

**Q6. What is operationalization?**

Operationalization is the process of defining how an abstract construct or variable will be observed or measured.

**Q7. What is study design?**

Study design is the overall plan for collecting and analyzing evidence to answer research questions.

**Q8. What is mixed-methods research?**

Mixed-methods research combines quantitative and qualitative approaches in one study.

**Q9. What is external validity?**

External validity refers to the extent to which research findings can be generalized to other populations, settings, or contexts.

**Q10. What is reliability?**

Reliability refers to the consistency of a research measurement or procedure.

**Q11. What is a pilot study?**

A pilot study is a small preliminary test conducted to identify problems in research instruments or procedures before the main study.

**Q12. What is informed consent?**

Informed consent is the voluntary agreement of participants after they understand the purpose, procedures, risks, and conditions of a study.

**Q13. What are the three principles of the Belmont Report?**

Respect for Persons, Beneficence, and Justice.

**Q14. What is PII?**

PII stands for Personally Identifiable Information, which can directly or indirectly identify an individual.

**Q15. What is data provenance?**

Data provenance is the documented origin and history of a dataset, including its collection, labeling, and transformations.

**Q16. What is an IRB?**

An Institutional Review Board is a committee that reviews research involving human participants to protect their rights, safety, and welfare.

**Q17. What is thematic analysis?**

Thematic analysis is a qualitative method for identifying, analyzing, and reporting patterns or themes in data.

**Q18. What is usability testing?**

Usability testing evaluates how effectively and efficiently users can complete tasks using a system or product.

**Q19. What is pseudonymization?**

Pseudonymization replaces direct identifiers with codes while retaining a separate key that may allow re-identification.

**Q20. Why is dataset ethics important?**

Dataset ethics ensures that data is collected and used responsibly, legally, and fairly while protecting privacy and reducing potential harm.

**Q21. Does public data mean ethically free data?**

No. Publicly available data may still contain personal information, licensing restrictions, or ethical risks.

**Q22. Why should researchers disclose AI use?**

Researchers should disclose AI use to maintain transparency, accountability, and research integrity.

---

# FINAL REVISION CHECKLIST

## Week 4
- [ ] Problem statement and research gap
- [ ] Research question definition and characteristics
- [ ] Six types of RQs
- [ ] RQ revision checklist
- [ ] Hypothesis: H1 and H0
- [ ] Constructs, variables, and operationalization
- [ ] Quantitative, qualitative, and mixed methods
- [ ] ML study design
- [ ] Six validity considerations
- [ ] Feasibility
- [ ] Alignment matrix
- [ ] Dataset selection and quality

## Week 5
- [ ] Human-participant and dataset tracks
- [ ] Survey design and common item problems
- [ ] Sampling and recruitment
- [ ] Interview and focus group
- [ ] Observation and usability testing
- [ ] Dataset evaluation protocol
- [ ] Pilot testing
- [ ] Six phases of thematic analysis
- [ ] Three Belmont principles
- [ ] Informed consent
- [ ] Privacy and data protection
- [ ] IRB
- [ ] Dataset ethics
- [ ] PII and data provenance
- [ ] Responsible AI use
- [ ] Dataset ethics note
- [ ] Ethics considerations draft

**Exam Tip:** For a broad question, write the definition first, explain the main points in numbered form, give one relevant example, and finish with the importance or application. This structure makes answers clear and complete.