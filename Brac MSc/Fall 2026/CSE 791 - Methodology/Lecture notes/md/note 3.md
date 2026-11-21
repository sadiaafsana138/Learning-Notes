# WEEK 5 — ADDITIONAL SLIDE CONTENT

## Add to Section 1: Human-Centered Research

### Continuity from Week 4

Week 4 produced revised research questions and a study design outline. Week 5 converts that design into actual research instruments and an ethical data collection plan.

The process is:

1. Design Outline: Revised RQs, constructs, methods, and evidence sources.
2. Instruments: Survey questions, interview guides, observation protocols, usability tasks, or dataset evaluation protocols.
3. Ethics Plan: Consent, recruitment, privacy, risk mitigation, storage, and review.
4. Responsible Collection: Pilot testing followed by documented data collection.

**Important Rule:** No instrument should reach participants and no dataset should enter the research pipeline before the relevant ethical questions have been addressed in writing.

A project using both human participants and datasets must complete both evidence-track deliverables.

---

## Add to Section 5: Survey Design

### Additional Survey Design Principles

1. Keep course-level surveys ideally within 10 minutes.
2. Prefer validated scales such as SUS, NASA-TLX, and published trust or credibility scales.
3. Adapt published scales with proper citation rather than inventing new measures unnecessarily.
4. Keep response scales consistent and label every scale point clearly.
5. Include a genuine neutral or "Prefer not to answer" option where appropriate.
6. Every survey item should map to a construct in the Week 4 variable map.

**Important:** Every additional question increases respondent effort and may reduce the completion rate.

---

## Add to Section 7: Interview Design

### Asking About Actual Behaviour

Researchers should prefer questions about concrete, recent experiences rather than hypothetical opinions.

Example:

- Better: "Walk me through the last time you verified a social media post."
- Less informative: "Would you use a verification tool?"

Concrete examples help participants describe what they actually did rather than what they think they might do.

---

## Add to Section 8: Focus Groups

### When Should We Use a Focus Group?

A focus group should be selected when group interaction itself is important research evidence.

It is useful for understanding:
- Shared beliefs and social norms.
- Agreement and disagreement.
- Community language.
- How participants' opinions change during discussion.

**Confidentiality Limitation:** Researchers can explain their own confidentiality responsibilities, but cannot guarantee that other participants will keep the discussion private. This limitation must be explained during consent.

---

## Add to Section 9: Observation

### Additional Ethical Considerations

Online observation includes forums, social media groups, and public comment threads.

However, public availability does not automatically mean that participants have consented to research use.

Researchers should:
- Consider privacy expectations.
- Anonymize identifiable information.
- Avoid verbatim quotations that can be traced through search engines when this creates privacy risks.
- Document the researcher's presence and role.

### Combining Observation and Interviews

Observation helps researchers understand what people actually do, while follow-up interviews help explain why they behave that way.

Combining both methods can provide complementary evidence.

---

## Add to Section 10: Usability Testing

### Additional Usability Testing Principles

**Task Design:** Tasks should be realistic, goal-based, and have clearly defined success criteria.

Example:
- Weak: "Explore the application."
- Strong: "Find a suspicious post and report it using the application."

**Think-Aloud Limitation:** Participants explain their thoughts while performing tasks. This helps identify confusion and reasoning, but may slightly affect task completion time.

**Small-Sample Logic:** Around five users may reveal many usability problems and support iterative improvement. However, this does not automatically provide a sufficient sample for statistical hypothesis testing.

---

## Add to Section 11: Dataset-Track Research Methods

### A. Existing Dataset Studies

Before model training:
1. Select a dataset against explicit research requirements.
2. Finalize train/test splits.
3. Define baseline models.
4. Select suitable evaluation metrics.
5. Plan ablation studies where applicable.

Dataset selection is a research design decision, not simply a process of choosing a popular dataset.

### B. Logged or Scraped Data

Researchers should:
- Check platform Terms of Service (ToS) and API rules.
- Define the data collection period.
- Document search queries and sampling procedures.
- Handle PII during data ingestion rather than waiting until after model training.

### C. Self-Collected and Annotated Data

Researchers should:
- Prepare written annotation guidelines.
- Use at least two annotators on a sample where feasible.
- Measure inter-annotator agreement, such as Cohen's kappa.
- Document labeling instructions and limitations.

---

## Add to Section 12: Instrument Quality and Pilot Testing

### Additional Instrument Quality Principles

A good instrument should produce consistent interpretations across participants.

Researchers should check:
- Whether participants understand the questions consistently.
- Whether response scales behave as expected.
- Whether interview questions produce relevant and answerable responses.
- Whether the instrument works across different education levels in the target population.

**Important:** If a pilot participant cannot understand a question, the researcher should reconsider the wording instead of blaming the participant.

---

## Add to Section 13: Thematic Analysis

### Practical Planning Before Data Collection

Researchers should consider analysis requirements before collecting qualitative data.

Important considerations:
1. Consent must explicitly cover audio or video recording.
2. One hour of audio may require approximately 4–6 hours of transcription.
3. For multilingual research, code the data in its original language where feasible.
4. Translate themes rather than unnecessarily translating all raw quotations before analysis.
5. Maintain a clear record of coding and theme development.

**Important:** Themes are developed through systematic analytical work. They do not automatically emerge from the data.

---

## Add to Section 15: Informed Consent

### Additional Elements of Consent

The consent document should also explain:

1. What happens to already-collected data if a participant withdraws.
2. Whether audio or video recording is involved.
3. That recording permission is a separate decision from general participation consent.

**Important:** Participants consent to a specific research purpose and data use, not to any future use the researcher may decide later.

---

## Add to Section 16: Privacy and Data Protection

### Indirect Identifiers

Information that does not directly identify a person may still identify them when combined with other details.

