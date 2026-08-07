# CSE 370 — DATABASE SYSTEMS
## Short Master Viva Notes
### প্রতিটি syllabus topic: 1–5 lines | English Answer + বাংলা ব্যাখ্যা

---

## 1. Database
**English:** A database is an organized collection of related data that can be stored, accessed, and managed efficiently.  
**বাংলা:** সম্পর্কিত data-কে structuredভাবে সংরক্ষণ করার collection হলো database।

## 2. Database System
**English:** A database system consists of the database, DBMS, applications, users, and supporting hardware/software.  
**বাংলা:** শুধু database নয়; DBMS, users, application ও প্রয়োজনীয় system মিলেই database system।

## 3. DBMS
**English:** A Database Management System is software used to define, create, store, retrieve, update, and control access to databases.  
**বাংলা:** Database তৈরি, manage, query, update ও security control করার software হলো DBMS।

## 4. Storing Data
**English:** DBMS stores data in an organized persistent form so it can be retrieved and updated efficiently.  
**বাংলা:** Data এমনভাবে store করা হয় যাতে পরে সহজে retrieve ও update করা যায়।

## 5. Manipulating Data
**English:** Data manipulation includes inserting, retrieving, updating, and deleting data. These are commonly expressed using SQL.  
**বাংলা:** Data insert, select/retrieve, update ও delete করাকে data manipulation বলে।

## 6. Stored Form
**English:** Stored data is persistent data kept on secondary storage so it remains available beyond program execution.  
**বাংলা:** Program বন্ধ হলেও যে data storage-এ থেকে যায় সেটিই persistent/stored data।

## 7. File Organisation
**English:** File organization determines how records are physically arranged in storage to support efficient access.  
**বাংলা:** Storage-এ record কীভাবে সাজানো থাকবে তা file organization নির্ধারণ করে।

## 8. File Retrieval
**English:** File retrieval is the process of locating and obtaining required records from stored data.  
**বাংলা:** Stored file/data থেকে প্রয়োজনীয় record খুঁজে বের করাই retrieval।

## 9. Database Model
**English:** A database model defines how data, relationships, constraints, and operations are represented.  
**বাংলা:** Database-এ data ও relationship কীভাবে represent হবে তার structure/model হলো database model।

## 10. Common Database Models
**English:** Major models include hierarchical, network, relational, object-oriented, and NoSQL-oriented models.  
**বাংলা:** Different models differentভাবে data ও relationship represent করে; relational model সবচেয়ে widely used traditional model।

## 11. Database Design
**English:** Database design is the process of identifying data requirements and creating an appropriate schema, relationships, and constraints.  
**বাংলা:** Requirement অনুযায়ী table, relationship, key ও constraint design করাই database design।

## 12. Database Schema
**English:** A schema is the logical structure/definition of a database, including tables, attributes, relationships, and constraints.  
**বাংলা:** Database-এর logical blueprint হলো schema।

## 13. DBMS Principles
**English:** DBMS principles include controlled data access, consistency, integrity, security, concurrency, and reliable data management.  
**বাংলা:** DBMS-এর লক্ষ্য হলো data reliable, consistent, secure ও efficiently manageable রাখা।

## 14. Relational Database
**English:** A relational database represents data using tables consisting of rows and columns, with relationships represented through keys.  
**বাংলা:** Relational database-এ data table আকারে থাকে; row = record, column = attribute।

## 15. RDBMS
**English:** A Relational Database Management System manages relational databases using tables, keys, constraints, and relational operations.  
**বাংলা:** Relational database manage করার DBMS হলো RDBMS।

## 16. Relation
**English:** In the relational model, a relation is conceptually represented as a table of tuples and attributes.  
**বাংলা:** Relation সাধারণভাবে table হিসেবে দেখা হয়।

## 17. Tuple
**English:** A tuple is a single row/record in a relation.  
**বাংলা:** Table-এর প্রতিটি row হলো tuple/record।

## 18. Attribute
**English:** An attribute is a named property/column of a relation.  
**বাংলা:** Table-এর column হলো attribute।

## 19. Primary Key
**English:** A primary key uniquely identifies each row in a table and cannot contain NULL values.  
**বাংলা:** প্রতিটি record uniquely identify করে; duplicate বা NULL primary key value allowed নয়।

