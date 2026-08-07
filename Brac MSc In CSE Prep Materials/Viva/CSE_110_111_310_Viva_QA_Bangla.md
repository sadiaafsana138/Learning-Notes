# CSE 110 / CSE 111 / CSE 310 — Viva Q&A
### Programming Language I · Programming Language II · Object Oriented Programming
### Format: Question → English Answer → বাংলা ব্যাখ্যা

> **Viva style:** প্রথমে English answer-এর key line বলবে; examiner “explain” করলে বাংলা explanation/example দেবে।
> **Coverage:** Course outline + uploaded Programming/OOP note-এর key concepts। Original note-ও শেষে রাখা হয়েছে যাতে কোনো source content হারিয়ে না যায়।

## PART 1 — CORE VIVA Q&A

### Q1. What is a computer program?
**English Answer:** A program is a sequence of instructions that tells a computer how to perform a task.
**বাংলা ব্যাখ্যা:** নির্দিষ্ট কাজ করানোর জন্য computer-কে দেওয়া instructions-এর সমষ্টি।

### Q2. What is an algorithm?
**English Answer:** An algorithm is a finite sequence of clear and unambiguous steps for solving a problem.
**বাংলা ব্যাখ্যা:** Problem solve করার step-by-step logical procedure।

### Q3. What is a flowchart?
**English Answer:** A flowchart is a graphical representation of an algorithm using standard symbols.
**বাংলা ব্যাখ্যা:** Algorithm-কে diagram আকারে দেখানো হয়।

### Q4. Why is debugging needed?
**English Answer:** Debugging finds, analyzes, and fixes errors in a program.
**বাংলা ব্যাখ্যা:** Program-এর error খুঁজে ঠিক করার process।

### Q5. What is a syntax error?
**English Answer:** An error caused by violating the grammatical rules of a programming language.
**বাংলা ব্যাখ্যা:** Language-এর syntax/rules ভাঙলে হয়।

### Q6. What is a runtime error?
**English Answer:** An error that occurs while a program is executing.
**বাংলা ব্যাখ্যা:** Program run করার সময় যে error হয়।

### Q7. What is a logical error?
**English Answer:** The program runs but produces an incorrect result because its logic is wrong.
**বাংলা ব্যাখ্যা:** Code চলে, কিন্তু output ভুল হয়।

### Q8. What is a data type?
**English Answer:** A data type specifies what kind of value a variable can store and how it is represented.
**বাংলা ব্যাখ্যা:** Variable কী ধরনের data রাখবে তা data type নির্ধারণ করে।

### Q9. What is operator precedence?
**English Answer:** Operator precedence determines which operator is evaluated first.
**বাংলা ব্যাখ্যা:** Expression-এ কোন operation আগে হবে তা নির্ধারণ করে।

### Q10. What is associativity?
**English Answer:** Associativity determines the evaluation direction when operators have the same precedence.
**বাংলা ব্যাখ্যা:** Same precedence হলে left-to-right বা right-to-left order নির্ধারণ করে।

### Q11. What is post-increment?
**English Answer:** i++ uses the current value first and increments it afterward.
**বাংলা ব্যাখ্যা:** আগে value ব্যবহার, পরে 1 বাড়ে।

### Q12. What is pre-increment?
**English Answer:** ++i increments the value first and then uses the new value.
**বাংলা ব্যাখ্যা:** আগে 1 বাড়ে, পরে value ব্যবহার হয়।

### Q13. What is integer division in C?
**English Answer:** Division of integers produces an integer result, so the fractional part is discarded.
**বাংলা ব্যাখ্যা:** 5/2 = 2; decimal অংশ বাদ যায়।

### Q14. What does % do in C?
**English Answer:** It returns the remainder of integer division.
**বাংলা ব্যাখ্যা:** ভাগশেষ বের করে।

### Q15. Can C's % operator be used with floating-point operands?
**English Answer:** No. Use fmod() for floating-point remainder.
**বাংলা ব্যাখ্যা:** C-তে float/double-এর জন্য fmod() ব্যবহার করতে হয়।

### Q16. What does fmod(a,b) do?
**English Answer:** It returns the floating-point remainder of a divided by b.
**বাংলা ব্যাখ্যা:** Floating-point remainder বের করে।

### Q17. What is fmod(3.14,2.1)?
**English Answer:** Approximately 1.04.
**বাংলা ব্যাখ্যা:** 3.14 - 2.1 = 1.04।

### Q18. What does round() do?
**English Answer:** It rounds a value to the nearest integer value.
**বাংলা ব্যাখ্যা:** কাছের পূর্ণসংখ্যায় round করে।

### Q19. What does ceil() do?
**English Answer:** It returns the smallest integer value greater than or equal to the input.
**বাংলা ব্যাখ্যা:** উপরের দিকে integer নেয়।

### Q20. What does floor() do?
**English Answer:** It returns the largest integer value less than or equal to the input.
**বাংলা ব্যাখ্যা:** নিচের দিকে integer নেয়।

### Q21. What does pow(a,b) do?
**English Answer:** It returns a raised to the power b.
**বাংলা ব্যাখ্যা:** a-এর b ঘাত।

### Q22. What does sqrt(x) do?
**English Answer:** It returns the square root of x.
**বাংলা ব্যাখ্যা:** x-এর বর্গমূল।

### Q23. What is a for loop?
**English Answer:** A for loop repeatedly executes a block using initialization, condition, and update.
**বাংলা ব্যাখ্যা:** Init → condition → body → update sequence-এ চলে।

### Q24. What is the execution order of a for loop?
**English Answer:** Initialization → condition → body → update → condition again.
**বাংলা ব্যাখ্যা:** Update body-এর পরে হয়।

### Q25. What is a while loop?
**English Answer:** A while loop checks its condition before executing its body.
**বাংলা ব্যাখ্যা:** Condition আগে check হয়।

### Q26. What is a do-while loop?
**English Answer:** A do-while loop executes its body before checking the condition.
**বাংলা ব্যাখ্যা:** তাই অন্তত একবার চলে।

### Q27. What is a nested loop?
**English Answer:** A loop placed inside another loop is a nested loop.
**বাংলা ব্যাখ্যা:** এক loop-এর ভিতরে আরেক loop।

### Q28. What is short-circuit evaluation?
**English Answer:** Logical evaluation stops when the final result is already known.
**বাংলা ব্যাখ্যা:** Result নিশ্চিত হলে বাকি expression execute হয় না।

### Q29. What happens in false && expression?
**English Answer:** The second expression is not evaluated.
**বাংলা ব্যাখ্যা:** AND-এ প্রথম false হলে দ্বিতীয় অংশ skip।

### Q30. What happens in true || expression?
**English Answer:** The second expression is not evaluated.
**বাংলা ব্যাখ্যা:** OR-এ প্রথম true হলে দ্বিতীয় অংশ skip।

### Q31. What is a pointer?
**English Answer:** A pointer is a variable that stores the address of another variable.
**বাংলা ব্যাখ্যা:** Pointer memory address রাখে।

### Q32. What does &a mean?
**English Answer:** It gives the memory address of a.
**বাংলা ব্যাখ্যা:** a-এর address।

### Q33. What does *p mean?
**English Answer:** It dereferences p and accesses the value at the stored address.
**বাংলা ব্যাখ্যা:** p যে address point করে সেখানকার value।

### Q34. What is an array?
**English Answer:** An array is a collection of same-type elements stored in contiguous memory.
**বাংলা ব্যাখ্যা:** একই type-এর data ধারাবাহিক memory-তে রাখা হয়।

### Q35. What is the first index of a C array?
**English Answer:** 0.
**বাংলা ব্যাখ্যা:** C array zero-indexed।

### Q36. What is the relation between arr[i] and *(arr+i)?
**English Answer:** They access the same array element.
**বাংলা ব্যাখ্যা:** দুটো equivalent array-access expression।

### Q37. What is a function?
**English Answer:** A function is a reusable block of code for a specific task.
**বাংলা ব্যাখ্যা:** নির্দিষ্ট কাজের reusable code block।

### Q38. What is recursion?
**English Answer:** Recursion is when a function calls itself to solve a smaller version of a problem.
**বাংলা ব্যাখ্যা:** Function নিজেকেই call করে।

### Q39. What is a base case?
**English Answer:** The base case stops recursion and prevents infinite calls.
**বাংলা ব্যাখ্যা:** Recursion থামানোর condition।

### Q40. Iteration vs recursion?
**English Answer:** Iteration uses loops; recursion uses repeated function calls.
**বাংলা ব্যাখ্যা:** Loop-based repetition বনাম self-call-based repetition।

### Q41. What is call by value?
**English Answer:** A copy of the argument value is passed, so normal changes do not affect the original variable.
**বাংলা ব্যাখ্যা:** Value-এর copy যায়; original সাধারণত বদলায় না।

