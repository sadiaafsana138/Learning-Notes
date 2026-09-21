# Deep Learning — Learning Notes (Mod 1–6)

A complete, hands-on collection of Deep Learning fundamentals from the Phitron course, with one
consolidated cheatsheet notebook plus the original module-by-module folders.

---

## TL;DR — Just open this one file

**[`DL_FULL_Cheatsheet.ipynb`](./DL_FULL_Cheatsheet.ipynb)**

Everything below is merged into that single notebook in the correct teaching order — biological
neuron → perceptron → why it fails (XOR) → gradient descent → differentiable activation functions →
stacking into an MLP → backprop/optimizers/regularization. It's runnable top to bottom with only
`numpy`, `pandas`, and `matplotlib` (no sklearn/tensorflow needed).

---

## Folder structure

```
DL_Learning_Notes/
├── DL_FULL_Cheatsheet.ipynb        <-- start here (everything merged)
├── README.md
│
├── Mod 1/
│   ├── drawing/
│   │   ├── intro.pdf                        (why DL, use cases)
│   │   ├── ml_vs_dl.pdf                      (ML vs DL, architecture/representation/non-linear)
│   │   ├── biological_neuron.pdf             (McCulloch & Pitts 1943, neuron -> logic gates)
│   │   ├── ann.pdf                           (biological neuron -> artificial neuron diagram)
│   │   ├── non_linearity.pdf                 (why linear boundaries aren't enough)
│   │   └── perceptron.pdf                    (perceptron structure + weight update derivation)
│   ├── Grokking Deep Learning by Andrew W. Trask (z-lib.org).pdf   (reference textbook)
│   ├── mini_project.ipynb                    (sklearn Perceptron on Iris, binary classification)
│   └── non_linear_pattern.ipynb              (two-spiral dataset: linear model vs. Keras MLP)
│
├── mod 2/
│   ├── drawing/
│   │   ├── intro.pdf                         (supervised algorithm intro, activation fn recap)
│   │   ├── solve_and_gate.pdf                (AND gate solved by hand, weight update formula)
│   │   └── weight_updation.pdf               (worked numeric perceptron update example)
│   └── 2_perceptron.ipynb                    (from-scratch Perceptron class; AND/OR/XOR demo)
│
├── mod 3/
│   ├── Module 03 Notebook.pdf                (decision boundary as Ax+By+C=0, misclassification
│   │                                          count as error, coefficient update rule)
│   └── Module 03 Notebook.png                (same content, rasterized)
│
├── mod 4/
│   ├── gradient descent.pdf                  (loss surface, mountain-descent analogy, dL/dm, dL/db)
│   ├── Loss Function.pdf                     (perceptron-vs-GD table, hinge loss derivation)
│   └── gradient_descent.ipynb                (from-scratch GDRegressor vs sklearn LinearRegression)
│
├── mod 5/
│   ├── Activation Funciton.pdf               (sigmoid derivation, ReLU, Leaky ReLU, tanh, softmax)
│   ├── Advantage and disadvantage of perceptron.pdf
│   ├── Binary Cross Entropy.pdf              (max-likelihood derivation of BCE)
│   ├── Blog and visulization links.docx      (reference links, see "Further reading" below)
│   └── 3_activation_functions.ipynb          (70-cell activation-function zoo with plots)
│
└── mod 6/
    ├── Main Idea.pdf                         (why stacking perceptrons -> non-linear regions)
    └── MLP Notation.pdf                      (layer/weight/bias notation, forward-prop matrix math,
                                                trainable-parameter counting)
```

The cheatsheet does **not** read any files from these subfolders — every dataset it needs (AND/OR/XOR
truth tables, the two-spiral dataset, synthetic regression data) is generated inline with `numpy`, so
it runs standalone anywhere.

---

## What's covered

### 1. ML vs DL, the biological neuron, non-linearity (Mod 1)
Why DL over classical ML (feature engineering, dataset size, pattern complexity), the McCulloch &
Pitts (1943) artificial neuron modeled on dendrites/soma/axon, and why a network needs a **non-linear
activation** — demonstrated with the two-spiral dataset that a linear classifier can't separate.

### 2. The Perceptron (Mod 1 & 2)
Structure ($z = w^Tx+b$, step activation), the **perceptron learning rule**
$w_{new}=w_{old}+\eta(y-\hat y)x_i$, a worked numeric example, and a from-scratch `Perceptron` class
solving AND and OR — then **failing** on XOR (not linearly separable), which sets up Section 8's MLP.

### 3. Perceptron advantages & disadvantages (Mod 5)
Simple/fast/efficient vs. linearly-separable-only, can't solve XOR, non-differentiable step function,
no probability output, no hidden layer.

### 4. Decision boundaries as line coefficients (Mod 3)
Generalizing $w_1x_1+w_2x_2+b=0$ to $Ax+By+C=0$; misclassification count as the error signal;
coefficient update rule identical in form to the perceptron rule.