## 20. Foreign Key
**English:** A foreign key is an attribute or set of attributes that references a key in another or the same table to represent relationships.  
**বাংলা:** দুই table-এর মধ্যে relationship তৈরি/maintain করতে foreign key ব্যবহৃত হয়।

## 21. Candidate Key
**English:** A candidate key is a minimal set of attributes that can uniquely identify a row.  
**বাংলা:** যে minimal attribute set uniquely record identify করতে পারে সেটি candidate key।

## 22. Composite Key
**English:** A composite key consists of two or more attributes used together to uniquely identify a row.  
**বাংলা:** একাধিক column মিলে key তৈরি করলে composite key।

## 23. Query
**English:** A query is a request for retrieving or manipulating data in a database.  
**বাংলা:** Database থেকে information চাওয়া বা data manipulate করার instruction হলো query।

## 24. Query Formulation
**English:** Query formulation means expressing a required data operation in a database query language such as SQL.  
**বাংলা:** User-এর information need-কে SQL query-তে convert করাই query formulation।

## 25. Query Language
**English:** A query language allows users to retrieve and manipulate data and sometimes define database structures. SQL is the standard language for relational databases.  
**বাংলা:** Database-এর সাথে communicate করার language হলো query language; relational DB-তে SQL সবচেয়ে গুরুত্বপূর্ণ।

## 26. SQL
**English:** SQL (Structured Query Language) is used to define, query, manipulate, and control relational database data.  
**বাংলা:** Relational database-এর data ও structure manage করার প্রধান language হলো SQL।

## 27. DDL
**English:** Data Definition Language defines or changes database objects. Common commands include CREATE, ALTER, and DROP.  
**বাংলা:** Database structure/table তৈরি বা পরিবর্তনের জন্য DDL ব্যবহৃত হয়।

## 28. DML
**English:** Data Manipulation Language modifies data using commands such as INSERT, UPDATE, and DELETE; SELECT is commonly treated as data retrieval/query language.  
**বাংলা:** Table-এর data insert, update, delete করার command group হলো DML।

## 29. DQL / SELECT
**English:** SELECT retrieves data from one or more tables and can use filtering, grouping, sorting, and joins.  
**বাংলা:** Database থেকে data বের করার সবচেয়ে গুরুত্বপূর্ণ SQL command হলো SELECT।

## 30. DCL
**English:** Data Control Language manages privileges, commonly using GRANT and REVOKE.  
**বাংলা:** User-এর database access permission control করতে DCL ব্যবহৃত হয়।

## 31. TCL
**English:** Transaction Control Language manages transaction boundaries, commonly using COMMIT and ROLLBACK.  
**বাংলা:** Transaction-এর changes permanently save বা undo করতে TCL ব্যবহৃত হয়।

## 32. SELECT
**English:** SELECT retrieves specified columns/expressions from one or more tables.  
**বাংলা:** কোন data দেখতে হবে তা SELECT দিয়ে specify করা হয়।

## 33. WHERE
**English:** WHERE filters rows according to a condition before grouping/aggregation.  
**বাংলা:** Condition অনুযায়ী নির্দিষ্ট row select করতে WHERE ব্যবহার হয়।

## 34. ORDER BY
**English:** ORDER BY sorts query results in ascending or descending order.  
**বাংলা:** Result sort করতে ORDER BY ব্যবহার হয়।

## 35. GROUP BY
**English:** GROUP BY groups rows with the same values so aggregate functions can be applied per group.  
**বাংলা:** একই value-এর row group করে aggregate calculation করতে GROUP BY ব্যবহার হয়।

## 36. HAVING
**English:** HAVING filters groups after GROUP BY, especially based on aggregate conditions.  
**বাংলা:** Group/aggregate result filter করতে HAVING ব্যবহার হয়।

## 37. Aggregate Functions
**English:** Common aggregate functions include COUNT, SUM, AVG, MIN, and MAX.  
**বাংলা:** একাধিক row-এর ওপর calculation করে summary result দেয়।

## 38. JOIN
**English:** JOIN combines rows from related tables based on a matching or specified condition.  
**বাংলা:** একাধিক related table-এর data একসাথে আনতে JOIN ব্যবহার হয়।