### Q42. What is call by reference?
**English Answer:** A reference/address is used so the called code can modify the original data.
**বাংলা ব্যাখ্যা:** Address/reference দিয়ে original data change করা যায়।

### Q43. Is Java pass-by-reference?
**English Answer:** No. Java is strictly pass-by-value; object references are passed by value.
**বাংলা ব্যাখ্যা:** Java-তে reference-এর value copy হয়, pass-by-reference নয়।

### Q44. What is a static variable in C?
**English Answer:** A static local variable retains its value between function calls and exists for the program lifetime.
**বাংলা ব্যাখ্যা:** Function শেষ হলেও value retain করে।

### Q45. What is file handling?
**English Answer:** File handling means programmatically creating, opening, reading, writing, updating, and closing files.
**বাংলা ব্যাখ্যা:** Program থেকে file read/write/manage করা।

### Q46. What is a data structure?
**English Answer:** A data structure organizes data so it can be stored and processed efficiently.
**বাংলা ব্যাখ্যা:** Data efficientভাবে organize করার method।

### Q47. Linear vs non-linear data structure?
**English Answer:** Linear structures are sequential; non-linear structures are hierarchical or network-based.
**বাংলা ব্যাখ্যা:** Array/stack/queue linear; tree/graph non-linear।

### Q48. What is syntax?
**English Answer:** Syntax is the set of rules defining the valid structure of a language.
**বাংলা ব্যাখ্যা:** Program কীভাবে validভাবে লিখতে হবে।

### Q49. What is semantics?
**English Answer:** Semantics defines the meaning or behavior of valid program constructs.
**বাংলা ব্যাখ্যা:** Code-এর meaning/behavior।

### Q50. Syntax vs semantics?
**English Answer:** Syntax is structure; semantics is meaning.
**বাংলা ব্যাখ্যা:** Syntax = grammar, semantics = meaning।

### Q51. What is a formal language?
**English Answer:** A formal language is a set of strings generated according to specified rules.
**বাংলা ব্যাখ্যা:** নির্দিষ্ট rules অনুযায়ী valid strings-এর set।

### Q52. What is an alphabet in formal language theory?
**English Answer:** An alphabet is a finite, non-empty set of symbols.
**বাংলা ব্যাখ্যা:** Symbols-এর finite set।

### Q53. What is a string?
**English Answer:** A string is a finite sequence of symbols from an alphabet.
**বাংলা ব্যাখ্যা:** Alphabet-এর symbols-এর sequence।

### Q54. What is the empty string?
**English Answer:** It is a string containing zero symbols, usually written ε.
**বাংলা ব্যাখ্যা:** কোনো symbol না থাকা string।

### Q55. What is structured programming?
**English Answer:** It organizes programs around sequence, selection, and iteration with controlled flow.
**বাংলা ব্যাখ্যা:** Sequence, selection, iteration দিয়ে structured code লেখা।

### Q56. What are the three basic control structures?
**English Answer:** Sequence, selection, and iteration.
**বাংলা ব্যাখ্যা:** ক্রম, decision, repetition।

### Q57. What is a high-level language?
**English Answer:** A language that provides abstractions closer to human-readable logic than machine instructions.
**বাংলা ব্যাখ্যা:** Machine language-এর তুলনায় মানুষের জন্য সহজ।

### Q58. What is portability?
**English Answer:** Portability is the ability to move software to another environment with little or no modification.
**বাংলা ব্যাখ্যা:** কম change-এ অন্য environment-এ software চালানো।

### Q59. What is OOP?
**English Answer:** OOP organizes software around objects containing data and behavior.
**বাংলা ব্যাখ্যা:** Object-এর state ও behavior কেন্দ্র করে programming।

### Q60. What is a class?
**English Answer:** A class is a blueprint that defines attributes and methods for objects.
**বাংলা ব্যাখ্যা:** Object তৈরির নকশা।

### Q61. What is an object?
**English Answer:** An object is an instance of a class containing state and behavior.
**বাংলা ব্যাখ্যা:** Class-এর বাস্তব instance।

### Q62. Class vs object?
**English Answer:** Class is the blueprint; object is an instance created from it.
**বাংলা ব্যাখ্যা:** Class = design, object = বাস্তব রূপ।

### Q63. What is an attribute?
**English Answer:** An attribute is data/state associated with an object.
**বাংলা ব্যাখ্যা:** Object-এর property/state।

### Q64. What is a method?
**English Answer:** A method is a function defined inside a class representing behavior.
**বাংলা ব্যাখ্যা:** Class-এর ভিতরের behavior/function।

### Q65. What is a constructor?
**English Answer:** A constructor initializes an object when it is created and has no return type.
**বাংলা ব্যাখ্যা:** Object তৈরির সময় initialization করে; return type নেই।

### Q66. What are the four pillars of OOP?
**English Answer:** Encapsulation, Inheritance, Polymorphism, and Abstraction.
**বাংলা ব্যাখ্যা:** OOP-এর চারটি মূল pillar।

### Q67. What is encapsulation?
**English Answer:** Encapsulation bundles data and methods and restricts direct access to internal data.
**বাংলা ব্যাখ্যা:** Data + method একসাথে এবং controlled access।

### Q68. How is encapsulation achieved in Java?
**English Answer:** Commonly with private fields and controlled access through getters/setters.
**বাংলা ব্যাখ্যা:** private field + getter/setter।

### Q69. What is data hiding?
**English Answer:** Data hiding prevents direct external access to internal object data.
**বাংলা ব্যাখ্যা:** বাইরের code যেন internal data সরাসরি access না করতে পারে।

### Q70. What is inheritance?
**English Answer:** Inheritance allows a child class to acquire properties and methods from a parent class.
**বাংলা ব্যাখ্যা:** Parent-এর feature child পায়।

### Q71. Which Java keyword is used for class inheritance?
**English Answer:** extends.
**বাংলা ব্যাখ্যা:** class Car extends Vehicle।

### Q72. What is single inheritance?
**English Answer:** One child class inherits from one parent class.
**বাংলা ব্যাখ্যা:** A → B।

### Q73. What is multilevel inheritance?
**English Answer:** Inheritance through multiple levels, such as A → B → C.
**বাংলা ব্যাখ্যা:** একাধিক স্তরের inheritance।

### Q74. What is hierarchical inheritance?
**English Answer:** Multiple child classes inherit from one parent.
**বাংলা ব্যাখ্যা:** A → B এবং A → C।

### Q75. Does Java support multiple inheritance through classes?
**English Answer:** No.
**বাংলা ব্যাখ্যা:** এক class একাধিক class extend করতে পারে না।

### Q76. Why does Java avoid multiple class inheritance?
**English Answer:** To avoid ambiguity such as the diamond problem.
**বাংলা ব্যাখ্যা:** দুই parent-এর same method হলে ambiguity হয়।

### Q77. How can Java support multiple inheritance-like behavior?
**English Answer:** A class can implement multiple interfaces.
**বাংলা ব্যাখ্যা:** একাধিক interface implement করা যায়।

### Q78. What is polymorphism?
**English Answer:** Polymorphism is the ability of one interface/name to take multiple forms.
**বাংলা ব্যাখ্যা:** এক নাম/interface-এর multiple behavior।

### Q79. What is compile-time polymorphism?
**English Answer:** Method overloading is the common form of compile-time polymorphism.
**বাংলা ব্যাখ্যা:** Compiler parameter দেখে method select করে।

### Q80. What is runtime polymorphism?
**English Answer:** Method overriding is the common form of runtime polymorphism.
**বাংলা ব্যাখ্যা:** Runtime-এ actual object অনুযায়ী method select হয়।

### Q81. What is abstraction?
**English Answer:** Abstraction exposes essential features while hiding implementation details.
**বাংলা ব্যাখ্যা:** দরকারি অংশ দেখিয়ে complexity লুকানো।

### Q82. Encapsulation vs abstraction?
**English Answer:** Encapsulation focuses on bundling/access control; abstraction focuses on hiding implementation complexity.
**বাংলা ব্যাখ্যা:** Encapsulation = access control; abstraction = implementation hiding।

### Q83. What is method overloading?
**English Answer:** Same method name with different parameter lists, usually in the same class.
**বাংলা ব্যাখ্যা:** Name same, parameter different।

### Q84. What is method overriding?
**English Answer:** A child class provides a new implementation of an inherited method with the same signature.
**বাংলা ব্যাখ্যা:** Parent method child নিজের মতো redefine করে।

### Q85. Overloading is compile-time or runtime?
**English Answer:** Compile-time.
**বাংলা ব্যাখ্যা:** Compile-time polymorphism।

