# SAT to 3-SAT Reduction

## Project Overview
This project demonstrates how to reduce a general SAT (Boolean satisfiability) problem to a 3-SAT problem. SAT is the problem of determining if there exists an assignment of Boolean values to variables that makes a given formula true. 3-SAT is a special case of SAT where each clause contains exactly three literals. The reduction process helps us understand the equivalence between these two problems.

## What Was the Extra Work?
This project focuses on solving the SAT to 3-SAT reduction problem by implementing a Python program that takes a SAT formula in CNF and transforms it into an equivalent 3-SAT formula. It includes:
- Implementing the reduction from SAT to 3-SAT.
- Testing the correctness of the reduction with multiple test cases.

## Why Did You Choose This Work?
I chose to implement this project because I wanted to improve my understanding of problem reductions, which are crucial in computational complexity. I do not remember the question exactly, but I believe the last question in the final was reductions, mapping, and time complexity. I also do not understand NP-completeness. I felt this would help me with problems related to NP-completeness and algorithm design. Additionally, the SAT and 3-SAT problems have been difficult for me to grasp, so this project helped solidify my understanding of them.

## Files in the Repository
- `sat_to_3sat.py`: Python script containing the implementation of the SAT to 3-SAT reduction.
- `test/test_cases.py`: Unit tests for the SAT to 3-SAT reduction.
- `test/example_inputs/`: Example SAT formulas for testing.
- `README.md`: This file, which explains the project.

## Why is SAT to 3-SAT Reduction Important?
SAT (Boolean Satisfiability Problem) was the first problem proven to be **NP-complete**, as demonstrated by Stephen Cook in 1971 (Cook’s Theorem). The reduction from SAT to 3-SAT shows that even a constrained version of SAT—where every clause has exactly three literals—remains NP-complete. This has significant implications in theoretical computer science:

### 1. **Equivalence Between Problems in NP**
SAT to 3-SAT reduction demonstrates that SAT and 3-SAT are computationally equivalent. Any solution to 3-SAT can be transformed to solve SAT, and vice versa, in polynomial time. This equivalence is essential for understanding the nature of NP problems: simplifying constraints does not necessarily make a problem easier to solve.

### 2. **Framework for Reductions**
The reduction provides a template for proving other problems are NP-complete. Many NP-complete problems are shown to be so by reducing 3-SAT to them in polynomial time. This establishes a chain of equivalences and supports the broader study of computational complexity.

### 3. **Implications for NP-Completeness**
Understanding SAT and its reductions helps us grapple with the P vs. NP question—a central open problem in computer science. If SAT can be solved in polynomial time, then all problems in NP can also be solved efficiently. However, no such solution is known, making SAT and its variants a cornerstone of complexity theory.

## What Does NP Mean?
- **NP (Nondeterministic Polynomial Time)** is the class of problems for which a given solution can be verified in polynomial time.
- A problem is in NP if we can guess a solution (possibly non-deterministically) and verify its correctness in polynomial time.

### Examples:
- **Traveling Salesman Problem (TSP)**: Verifying that a given route is shorter than a certain distance can be done in polynomial time.
- **Boolean Satisfiability**: Verifying that a given assignment of variables satisfies the formula is efficient.

## What Does NP-Completeness Mean?
- A problem is **NP-complete** if:
  1. It is in NP.
  2. Every other problem in NP can be reduced to it in polynomial time.
- NP-complete problems are the hardest problems in NP. If we solve one NP-complete problem efficiently, we can solve all NP problems efficiently.

### Why Is This Important?
The concept of NP-completeness underlines the quest to determine whether **P = NP**: Can every problem whose solution can be verified quickly also be solved quickly? If SAT (or 3-SAT) is solvable in polynomial time, this would imply P = NP, revolutionizing computer science.

## What I Learned
Through this project, I gained a better understanding of:
- Polynomial and non-polynomial time complexities.
- The importance of problem reductions in theoretical computer science.
- The distinction between P, NP, and NP-completeness.

By working through examples and coding the reduction, I improved my grasp of how NP-complete problems relate to one another and why solving them efficiently remains one of the greatest challenges in computing.


