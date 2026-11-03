# Generated: L-2/L-3 Quiz Bank-এর missing অংশ

> ⚠️ **এগুলো PDF-এ নেই, আমি generate করেছি।** Bank-এর header-এ "25 T/F" আর "10 graph" লেখা, কিন্তু PDF-এ আছে 19 T/F আর 5 graph।
> সব মান/fact merged PDF + bank থেকে নেওয়া (source প্রতিটার পাশে)। অনুমান কিছু নেই।

---

## Part II (continued) — T/F 20–25 (generated)

20. Linear regression can be viewed as a single neuron with an identity activation function.
    **True.** ŷ=wᵀx+b ; neuron z=wᵀx+b, a=f(z) with f(z)=z. *(merged_L2 p3)*

21. Stacking several linear layers without any nonlinear activation can represent a nonlinear function such as y=x².
    **False.** W₂(W₁x+b₁)+b₂ = (W₂W₁)x+(W₂b₁+b₂), এখনও linear/affine। *(merged_L2 p14; merged-KL p15)*

22. For the half-squared loss L=½(ŷ−y)², the derivative is ∂L/∂ŷ = ŷ−y.
    **True.** ½ factor 2-এর সাথে কেটে যায়। *(bank notation guide)*

23. For a dataset with errors 0, 0, 0 and −1, the MSE is 1.
    **False.** MSE = (0+0+0+1)/4 = **0.25**, শুধু sum না, average। *(merged_L2 p4)*

24. If a hidden unit's ReLU output h₂ is 0, the gradient ∂L/∂v₂ is also 0 for that example.
    **True.** ∂L/∂v₂=(ŷ−y)h₂=0; inactive neuron error back করে না। *(merged_L2 p22–24)*

25. The output activation of a network is chosen by the task type: linear for continuous regression, sigmoid for binary and softmax for multiclass classification.
    **True.** Hidden layer-এ ReLU, output activation task নির্ধারণ করে। *(merged_L2 p18)*

---

## Part IV (continued) — Graph Plotting Exercises 6–10 (generated)

Reference plot: `Generated_Graphs_6-10.png` (এই folder-এ; ৬ষ্ঠ panel extra)

### Graph Plotting Exercise 6. Bias effect
**Task:** Plot ŷ=2x (b=0) and ŷ=2x+5 on the same axes.
**Points:** x=0 → (0,0) ও (0,5); x=1 → (1,2) ও (1,7); x=2 → (2,4) ও (2,9)।
**Check:** দুটো line parallel (slope w=2 একই); প্রথমটা origin দিয়ে যায়; দ্বিতীয়টা y-axis কাটে 5-এ, bias = intercept। *(merged_L2 p4–5)*

### Graph Plotting Exercise 7. Softmax output
**Task:** Draw a bar chart of the softmax probabilities for logits z=[2,1,0].
**Points:** e²=7.389, e¹=2.718, e⁰=1, sum=11.107 → bars 0.665, 0.245, 0.090।
**Check:** সবচেয়ে বড় logit-এর bar সবচেয়ে উঁচু; bar-এর যোগফল 1.000। *(Problem 10)*

### Graph Plotting Exercise 8. Binary cross-entropy, y=1
**Task:** Plot L(p)=−ln p for p from 0.1 to 0.9 and mark p=0.1, 0.5, 0.8.
**Points:** (0.1,2.3026), (0.2,1.6094), (0.3,1.2040), (0.4,0.9163), (0.5,0.6931), (0.6,0.5108), (0.7,0.3567), (0.8,0.2231), (0.9,0.1054)।
**Check:** p বাড়লে loss কমে; p→0 হলে loss খুব বড়; p=1-এ loss 0। *(Ch6 D3; merged-KL p4)*

### Graph Plotting Exercise 9. Loss versus iteration in gradient descent
**Task:** For f(x)=x², x₀=4, η=0.1, plot f(xₜ) against iteration t for t=0…9.
**Points:** 16.0000, 10.2400, 6.5536, 4.1943, 2.6844, 1.7180, 1.0995, 0.7037, 0.4504, 0.2882 (exact; image-এ t=5,6,8,9-এ ছোট ছাপার ভুল আছে: 1.7189, 1.1005, 0.4503, 0.2883)।
**Check:** প্রতি step-এ কমে; কমার পরিমাণ ক্রমশ ছোট (slope ছোট হচ্ছে); 0-এর দিকে যায়। *(f_x_gradient_descent.webp)*

### Graph Plotting Exercise 10. One SGD update on logistic regression
**Task:** Draw a bar chart of the BCE loss before and after one SGD step (x=2, y=1, w=b=0, η=0.1).
**Points:** before 0.6931 (p=0.5000); after 0.5759 (p=0.5622); w=0.10, b=0.05।
**Check:** loss কমেছে ~0.1172; p সঠিক class (y=1)-এর দিকে বেড়েছে। *(Ch6 C7–C8; merged-KL p6–7)*

*(Extra, panel 6:)* Dataset A–D residual: ŷ=2x₁+3x₂+5-এর D point-এ y=35, ŷ=36, r=−1, error²=1, MSE=0.25। *(merged_L2 p4)*

---

## Updated counts (generated সহ)
| | PDF-এ আছে | Generated | মোট (header অনুযায়ী) |
|---|---|---|---|
| T/F | 19 | 6 (T/F 20–25) | 25 |
| Graph | 5 | 5 (Ex. 6–10) | 10 |