### Q86. Overriding is compile-time or runtime?
**English Answer:** Runtime.
**বাংলা ব্যাখ্যা:** Runtime polymorphism।

### Q87. Can return type alone overload a method?
**English Answer:** No.
**বাংলা ব্যাখ্যা:** Parameter list different হওয়া দরকার।

### Q88. Does overriding require inheritance?
**English Answer:** Yes.
**বাংলা ব্যাখ্যা:** Parent-child relationship দরকার।

### Q89. What is dynamic method dispatch?
**English Answer:** Runtime selection of an overridden method based on the actual object.
**বাংলা ব্যাখ্যা:** Reference type নয়, actual object অনুযায়ী method চলে।

### Q90. What is an abstract class?
**English Answer:** A class that cannot normally be instantiated and may contain abstract and concrete methods.
**বাংলা ব্যাখ্যা:** Abstract class-এর direct object সাধারণত তৈরি করা যায় না।

### Q91. What is an abstract method?
**English Answer:** A method declared without an implementation.
**বাংলা ব্যাখ্যা:** Declaration থাকে, body থাকে না।

### Q92. What is an interface?
**English Answer:** An interface defines a contract that implementing classes agree to follow.
**বাংলা ব্যাখ্যা:** Class কী behavior provide করবে তার contract।

### Q93. Can a class implement multiple interfaces?
**English Answer:** Yes.
**বাংলা ব্যাখ্যা:** একাধিক interface implement করা যায়।

### Q94. What keyword is used to implement an interface?
**English Answer:** implements.
**বাংলা ব্যাখ্যা:** class X implements A।

### Q95. What is an access modifier?
**English Answer:** It controls where a class member can be accessed.
**বাংলা ব্যাখ্যা:** Member-এর accessibility control করে।

### Q96. What does private mean?
**English Answer:** Accessible only within the declaring class.
**বাংলা ব্যাখ্যা:** শুধু নিজের class-এর ভিতরে।

### Q97. What does protected mean?
**English Answer:** Accessible within the package and through subclasses subject to Java's rules.
**বাংলা ব্যাখ্যা:** Same package ও subclass-এর access।

### Q98. What does public mean?
**English Answer:** Accessible wherever the class/member is accessible.
**বাংলা ব্যাখ্যা:** সবচেয়ে broad access।

### Q99. What is object-oriented analysis?
**English Answer:** It identifies objects, classes, responsibilities, relationships, and requirements in a problem domain.
**বাংলা ব্যাখ্যা:** Real-world problem-কে object/class/relationship হিসেবে analyze করা।

### Q100. What is object-oriented design?
**English Answer:** It turns the analysis into a software structure of classes, objects, interfaces, and relationships.
**বাংলা ব্যাখ্যা:** Analysis থেকে software architecture/design তৈরি করা।

### Q101. What is object persistence?
**English Answer:** It means preserving an object's state beyond the lifetime of the program/process.
**বাংলা ব্যাখ্যা:** Program বন্ধ হলেও object-এর data টিকে থাকে।

### Q102. What is an object-oriented database?
**English Answer:** A database designed to store and manage objects, attributes, methods, and relationships.
**বাংলা ব্যাখ্যা:** Object model-এ data store/manage করে।

### Q103. What is bytecode?
**English Answer:** Bytecode is the intermediate .class code produced by the Java compiler.
**বাংলা ব্যাখ্যা:** javac-এর তৈরি intermediate code।

### Q104. Is bytecode platform-independent?
**English Answer:** Yes.
**বাংলা ব্যাখ্যা:** Bytecode platform-independent।

### Q105. Is JVM platform-independent?
**English Answer:** No. JVM implementations are platform-dependent.
**বাংলা ব্যাখ্যা:** OS অনুযায়ী JVM implementation আলাদা।

### Q106. Why is Java platform independent?
**English Answer:** Because the same bytecode can run on a suitable JVM for different platforms.
**বাংলা ব্যাখ্যা:** একই bytecode বিভিন্ন OS-এর JVM-এ চলে।

### Q107. What is WORA?
**English Answer:** Write Once, Run Anywhere.
**বাংলা ব্যাখ্যা:** Java portability principle।

### Q108. What is JVM?
**English Answer:** JVM is the runtime engine that executes Java bytecode.
**বাংলা ব্যাখ্যা:** Bytecode চালানোর engine।

### Q109. What is JRE?
**English Answer:** JRE provides JVM and runtime libraries needed to run Java applications.
**বাংলা ব্যাখ্যা:** Java program run করার environment।

### Q110. What is JDK?
**English Answer:** JDK contains JRE plus development tools such as the compiler.
**বাংলা ব্যাখ্যা:** Java develop করার kit।

### Q111. What is the JDK/JRE/JVM relationship?
**English Answer:** Conceptually JDK contains JRE, and JRE contains JVM and runtime libraries.
**বাংলা ব্যাখ্যা:** JDK ⊃ JRE ⊃ JVM।

### Q112. What is an exception?
**English Answer:** An exception is an abnormal event that disrupts normal program execution.
**বাংলা ব্যাখ্যা:** Unexpected runtime problem।

### Q113. What is exception handling?
**English Answer:** It is the mechanism for detecting and managing exceptional conditions.
**বাংলা ব্যাখ্যা:** Exception controlledভাবে handle করা।

### Q114. What is try?
**English Answer:** try contains code that may throw an exception.
**বাংলা ব্যাখ্যা:** Risky code এখানে থাকে।

### Q115. What is catch?
**English Answer:** catch handles a matching exception.
**বাংলা ব্যাখ্যা:** Exception ধরা ও handle করা।

### Q116. What is finally?
**English Answer:** finally is used for cleanup code that should execute after try/catch processing.
**বাংলা ব্যাখ্যা:** Cleanup/resource closing-এর জন্য ব্যবহৃত হয়।

### Q117. What does throw do?
**English Answer:** It explicitly throws an exception.
**বাংলা ব্যাখ্যা:** নিজে exception ছোড়ে।

### Q118. What does throws do?
**English Answer:** It declares exceptions a method may propagate.
**বাংলা ব্যাখ্যা:** Method signature-এ exception declare করে।

### Q119. What is a checked exception?
**English Answer:** An exception checked by the compiler and subject to handling/propagation requirements.
**বাংলা ব্যাখ্যা:** Compiler checked করে; handling/propagation enforce হতে পারে।

### Q120. What is an unchecked exception?
**English Answer:** A RuntimeException and its subclasses are unchecked exceptions.
**বাংলা ব্যাখ্যা:** Runtime exception; compile-time handling বাধ্যতামূলক নয়।

### Q121. Give checked exception examples.
**English Answer:** IOException, SQLException, and ClassNotFoundException.
**বাংলা ব্যাখ্যা:** Checked exception-এর common example।

### Q122. Give unchecked exception examples.
**English Answer:** NullPointerException, ArithmeticException, and ArrayIndexOutOfBoundsException.
**বাংলা ব্যাখ্যা:** Runtime exception-এর example।

### Q123. Is Java String mutable?
**English Answer:** No. String is immutable.
**বাংলা ব্যাখ্যা:** String change করলে নতুন object তৈরি হয়।

### Q124. What is StringBuffer?
**English Answer:** A mutable, synchronized character sequence.
**বাংলা ব্যাখ্যা:** Mutable ও synchronized।

### Q125. What is StringBuilder?
**English Answer:** A mutable, non-synchronized character sequence, generally faster for single-threaded modification.
**বাংলা ব্যাখ্যা:** Mutable এবং সাধারণত faster।

### Q126. What is == vs equals() in Java?
**English Answer:** == compares references; equals() compares logical/content equality when appropriately implemented.
**বাংলা ব্যাখ্যা:** Reference বনাম content/value comparison।

### Q127. Why can a == c be false for equal strings?
**English Answer:** Because they may be different objects even if their contents are equal.
**বাংলা ব্যাখ্যা:** Content same, object/reference আলাদা হতে পারে।

### Q128. What is garbage collection?
**English Answer:** Automatic reclamation of memory occupied by unreachable objects.
**বাংলা ব্যাখ্যা:** Unreachable object-এর memory JVM reclaim করে।

### Q129. Does Java have manual free/delete for objects?
**English Answer:** No. Java uses automatic garbage collection.
**বাংলা ব্যাখ্যা:** C/C++-এর মতো manually object free করতে হয় না।

### Q130. What is a static member in Java?
**English Answer:** A member that belongs to the class rather than an individual object.
**বাংলা ব্যাখ্যা:** Class-level member।

### Q131. Can a static method directly use this?
**English Answer:** No, because this refers to a current object and static methods are not tied to one object.
**বাংলা ব্যাখ্যা:** Static method object-specific নয়।