## 39. INNER JOIN
**English:** INNER JOIN returns rows with matching values in both joined tables.  
**বাংলা:** দুই table-এই match থাকা record return করে।

## 40. LEFT JOIN
**English:** LEFT JOIN returns all rows from the left table and matching rows from the right table; unmatched right-side values become NULL.  
**বাংলা:** Left table-এর সব row থাকে, match না থাকলে right side NULL হয়।

## 41. RIGHT JOIN
**English:** RIGHT JOIN returns all rows from the right table and matching rows from the left table.  
**বাংলা:** Right table-এর সব row থাকে, match না থাকলে left side NULL হয়।

## 42. Database Administration
**English:** Database administration includes managing users, security, storage, backup/recovery, performance, and database availability.  
**বাংলা:** DBA database-এর security, backup, performance, users ও availability manage করে।

## 43. DBA
**English:** A Database Administrator is responsible for operating, securing, maintaining, backing up, and tuning databases.  
**বাংলা:** Database-এর overall administration ও maintenance-এর দায়িত্বে থাকা ব্যক্তি হলো DBA।

## 44. Data Storage Methods
**English:** Data storage methods determine how records, files, pages, indexes, and related structures are physically organized for efficient access.  
**বাংলা:** Storage-এর ভিতরে data কীভাবে রাখা হবে যাতে access efficient হয় তা storage method নির্ধারণ করে।

## 45. Data Selection
**English:** Data selection identifies required records using queries and conditions such as WHERE, joins, and predicates.  
**বাংলা:** প্রয়োজনীয় record condition/query দিয়ে বেছে নেওয়া হয়।

## 46. Data Presentation
**English:** Data presentation formats query results into useful outputs such as reports, tables, views, or application displays.  
**বাংলা:** Retrieved data user-এর বোঝার মতো format-এ দেখানোকে presentation বলে।

## 47. Database Integrity
**English:** Database integrity ensures that stored data remains accurate, valid, and consistent according to defined rules.  
**বাংলা:** Database-এর data correct, valid ও consistent রাখাই integrity।

## 48. Entity Integrity
**English:** Entity integrity requires every relation to have a primary key and primary-key values cannot be NULL.  
**বাংলা:** Primary key NULL হতে পারবে না এবং record uniquely identify করতে হবে।

## 49. Referential Integrity
**English:** Referential integrity ensures that a foreign-key value refers to a valid referenced key value or is NULL when permitted.  
**বাংলা:** Foreign key যেন invalid/non-existing record reference না করে তা নিশ্চিত করে।

## 50. Domain Integrity
**English:** Domain integrity ensures that an attribute contains values allowed by its data type, range, format, or defined constraints.  
**বাংলা:** Column-এ valid type/range/format-এর value রাখা নিশ্চিত করে।

## 51. Database Security
**English:** Database security protects data against unauthorized access, modification, disclosure, or destruction.  
**বাংলা:** Unauthorized user যেন data দেখতে/পরিবর্তন/নষ্ট করতে না পারে তা security নিশ্চিত করে।

## 52. Authentication
**English:** Authentication verifies the identity of a user or system.  
**বাংলা:** User কে তা verify করাই authentication।

## 53. Authorization
**English:** Authorization determines what an authenticated user is allowed to access or perform.  
**বাংলা:** User কী কী কাজ করতে পারবে তা authorization নির্ধারণ করে।

## 54. Database Languages
**English:** Database languages include SQL components for definition, manipulation, querying, and access control.  
**বাংলা:** Database structure, data, query ও permission manage করার জন্য বিভিন্ন SQL command category ব্যবহৃত হয়।

## 55. Application Packages
**English:** Database application packages/tools provide interfaces for designing, querying, managing, and presenting database data.  
**বাংলা:** Database নিয়ে কাজ সহজ করার জন্য GUI/tools/application packages ব্যবহার করা হয়।

## 56. Common DBMS
**English:** Common relational DBMS examples include MySQL, PostgreSQL, Oracle Database, Microsoft SQL Server, and SQLite.  
**বাংলা:** এগুলো widely used relational database systems।

