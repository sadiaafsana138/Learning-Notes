# MACHINE LEARNING & DEEP LEARNING
## Master Viva Notes — Complete
### English Answer + বাংলা ব্যাখ্যা | প্রতিটি topic 1–5 lines | কিছু বাদ না দেওয়ার জন্য consolidated version

> **Coverage:** ML/DL Basics + Part 2-এর সব listed topic, formulas, comparisons, viva questions, revision checklist.

---

# PART A — MACHINE LEARNING BASICS

## 1. Artificial Intelligence (AI)
**English Answer:** Artificial Intelligence is the broad field of making machines perform tasks that normally require human intelligence.  
**বাংলা ব্যাখ্যা:** Human intelligence-এর মতো কাজ machine দিয়ে করানোর broad field হলো AI।

## 2. Machine Learning (ML)
**English Answer:** Machine Learning is a subset of AI where systems learn patterns from data without being explicitly programmed for every rule.  
**বাংলা ব্যাখ্যা:** Data থেকে pattern শিখে নিজে prediction/decision করার পদ্ধতি।

## 3. Deep Learning (DL)
**English Answer:** Deep Learning is a subset of ML that uses multi-layer neural networks to automatically learn features from data.  
**বাংলা ব্যাখ্যা:** Multiple neural-network layer ব্যবহার করে data থেকে feature নিজে শেখে।

## 4. AI vs ML vs DL
**English Answer:** AI is the broadest field; ML is a subset of AI; DL is a subset of ML. Thus, **AI ⊃ ML ⊃ DL**.  
**বাংলা ব্যাখ্যা:** AI সবচেয়ে বড় field, তার ভিতরে ML, আর ML-এর ভিতরে DL।

## 5. Traditional Programming vs ML
**English Answer:** Traditional programming uses rules + data to produce output; ML uses data + known outputs to learn rules/patterns.  
**বাংলা ব্যাখ্যা:** Traditional = rules + data → output; ML = data + output → learned model।

## 6. ML vs DL
**English Answer:** ML often requires manual feature engineering and less data; DL learns features automatically and usually needs more data and computation.  
**বাংলা ব্যাখ্যা:** ML-এ feature manually বানাতে হয়; DL নিজে feature শেখে এবং সাধারণত বেশি data/GPU লাগে।

---

# TYPES OF MACHINE LEARNING

## 7. Supervised Learning
**English Answer:** Supervised learning learns from labeled data where each input has a known target/output.  
**বাংলা ব্যাখ্যা:** Input-এর সাথে correct answer/label দেওয়া থাকে; model সেই relationship শেখে।

## 8. Classification
**English Answer:** Classification predicts a discrete class or category, such as spam/not-spam.  
**বাংলা ব্যাখ্যা:** উত্তর যদি “কোনটা?” হয়—যেমন spam না normal—তাহলে classification।

## 9. Regression
**English Answer:** Regression predicts a continuous numerical value, such as price, temperature, or sales.  
**বাংলা ব্যাখ্যা:** উত্তর যদি “কত?” হয়—যেমন price বা temperature—তাহলে regression।

## 10. Unsupervised Learning
**English Answer:** Unsupervised learning learns from unlabeled data to discover hidden patterns, groups, or structure.  
**বাংলা ব্যাখ্যা:** কোনো label নেই; model নিজেই data-এর pattern/group খুঁজে।

## 11. Clustering
**English Answer:** Clustering groups similar data points together without predefined class labels.  
**বাংলা ব্যাখ্যা:** Similar data একসাথে group করা; যেমন customer segmentation।

## 12. Dimensionality Reduction
**English Answer:** Dimensionality reduction reduces the number of features while preserving as much useful information as possible.  
**বাংলা ব্যাখ্যা:** অনেক feature কমিয়ে গুরুত্বপূর্ণ information ধরে রাখা; PCA একটি common method।

## 13. Semi-Supervised Learning
**English Answer:** Semi-supervised learning uses a small amount of labeled data together with a larger amount of unlabeled data.  
**বাংলা ব্যাখ্যা:** কিছু data labeled, বেশিরভাগ unlabeled; labeling expensive হলে useful।

## 14. Reinforcement Learning
**English Answer:** Reinforcement learning trains an agent through interaction with an environment using rewards or penalties.  
**বাংলা ব্যাখ্যা:** Agent action নেয়, ভালো হলে reward, খারাপ হলে penalty—এভাবে policy শেখে।

## 15. Reinforcement Learning Components
**English Answer:** Main components are agent, environment, state, action, reward, and policy.  
**বাংলা ব্যাখ্যা:** Agent + Environment + State + Action + Reward + Policy—এইগুলো মূল অংশ।

## 16. ML Type Comparison
| Type | Data | Main Goal | Examples |
|---|---|---|---|
| Supervised | Labeled | Prediction | Linear/Logistic Regression, SVM, KNN |
| Unsupervised | Unlabeled | Pattern discovery | K-Means, PCA |
| Semi-supervised | Labeled + Unlabeled | Learn with limited labels | Self-training |
| Reinforcement | Reward signal | Maximize reward | Q-Learning, DQN |

---

# COMMON ML ALGORITHMS

## 17. Linear Regression
**English Answer:** Linear Regression models a continuous target using a linear relationship, commonly written as **ŷ = wx + b**.  
**বাংলা ব্যাখ্যা:** Data-এর মধ্যে best-fit straight line বসিয়ে continuous value predict করে।

## 18. Logistic Regression
**English Answer:** Logistic Regression is a supervised classification algorithm that commonly uses the sigmoid function to produce probabilities.  
**বাংলা ব্যাখ্যা:** নাম regression হলেও এটি মূলত classification-এর জন্য ব্যবহৃত হয়।

## 19. K-Nearest Neighbors (KNN)
**English Answer:** KNN predicts a new point using the labels/values of its k nearest training examples.  
**বাংলা ব্যাখ্যা:** কাছের k জন neighbor দেখে majority vote/average দিয়ে prediction করে।

## 20. Decision Tree
**English Answer:** A Decision Tree makes predictions through a sequence of feature-based decisions represented as a tree of nodes and leaves.  
**বাংলা ব্যাখ্যা:** Question/condition-এর গাছ; node-এ condition, leaf-এ final answer।

## 21. Random Forest
**English Answer:** Random Forest is an ensemble of many Decision Trees whose predictions are combined to improve generalization and reduce variance.  
**বাংলা ব্যাখ্যা:** অনেক Decision Tree-এর combined vote; একক tree-এর overfitting কমায়।

## 22. Support Vector Machine (SVM)
**English Answer:** SVM finds a decision boundary, or hyperplane, that maximizes the margin between classes.  
**বাংলা ব্যাখ্যা:** দুই class-এর মাঝে সবচেয়ে বড় margin রেখে boundary তৈরি করে।

## 23. Naive Bayes
**English Answer:** Naive Bayes applies Bayes' theorem while assuming the features are conditionally independent given the class.  
**বাংলা ব্যাখ্যা:** Bayes theorem ব্যবহার করে এবং feature-গুলো independent ধরে নেয়।

## 24. K-Means
**English Answer:** K-Means is an unsupervised clustering algorithm that assigns points to the nearest centroid and repeatedly updates centroids.  
**বাংলা ব্যাখ্যা:** kটি cluster বানিয়ে nearest centroid অনুযায়ী data assign করে এবং centroid update করে।

### K-Means Steps
1. kটি initial centroid choose.
2. প্রতিটি point nearest centroid-এ assign.
3. প্রতিটি cluster-এর mean নিয়ে নতুন centroid.
4. Centroid stable না হওয়া পর্যন্ত repeat.

## 25. PCA
**English Answer:** Principal Component Analysis reduces dimensionality by projecting data onto directions that capture high variance.  
**বাংলা ব্যাখ্যা:** বেশি variance-এর direction ধরে feature/dimension কমায়।

---

# MODEL TRAINING & EVALUATION