### Q132. What is high cohesion?
**English Answer:** A module/class has closely related responsibilities.
**বাংলা ব্যাখ্যা:** এক class-এর কাজগুলো logically related।

### Q133. What is low coupling?
**English Answer:** Modules have minimal dependency on one another.
**বাংলা ব্যাখ্যা:** এক module-এর change অন্যটায় কম impact ফেলে।

### Q134. Why are high cohesion and low coupling desirable?
**English Answer:** They improve maintainability, testing, reuse, and flexibility.
**বাংলা ব্যাখ্যা:** Software সহজে maintain ও modify করা যায়।

## PART 2 — MUST-KNOW CODE / TRACE ANSWERS
### Q135. What is the output of `2 + 3 * 4`?
**English Answer:** 14.
**বাংলা ব্যাখ্যা:** `*` আগে: 3×4=12; তারপর 2+12=14।

### Q136. What is the output of `10 + 20 % 3 * 2`?
**English Answer:** 14.
**বাংলা ব্যাখ্যা:** `%` ও `*` same precedence, left-to-right: 20%3=2, 2×2=4, 10+4=14।

### Q137. What is the output of `int i=5; printf("%d",i++);`?
**English Answer:** 5.
**বাংলা ব্যাখ্যা:** Post-increment-এ আগে 5 use/print হয়, পরে i=6।

### Q138. What is the output of `int j=5; printf("%d",++j);`?
**English Answer:** 6.
**বাংলা ব্যাখ্যা:** Pre-increment-এ আগে j=6 হয়, তারপর 6 print হয়।

### Q139. What is the output of `int i=0; while(i++<3) print(i);` followed by printing i?
**English Answer:** 1 2 3 4.
**বাংলা ব্যাখ্যা:** Condition-এ post-increment প্রতিবার value use করার পর i বাড়ায়; শেষ failed test-এও i=4 হয়।

### Q140. What is the output of `if(x++>0 && ++x>1)` when x starts at 0?
**English Answer:** x becomes 1.
**বাংলা ব্যাখ্যা:** প্রথম condition false; তাই && short-circuit করে `++x` execute হয় না।

### Q141. What is the important Java loop output from the note?
**English Answer:** `0 6 1 7 2 8 3 8`.
**বাংলা ব্যাখ্যা:** শেষবার i<3 false হওয়ায় `j++` short-circuit হয়ে skip হয়; তাই j=8 থাকে।

## PART 3 — TOP COMPARISONS
### Overloading vs Overriding
**English Answer:** Overloading: same name, different parameters, compile-time. Overriding: same inherited signature, runtime.
**বাংলা ব্যাখ্যা:** Overloading = parameter change; overriding = parent method child redefine করে।

### Encapsulation vs Abstraction
**English Answer:** Encapsulation bundles data/methods and controls access; abstraction hides implementation details.
**বাংলা ব্যাখ্যা:** Encapsulation = access control; abstraction = implementation complexity hide।

### Class vs Object
**English Answer:** Class is a blueprint; object is an instance.
**বাংলা ব্যাখ্যা:** Class = নকশা; object = বাস্তব instance।

### while vs do-while
**English Answer:** while checks before the body; do-while checks after the body.
**বাংলা ব্যাখ্যা:** while zero times চলতে পারে; do-while অন্তত একবার।

### Compiler vs Interpreter
**English Answer:** Compiler translates before execution; interpreter translates/executes during runtime.
**বাংলা ব্যাখ্যা:** Compiler আগে translate করে; interpreter চলার সময় translate করে।

### Syntax vs Semantics
**English Answer:** Syntax is structure; semantics is meaning.
**বাংলা ব্যাখ্যা:** Syntax = grammar; semantics = meaning।

### JDK vs JRE vs JVM
**English Answer:** JDK = JRE + development tools; JRE = JVM + runtime libraries; JVM executes bytecode.
**বাংলা ব্যাখ্যা:** মনে রাখো: JDK ⊃ JRE ⊃ JVM।

### String vs StringBuffer vs StringBuilder
**English Answer:** String immutable; StringBuffer mutable/synchronized; StringBuilder mutable/not synchronized and usually faster.
**বাংলা ব্যাখ্যা:** Immutable → String; synchronized mutable → StringBuffer; fast mutable → StringBuilder।

### Abstract class vs Interface
**English Answer:** Abstract class can contain state/constructors and concrete methods; interface defines a contract and supports multiple implementation.
**বাংলা ব্যাখ্যা:** Shared base/state দরকার হলে abstract class; multiple contract দরকার হলে interface।

## PART 4 — LAST-MINUTE TOP 30 TRAPS
1. `5/2 = 2` in C; `5.0/2 = 2.5`.
2. C-তে floating-point remainder-এর জন্য `fmod()` লাগে; `%` নয়।
3. Java-তে `%` floating-point-এর সাথেও কাজ করে।
4. `round(1.2)=1`, কিন্তু `ceil(1.2)=2`।
5. `i++` = আগে use, পরে increment; `++i` = আগে increment, পরে use।
6. `&&`: first false হলে second expression execute হয় না।
7. `||`: first true হলে second expression execute হয় না।
8. `for`: initialization → condition → body → update।
9. `do-while` অন্তত একবার চলে।
10. `&a` = address; `*p` = pointed value।
11. Java strictly pass-by-value.
12. `static` local variable function call-এর মধ্যে value retain করে।
13. Class = blueprint; Object = instance.
14. OOP-এর 4 pillars = Encapsulation, Inheritance, Polymorphism, Abstraction.
15. Java class দিয়ে multiple inheritance support করে না.
16. Multiple interfaces implement করা যায়।
17. Overloading = compile-time; Overriding = runtime.
18. শুধু return type বদলে overloading করা যায় না।
19. Overriding-এর জন্য inheritance দরকার।
20. `private` member declaring class-এর বাইরে direct access করা যায় না।
21. `protected` same package/subclass access দিতে পারে।
22. `public` broad access দেয়।
23. Bytecode platform-independent; JVM platform-dependent.
24. Java principle = WORA: Write Once, Run Anywhere.
25. JDK ⊃ JRE ⊃ JVM.
26. Checked exceptions compiler-level checking-এর আওতায়; unchecked exceptions runtime family.
27. `String` immutable.
28. `==` reference comparison; `.equals()` logical/content equality-এর জন্য।
29. Java object memory automatic garbage collection-এর মাধ্যমে reclaim করা হয়।
30. `static` method-এ `this` ব্যবহার করা যায় না।

## PART 5 — COURSE-OUTLINE COVERAGE CHECK
- **CSE 110:** Computer/programming fundamentals, algorithm, flowchart, information representation, data types/operators, debugging, arrays, pointers, functions, recursion, iteration, basic algorithm analysis, file handling.
- **CSE 111:** Data structures, syntax/formal specification, syntax vs semantics, formal languages, mathematical preliminaries at viva level, structured programming, high-level language features, application/problem design.
- **CSE 310:** Objects/classes, inheritance, polymorphism, abstraction, encapsulation, OOP analysis/design, object persistence, object-oriented database, software principles, advantages/problems of OOP, Java concepts.

## PART 6 — ORIGINAL SOURCE NOTES

> The complete uploaded note is preserved below. This section is intentionally included so the viva file does not silently drop source material.

# 💻 PROGRAMMING & OOP — সম্পূর্ণ নোট
### CSE 110 / 111 / 310 — BRAC MSc CSE Admission

> **Sample paper-এ ৩টা প্রশ্ন** (Q6 fmod, Q7 round, Q8 Java loop trace, Q9 platform independence — আসলে ৪টা)।
> **Q8-এর সম্পূর্ণ trace** Module 3-এ আছে — ওটাই এই বিষয়ের সবচেয়ে গুরুত্বপূর্ণ অংশ।

---

## 📑 সূচি
| Module | বিষয় | Dry Run |
|---|---|---|
| 1 | Data Type · Operator · Precedence | ✅ |
| 2 | **math.h / Math Functions** ⭐ | ✅ |
| 3 | **Loop Tracing (Q8)** ⭐⭐⭐ | ✅ |
| 4 | Pointer · Array · Function | ✅ |
| 5 | **OOP-এর ৪ স্তম্ভ** ⭐⭐⭐ | — |
| 6 | **Overloading vs Overriding** ⭐ | ✅ |
| 7 | **Platform Independence (Q9)** ⭐⭐⭐ | ✅ |
| 8 | Exception · String | — |
| 9 | Final Revision | — |

---
---

# MODULE 1 — DATA TYPE, OPERATOR, PRECEDENCE

## Topic 1: Data Type ও আকার ⭐