## 57. Structure of SQL
**English:** SQL contains statements for defining objects, manipulating/querying data, controlling privileges, and managing transactions.  
**বাংলা:** SQL-এর command বিভিন্ন কাজের জন্য ভাগ করা—DDL, DML/query, DCL, TCL ইত্যাদি।

## 58. Principles Behind SQL Design
**English:** SQL is designed around declarative querying: users specify what data/result they want rather than the exact procedural steps to obtain it.  
**বাংলা:** SQL-এ সাধারণত কী result চাই তা বলা হয়; DBMS execution-এর internal method ঠিক করে।

## 59. Declarative Language
**English:** SQL is primarily declarative: the user specifies the desired result, while the DBMS determines how to execute the query.  
**বাংলা:** কী চাই বলা হয়, কীভাবে করবে সেটা DBMS decide করে।

## 60. SQL Constraints
**English:** Constraints enforce rules on data; common examples are PRIMARY KEY, FOREIGN KEY, UNIQUE, NOT NULL, and CHECK.  
**বাংলা:** Invalid data ঢোকা ঠেকাতে constraints ব্যবহার হয়।

## 61. NOT NULL
**English:** NOT NULL requires a column to contain a value rather than NULL.  
**বাংলা:** Column-এ NULL value রাখা যাবে না।

## 62. UNIQUE
**English:** UNIQUE prevents duplicate values in the constrained column or column combination, subject to DBMS NULL semantics.  
**বাংলা:** একই value duplicate হওয়া prevent করে।

## 63. CHECK
**English:** CHECK restricts values according to a Boolean condition.  
**বাংলা:** নির্দিষ্ট condition satisfy না করলে data accept করা হয় না।

## 64. NULL
**English:** NULL represents missing, unknown, or inapplicable information; it is not the same as zero or an empty string.  
**বাংলা:** NULL মানে value জানা নেই/প্রযোজ্য নয়; এটি 0 নয়।

## 65. View
**English:** A view is a virtual table defined by a query and can provide simplified access or restricted data exposure.  
**বাংলা:** Query-এর ওপর ভিত্তি করে তৈরি virtual table হলো view।

## 66. Index
**English:** An index is an auxiliary data structure that can speed up data retrieval at the cost of extra storage and update overhead.  
**বাংলা:** Search দ্রুত করে, তবে extra storage লাগে এবং insert/update কিছুটা costly হতে পারে।

## 67. Transaction
**English:** A transaction is a logical unit of database work that should be completed according to defined transaction guarantees.  
**বাংলা:** Database-এর এক বা একাধিক related operation-এর logical unit হলো transaction।

## 68. COMMIT
**English:** COMMIT permanently makes the current transaction's changes durable according to the DBMS transaction mechanism.  
**বাংলা:** Transaction-এর changes permanently save করার জন্য COMMIT।

## 69. ROLLBACK
**English:** ROLLBACK undoes uncommitted changes of the current transaction according to the DBMS rules.  
**বাংলা:** Commit করার আগে changes undo করতে ROLLBACK ব্যবহার হয়।

## 70. SQL Assignment / Lab Focus
**English:** Core SQL practice should cover table creation, constraints, INSERT, SELECT, filtering, sorting, grouping, aggregation, joins, UPDATE, DELETE, and basic views/subqueries.  
**বাংলা:** Lab/viva-এর জন্য এই SQL operations হাতে লিখে practice করা সবচেয়ে গুরুত্বপূর্ণ।

---

# QUICK SQL COMMAND MAP

| Purpose | Commands |
|---|---|
| Create structure | CREATE |
| Modify structure | ALTER |
| Remove structure | DROP |
| Add data | INSERT |
| Retrieve data | SELECT |
| Modify data | UPDATE |
| Remove data | DELETE |
| Filter rows | WHERE |
| Sort result | ORDER BY |
| Group rows | GROUP BY |
| Filter groups | HAVING |
| Combine tables | JOIN |
| Give permission | GRANT |
| Remove permission | REVOKE |
| Save transaction | COMMIT |
| Undo uncommitted changes | ROLLBACK |

---

# IMPORTANT DIFFERENCES