## 26. Training Set
**English Answer:** Training data is used by the model to learn parameters.  
**বাংলা ব্যাখ্যা:** Model training/learning-এর জন্য ব্যবহার করা data।

## 27. Validation Set
**English Answer:** Validation data is used during model development to tune hyperparameters and compare models.  
**বাংলা ব্যাখ্যা:** Hyperparameter/model selection-এর জন্য ব্যবহৃত data।

## 28. Test Set
**English Answer:** Test data is used for final unbiased evaluation after model development is complete.  
**বাংলা ব্যাখ্যা:** Final performance মাপার জন্য আলাদা data।

## 29. Cross-Validation
**English Answer:** In k-fold cross-validation, data is divided into k folds and each fold is used for validation while the others are used for training.  
**বাংলা ব্যাখ্যা:** Data k ভাগ করে পালা করে validation নিয়ে average performance বের করা হয়।

## 30. Overfitting
**English Answer:** Overfitting occurs when a model learns training data too closely, achieving high training performance but poor generalization to unseen data.  
**বাংলা ব্যাখ্যা:** Model training data মুখস্থ করে ফেলে; train ভালো কিন্তু test খারাপ। এটি high variance।

## 31. Underfitting
**English Answer:** Underfitting occurs when a model is too simple to capture the underlying pattern, resulting in poor training and test performance.  
**বাংলা ব্যাখ্যা:** Model যথেষ্ট শেখেইনি; train ও test দুটোতেই performance কম। এটি high bias।

## 32. Bias-Variance Tradeoff
**English Answer:** Bias represents error from overly simple assumptions, while variance represents sensitivity to training data; a good model balances both.  
**বাংলা ব্যাখ্যা:** Model খুব simple হলে bias বেশি, খুব complex হলে variance বেশি; মাঝামাঝি balance দরকার।

## 33. Regularization
**English Answer:** Regularization adds a penalty to the learning objective to discourage overly complex models and reduce overfitting.  
**বাংলা ব্যাখ্যা:** Model-এর complexity control করে overfitting কমানো।

## 34. L1 Regularization
**English Answer:** L1 regularization penalizes the absolute values of weights and can drive some weights exactly to zero.  
**বাংলা ব্যাখ্যা:** কিছু weight zero করে feature selection-এ সাহায্য করে; Lasso।

## 35. L2 Regularization
**English Answer:** L2 regularization penalizes squared weights and generally shrinks weights toward zero without forcing many to exactly zero.  
**বাংলা ব্যাখ্যা:** Weight ছোট করে; সাধারণত zero করে না; Ridge।

---

# CONFUSION MATRIX & METRICS

## 36. Confusion Matrix
**English Answer:** A confusion matrix summarizes binary classification results using TP, TN, FP, and FN.  
**বাংলা ব্যাখ্যা:** Prediction-এর চার ধরনের outcome: True Positive, True Negative, False Positive, False Negative।

```text
                 Predicted
              Positive Negative
Actual Pos       TP       FN
Actual Neg       FP       TN
```

## 37. True Positive (TP)
**English Answer:** The model predicts positive and the actual class is positive.  
**বাংলা ব্যাখ্যা:** সত্যিই positive এবং model-ও positive বলেছে।

## 38. True Negative (TN)
**English Answer:** The model predicts negative and the actual class is negative.  
**বাংলা ব্যাখ্যা:** সত্যিই negative এবং model-ও negative বলেছে।

## 39. False Positive (FP)
**English Answer:** The model predicts positive but the actual class is negative.  
**বাংলা ব্যাখ্যা:** আসলে negative, কিন্তু model positive বলেছে; false alarm।

## 40. False Negative (FN)
**English Answer:** The model predicts negative but the actual class is positive.  
**বাংলা ব্যাখ্যা:** আসলে positive, কিন্তু model ধরতে পারেনি।

## 41. Accuracy
**English Answer:** Accuracy = **(TP + TN) / Total**. It is the proportion of all predictions that are correct.  
**বাংলা ব্যাখ্যা:** মোট prediction-এর কত শতাংশ correct।

## 42. Precision
**English Answer:** Precision = **TP / (TP + FP)**. It measures how many predicted positives are actually positive.  
**বাংলা ব্যাখ্যা:** “যেগুলোকে positive বলেছি, তার কতটা সত্যি?”

## 43. Recall
**English Answer:** Recall = **TP / (TP + FN)**. It measures how many actual positives were correctly detected.  
**বাংলা ব্যাখ্যা:** “যতগুলো সত্যি positive ছিল, তার কতটা ধরতে পেরেছি?”

## 44. F1-Score
**English Answer:** F1 = **2PR / (P + R)**, the harmonic mean of precision and recall.  
**বাংলা ব্যাখ্যা:** Precision ও Recall-এর balanced measure।

## 45. ROC-AUC
**English Answer:** ROC-AUC measures the area under the ROC curve and evaluates ranking/discrimination performance across thresholds.  
**বাংলা ব্যাখ্যা:** Different threshold-এ classifier কত ভালো positive/negative আলাদা করতে পারে তা measure করে।

## 46. Imbalanced Data
**English Answer:** Imbalanced data has highly unequal class frequencies, making accuracy potentially misleading.  
**বাংলা ব্যাখ্যা:** এক class অনেক বেশি হলে সবসময় majority class predict করেও high accuracy পাওয়া যায়; তাই Precision/Recall/F1 গুরুত্বপূর্ণ।

## 47. Precision vs Recall
**English Answer:** Precision is important when false positives are costly; recall is important when false negatives are costly.  
**বাংলা ব্যাখ্যা:** Spam filter-এ Precision, cancer/fraud detection-এ Recall বেশি গুরুত্বপূর্ণ।

---

# DEEP LEARNING BASICS

## 48. Artificial Neural Network (ANN)
**English Answer:** ANN is a network of interconnected artificial neurons organized into input, hidden, and output layers.  
**বাংলা ব্যাখ্যা:** Brain-inspired network যেখানে neuron layer-by-layer data process করে।

## 49. Neuron
**English Answer:** A neuron computes a weighted sum of inputs plus bias and passes it through an activation function: **output = Activation(Σwx + b)**.  
**বাংলা ব্যাখ্যা:** Input-এর weighted sum + bias নিয়ে activation function দিয়ে output দেয়।

## 50. Weight
**English Answer:** A weight represents the learned importance of an input connection.  
**বাংলা ব্যাখ্যা:** কোন input কতটা গুরুত্বপূর্ণ তা weight দিয়ে শেখে।

## 51. Bias
**English Answer:** Bias is a learned offset that shifts the activation function and increases model flexibility.  
**বাংলা ব্যাখ্যা:** Output/threshold shift করতে সাহায্য করে।

## 52. Activation Function
**English Answer:** An activation function introduces non-linearity into a neural network so it can learn complex relationships.  
**বাংলা ব্যাখ্যা:** Non-linearity না থাকলে multiple layer থাকলেও network শেষ পর্যন্ত linear function-এর মতো হবে।

## 53. Sigmoid
**English Answer:** Sigmoid maps values to approximately **0–1** and is commonly used for binary classification output.  
**বাংলা ব্যাখ্যা:** Probability-like output দেয়; binary output-এ common।

## 54. Tanh
**English Answer:** Tanh maps values to **−1 to 1** and is zero-centered but can suffer from vanishing gradients.  
**বাংলা ব্যাখ্যা:** Zero-centered activation; তবে vanishing gradient সমস্যা হতে পারে।

## 55. ReLU
**English Answer:** ReLU outputs max(0, x) and is widely used in hidden layers because it is simple and helps with gradient flow.  
**বাংলা ব্যাখ্যা:** Negative হলে 0, positive হলে value নিজেই; hidden layer-এর common default।

## 56. Leaky ReLU
**English Answer:** Leaky ReLU gives a small non-zero output for negative inputs to reduce the dying-ReLU problem.  
**বাংলা ব্যাখ্যা:** Negative side পুরো zero না করে ছোট value রাখে।