| Type | আকার (byte) | পরিসর |
|---|---|---|
| `char` | **1** | −128 to 127 |
| `int` | **4** | −2,147,483,648 to 2,147,483,647 |
| `float` | **4** | ~7 দশমিক ঘর নির্ভুল |
| `double` | **8** | ~15 দশমিক ঘর নির্ভুল |
| `long` (Java) | 8 | বড় পূর্ণসংখ্যা |
| `boolean` (Java) | 1 | true / false |

**Formula:** n bit-এর signed type-এর পরিসর = **−2ⁿ⁻¹ থেকে 2ⁿ⁻¹ − 1**
*উদাহরণ:* `int` = 32 bit → −2³¹ থেকে 2³¹−1

## Topic 2: Operator Precedence ⭐⭐⭐

**উপর থেকে নিচে — উপরেরটা আগে চলে:**

| ক্রম | Operator | দিক |
|---|---|---|
| 1 | `()` `[]` `.` | বাম → ডান |
| 2 | `++` `--` `!` `~` (unary) | **ডান → বাম** |
| 3 | `*` `/` `%` | বাম → ডান |
| 4 | `+` `-` | বাম → ডান |
| 5 | `<<` `>>` | বাম → ডান |
| 6 | `<` `<=` `>` `>=` | বাম → ডান |
| 7 | `==` `!=` | বাম → ডান |
| 8 | `&&` | বাম → ডান |
| 9 | `\|\|` | বাম → ডান |
| 10 | `?:` | ডান → বাম |
| 11 | `=` `+=` `-=` | **ডান → বাম** |

⭐ **মুখস্থ:** **PUMA-RS-LA**
**P**arenthesis → **U**nary → **M**ultiply/Divide/Mod → **A**dd/Sub → **R**elational → **S**hift... মূল কথা: `()` > `++` > `*/%` > `+-` > তুলনা > `&&` > `||` > `=`

### 🔍 DRY RUN — Precedence
```c
int result = 2 + 3 * 4;
```
```
* আগে চলবে → 3*4 = 12
তারপর +    → 2+12 = 14

result = 14   (20 নয়!) ✅
```

```c
int x = 10 + 20 % 3 * 2;
```
```
% আর * সমান precedence → বাম থেকে ডানে
20 % 3 = 2
2 * 2  = 4
10 + 4 = 14   ✅
```

## Topic 3: `i++` vs `++i` ⭐⭐⭐

| | **`i++` (Post-increment)** | **`++i` (Pre-increment)** |
|---|---|---|
| কাজের ক্রম | **আগে ব্যবহার, পরে বাড়ে** | **আগে বাড়ে, পরে ব্যবহার** |

### 🔍 DRY RUN
```c
int i = 5;
printf("%d", i++);    // ছাপবে 5, তারপর i হবে 6
printf("%d", i);      // ছাপবে 6

int j = 5;
printf("%d", ++j);    // j আগে 6 হবে, তারপর ছাপবে 6
```

```c
int a = 5;
int b = a++ + ++a;
```
```
ধাপ 1: a++ → বর্তমান মান 5 ব্যবহার হবে, তারপর a = 6
ধাপ 2: ++a → a আগে 7 হবে, তারপর 7 ব্যবহার হবে
ধাপ 3: b = 5 + 7 = 12,  a = 7  ✅
```

## Topic 4: Division ও Modulus ⭐

```c
5 / 2      = 2      ⚠️ Integer division — দশমিক কেটে যায়
5.0 / 2    = 2.5    ✅ একটা float হলেই float division
5 % 2      = 1      ✅ ভাগশেষ

-5 / 2     = -2     (C-তে শূন্যের দিকে কাটে)
-5 % 2     = -1
```

⚠️ **`%` শুধু integer-এ চলে।** `5.5 % 2` লিখলে C-তে **compile error** ⭐

### 🔁 Revision Box
`int`=4 byte, `char`=1, `float`=4, `double`=8। Precedence: **`()` > `++` > `*/%` > `+-` > তুলনা > `&&` > `||` > `=`**। **`i++` = আগে ব্যবহার পরে বাড়ে**, **`++i` = আগে বাড়ে পরে ব্যবহার**। **`5/2 = 2`** (integer division), **`5.0/2 = 2.5`**। **`%` শুধু integer-এ**।

---
---

# MODULE 2 — MATH FUNCTIONS ⭐⭐⭐

> **Q6 ও Q7 এখান থেকে সরাসরি।**

## Topic 1: C-তে `math.h`

| Function | কাজ | উদাহরণ |
|---|---|---|
| **`fmod(a, b)`** | **float-এর ভাগশেষ** ⭐ | `fmod(3.14, 2.1)` = 1.04 |
| **`round(x)`** | নিকটতম পূর্ণসংখ্যায় ⭐ | `round(1.66)` = 2.0 |
| `ceil(x)` | **উপরের** পূর্ণসংখ্যা | `ceil(1.2)` = 2.0 |
| `floor(x)` | **নিচের** পূর্ণসংখ্যা | `floor(1.8)` = 1.0 |
| `pow(a, b)` | a-এর b ঘাত | `pow(2,3)` = 8 |
| `sqrt(x)` | বর্গমূল | `sqrt(16)` = 4 |
| `fabs(x)` | float-এর পরম মান | `fabs(-3.5)` = 3.5 |
| `abs(x)` | int-এর পরম মান | `abs(-5)` = 5 |

⚠️ ব্যবহার করতে হলে **`#include <math.h>`** লিখতে হবে, আর compile-এ **`-lm`** flag লাগতে পারে।

## 🔍 Q6-এর উত্তর — 3.14 ÷ 2.1-এর ভাগশেষ

```c
#include <stdio.h>
#include <math.h>

int main() {
    double result = fmod(3.14, 2.1);
    printf("%.2lf", result);      // ফলাফল: 1.04
    return 0;
}
```

**কেন `%` নয়?**
```c
double r = 3.14 % 2.1;    // ❌ Compile Error!
                          // % operator শুধু integer-এ কাজ করে
```

**হিসাব যাচাই:**
```
3.14 ÷ 2.1 = 1.495...
পূর্ণ ভাগফল = 1
ভাগশেষ = 3.14 − (1 × 2.1) = 3.14 − 2.1 = 1.04  ✅
```

**Java-তে:**
```java
double result = 3.14 % 2.1;    // ✅ Java-তে % float-এও চলে!
// অথবা
double result = Math.IEEEremainder(3.14, 2.1);
```
⭐ **এটাই C ও Java-র বড় পার্থক্য — Java-তে `%` float-এ চলে, C-তে চলে না।**

## 🔍 Q7-এর উত্তর — 1.66 কে 2.0 করা

```c
// C
double x = round(1.66);       // 2.0  ✅
```
```java
// Java
long x = Math.round(1.66);    // 2  ✅
double y = Math.ceil(1.66);   // 2.0 ✅ (এটাও কাজ করবে)
```

### ⚠️ round vs ceil vs floor — পার্থক্য দেখো

| মান | `round()` | `ceil()` | `floor()` |
|---|---|---|---|
| 1.2 | **1** | **2** | **1** |
| 1.5 | **2** | 2 | 1 |
| **1.66** | **2** ✅ | **2** | 1 |
| −1.5 | −2 (C) / −1 (Java) | −1 | −2 |

⚠️ **Trap:** `ceil(1.2)` = **2** কিন্তু `round(1.2)` = **1** — এই পার্থক্যটা MCQ-তে আসে।

### 🔁 Revision Box
**`fmod(3.14, 2.1)` = 1.04** — C-তে float-এর ভাগশেষ (`%` চলে না)। **Java-তে `%` float-এও চলে**। **`round(1.66)` = 2.0** / `Math.round(1.66)` = 2। **`ceil` = উপরে, `floor` = নিচে, `round` = নিকটতম**।

---
---

# MODULE 3 — LOOP TRACING ⭐⭐⭐

> **Q8 এখানে। এটাই সবচেয়ে বেশি নম্বরের একক প্রশ্ন — ধাপে ধাপে করছি।**

## Topic 1: Short-Circuit Evaluation ⭐⭐⭐

### নিয়ম
| Operator | নিয়ম |
|---|---|
| **`&&` (AND)** | **প্রথমটা `false` হলে দ্বিতীয়টা মোটেও চলবে না** ⭐ |
| **`\|\|` (OR)** | **প্রথমটা `true` হলে দ্বিতীয়টা মোটেও চলবে না** |

```c
int i = 0;
if (0 && (i++ > 5))  { }
// প্রথমটা false → i++ কখনো চলবে না → i রয়ে গেল 0 ⚠️

if (1 || (i++ > 5))  { }
// প্রথমটা true → i++ চলবে না → i এখনো 0
```

⭐ **এটাই Q8-এর পুরো ফাঁদ।**

## Topic 2: `for` loop-এর চলার ক্রম ⭐