## DB vs DBMS
**Database:** Stored collection of data.  
**DBMS:** Software that manages the database.  
**বাংলা:** Database হলো data; DBMS হলো data manage করার software।

## Primary Key vs Foreign Key
**Primary Key:** Uniquely identifies a row.  
**Foreign Key:** References a key in another/same table.  
**বাংলা:** Primary key identity দেয়; foreign key relationship তৈরি করে।

## WHERE vs HAVING
**WHERE:** Filters rows before grouping.  
**HAVING:** Filters groups after GROUP BY.  
**বাংলা:** WHERE row-level, HAVING group-level।

## DELETE vs DROP
**DELETE:** Removes rows; table structure remains.  
**DROP:** Removes the database object/table itself.  
**বাংলা:** DELETE data সরায়; DROP table/object-ই সরিয়ে দেয়।

## DELETE vs TRUNCATE
**DELETE:** Removes rows and can use a WHERE condition.  
**TRUNCATE:** Removes all rows as a bulk operation; exact transactional/identity behavior depends on DBMS.  
**বাংলা:** DELETE selective হতে পারে; TRUNCATE সাধারণত পুরো table empty করে।

## DDL vs DML
**DDL:** Defines/changes structure — CREATE, ALTER, DROP.  
**DML:** Changes stored data — INSERT, UPDATE, DELETE.  
**বাংলা:** DDL structure নিয়ে, DML data নিয়ে।

## Authentication vs Authorization
**Authentication:** Who are you?  
**Authorization:** What can you do?  
**বাংলা:** Identity verify বনাম permission determine।

## INNER JOIN vs LEFT JOIN
**INNER:** Only matching rows.  
**LEFT:** All left rows + matching right rows.  
**বাংলা:** INNER শুধু match; LEFT left table-এর সব রাখে।

---

# LAST-MINUTE VIVA — 15 MUST KNOW

1. **What is DBMS?** Software for creating, storing, retrieving, updating, and controlling databases.
2. **What is RDBMS?** A DBMS based on the relational/table model.
3. **What is a primary key?** A unique, non-NULL identifier for rows.
4. **What is a foreign key?** An attribute that references a key to represent a relationship.
5. **What is SQL?** A language for defining, querying, manipulating, and controlling relational databases.
6. **What is SELECT?** SQL statement used to retrieve data.
7. **WHERE vs HAVING?** WHERE filters rows; HAVING filters groups.
8. **What is JOIN?** Combines related rows from multiple tables.
9. **What is normalization?** Organizing relational data to reduce redundancy and update anomalies.
10. **What is integrity?** Maintaining valid, accurate, and consistent data.
11. **What is security?** Protecting data from unauthorized access or misuse.
12. **What is an index?** Auxiliary structure that speeds retrieval but adds storage/update cost.
13. **What is a transaction?** A logical unit of database work.
14. **COMMIT vs ROLLBACK?** COMMIT saves transaction changes; ROLLBACK undoes uncommitted changes.
15. **Why is SQL called declarative?** It specifies the desired result rather than the exact execution procedure.

---

# CSE 370 SYLLABUS COVERAGE CHECKLIST

- [x] Concepts and methods for storing data
- [x] Manipulating stored data
- [x] File retrieval
- [x] File organisation
- [x] Database models
- [x] Database system design
- [x] Principles of DBMS
- [x] Relational DBMS
- [x] Query formulation
- [x] Query language
- [x] Database administration
- [x] Storage methods
- [x] Data selection
- [x] Data presentation
- [x] Database integrity
- [x] Database security
- [x] Database languages
- [x] Application packages
- [x] Common DBMS
- [x] SQL structure
- [x] Principles behind SQL design
- [x] SQL lab/assignment focus

---

# EXAM PRIORITY

### Must Memorize
**DBMS, RDBMS, relational model, table/row/column, primary key, foreign key, candidate key, SQL, DDL/DML/DCL/TCL, SELECT, WHERE, GROUP BY, HAVING, JOIN, integrity, security, authentication, authorization, transaction, COMMIT, ROLLBACK.**

### Must Practice
**CREATE TABLE → constraints → INSERT → SELECT → WHERE → ORDER BY → GROUP BY → HAVING → JOIN → UPDATE → DELETE.**