## 57. Softmax
**English Answer:** Softmax converts multiple scores into probabilities whose sum is 1, commonly for multi-class classification.  
**বাংলা ব্যাখ্যা:** Multi-class output-এর probabilityগুলো বের করে এবং সব probability-এর sum 1।

## 58. Activation Function Selection
**English Answer:** Hidden layer → ReLU; binary output → Sigmoid; multi-class output → Softmax.  
**বাংলা ব্যাখ্যা:** Viva-তে এই mapping মুখস্থ রাখবে।

---

# NEURAL NETWORK TRAINING

## 59. Forward Propagation
**English Answer:** Forward propagation passes inputs through the network to compute a prediction.  
**বাংলা ব্যাখ্যা:** Input থেকে সামনে গিয়ে final prediction বের করা।

## 60. Loss Function
**English Answer:** A loss function measures the difference between the model prediction and the true target.  
**বাংলা ব্যাখ্যা:** Prediction কতটা ভুল তা measure করে।

## 61. Backpropagation
**English Answer:** Backpropagation computes gradients of the loss with respect to model parameters by propagating error information backward through the network.  
**বাংলা ব্যাখ্যা:** Loss থেকে backward গিয়ে প্রতিটি weight-এর gradient বের করা।

## 62. Gradient Descent
**English Answer:** Gradient descent updates parameters in the direction that reduces the loss: **w_new = w_old − learning_rate × gradient**.  
**বাংলা ব্যাখ্যা:** Loss কমানোর direction-এ weight update করা।

## 63. Learning Rate
**English Answer:** Learning rate controls the size of each parameter update during optimization.  
**বাংলা ব্যাখ্যা:** প্রতি update-এ weight কতটা বদলাবে তা ঠিক করে।

## 64. Epoch
**English Answer:** An epoch is one complete pass through the entire training dataset.  
**বাংলা ব্যাখ্যা:** পুরো training data একবার সম্পূর্ণ process করা।

## 65. Batch Size
**English Answer:** Batch size is the number of training samples processed before one parameter update.  
**বাংলা ব্যাখ্যা:** একবার weight update করার আগে কত sample process হবে।

## 66. Iteration
**English Answer:** One iteration is one batch processed and one corresponding parameter update.  
**বাংলা ব্যাখ্যা:** একটি batch process = একটি iteration।

## 67. Iterations per Epoch
**English Answer:** Approximately **iterations per epoch = total samples / batch size**.  
**বাংলা ব্যাখ্যা:** 1000 sample ও batch 100 হলে 10 iteration = 1 epoch।

## 68. Batch Gradient Descent
**English Answer:** Batch GD uses the entire training dataset for each update; it is stable but can be slow.  
**বাংলা ব্যাখ্যা:** পুরো dataset দিয়ে প্রতিবার update।

## 69. Stochastic Gradient Descent
**English Answer:** SGD updates parameters using one training sample at a time; it is fast but noisy.  
**বাংলা ব্যাখ্যা:** এক sample দিয়ে update; দ্রুত কিন্তু update বেশি noisy।

## 70. Mini-Batch Gradient Descent
**English Answer:** Mini-batch GD updates parameters using a small batch of samples and is widely used in practice.  
**বাংলা ব্যাখ্যা:** ছোট batch, যেমন 32/64/128 sample দিয়ে update; practical standard।

## 71. Adam Optimizer
**English Answer:** Adam combines adaptive learning-rate ideas with momentum-like first-moment information and is widely used for neural-network training.  
**বাংলা ব্যাখ্যা:** Momentum + adaptive learning rate-এর সুবিধা combine করে; খুব popular optimizer।

## 72. Vanishing Gradient
**English Answer:** Vanishing gradients occur when gradients become extremely small, making earlier layers learn very slowly or stop learning effectively.  
**বাংলা ব্যাখ্যা:** Gradient খুব ছোট হয়ে গেলে early layer ঠিকমতো শেখে না; ReLU/LSTM/ResNet ইত্যাদি সাহায্য করতে পারে।

## 73. Exploding Gradient
**English Answer:** Exploding gradients occur when gradients become excessively large, causing unstable training.  
**বাংলা ব্যাখ্যা:** Gradient অনেক বড় হয়ে training unstable করে; gradient clipping ব্যবহার করা যায়।

## 74. Dropout
**English Answer:** Dropout randomly disables some neurons during training to reduce over-reliance on particular neurons and help prevent overfitting.  
**বাংলা ব্যাখ্যা:** Training-এর সময় random কিছু neuron বন্ধ রাখা হয় যাতে model overfit কম করে।

## 75. Loss Functions
**English Answer:** Regression commonly uses MSE; binary classification uses binary cross-entropy; multi-class classification commonly uses categorical cross-entropy.  
**বাংলা ব্যাখ্যা:** Regression → MSE; Binary → BCE; Multi-class → Categorical Cross-Entropy।

---

# DEEP LEARNING ARCHITECTURES

## 76. ANN / MLP
**English Answer:** ANN/MLP uses fully connected layers and is commonly suitable for general/tabular data.  
**বাংলা ব্যাখ্যা:** সাধারণ structured/tabular data-এর জন্য fully connected network।

## 77. CNN
**English Answer:** CNN uses convolutional filters to learn spatial features and is especially effective for images and video.  
**বাংলা ব্যাখ্যা:** Image-এর edge, texture, shape ইত্যাদি spatial feature শেখে।

## 78. RNN
**English Answer:** RNN processes sequential data while carrying information from previous steps through recurrent connections.  
**বাংলা ব্যাখ্যা:** Previous information পরের step-এ carry করে sequence/time-series handle করে।

## 79. LSTM
**English Answer:** LSTM is an RNN architecture using gates to preserve or discard information and handle long-term dependencies better.  
**বাংলা ব্যাখ্যা:** Gate mechanism দিয়ে long-term dependency ধরে এবং vanishing-gradient problem কমায়।

## 80. GRU
**English Answer:** GRU is a gated recurrent architecture similar to LSTM but with a simpler gate structure.  
**বাংলা ব্যাখ্যা:** LSTM-এর তুলনায় simpler gated RNN।

## 81. Transformer
**English Answer:** Transformer is a neural architecture based primarily on attention mechanisms and supports highly parallel processing.  
**বাংলা ব্যাখ্যা:** Attention ব্যবহার করে; RNN-এর মতো sequential processing না করে parallel training করতে পারে।

## 82. GAN
**English Answer:** GAN consists of a Generator and Discriminator trained competitively to generate realistic synthetic data.  
**বাংলা ব্যাখ্যা:** Generator data বানায়, Discriminator real/fake চেনে—দুই model-এর competition।

## 83. Autoencoder
**English Answer:** An autoencoder learns to encode input into a compact representation and then reconstruct the input through a decoder.  
**বাংলা ব্যাখ্যা:** Encoder → compressed representation → Decoder; compression/anomaly detection-এ useful।

---

# MODEL PARAMETERS & TUNING

## 84. Parameter
**English Answer:** A parameter is a value learned by the model from training data, such as weights and biases.  
**বাংলা ব্যাখ্যা:** Training-এর সময় model নিজে শেখে—যেমন weight, bias।

## 85. Hyperparameter
**English Answer:** A hyperparameter is a setting chosen before/during training to control the learning process, such as learning rate, batch size, k, or tree depth.  
**বাংলা ব্যাখ্যা:** Model নিজে শেখে না; developer সেট করে।

## 86. Parameter vs Hyperparameter
**English Answer:** Parameter = learned by model; Hyperparameter = selected by developer.  
**বাংলা ব্যাখ্যা:** “Model শিখেছে নাকি আমি বসিয়েছি?”—এই test মনে রাখবে।

## 87. Grid Search
**English Answer:** Grid Search evaluates all specified hyperparameter combinations.  
**বাংলা ব্যাখ্যা:** সব possible combination try করে; thorough কিন্তু slow।