```c
for (initialization ; condition ; update) {
    body
}
```

**চলার ক্রম:**
```
1. Initialization      (একবারই)
2. Condition যাচাই  →  false হলে loop শেষ
3. Body চলে
4. Update চলে
5. আবার ধাপ 2-এ ফিরে যায়
```

⚠️ **গুরুত্বপূর্ণ:** Update (`i++`) **body-র পরে** চলে, আগে নয়।

---

## 🔍 Q8-এর সম্পূর্ণ DRY RUN ⭐⭐⭐

```java
public class Test {
    public static void main(String args[]) {
        int i = 0, j = 5;
        for( ; (i < 3) && (j++ < 10) ; i++ ) {
            System.out.print(" " + i + " " + j );
        }
        System.out.print(" " + i + " " + j );
    }
}
```

### লক্ষ্য করার তিনটি বিষয়
1. **Initialization খালি** — `i=0, j=5` আগেই সেট করা
2. Condition-এ **`j++`** আছে — condition যাচাই করার সময়ই j বাড়ে
3. **`&&` short-circuit** — `i < 3` false হলে `j++` চলবেই না ⚠️

### ধাপে ধাপে

```
শুরু: i = 0, j = 5
```

**─── পুনরাবৃত্তি ১ ───**
```
Condition যাচাই:
  (i < 3)  →  0 < 3  →  TRUE ✅
  (j++ < 10) →  j-র বর্তমান মান 5 ব্যবহার হবে → 5 < 10 → TRUE ✅
              তারপর j বেড়ে হলো 6
  সামগ্রিক: TRUE && TRUE = TRUE → loop চলবে

Body:  print " " + i + " " + j  →  " 0 6"

Update: i++  →  i = 1
```

**─── পুনরাবৃত্তি ২ ───**
```
Condition:
  (1 < 3) → TRUE ✅
  (j++ < 10) → 6 < 10 → TRUE ✅, তারপর j = 7
  → loop চলবে

Body:  " 1 7"

Update: i++  →  i = 2
```

**─── পুনরাবৃত্তি ৩ ───**
```
Condition:
  (2 < 3) → TRUE ✅
  (j++ < 10) → 7 < 10 → TRUE ✅, তারপর j = 8
  → loop চলবে

Body:  " 2 8"

Update: i++  →  i = 3
```

**─── পুনরাবৃত্তি ৪ (চেষ্টা) ───**
```
Condition:
  (3 < 3) → FALSE ❌

  ⚠️ SHORT-CIRCUIT!  && এর প্রথমটা false, তাই
     (j++ < 10) মোটেও চলবে না
     → j বাড়বে না, j রয়ে গেল 8

  → loop শেষ
```

**─── Loop-এর বাইরের print ───**
```
i = 3,  j = 8
print " 3 8"
```

### ✅ চূড়ান্ত উত্তর

```
Output:  0 6 1 7 2 8 3 8
```

### সারণী আকারে
| পুনরাবৃত্তি | i | j (যাচাইয়ের আগে) | i<3 | j++<10 | j (পরে) | ছাপা হলো |
|---|---|---|---|---|---|---|
| 1 | 0 | 5 | ✅ | ✅ | 6 | ` 0 6` |
| 2 | 1 | 6 | ✅ | ✅ | 7 | ` 1 7` |
| 3 | 2 | 7 | ✅ | ✅ | 8 | ` 2 8` |
| 4 | 3 | 8 | ❌ | **চলেনি** | **8** | — |
| শেষ | 3 | 8 | — | — | — | ` 3 8` |

### ⚠️ সবচেয়ে বড় ভুল যেটা মানুষ করে
> শেষে `j = 9` লেখা।
> **কেন ভুল?** কারণ `i < 3` false হওয়ায় short-circuit-এর কারণে `j++` **চলেইনি**। j আটকে গেছে **8**-এ। ⭐

## Topic 3: আরও কিছু Loop Trace

### `while` vs `do-while`
```c
int i = 10;
while (i < 5) { printf("A"); }      // কিছুই ছাপবে না (শর্ত শুরুতেই false)

int j = 10;
do { printf("B"); } while (j < 5);  // "B" একবার ছাপবে ⭐
```
⭐ **`do-while` অন্তত একবার চলবেই** — শর্ত পরে যাচাই হয়।

### Nested loop
```c
for(int i=1; i<=3; i++)
    for(int j=1; j<=2; j++)
        printf("%d%d ", i, j);
```
```
i=1: j=1 → "11", j=2 → "12"
i=2: j=1 → "21", j=2 → "22"
i=3: j=1 → "31", j=2 → "32"

Output: 11 12 21 22 31 32
মোট চলল: 3 × 2 = 6 বার
```

### 🔁 Revision Box
`for` চলার ক্রম: **init → condition → body → update → condition...**। **`&&`-এ প্রথমটা false হলে দ্বিতীয়টা চলে না** (short-circuit) — **Q8-এর পুরো ফাঁদ এটাই**। Q8-এর উত্তর: **` 0 6 1 7 2 8 3 8`**। **`do-while` অন্তত একবার চলে**।

---
---

# MODULE 4 — POINTER, ARRAY, FUNCTION

## Topic 1: Pointer ⭐

```c
int a = 10;
int *p = &a;      // p তে a-র ঠিকানা

printf("%d", a);    // 10   — মান
printf("%p", &a);   // 0x7ffd...  — ঠিকানা
printf("%p", p);    // 0x7ffd...  — একই ঠিকানা
printf("%d", *p);   // 10   — ঠিকানার ভিতরের মান (dereference)
```

```
     a                    p
┌────────┐          ┌──────────┐
│   10   │◄─────────│ 0x1000   │
└────────┘          └──────────┘
 ঠিকানা              p-তে a-র
 0x1000              ঠিকানা রাখা
```

| প্রতীক | অর্থ |
|---|---|
| `&a` | a-র **ঠিকানা** |
| `*p` | p যে ঠিকানায় আছে সেখানকার **মান** |

## Topic 2: Call by Value vs Call by Reference ⭐⭐

### 🔍 DRY RUN
```c
// Call by Value — নকল পাঠানো হয়
void swap1(int x, int y) { int t=x; x=y; y=t; }

// Call by Reference — ঠিকানা পাঠানো হয়
void swap2(int *x, int *y) { int t=*x; *x=*y; *y=t; }

int main() {
    int a=5, b=10;
    swap1(a, b);   printf("%d %d", a, b);   // 5 10  ⚠️ বদলায়নি!
    swap2(&a, &b); printf("%d %d", a, b);   // 10 5  ✅ বদলেছে
}
```

| | **Call by Value** | **Call by Reference** |
|---|---|---|
| কী পাঠায় | মানের **নকল** | **ঠিকানা** |
| মূল variable | **বদলায় না** | **বদলায়** |
| Java-তে | primitive-এর জন্য | object-এর জন্য (reference-এর নকল) |

⚠️ **Java-তে সবকিছুই আসলে call by value** — তবে object-এর ক্ষেত্রে **reference-এর মান** কপি হয়, তাই object-এর ভিতরের data বদলানো যায়।

## Topic 3: Array ও Pointer-এর সম্পর্ক
```c
int arr[5] = {10,20,30,40,50};

arr        ≡  &arr[0]      // array-র নাম = প্রথম element-এর ঠিকানা
*(arr + 2) ≡  arr[2]       // = 30
```

## Topic 4: Storage Class (C)
| Class | কোথায় | আয়ু |
|---|---|---|
| `auto` | Stack | function-এর ভিতরে |
| `static` | Data segment | **পুরো program জুড়ে** ⭐ |
| `extern` | Global | পুরো program |
| `register` | CPU register (অনুরোধ) | function-এর ভিতরে |

### 🔁 Revision Box
`&a` = ঠিকানা, `*p` = ঠিকানার মান। **Call by Value = নকল, মূল বদলায় না**; **Call by Reference = ঠিকানা, মূল বদলায়**। `arr ≡ &arr[0]`, `*(arr+i) ≡ arr[i]`। **`static` variable-এর মান function শেষেও থাকে**।

---
---

# MODULE 5 — OOP-এর ৪ স্তম্ভ ⭐⭐⭐

## Topic 1: Class vs Object

```java
class Car {              // Class = নকশা / blueprint
    String color;        // Attribute (state)
    void drive() { }     // Method (behavior)
}

Car myCar = new Car();   // Object = নকশা থেকে বানানো বাস্তব জিনিস
```

⭐ **Class = নকশা** (একটাই), **Object = সেই নকশা থেকে বানানো** (অনেকগুলো হতে পারে)।

## Topic 2: ৪ স্তম্ভ ⭐⭐⭐

### 1️⃣ Encapsulation
**Definition:** Wrapping **data and methods** together into a single unit and **restricting direct access** to the data.

