# General AI/ML Intro Slides

> These 3 slide decks + 1 paper are a general "what is AI/ML" intro — not specific to any one algorithm — so they live here as their own topic rather than inside `Linear Regression/`. Content transcribed below so it's readable on GitHub without opening PowerPoint.

---

## `The Beginning of Artificial Intelligence.pptx` — AI history & family tree

**The intelligence loop:** learn → adapt → reason → remember — the cycle intelligence (human or machine) runs on.

**Milestones:**
- **Alan Turing (1950)** — "Can machines think?"
- **Dartmouth (1956)** — the term "Artificial Intelligence" was coined; a summer workshop that (over-optimistically) set out to solve intelligence in two months. *(See the companion `Paper on Dartmouth AI Summer Project.pdf` in this folder for the original proposal.)*
- **Arthur Samuel (1959)** — built a self-playing checkers program that learned to beat its own creator; the birth of Machine Learning ("learning patterns from data instead of following manual rules").

**ANI vs AGI:**

| | ANI (Narrow) | AGI (General) |
|---|---|---|
| Scope | Expert in ONE task | Learns anything, transfers across domains |
| Today | This is all that exists | Hypothetical |
| Example | Chess engine, face recognition | Human-like general reasoning |

**The AI family tree:** Artificial Intelligence ⊃ Machine Learning ⊃ Deep Learning (a specialized ML approach using layered neural networks — input layer → hidden layers (pattern recognition) → output layer).

**Why AI is exploding *now*, not in 1950:** Big Data (enough examples to learn from) + Powerful GPUs (compute that fits in your hand) + Better Math (new algorithms in the last ~10 years) — "the perfect storm."

---

## `The ML PipeLine.pptx` — the 9-step production ML pipeline

| Step | What happens |
|---|---|
| 1. Problem Framing | Define the target variable, success metric, and whether it's Regression (predict a number) or Classification (predict a category) |
| 2. Data Collection | Structured (SQL/CSV), Unstructured (images/text/audio), or Real-time streams |
| 3. Data Preprocessing | Handle missing values, remove/cap outliers, encode categoricals |
| 4. Feature Engineering | Extraction (e.g. timestamp → day-of-week), Scaling (put features on comparable ranges), Selection (drop noise that doesn't predict the target) |
| 5. Train/Test Split | Golden rule: never let the model see test data during training (typically 80/20) |
| 6. Model Training | The algorithm iterates over the data, adjusting weights to minimize error |
| 7. Evaluation | Pick the metric that matches the cost of being wrong — e.g. Recall matters more than Precision for fraud detection, and vice versa for a spam filter |
| 8. Hyperparameter Tuning | Manually-set knobs (not learned from data) — e.g. Grid Search over tree depth |
| 9. Delivery & Monitoring | Deploy as an API; watch for **model drift** as the real world changes — ML is a living lifecycle (ingest → prep → train → deploy → monitor → repeat), not a one-off project |

---

## `Types of ML .pptx` — Supervised vs Unsupervised

**Supervised Learning** ("the teacher") — trained on labeled input→answer pairs, learns the relationship to predict on new unseen data.
- **Regression** — predicts a number ("how much?") — e.g. house price from size/location/age.
- **Classification** — predicts a category ("which group?") — e.g. spam vs inbox, benign vs malignant.

**Unsupervised Learning** ("the explorer") — no labels; the model finds structure on its own.
- **Clustering** — groups data points by hidden similarity, without knowing what the groups "mean" — e.g. a retail dataset splitting into "young tech-heavy spenders," "weekly grocery shoppers," "occasional luxury buyers" with no pre-set labels.

| | Supervised | Unsupervised |
|---|---|---|
| Data | Labeled | Unlabeled |
| Goal | Predict a specific output | Find hidden structure |
| Feedback | Direct (correct/incorrect) | None |
| Tasks | Regression, Classification | Clustering |

This maps directly onto the folder structure one level up: `ML - Algorithm/Supervised/` and `ML - Algorithm/Unsupervised/`.