## 88. Random Search
**English Answer:** Random Search evaluates randomly selected hyperparameter combinations.  
**বাংলা ব্যাখ্যা:** Random combination try করে; অনেক ক্ষেত্রে Grid-এর চেয়ে efficient।

## 89. Bayesian Optimization
**English Answer:** Bayesian optimization uses previous evaluation results to choose promising hyperparameter configurations.  
**বাংলা ব্যাখ্যা:** আগের result দেখে পরের promising configuration intelligently choose করে।

---

# FEATURE ENGINEERING

## 90. Feature Engineering
**English Answer:** Feature engineering creates, transforms, selects, or represents input variables to improve model learning.  
**বাংলা ব্যাখ্যা:** Raw data থেকে useful feature তৈরি/transform/select করা।

## 91. Normalization
**English Answer:** Normalization, commonly Min-Max scaling, rescales values to a fixed range such as [0,1]: **x'=(x−min)/(max−min)**.  
**বাংলা ব্যাখ্যা:** Value-কে সাধারণত 0 থেকে 1 range-এ আনা হয়।

## 92. Standardization
**English Answer:** Standardization transforms values to have mean 0 and standard deviation 1: **x'=(x−μ)/σ**.  
**বাংলা ব্যাখ্যা:** Mean 0 এবং standard deviation 1-এর scale তৈরি করে।

## 93. Normalization vs Standardization
**English Answer:** Normalization gives a fixed range and is sensitive to outliers; standardization gives mean 0/std 1 without a fixed range and is often useful for SVM, PCA, and regression.  
**বাংলা ব্যাখ্যা:** Normalization → [0,1]; Standardization → mean 0, std 1।

## 94. Algorithms Usually Not Requiring Scaling
**English Answer:** Decision Trees, Random Forests, and similar tree-based methods generally do not require feature scaling because they split using thresholds.  
**বাংলা ব্যাখ্যা:** Tree distance/scale-এর ওপর নির্ভর করে না, তাই সাধারণত scaling দরকার নেই।

## 95. Label Encoding
**English Answer:** Label encoding maps categories to integer labels; it is appropriate when categories have meaningful order.  
**বাংলা ব্যাখ্যা:** Ordinal data যেমন Low/Medium/High-এ useful।

## 96. One-Hot Encoding
**English Answer:** One-hot encoding creates a separate binary feature for each category.  
**বাংলা ব্যাখ্যা:** Nominal data যেমন Red/Green/Blue-এর জন্য ব্যবহার করা হয়।

## 97. Missing Value Handling
**English Answer:** Missing values can be removed, imputed using statistics such as mean/median/mode, or predicted using a model.  
**বাংলা ব্যাখ্যা:** Missing data বাদ, statistical imputation বা model-based prediction করা যায়।

## 98. Outlier Handling
**English Answer:** Outliers can be identified or handled using methods such as IQR, Z-score, or Winsorization.  
**বাংলা ব্যাখ্যা:** অস্বাভাবিক extreme value IQR/Z-score ইত্যাদি দিয়ে detect/handle করা যায়।

## 99. Imbalanced Data Handling
**English Answer:** Common approaches include oversampling such as SMOTE, undersampling, and class-weighted learning.  
**বাংলা ব্যাখ্যা:** Minority class বাড়ানো, majority class কমানো বা class weight ব্যবহার করা যায়।

## 100. Curse of Dimensionality
**English Answer:** As the number of dimensions grows, data becomes sparse and many algorithms become less effective; PCA or feature selection can help.  
**বাংলা ব্যাখ্যা:** Feature বেশি হলে data space-এ ছড়িয়ে যায় এবং model-এর performance খারাপ হতে পারে।

## 101. Data Leakage
**English Answer:** Data leakage occurs when information unavailable at prediction time, such as test information, influences training, causing overly optimistic evaluation.  
**বাংলা ব্যাখ্যা:** Test-এর information training-এ ঢুকে গেলে fake/high accuracy দেখা যায়।

---

# ENSEMBLE LEARNING

## 102. Ensemble Learning
**English Answer:** Ensemble learning combines multiple models to produce a stronger overall predictor.  
**বাংলা ব্যাখ্যা:** অনেক model-এর output combine করে stronger model তৈরি করা।

## 103. Bagging
**English Answer:** Bagging trains multiple models independently, often on bootstrap samples, and combines their predictions; it mainly reduces variance.  
**বাংলা ব্যাখ্যা:** Parallel/independent model; variance কমায়।

## 104. Boosting
**English Answer:** Boosting builds models sequentially, with later models focusing on errors or weaknesses of earlier models; it mainly reduces bias.  
**বাংলা ব্যাখ্যা:** Sequentially model বানায় এবং আগের model-এর ভুল থেকে শেখে।

## 105. Random Forest
**English Answer:** Random Forest is a bagging-based ensemble of randomized Decision Trees.  
**বাংলা ব্যাখ্যা:** Random Forest = Bagging-style ensemble + many randomized trees।

## 106. XGBoost / AdaBoost
**English Answer:** XGBoost and AdaBoost are popular boosting methods that build ensembles sequentially.  
**বাংলা ব্যাখ্যা:** Boosting-এর common algorithms।

## 107. Stacking
**English Answer:** Stacking combines predictions from different base models using another model called a meta-learner.  
**বাংলা ব্যাখ্যা:** কয়েকটি model-এর output নিয়ে আরেকটি model final decision নেয়।

## 108. Bagging vs Boosting
| | Bagging | Boosting |
|---|---|---|
| Training | Parallel | Sequential |
| Main effect | Reduces variance | Reduces bias |
| Example | Random Forest | AdaBoost, XGBoost |
| Main idea | Independent models | Later models focus on previous errors |

---

# IMPORTANT FORMULAS

## 109. Linear Regression
**Formula:** `ŷ = w·x + b`  
**Cost:** `J = (1/n) Σ(y−ŷ)²`  
**বাংলা:** Input-এর linear combination থেকে prediction; MSE দিয়ে error মাপা হয়।

## 110. Sigmoid
**Formula:** `σ(z) = 1 / (1 + e^(-z))`  
**বাংলা:** Output 0–1 range-এ; binary classification-এর জন্য।

## 111. Softmax
**Formula:** `softmax(zᵢ) = e^(zᵢ) / Σe^(zⱼ)`  
**বাংলা:** Multi-class probability; সব output-এর sum = 1।

## 112. Entropy
**Formula:** `Entropy(S) = −Σ pᵢ log₂(pᵢ)`  
**বাংলা:** Data কতটা mixed/uncertain তা measure করে; pure node-এর entropy 0।

## 113. Information Gain
**Formula:** `IG = Entropy(parent) − Weighted Entropy(children)`  
**বাংলা:** Decision Tree সাধারণত বেশি Information Gain পাওয়া feature দিয়ে split করে।

## 114. Gini Impurity
**Formula:** `Gini = 1 − Σ(pᵢ)²`  
**বাংলা:** Impurity measure; CART-এ common এবং entropy-এর alternative।

## 115. Bayes Theorem
**Formula:** `P(A|B) = P(B|A)P(A) / P(B)`  
**বাংলা:** Posterior = Likelihood × Prior / Evidence।

## 116. Gradient Descent
**Formula:** `w_new = w_old − learning_rate × ∂J/∂w`  
**বাংলা:** Loss কমানোর direction-এ parameter update করা।

## 117. Euclidean Distance
**Formula:** `d = √[(x₂−x₁)² + (y₂−y₁)² + ...]`  
**বাংলা:** KNN/K-Means-এ point-এর distance মাপতে common।

## 118. CNN Output Size
**Formula:** `Output = ((W − F + 2P) / S) + 1`  
**বাংলা:** W=input size, F=filter size, P=padding, S=stride।

---

# ALGORITHM DETAILS