```java
class Account {
    private double balance;                    // ← বাইরে থেকে ছোঁয়া যাবে না

    public double getBalance() { return balance; }        // Getter
    public void deposit(double amt) {                     // Setter
        if (amt > 0) balance += amt;                      // ← নিয়ন্ত্রণ
    }
}
```
⭐ **Data Hiding** — `private` করে `getter/setter` দিয়ে নিয়ন্ত্রিত access দেওয়া।

### 2️⃣ Inheritance
**Definition:** A class **acquires properties and methods** of another class.

```java
class Vehicle {                          // Parent / Super class
    void start() { }
}
class Car extends Vehicle {              // Child / Sub class
    void openSunroof() { }
}
// Car পাবে start() + নিজের openSunroof()
```

**ধরন:**
| Type | গঠন | Java-তে? |
|---|---|---|
| **Single** | A → B | ✅ |
| **Multilevel** | A → B → C | ✅ |
| **Hierarchical** | A → B, A → C | ✅ |
| **Multiple** | A, B → C | ❌ **class দিয়ে নয়** ⭐ |
| **Hybrid** | মিশ্র | ❌ |

⚠️ **Java-তে multiple inheritance নেই কেন?**
**Diamond Problem** — দুই parent-এ একই নামের method থাকলে child কোনটা নেবে? দ্ব্যর্থতা এড়াতে Java এটা বাদ দিয়েছে। **Interface দিয়ে** এই কাজ করা যায়। ⭐

### 3️⃣ Polymorphism
**Definition:** The ability of one interface to take **many forms**.

| Type | কখন ঠিক হয় | কীভাবে |
|---|---|---|
| **Compile-time (Static)** | **Compile-এর সময়** | **Method Overloading** |
| **Run-time (Dynamic)** | **চলার সময়** | **Method Overriding** |

### 4️⃣ Abstraction
**Definition:** Showing only **essential features** and hiding implementation details.

```java
abstract class Shape {
    abstract void draw();       // শুধু ঘোষণা, কাজ নেই
}
class Circle extends Shape {
    void draw() { /* বৃত্ত আঁকার কাজ */ }
}
```
⭐ **Encapsulation vs Abstraction:**
- **Encapsulation** = **কীভাবে** লুকানো হয় (private + getter/setter)
- **Abstraction** = **কী** লুকানো হয় (implementation-এর জটিলতা)

### 🔁 Revision Box
**Class = নকশা, Object = বাস্তব রূপ**। ৪ স্তম্ভ: **Encapsulation** (data + method একসাথে, private + getter/setter), **Inheritance** (গুণাবলি উত্তরাধিকার, `extends`), **Polymorphism** (এক interface অনেক রূপ), **Abstraction** (শুধু প্রয়োজনীয়টা দেখানো)। **Java-তে multiple inheritance নেই — Diamond Problem; interface দিয়ে হয়**।

---
---

# MODULE 6 — OVERLOADING vs OVERRIDING ⭐⭐⭐

## 🔍 DRY RUN — পার্থক্য দেখো

### Method Overloading (Compile-time)
```java
class Calculator {
    int add(int a, int b)          { return a + b; }        // ১
    int add(int a, int b, int c)   { return a+b+c; }        // ২ — parameter সংখ্যা ভিন্ন
    double add(double a, double b) { return a + b; }        // ৩ — type ভিন্ন
}

Calculator c = new Calculator();
c.add(2, 3);          // ১ নম্বরটা চলবে → 5
c.add(2, 3, 4);       // ২ নম্বরটা চলবে → 9
c.add(2.5, 3.5);      // ৩ নম্বরটা চলবে → 6.0
```
⭐ **একই class-এ একই নামের method, কিন্তু parameter ভিন্ন।**

### Method Overriding (Run-time)
```java
class Animal {
    void sound() { System.out.println("Some sound"); }
}
class Dog extends Animal {
    @Override
    void sound() { System.out.println("Bark"); }     // parent-এর টা বদলে দিলো
}

Animal a = new Dog();     // ⭐ reference Animal, object Dog
a.sound();                // "Bark" ছাপবে (Dog-এর টা)
```
⭐ **এটাই Dynamic Method Dispatch** — কোন method চলবে তা **চলার সময়** object দেখে ঠিক হয়, reference-এর type দেখে নয়। **Run-time polymorphism-এর মূল।**

## Comparison ⭐⭐⭐

| Feature | **Overloading** | **Overriding** |
|---|---|---|
| কখন ঠিক হয় | **Compile time** | **Run time** |
| Polymorphism | **Static** | **Dynamic** |
| কোথায় | **একই class-এ** | **Parent-Child class-এ** |
| Parameter | **ভিন্ন হতেই হবে** | **হুবহু একই হতে হবে** |
| Return type | ভিন্ন হতে পারে | একই (বা covariant) |
| Inheritance | লাগে না | **লাগে** |

⚠️ **Trap:** শুধু **return type ভিন্ন** করে overload করা যায় **না** — parameter ভিন্ন হতেই হবে ⭐

## Abstract Class vs Interface ⭐

| Feature | **Abstract Class** | **Interface** |
|---|---|---|
| Method | Abstract + concrete দুটোই | সব abstract (Java 8+ এ default/static চলে) |
| Variable | যেকোনো ধরনের | সব `public static final` |
| Constructor | ✅ আছে | ❌ নেই |
| Multiple | ❌ একটাই extend করা যায় | ✅ **একাধিক implement করা যায়** ⭐ |
| Keyword | `extends` | `implements` |
| কখন | কিছু সাধারণ code শেয়ার করতে | শুধু চুক্তি (contract) ঠিক করতে |

## Access Modifiers ⭐

| Modifier | একই class | একই package | Child class | সব জায়গায় |
|---|---|---|---|---|
| `private` | ✅ | ❌ | ❌ | ❌ |
| `default` | ✅ | ✅ | ❌ | ❌ |
| `protected` | ✅ | ✅ | ✅ | ❌ |
| `public` | ✅ | ✅ | ✅ | ✅ |

### 🔁 Revision Box
**Overloading = একই class, parameter ভিন্ন, compile-time**। **Overriding = parent-child, parameter হুবহু একই, run-time**। শুধু return type বদলে overload হয় **না**। **Abstract class = `extends`, একটাই**; **Interface = `implements`, একাধিক**। Access: `private < default < protected < public`।

---
---

# MODULE 7 — PLATFORM INDEPENDENCE ⭐⭐⭐

> **Q9-এর উত্তর।**

## 🔍 DRY RUN — Java কীভাবে চলে

```
     Test.java  (Source Code — মানুষের পড়ার মতো)
         │
         │  javac Test.java
         ▼
   ┌─────────────────┐
   │  Java Compiler  │
   └─────────────────┘
         │
         ▼
     Test.class  (BYTECODE — মধ্যবর্তী রূপ) ⭐
         │
         │  একই .class file সব OS-এ চলবে
         │
    ┌────┴──────┬──────────┐
    ▼           ▼          ▼
┌────────┐ ┌────────┐ ┌────────┐
│JVM for │ │JVM for │ │JVM for │   ← JVM প্রতিটি OS-এর জন্য আলাদা
│Windows │ │ Linux  │ │  Mac   │
└────────┘ └────────┘ └────────┘
    │           │          │
    ▼           ▼          ▼
 Machine     Machine    Machine
  Code        Code       Code
```

## মূল কথা ⭐⭐⭐

> **Bytecode হলো platform-independent। JVM হলো platform-dependent।**

এই এক বাক্যেই Q9-এর উত্তরের সারমর্ম।

### Q9-এর পূর্ণ উত্তর

> **Platform Independence** মানে একটি programming language-এ লেখা program একবার compile করে **যেকোনো operating system-এ কোনো পরিবর্তন ছাড়াই** চালানো যাওয়া।
>
> Java এটি অর্জন করে **Bytecode** ব্যবহার করে। Java compiler (`javac`) source code-কে সরাসরি machine code-এ নয়, **Bytecode** (`.class` file)-এ রূপান্তর করে। এই Bytecode কোনো নির্দিষ্ট OS-নির্ভর নয়।
>
> প্রতিটি operating system-এর জন্য আলাদা **JVM (Java Virtual Machine)** থাকে, যা সেই Bytecode-কে ঐ machine-এর নিজস্ব code-এ রূপান্তর করে চালায়।
>
> এজন্যই Java-র নীতি: **"Write Once, Run Anywhere" (WORA)**।
>
> সংক্ষেপে — **Bytecode platform-independent, কিন্তু JVM platform-dependent**।

## Java vs C/C++ ⭐