Example:
- Role
- Department
- Gender
- Institution

In a small research community, this combination may identify a specific individual.

Researchers should generalize or aggregate such information when necessary.

### Data Protection Principle

Use encrypted and access-controlled storage, keep identity keys separate, and establish a clear retention and deletion plan.

---

## Add to Section 17: IRB and Ethics Review

### Risk-Benefit Assessment

Before data collection, researchers should identify:

1. The worst realistic harm that could happen to a participant.
2. The likelihood of that harm.
3. The possible impact.
4. The measures taken to prevent or reduce it.

If the risks cannot be adequately managed, the research design should be revised.

### Course-Level Review

According to the lecture's course-level guidance, the instructor should review instruments and ethics considerations before data collection begins. Formal thesis research may require the university's designated ethics review process.

---

## Add to Section 18: Dataset Ethics

### Scraping, Licensing, and Secondary Use

**Scraping and Terms of Service:**
Technically downloadable data is not automatically permitted for research use. Researchers should check platform rules and API restrictions.

**Licensing:**
A dataset's license should explicitly support the intended research use, redistribution, or model training where applicable.

**Secondary Use:**
Data collected for one purpose may carry expectations that restrict unrelated future uses.

Example: Using sensitive crisis-related social media posts to train an unrelated model may create ethical risks even if the posts are publicly accessible.

**Comfort Test:** Researchers should consider whether the people represented in the dataset would reasonably be comfortable with the specific intended use.

---

## Add to Section 20: Data Provenance

### Additional Provenance Requirements

Provenance should also document:
- Funding and collection purpose.
- Sampling and collection methods.
- Annotator instructions and agreement.
- Annotation labor and payment conditions, where relevant.
- Dataset versioning.
- Every major preprocessing and cleaning decision.

Researchers are also data creators when they collect, filter, label, or transform datasets.

**Important:** If dataset provenance cannot be established, its size or popularity does not make it trustworthy.

---

## Add to Section 22: Dataset Ethics Note

### Recommended Length and Documentation

A dataset ethics note should generally be around 1–2 pages for the course milestone.

Every statement should have a checkable basis.

If information about consent, provenance, or licensing is unavailable, explicitly write "Unknown" rather than making assumptions.

---

## Add to Section 23: Ethics Considerations Draft

### Additional Requirements

For human-participant studies:
- Include withdrawal rights and a contact point.
- Explain what happens to already-collected data after withdrawal.

For dataset/ML studies:
- Include a process for handling data takedown requests.
- Identify a contact point for concerns about the dataset or its use.

The draft should generally be 1–2 pages and contain project-specific ethical risks and protection measures rather than generic template statements.

---

## Additional Section: Dataset Requirement Audit

Before selecting a dataset, researchers should derive explicit requirements from the RQ.

### Step 1: Define Requirements

Specify:
- Research task and labels.
- Unit of analysis.
- Target population or domain.
- Conditions and time period.
- Minimum dataset scale and class requirements.
- License and provenance requirements.

### Step 2: Audit the Dataset

1. Read the dataset paper or datasheet.
2. Inspect approximately 50–100 samples manually where feasible.
3. Check label correctness.
4. Identify duplicates.
5. Verify whether the actual content matches the dataset description.

### Step 3: Make a Decision

| Decision | Meaning |
|---|---|
| Fit | Meets the core research requirements |
| Partial Fit | Has limitations but each has a realistic mitigation |
| Reject | A core requirement fails without an honest mitigation |

### Worked Example: Dataset Fit

**Research Question:** To what extent can a detection model identify helmet non-use among motorcycle riders in Dhaka daytime traffic images?

**Candidate Dataset:** A public helmet dataset collected from Indian urban traffic CCTV.

| Requirement | Candidate limitation | Decision |
|---|---|---|
| Task and labels | Helmet boxes are available but not linked to individual riders | Partial fit |
| Domain | Indian urban traffic differs from Dhaka traffic | Domain shift risk |
| Conditions | Daytime and dry weather only | Narrow the claim |
| Class balance | 12,000 helmet vs. 1,800 no-helmet instances | Imbalance risk |
| License | CC BY-NC 4.0 | Research use subject to license conditions |
| Provenance | No clear annotator agreement information | Document uncertainty |

**Conclusion:** The dataset may be partially suitable if limitations are addressed. The generalization claim must be restricted to the conditions actually represented by the data.

---

## Additional Section: Week 5 Workshop

### Instrument and Ethics Design Workshop

The workshop follows four steps:

| Step | Activity | Expected Output |
|---|---|---|
| 1 — 10 min | Map each RQ to an instrument or data source | Instrument-RQ map |
| 2 — 25 min | Draft survey/interview/usability tasks or audit a dataset | Draft instrument or dataset audit |
| 3 — 15 min | Peer-review consent, coercion, privacy, and provenance | Written risk list |
| 4 — 10 min | Revise the draft and record unresolved questions | Revised draft and open questions |

**Workshop Question:** What is the worst realistic thing that could happen to a participant or data subject, and where does your draft address that risk?

---

## Additional Section: Recommended Reading Materials

| Topic | Recommended Reading |
|---|---|
| HCI Methods | Lazar, Feng & Hochheiser — Research Methods in Human-Computer Interaction |
| Thematic Analysis | Braun & Clarke — Using Thematic Analysis in Psychology (2006) |
| Research Ethics | The Belmont Report |
| Survey Design | Groves et al. — Survey Methodology |
| Dataset Ethics | Gebru et al. — Datasheets for Datasets |
| Responsible AI | ACM Code of Ethics and target publication venue's AI-use policy |

**Week 5 Milestone:** Bring a draft instrument or dataset ethics note, an ethics considerations draft, and one unresolved ethical question for discussion.