## 119. K-Means — Choosing k
**English Answer:** The Elbow Method runs K-Means for several k values and chooses the point where WCSS begins to show diminishing returns.  
**বাংলা ব্যাখ্যা:** Different k-এর WCSS plot করে curve-এর elbow point choose করা হয়।

## 120. WCSS
**English Answer:** Within-Cluster Sum of Squares measures the total squared distance of points from their assigned cluster centroids.  
**বাংলা ব্যাখ্যা:** Cluster-এর pointগুলো centroid থেকে কত দূরে তার squared distance-এর total।

## 121. SVM Kernel Trick
**English Answer:** The kernel trick implicitly maps data into a higher-dimensional feature space where a nonlinear separation may become easier.  
**বাংলা ব্যাখ্যা:** Nonlinear data-কে higher-dimensional space-এ নিয়ে separable করার ধারণা।

## 122. Common SVM Kernels
**English Answer:** Common kernels include Linear, Polynomial, and RBF/Gaussian; RBF is widely used for nonlinear boundaries.  
**বাংলা ব্যাখ্যা:** Linear → simple; Polynomial → moderate complexity; RBF → complex nonlinear boundary।

## 123. Support Vector
**English Answer:** Support vectors are training points closest to the decision boundary that strongly determine the SVM hyperplane.  
**বাংলা ব্যাখ্যা:** Boundary-এর সবচেয়ে কাছের point; এগুলো hyperplane নির্ধারণে গুরুত্বপূর্ণ।

## 124. KNN — Choosing k
**English Answer:** Small k can overfit and be noise-sensitive; large k can smooth too much and underfit. Odd k can avoid ties in binary classification.  
**বাংলা ব্যাখ্যা:** k ছোট → overfit; k বড় → underfit; binary classification-এ odd k useful।

## 125. KNN as Lazy Learner
**English Answer:** KNN is called a lazy learner because it performs little explicit training and does most computation at prediction time.  
**বাংলা ব্যাখ্যা:** Training phase-এ model খুব কম শেখে; prediction-এর সময় distance calculation করে।

## 126. Why Random Forest Reduces Overfitting
**English Answer:** Random Forest averages/votes across diverse trees trained on different samples/features, reducing variance compared with a single tree.  
**বাংলা ব্যাখ্যা:** অনেক diverse tree-এর vote নিলে single tree-এর variance/overfitting কমে।

---

# CNN DEEP DIVE

## 127. Convolution / Filter / Kernel
**English Answer:** A convolution filter/kernel is a small matrix that slides over an image to detect local features.  
**বাংলা ব্যাখ্যা:** ছোট matrix image-এর ওপর slide করে edge/texture-এর মতো feature detect করে।

## 128. Feature Map
**English Answer:** A feature map is the output produced by applying a convolution filter to the input.  
**বাংলা ব্যাখ্যা:** Filter convolution-এর result হলো feature map।

## 129. Stride
**English Answer:** Stride is the number of pixels by which the filter moves at each step.  
**বাংলা ব্যাখ্যা:** Filter প্রতিবার কত pixel move করবে।

## 130. Padding
**English Answer:** Padding adds pixels, often zeros, around the input to control spatial output size.  
**বাংলা ব্যাখ্যা:** Image-এর চারপাশে extra pixels যোগ করে output size control করা হয়।

## 131. Pooling
**English Answer:** Pooling reduces spatial dimensions while retaining important information; max pooling is common.  
**বাংলা ব্যাখ্যা:** Feature map-এর size কমানো; Max Pooling-এ maximum value নেওয়া হয়।

## 132. Flatten
**English Answer:** Flatten converts multi-dimensional feature maps into a one-dimensional vector for fully connected layers.  
**বাংলা ব্যাখ্যা:** 2D/3D feature map → 1D vector।

## 133. CNN Layers
**English Answer:** A common CNN pipeline is Convolution → Pooling → Fully Connected/Output layers.  
**বাংলা ব্যাখ্যা:** Convolution feature বের করে, Pooling size কমায়, শেষে FC classification করতে পারে।

## 134. Why CNN for Images?
**English Answer:** CNNs exploit local spatial structure, parameter sharing, and hierarchical feature learning, making them effective for images.  
**বাংলা ব্যাখ্যা:** একই filter বিভিন্ন জায়গায় ব্যবহার করে parameter কমায় এবং edge→shape→object hierarchy শেখে।

---

# OTHER DL TOPICS

## 135. Batch Normalization
**English Answer:** Batch normalization normalizes intermediate activations during training and can improve training stability and speed.  
**বাংলা ব্যাখ্যা:** Layer-এর activation normalize করে training stable/fast করতে সাহায্য করে।

## 136. Transfer Learning
**English Answer:** Transfer learning starts with a model pretrained on a large dataset and adapts it to a related new task.  
**বাংলা ব্যাখ্যা:** বড় dataset-এ pretrained model নিয়ে ছোট নিজের dataset-এর problem-এ ব্যবহার করা।

## 137. Feature Extraction
**English Answer:** In transfer learning, feature extraction freezes pretrained layers and trains mainly the new task-specific output layers.  
**বাংলা ব্যাখ্যা:** পুরোনো layer freeze করে নতুন final layer train করা।

## 138. Fine-Tuning
**English Answer:** Fine-tuning unfreezes some pretrained layers and trains them further, usually with a smaller learning rate.  
**বাংলা ব্যাখ্যা:** Pretrained model-এর কিছু layer unfreeze করে নিজের data-তে carefully retrain করা।

## 139. Common Pretrained Models
**English Answer:** ResNet, VGG, Inception, and EfficientNet are common vision models; BERT and GPT are common NLP/Transformer models.  
**বাংলা ব্যাখ্যা:** Vision-এ ResNet/VGG; NLP-তে BERT/GPT পরিচিত pretrained models।

## 140. Optimizer — SGD
**English Answer:** SGD updates parameters using gradient information and is simple but may be noisy.  
**বাংলা ব্যাখ্যা:** Basic optimizer; update noisy হতে পারে।

## 141. Momentum
**English Answer:** Momentum uses information from previous updates to smooth optimization and accelerate movement in consistent directions.  
**বাংলা ব্যাখ্যা:** আগের direction মনে রেখে oscillation কমায়।

## 142. RMSprop
**English Answer:** RMSprop adapts the effective learning rate using a moving average of squared gradients.  
**বাংলা ব্যাখ্যা:** Parameter অনুযায়ী adaptive learning rate-এর ধারণা ব্যবহার করে।

## 143. Adam
**English Answer:** Adam combines momentum-like first-moment information with adaptive second-moment scaling and is widely used.  
**বাংলা ব্যাখ্যা:** Momentum ও adaptive gradient scaling-এর সুবিধা combine করে।

---

# NLP & LLM BASICS

## 144. Natural Language Processing (NLP)
**English Answer:** NLP is the field of AI concerned with processing, understanding, and generating human language.  
**বাংলা ব্যাখ্যা:** Human language computer দিয়ে process/understand/generate করার field।

## 145. Tokenization
**English Answer:** Tokenization splits text into smaller units such as words, subwords, or tokens.  
**বাংলা ব্যাখ্যা:** Text-কে ছোট token-এ ভাঙা।

## 146. Stop Word Removal
**English Answer:** Stop-word removal removes very common words that may contribute little to a specific task.  
**বাংলা ব্যাখ্যা:** Task অনুযায়ী কম informative common word বাদ দেওয়া।

## 147. Stemming
**English Answer:** Stemming heuristically removes word endings to obtain a rough root form; it is fast but may produce invalid roots.  
**বাংলা ব্যাখ্যা:** Word-এর ending কেটে root আনা; দ্রুত কিন্তু সবসময় linguistically correct নয়।

## 148. Lemmatization
**English Answer:** Lemmatization uses linguistic knowledge to obtain a valid base form or lemma; it is generally more accurate than stemming.  
**বাংলা ব্যাখ্যা:** Dictionary/linguistic rules দিয়ে correct base form আনে; stemming-এর চেয়ে accurate কিন্তু slower।