| | **Java** | **C / C++** |
|---|---|---|
| Compile হয়ে যায় | **Bytecode** | **Machine code** |
| Platform | **Independent** ✅ | **Dependent** ❌ |
| চালায় | **JVM** | সরাসরি OS |
| গতি | কিছুটা ধীর (JVM layer) | **দ্রুত** |
| Memory | **Garbage Collector** | manual (`free`, `delete`) |
| Pointer | নেই (reference আছে) | আছে |

## JDK vs JRE vs JVM ⭐⭐

```
┌─────────────────────────────────────┐
│  JDK  (Java Development Kit)        │  ← বানানোর জন্য
│  ┌───────────────────────────────┐  │
│  │  JRE  (Java Runtime Env.)     │  │  ← চালানোর জন্য
│  │  ┌─────────────────────────┐  │  │
│  │  │  JVM (Virtual Machine)  │  │  │  ← আসল ইঞ্জিন
│  │  └─────────────────────────┘  │  │
│  │      + Library                │  │
│  └───────────────────────────────┘  │
│      + Compiler (javac), Debugger    │
└─────────────────────────────────────┘
```

| | কী আছে | কার জন্য |
|---|---|---|
| **JVM** | Bytecode চালানোর ইঞ্জিন | — |
| **JRE** | JVM + Library | যারা **শুধু চালাবে** |
| **JDK** | JRE + Compiler + Tools | **Developer** |

### 🔁 Revision Box
**Source (.java) → Compiler (javac) → Bytecode (.class) → JVM → Machine code**।
⭐ **Bytecode platform-independent, JVM platform-dependent** — এটাই মূল উত্তর।
নীতি: **"Write Once, Run Anywhere"**। **JDK ⊃ JRE ⊃ JVM**।

---
---

# MODULE 8 — EXCEPTION & STRING

## Topic 1: Exception Handling ⭐

```java
try {
    int x = 10 / 0;                          // ঝুঁকিপূর্ণ code
} catch (ArithmeticException e) {
    System.out.println("Divide by zero!");   // ভুল সামলানো
} finally {
    System.out.println("সবসময় চলবে");        // ⭐ ভুল হোক না হোক, চলবেই
}
```

| Keyword | কাজ |
|---|---|
| `try` | ঝুঁকিপূর্ণ code |
| `catch` | ভুল ধরা |
| `finally` | **সবসময়** চলে (resource বন্ধ করতে) |
| `throw` | **নিজে** exception তৈরি করা |
| `throws` | Method **ঘোষণা** করে যে সে exception ছুঁড়তে পারে |

### Checked vs Unchecked ⭐

| | **Checked** | **Unchecked (Runtime)** |
|---|---|---|
| কখন ধরা পড়ে | **Compile time** | **Run time** |
| Handle করা | **বাধ্যতামূলক** | ঐচ্ছিক |
| উদাহরণ | `IOException`, `SQLException`, `ClassNotFoundException` | `NullPointerException`, `ArithmeticException`, `ArrayIndexOutOfBoundsException` |

## Topic 2: String ⭐

| | `String` | `StringBuffer` | `StringBuilder` |
|---|---|---|---|
| পরিবর্তনযোগ্য? | ❌ **Immutable** | ✅ Mutable | ✅ Mutable |
| Thread-safe? | ✅ | ✅ **হ্যাঁ** (synchronized) | ❌ না |
| গতি | ধীর (বারবার বদলালে) | ধীর | **দ্রুত** ⭐ |

### ⚠️ `==` vs `.equals()` ⭐⭐⭐
```java
String a = "hello";
String b = "hello";
String c = new String("hello");

a == b          // true   (দুটোই string pool-এর একই object)
a == c          // false  ⚠️ (c আলাদা object, ঠিকানা ভিন্ন)
a.equals(c)     // true   ✅ (মান তুলনা করে)
```
⭐ **`==` ঠিকানা তুলনা করে, `.equals()` মান তুলনা করে।** নিশ্চিত MCQ।

### 🔁 Revision Box
`try-catch-finally`; **`finally` সবসময় চলে**। **Checked = compile-time, handle বাধ্যতামূলক** (IOException); **Unchecked = runtime** (NullPointerException)। **String immutable**, StringBuffer **thread-safe**, StringBuilder **দ্রুত**। **`==` ঠিকানা, `.equals()` মান**।

---
---

# ★ FINAL REVISION

## 1. Sample Paper-এর উত্তর ⭐⭐⭐

**Q6.** `fmod(3.14, 2.1)` → **1.04** (C-তে `%` float-এ চলে না; Java-তে `3.14 % 2.1` লেখা যায়)

**Q7.** `round(1.66)` → **2.0** · Java-তে `Math.round(1.66)` → **2**

**Q8.** Output: **` 0 6 1 7 2 8 3 8`**
> মূল কারণ — শেষবার `i < 3` false হওয়ায় **short-circuit**-এর জন্য `j++` চলেনি, তাই j আটকে গেছে 8-এ।

**Q9.** Bytecode + JVM = "Write Once, Run Anywhere"। **Bytecode platform-independent, JVM platform-dependent**।

## 2. Top 20 MCQ Traps ⭐

1. **`5/2 = 2`** (integer division), **`5.0/2 = 2.5`**
2. **C-তে `%` float-এ চলে না** — `fmod()` লাগে; **Java-তে চলে**
3. **`round(1.2) = 1` কিন্তু `ceil(1.2) = 2`**
4. **`&&`-এ প্রথমটা false হলে দ্বিতীয়টা চলে না** (short-circuit)
5. **`i++` = আগে ব্যবহার**, **`++i` = আগে বাড়ে**
6. **`do-while` অন্তত একবার চলে**
7. `for`-এ **update body-র পরে** চলে
8. **Java-তে multiple inheritance নেই** (Diamond Problem) — interface দিয়ে হয়
9. **Overloading = compile-time**, **Overriding = run-time**
10. শুধু **return type বদলে overload করা যায় না**
11. **Interface একাধিক implement করা যায়**, class একটাই extend
12. **Constructor-এর return type থাকে না**, class-এর নামেই হয়
13. **`==` ঠিকানা তুলনা, `.equals()` মান তুলনা**
14. **String immutable**
15. **`finally` সবসময় চলে** (return থাকলেও)
16. **Checked = compile-time** (IOException), **Unchecked = runtime** (NullPointerException)
17. **Bytecode platform-independent, JVM platform-dependent**
18. **JDK ⊃ JRE ⊃ JVM**
19. **`static` method-এ `this` ব্যবহার করা যায় না**
20. **Call by Value-তে মূল variable বদলায় না**

## 3. দ্রুত সংজ্ঞা

| Term | এক লাইনে |
|---|---|
| **Class** | Object তৈরির নকশা |
| **Object** | Class-এর বাস্তব রূপ |
| **Constructor** | Object তৈরির সময় নিজে থেকে চলা method, return type নেই |
| **Encapsulation** | Data + method একসাথে, private + getter/setter |
| **Inheritance** | Parent-এর গুণাবলি child পায় |
| **Polymorphism** | এক নাম, অনেক রূপ |
| **Abstraction** | শুধু প্রয়োজনীয়টা দেখানো |
| **Bytecode** | Platform-independent মধ্যবর্তী code |
| **JVM** | Bytecode চালানোর platform-নির্ভর ইঞ্জিন |
| **Garbage Collector** | অব্যবহৃত memory স্বয়ংক্রিয়ভাবে মুক্ত করা |

---

# ✍️ নিজে করো (উত্তর নিচে)

```java
// 1.
int i = 0;
while (i++ < 3) { System.out.print(i + " "); }
System.out.print(i);

// 2.
int a = 5;
int b = ++a + a++;
System.out.println(a + " " + b);

// 3.
int x = 0;
if (x++ > 0 && ++x > 1) { }
System.out.println(x);
```

<details>
<summary>উত্তর</summary>

**1.**
```
i=0: 0<3 ✅, i হয় 1 → ছাপে "1 "
i=1: 1<3 ✅, i হয় 2 → ছাপে "2 "
i=2: 2<3 ✅, i হয় 3 → ছাপে "3 "
i=3: 3<3 ❌, i হয় 4 → loop শেষ
শেষে ছাপে 4

Output: 1 2 3 4
```

**2.**
```
++a → a আগে 6 হয়, 6 ব্যবহার হয়
a++ → বর্তমান 6 ব্যবহার হয়, তারপর a = 7
b = 6 + 6 = 12,  a = 7

Output: 7 12
```

**3.**
```
x++ > 0  →  0 > 0 → FALSE, কিন্তু x বেড়ে হলো 1
&& এর প্রথমটা false → SHORT-CIRCUIT → ++x চলবেই না
x রয়ে গেল 1

Output: 1
```
(⭐ এটাও Q8-এর মতোই short-circuit-এর ফাঁদ)

</details>