### 5. Gradient Descent (Mod 4)
Loss surface for linear regression ($L=\sum(y-mx-b)^2$), the mountain-descent analogy, deriving
$\partial L/\partial m$ and $\partial L/\partial b$, and a **perceptron-rule vs. gradient-descent**
comparison table. Includes a from-scratch `GDRegressor` that converges to the same coefficients as
closed-form linear regression.

### 6. Loss functions (Mod 4 & 5)
MSE, **hinge/perceptron loss** ($\max(0,-y_if(x_i))$, with sub-gradient derivation), and **Binary
Cross-Entropy** derived from maximum likelihood, with a worked numeric example.

### 7. Activation functions — the full zoo (Mod 5)

| Function | Formula | Range |
|---|---|---|
| Sigmoid | $1/(1+e^{-x})$ | $(0,1)$ |
| Tanh | $(e^x-e^{-x})/(e^x+e^{-x})$ | $(-1,1)$ |
| ReLU | $\max(0,x)$ | $[0,\infty)$ |
| Leaky ReLU | $x$ or $\alpha x$ | $(-\infty,\infty)$ |
| ELU | $x$ or $\alpha(e^x-1)$ | $(-\alpha,\infty)$ |
| Softmax | $e^{x_j}/\sum_k e^{x_k}$ | sums to 1 |
| Swish, Softplus, Softsign | — | quick-reference only |

Each core function (sigmoid, tanh, ReLU, Leaky ReLU, ELU, softmax) gets its formula, hand-derived
derivative where the notes derive one, a plot, and pros/cons.

### 8. The Multi-Layer Perceptron (Mod 6)
The "main idea" — stacking perceptrons combines multiple linear boundaries into non-linear decision
regions — plus formal notation ($b_{ij}$, $W^k_{ij}$), a worked trainable-parameter count (26 params
for a 4-3-2-1 network), and a matrix-form forward-propagation walkthrough. Two capstone demos:
a from-scratch MLP that **solves XOR** (where the Section 2 perceptron failed), and the same MLP
solving the Section 1 spiral dataset.

### 9. Quick-reference summary
Consolidated activation-function and loss-function tables, plus the "golden order" of concepts.

### Beyond the modules — bonus deep-dive (Section 10)
Not in the original course notes, added for completeness:
- **Backpropagation** — the chain rule worked by hand through a tiny 2-layer network
- **Vanishing / exploding gradients** and why ReLU helps
- **Weight initialization** — why zero-init fails; Xavier and He init
- **Optimizers** — momentum, RMSprop, Adam (formulas + a GD-vs-momentum demo)
- **Regularization** — L1/L2, dropout, early stopping, batch normalization
- **Categorical cross-entropy** — the multi-class generalization of BCE + softmax

---

## How to run

1. `pip install numpy pandas matplotlib`
2. Open `DL_FULL_Cheatsheet.ipynb` in Jupyter or VS Code.
3. Run cells top to bottom — every section reuses helper functions (`sigmoid`, `binary_cross_entropy`,
   the `AND`/`OR`/`XOR` DataFrames, the spiral dataset) defined earlier, so order matters.

---

## Further reading (from `mod 5/Blog and visulization links.docx`)

- [Binary Cross-Entropy / Log Loss — GeeksforGeeks](https://www.geeksforgeeks.org/deep-learning/binary-cross-entropy-log-loss-for-binary-classification/)
- [The Role of Softmax in Neural Networks — GeeksforGeeks](https://www.geeksforgeeks.org/deep-learning/the-role-of-softmax-in-neural-networks-detailed-explanation-and-applications/)
- [Softmax visualization (Desmos)](https://www.desmos.com/calculator/drqqhtb037)
- [Log calculator](https://www.calculator.net/log-calculator.html)

---

## Notes — things worth remembering

- The perceptron update rule is always **`new = old + η × error × input`** (error `= y - ŷ`) — every
  later "coefficient update" (Mod 3's line coefficients, gradient descent's `w -= η × slope`) is a
  variation of this same idea.
- **Always split → impute/handle-missing → then fit**, but for perceptrons specifically: check
  **linear separability** before trusting convergence — a perceptron will loop forever on XOR-like
  data since Rosenblatt's convergence theorem only guarantees convergence when a separating
  hyperplane exists.
- **ReLU is the default hidden-layer activation** today mainly because its derivative is exactly `1`
  for positive inputs — it doesn't vanish the way sigmoid/tanh gradients do across many layers.
- **BCE loss simplifies beautifully when paired with a sigmoid output**: the combined gradient
  $\partial L/\partial z = (\hat y - y)$ is what makes the `SimpleMLP.backward` code in Section 8.4 so
  short — this pairing (sigmoid + BCE, or softmax + categorical cross-entropy) is standard practice,
  not a coincidence.
- **Weight init must break symmetry** — never initialize a real network's weights to all zeros
  (Section 10.3); it's fine for a *single* perceptron (Section 2) only because there's no layer
  behind it to become symmetric with.