## 149. POS Tagging
**English Answer:** Part-of-Speech tagging assigns grammatical categories such as noun, verb, adjective, or adverb to tokens.  
**বাংলা ব্যাখ্যা:** প্রতিটি word noun/verb/adjective ইত্যাদি কোন grammatical role তা identify করা।

## 150. Bag of Words
**English Answer:** Bag of Words represents text using word occurrence counts while ignoring word order.  
**বাংলা ব্যাখ্যা:** কোন word কতবার এসেছে count করে; word order হারিয়ে যায়।

## 151. TF-IDF
**English Answer:** TF-IDF weights terms by their frequency in a document and their rarity across documents, giving more importance to informative terms.  
**বাংলা ব্যাখ্যা:** Document-এ frequent কিন্তু পুরো corpus-এ rare word বেশি গুরুত্ব পায়।

## 152. Word Embedding
**English Answer:** Word embeddings represent words as dense numerical vectors that capture semantic relationships.  
**বাংলা ব্যাখ্যা:** Word-কে dense vector-এ convert করে meaning/relationship capture করে; Word2Vec/GloVe examples।

## 153. Contextual Embedding
**English Answer:** Contextual embeddings produce representations that depend on the surrounding context, as in BERT.  
**বাংলা ব্যাখ্যা:** একই word context অনুযায়ী different representation পেতে পারে।

## 154. Attention
**English Answer:** Attention lets a model assign different importance/weights to different input tokens when computing a representation.  
**বাংলা ব্যাখ্যা:** Sentence-এর কোন word অন্য word বোঝার জন্য বেশি important তা model weight দিয়ে determine করে।

## 155. Transformer
**English Answer:** Transformer is an attention-based architecture that supports parallel sequence processing and is central to modern NLP and LLMs.  
**বাংলা ব্যাখ্যা:** Attention-based architecture; NLP/LLM-এর foundation এবং parallel processing করতে পারে।

## 156. Transformer vs RNN
**English Answer:** RNN processes sequences recurrently and sequentially; Transformers use attention and allow much more parallel processing while handling long-range dependencies effectively.  
**বাংলা ব্যাখ্যা:** RNN sequential; Transformer parallel + attention, তাই training দ্রুত এবং long dependency ভালো handle করে।

## 157. “Attention Is All You Need”
**English Answer:** “Attention Is All You Need” is the 2017 research paper that introduced the Transformer architecture.  
**বাংলা ব্যাখ্যা:** 2017 সালের landmark paper যা Transformer architecture introduce করে।

## 158. Large Language Model (LLM)
**English Answer:** An LLM is a large neural language model trained on massive text data to model and generate language.  
**বাংলা ব্যাখ্যা:** বিশাল text data-তে train করা language model, যা text understand/generate করতে পারে।

## 159. Token in LLM
**English Answer:** A token is a unit of text processed by a language model, which may be a word, subword, or character-like unit.  
**বাংলা ব্যাখ্যা:** Model-এর input/output processing-এর basic text unit।

## 160. Pre-training
**English Answer:** Pre-training learns general language patterns from a large dataset before task-specific adaptation.  
**বাংলা ব্যাখ্যা:** বড় text corpus থেকে general language knowledge শেখা।

## 161. Fine-Tuning in LLM
**English Answer:** Fine-tuning further trains a pretrained model on task- or domain-specific data.  
**বাংলা ব্যাখ্যা:** Specific task/domain-এর জন্য pretrained model-কে আরও train করা।

## 162. RLHF
**English Answer:** RLHF means Reinforcement Learning from Human Feedback, where human preferences help align model behavior.  
**বাংলা ব্যাখ্যা:** Human feedback ব্যবহার করে model-এর output behavior improve/align করা।

## 163. Prompt Engineering
**English Answer:** Prompt engineering is the practice of designing effective instructions/inputs to obtain useful model outputs.  
**বাংলা ব্যাখ্যা:** ভালো prompt লিখে desired output পাওয়ার technique।

## 164. Hallucination
**English Answer:** Hallucination is when a model generates information that sounds plausible but is incorrect, unsupported, or fabricated.  
**বাংলা ব্যাখ্যা:** Model confidentভাবে ভুল/বানানো information দিতে পারে—এটাই hallucination।

## 165. RAG
**English Answer:** Retrieval-Augmented Generation retrieves relevant external information and uses it to ground a generated response.  
**বাংলা ব্যাখ্যা:** External document/data retrieve করে তার ওপর ভিত্তি করে answer generate করা।

---

# TOOLS & LIBRARIES

## 166. NumPy
**English Answer:** NumPy provides efficient numerical computing and array operations in Python.  
**বাংলা ব্যাখ্যা:** Numerical calculation ও array processing-এর জন্য।

## 167. Pandas
**English Answer:** Pandas provides data structures and tools for data manipulation and analysis, especially DataFrames.  
**বাংলা ব্যাখ্যা:** Data cleaning, manipulation, analysis-এর জন্য।

## 168. Matplotlib / Seaborn
**English Answer:** Matplotlib and Seaborn are Python libraries commonly used for data visualization.  
**বাংলা ব্যাখ্যা:** Graph/chart/visualization তৈরির জন্য।

## 169. Scikit-learn
**English Answer:** Scikit-learn provides classical ML algorithms and tools for preprocessing, model selection, and evaluation.  
**বাংলা ব্যাখ্যা:** Regression, classification, clustering, preprocessing ইত্যাদির জন্য common ML library।

## 170. TensorFlow / Keras
**English Answer:** TensorFlow is a deep-learning framework, while Keras provides a high-level API commonly used to build neural networks.  
**বাংলা ব্যাখ্যা:** Deep learning model তৈরি/train করার ecosystem।

## 171. PyTorch
**English Answer:** PyTorch is a widely used deep-learning framework known for flexible tensor computation and research use.  
**বাংলা ব্যাখ্যা:** Deep learning ও research-এ widely used framework।

## 172. OpenCV
**English Answer:** OpenCV is a computer-vision library for image/video processing and analysis.  
**বাংলা ব্যাখ্যা:** Image/video processing ও computer vision-এর জন্য।

## 173. NLTK / spaCy
**English Answer:** NLTK and spaCy are Python libraries for natural language processing tasks.  
**বাংলা ব্যাখ্যা:** NLP preprocessing ও linguistic processing-এর জন্য।

## 174. Hugging Face
**English Answer:** Hugging Face provides tools, libraries, and pretrained Transformer models widely used for NLP and modern AI.  
**বাংলা ব্যাখ্যা:** Pretrained Transformer/LLM model ও tools-এর বড় ecosystem।

---

# HIGH-YIELD DIFFERENCES

## 175. KNN vs K-Means
**English Answer:** KNN is supervised and predicts using labeled neighbors; K-Means is unsupervised and clusters unlabeled data.  
**বাংলা:** **KNN = supervised**, **K-Means = unsupervised**।

## 176. Classification vs Regression
**English Answer:** Classification predicts discrete classes; regression predicts continuous numerical values.  
**বাংলা:** “কোনটা?” = classification; “কত?” = regression।

## 177. Overfitting vs Underfitting
**English Answer:** Overfitting = high training performance but poor generalization; underfitting = poor training and test performance.  
**বাংলা:** Overfit = মুখস্থ; Underfit = ঠিকমতো শেখেনি।

## 178. Precision vs Recall
**English Answer:** Precision focuses on correctness among predicted positives; recall focuses on coverage of actual positives.  
**বাংলা:** Precision = যা positive বলেছি তার কতটা সত্যি; Recall = সত্যি positive-এর কতটা ধরেছি।

## 179. Parameter vs Hyperparameter
**English Answer:** Parameters are learned from data; hyperparameters are chosen to control training/model behavior.  
**বাংলা:** Model শেখে বনাম developer সেট করে।

## 180. Normalization vs Standardization
**English Answer:** Normalization usually maps to [0,1]; standardization maps to mean 0 and standard deviation 1.  
**বাংলা:** [0,1] বনাম mean 0/std 1।

## 181. Label Encoding vs One-Hot Encoding
**English Answer:** Label encoding assigns integer codes and is suitable for ordinal categories; one-hot creates separate binary columns and is suitable for nominal categories.  
**বাংলা:** Ordinal → Label; Nominal → One-Hot।

## 182. Bagging vs Boosting
**English Answer:** Bagging trains models independently/parallel and mainly reduces variance; boosting trains sequentially and mainly reduces bias.  
**বাংলা:** Bagging = parallel + variance; Boosting = sequential + bias।

## 183. Sigmoid vs Softmax
**English Answer:** Sigmoid is commonly used for binary output; Softmax is commonly used for multi-class output and sums probabilities to 1.  
**বাংলা:** Binary → Sigmoid; Multi-class → Softmax।

## 184. Stemming vs Lemmatization
**English Answer:** Stemming is faster and heuristic; lemmatization is slower but linguistically more accurate.  
**বাংলা:** Stemming = দ্রুত/rough; Lemmatization = ধীর/accurate।

## 185. CNN vs RNN vs Transformer
**English Answer:** CNN is mainly for spatial data such as images; RNN/LSTM for sequential data; Transformer uses attention and is dominant in modern NLP/LLMs.  
**বাংলা:** CNN → Image; RNN/LSTM → Sequence; Transformer → NLP/LLM।

## 186. Feature Extraction vs Fine-Tuning
**English Answer:** Feature extraction freezes pretrained layers and trains new layers; fine-tuning also updates some pretrained layers.  
**বাংলা:** Freeze করে শুধু নতুন layer train বনাম কিছু পুরোনো layer-ও train।

---

# NUMERICAL VIVA EXAMPLE — CONFUSION MATRIX

Given:
- TP = 15
- FN = 5
- FP = 10
- TN = 70

**Accuracy:** `(15+70)/100 = 85%`  
**Precision:** `15/(15+10) = 60%`  
**Recall:** `15/(15+5) = 75%`  
**F1:** `2×0.60×0.75/(0.60+0.75) ≈ 66.7%`

**বাংলা:** Model 25টি spam বলেছে, তার মধ্যে 15টি সত্যি → Precision 60%; আসল 20টি spam-এর 15টি ধরেছে → Recall 75%।

---

# 40 MUST-KNOW VIVA QUESTIONS

## 1. What is AI?
**English:** The broad field of making machines perform tasks requiring human-like intelligence.  
**বাংলা:** Human-like intelligent task machine দিয়ে করানো।

## 2. What is ML?
**English:** A subset of AI where models learn patterns from data.  
**বাংলা:** Data থেকে pattern শেখা।

## 3. What is DL?
**English:** ML using multi-layer neural networks to learn features.  
**বাংলা:** Multi-layer neural network-based ML।

## 4. Difference between AI, ML and DL?
**English:** AI ⊃ ML ⊃ DL.  
**বাংলা:** AI সবচেয়ে বড়, ML তার subset, DL ML-এর subset।

## 5. Supervised vs unsupervised?
**English:** Labeled data vs unlabeled data.  
**বাংলা:** Label আছে বনাম label নেই।

## 6. Classification vs regression?
**English:** Discrete class prediction vs continuous value prediction.  
**বাংলা:** কোনটা বনাম কত।

## 7. KNN supervised কেন?
**English:** It predicts using labeled training examples.  
**বাংলা:** Training data-এর label ব্যবহার করে।

## 8. K-Means supervised নয় কেন?
**English:** It clusters unlabeled data without target labels.  
**বাংলা:** Target label লাগে না।

## 9. Why is Logistic Regression classification?
**English:** It models class probability, commonly using a sigmoid function.  
**বাংলা:** Probability বের করে class predict করে।

## 10. What is PCA?
**English:** A dimensionality-reduction method based on directions of high variance.  
**বাংলা:** Feature/dimension কমায়।

## 11. What is overfitting?
**English:** Excellent training fit but poor generalization.  
**বাংলা:** Training data মুখস্থ করে ফেলা।

## 12. How to reduce overfitting?
**English:** Regularization, dropout, more data, data augmentation, early stopping, and suitable cross-validation.  
**বাংলা:** Model complexity কমানো/আরও data/regularization/dropout।

## 13. What is underfitting?
**English:** A model too simple to learn the underlying pattern.  
**বাংলা:** Model যথেষ্ট শেখেনি।

## 14. What is precision?
**English:** TP/(TP+FP).  
**বাংলা:** Predicted positive-এর মধ্যে সত্যি positive কত।

## 15. What is recall?
**English:** TP/(TP+FN).  
**বাংলা:** Actual positive-এর মধ্যে কত ধরেছে।

## 16. Cancer detection-এ recall কেন?
**English:** Missing a true positive can be very costly.  
**বাংলা:** রোগীকে miss করা dangerous, তাই FN কমাতে recall দরকার।

## 17. Spam filter-এ precision কেন?
**English:** False positives can incorrectly send legitimate mail to spam.  
**বাংলা:** Genuine mail spam হিসেবে mark হওয়া costly।

## 18. Why accuracy can be misleading?
**English:** On imbalanced data, majority-class predictions can achieve high accuracy while missing the minority class.  
**বাংলা:** 99% normal হলে সব normal বলেও 99% accuracy পাওয়া যায়।

## 19. What is a neuron?
**English:** A unit computing weighted inputs plus bias followed by an activation function.  
**বাংলা:** Σwx+b নিয়ে activation দিয়ে output দেয়।

## 20. Why activation function?
**English:** To introduce non-linearity.  
**বাংলা:** Complex nonlinear relationship শেখার জন্য।

## 21. Hidden layer-এর common activation?
**English:** ReLU.  
**বাংলা:** Hidden layer-এ সাধারণত ReLU।

## 22. Binary output-এর activation?
**English:** Sigmoid.  
**বাংলা:** Binary classification → Sigmoid।

## 23. Multi-class output?
**English:** Softmax.  
**বাংলা:** Multi-class → Softmax।

## 24. How does neural network learn?
**English:** Forward propagation → loss → backpropagation → gradient-based update.  
**বাংলা:** সামনে prediction → error → পিছনে gradient → weight update।

## 25. What is backpropagation?
**English:** Computing gradients backward through the network.  
**বাংলা:** Loss-এর gradient backward calculate করা।

## 26. What is learning rate?
**English:** The step size used for parameter updates.  
**বাংলা:** Weight কতটা পরিবর্তন হবে।

## 27. What is epoch?
**English:** One complete pass through the training dataset.  
**বাংলা:** পুরো dataset একবার process।

## 28. Parameter vs hyperparameter?
**English:** Learned value vs developer-set value.  
**বাংলা:** Weight/bias বনাম learning rate/k/tree depth।

## 29. Bagging vs boosting?
**English:** Parallel variance reduction vs sequential bias reduction.  
**বাংলা:** Bagging = parallel/variance; Boosting = sequential/bias।

## 30. Why Random Forest?
**English:** It combines diverse trees and generally reduces variance compared with a single tree.  
**বাংলা:** Multiple tree-এর vote overfitting/variance কমায়।

## 31. What is normalization?
**English:** Rescaling values, commonly to [0,1].  
**বাংলা:** Fixed range-এ value আনা।

## 32. What is standardization?
**English:** Transforming values to mean 0 and standard deviation 1.  
**বাংলা:** Mean 0, std 1।

## 33. What is data leakage?
**English:** Training receives information it should not have, such as test information.  
**বাংলা:** Test-এর information train-এ ঢুকে fake performance দেয়।

## 34. What is transfer learning?
**English:** Adapting a pretrained model to a related new task.  
**বাংলা:** Pretrained model নিয়ে নিজের task-এ adapt করা।

## 35. What is CNN?
**English:** A neural network using convolution to learn spatial features, especially from images.  
**বাংলা:** Image-এর spatial feature শেখার network।

## 36. What is RNN?
**English:** A recurrent architecture for sequential data.  
**বাংলা:** Sequence/time-series data-এর জন্য recurrent network।

## 37. Why Transformer over RNN?
**English:** Attention enables parallel processing and effective long-range dependency handling.  
**বাংলা:** Parallel processing + attention-এর কারণে long dependency ভালো handle করে।

## 38. What is attention?
**English:** A mechanism that assigns different importance to input tokens when computing representations.  
**বাংলা:** কোন word/context বেশি important তা weight করে।

## 39. What is hallucination?
**English:** Plausible-sounding but incorrect or unsupported model-generated information.  
**বাংলা:** Confidentভাবে ভুল/বানানো তথ্য generate করা।

## 40. What is RAG?
**English:** Retrieval-Augmented Generation retrieves external information and uses it to support generation.  
**বাংলা:** External document/data retrieve করে grounded answer তৈরি করা।

---

# FINAL 30-SECOND REVISION

1. **AI ⊃ ML ⊃ DL**
2. Supervised = labeled
3. Unsupervised = unlabeled
4. RL = reward
5. Classification = “কোনটা?”
6. Regression = “কত?”
7. KNN = supervised
8. K-Means = unsupervised
9. Logistic Regression = classification
10. PCA = dimensionality reduction
11. Overfit = high variance
12. Underfit = high bias
13. Precision = TP/(TP+FP)
14. Recall = TP/(TP+FN)
15. Cancer → Recall
16. Spam → Precision
17. L1 → feature selection/sparse weights
18. L2 → weight shrinkage
19. Hidden → ReLU
20. Binary → Sigmoid
21. Multi-class → Softmax
22. Forward → Loss → Backprop → Update
23. Epoch = full dataset
24. Parameter = model learns
25. Hyperparameter = developer sets
26. Bagging → parallel → variance → Random Forest
27. Boosting → sequential → bias → XGBoost
28. Normalization → [0,1]
29. Standardization → mean 0, std 1
30. CNN → Image
31. RNN/LSTM → Sequence
32. Transformer → Attention/NLP/LLM
33. Transfer Learning → pretrained model
34. Stemming = rough/fast
35. Lemmatization = accurate/slower
36. Hallucination = plausible but wrong output
37. RAG = retrieve + generate
38. Data Leakage = test info enters training
39. K-Means k → Elbow Method
40. SVM → maximum-margin hyperplane

---

# FULL COVERAGE CHECKLIST

## ML Fundamentals
- [x] AI
- [x] ML
- [x] DL
- [x] AI vs ML vs DL
- [x] Traditional Programming vs ML
- [x] ML vs DL

## Learning Types
- [x] Supervised
- [x] Classification
- [x] Regression
- [x] Unsupervised
- [x] Clustering
- [x] Dimensionality Reduction
- [x] Semi-Supervised
- [x] Reinforcement Learning
- [x] RL components

## Classical ML
- [x] Linear Regression
- [x] Logistic Regression
- [x] KNN
- [x] Decision Tree
- [x] Random Forest
- [x] SVM
- [x] Naive Bayes
- [x] K-Means
- [x] PCA

## Training/Evaluation
- [x] Train/Validation/Test
- [x] Cross-validation
- [x] Overfitting
- [x] Underfitting
- [x] Bias-Variance
- [x] Regularization
- [x] L1
- [x] L2
- [x] Confusion Matrix
- [x] Accuracy
- [x] Precision
- [x] Recall
- [x] F1
- [x] ROC-AUC
- [x] Imbalanced Data

## Deep Learning
- [x] ANN
- [x] Neuron
- [x] Weight
- [x] Bias
- [x] Activation
- [x] Sigmoid
- [x] Tanh
- [x] ReLU
- [x] Leaky ReLU
- [x] Softmax
- [x] Forward Propagation
- [x] Loss
- [x] Backpropagation
- [x] Gradient Descent
- [x] Learning Rate
- [x] Epoch
- [x] Batch Size
- [x] Iteration
- [x] Batch/SGD/Mini-batch
- [x] Adam
- [x] Vanishing Gradient
- [x] Exploding Gradient
- [x] Dropout
- [x] Loss Functions

## DL Architectures
- [x] ANN/MLP
- [x] CNN
- [x] RNN
- [x] LSTM
- [x] GRU
- [x] Transformer
- [x] GAN
- [x] Autoencoder
- [x] CNN layers
- [x] CNN output formula

## Tuning & Feature Engineering
- [x] Parameter
- [x] Hyperparameter
- [x] Grid Search
- [x] Random Search
- [x] Bayesian Optimization
- [x] Feature Engineering
- [x] Normalization
- [x] Standardization
- [x] Label Encoding
- [x] One-Hot Encoding
- [x] Missing Values
- [x] Outliers
- [x] Imbalanced Data
- [x] Curse of Dimensionality
- [x] Data Leakage

## Ensemble
- [x] Ensemble Learning
- [x] Bagging
- [x] Boosting
- [x] Random Forest
- [x] AdaBoost
- [x] XGBoost
- [x] Stacking

## Formulas
- [x] Linear Regression
- [x] MSE
- [x] Sigmoid
- [x] Softmax
- [x] Entropy
- [x] Information Gain
- [x] Gini
- [x] Bayes Theorem
- [x] Gradient Descent
- [x] Euclidean Distance
- [x] CNN Output Size

## Advanced Viva
- [x] Elbow Method
- [x] WCSS
- [x] SVM Kernel Trick
- [x] Support Vector
- [x] KNN k selection
- [x] Lazy Learner
- [x] Random Forest variance reduction
- [x] Batch Normalization
- [x] Transfer Learning
- [x] Feature Extraction
- [x] Fine-Tuning
- [x] Optimizers

## NLP / LLM
- [x] NLP
- [x] Tokenization
- [x] Stop Words
- [x] Stemming
- [x] Lemmatization
- [x] POS Tagging
- [x] Bag of Words
- [x] TF-IDF
- [x] Word Embedding
- [x] Contextual Embedding
- [x] Attention
- [x] Transformer
- [x] Transformer vs RNN
- [x] LLM
- [x] Token
- [x] Pre-training
- [x] Fine-tuning
- [x] RLHF
- [x] Prompt Engineering
- [x] Hallucination
- [x] RAG

## Tools
- [x] NumPy
- [x] Pandas
- [x] Matplotlib
- [x] Seaborn
- [x] Scikit-learn
- [x] TensorFlow
- [x] Keras
- [x] PyTorch
- [x] OpenCV
- [x] NLTK
- [x] spaCy
- [x] Hugging Face

---

# LAST-MINUTE PRIORITY

### ⭐⭐⭐ MUST KNOW
**AI vs ML vs DL, supervised/unsupervised, classification/regression, KNN vs K-Means, Logistic Regression, Decision Tree, Random Forest, SVM, overfitting/underfitting, Precision/Recall/F1, confusion matrix, neural-network training, activation functions, CNN, parameter vs hyperparameter, normalization vs standardization, Bagging vs Boosting, Transfer Learning, Transformer vs RNN.**

### ⭐⭐ SHOULD KNOW
**PCA, Naive Bayes, K-Means Elbow, SVM kernels, regularization, L1/L2, dropout, optimizers, batch normalization, data leakage, feature encoding, CNN output formula, NLP preprocessing, embeddings, RAG.**

### ⭐ VIVA BONUS
**RLHF, prompt engineering, hallucination, GAN, Autoencoder, Bayesian optimization, WCSS, GRU, PyTorch/Hugging Face.**

### One answer to prepare especially well:
**“What do you want to work on in your MSc?”**
Prepare: **specific area + why you chose it + one real problem + how ML/DL could solve it.**
