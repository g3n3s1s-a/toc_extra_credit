# SAT to 3-SAT Reduction

## Project Overview
This project demonstrates how to reduce a general SAT (Boolean satisfiability) problem to a 3-SAT problem. SAT is the problem of determining if there exists an assignment of Boolean values to variables that makes a given formula true. 3-SAT is a special case of SAT where each clause contains exactly three literals. The reduction process helps us understand the equivalence between these two problems.

## What Was the Extra Work?
This project focuses on solving the SAT to 3-SAT reduction problem by implementing a Python program that takes a SAT formula in CNF and transforms it into an equivalent 3-SAT formula. It includes:
- Implementing the reduction from SAT to 3-SAT.
- Testing the correctness of the reduction with multiple test cases.

## Why Did You Choose This Work?
I chose to implement this project because I wanted to improve my understanding of problem reductions, which are crucial in computational complexity. I do not remember the question exactly, but I believe the last test in the final was reductions,mapping, and time complexity. I also do not understand NP-completeness. I felt this would help me with problems related to NP-completeness and algorithm design. Additionally, the SAT and 3-SAT problems have been difficult for me to grasp, so this project helped solidify my understanding of them.

## Files in the Repository
- `sat_to_3sat.py`: Python script containing the implementation of the SAT to 3-SAT reduction.
- `test/test_cases.py`: Unit tests for the SAT to 3-SAT reduction.
- `test/example_inputs/`: Example SAT formulas for testing.
- `README.md`: This file, which explains the project.


## What I learned 
First, we can check the time needed to complete the following algorithm class:
1. O(N) -> say it requires 1 second to process N=100
2. O(N^3) -> 3 nested loops -> now requires N^3=1000000/100 * 1_second = 10000 seconds = ~ 3 hours
3. O(2^N) -> N levels (binary tree) of computations -> 2^N = 1.26e+30 seconds
4. O(n!) -> N levels (of increasing branches, 1x2x3x...xN) of computations -> 9.332622e+157 seconds


### All about P

#### What is polynomial?
> **Math definition**:
> an expression of more than two algebraic terms, especially the sum of several terms that contain different powers of the same variable(s).`
> Example: 6x4+3x3+3x2+2x+1 (Quartic Polynomial)

- N, N^k, etc are polynomial functions
- 2^N, N!, N^N, are **non**-polynomial functions

So in general, polynomial time refers to:
> O(n^k) where _n_ is the problem size, and _k_ is a constant

#### Sample problems
- Adding n numbers: O(n)
- Sorting n items: O(n log n)
- Multiple 2 n by n matrices: O(n^2.37) --> ***PROVE IT***
- Finding the shortest route between 2 points in a network with n roads (Dijkstra): O(n log n) --> [more](https://stackoverflow.com/questions/26547816/understanding-time-complexity-calculation-for-dijkstra-algorithm)
- Solving a system of n linear equations: O(n^3)

#### What is P?
- Problems that can be solved in polynomial time
- Can be solved efficiently (does not hang the computer)
- Independent of
	- hardware (non-quantum)
	- operating system
	- programming language

#### What is not P?
- Travelling Salesman Problem
- Formula satisfiability

#### Now, what is NP (non-deterministic polynomial)?

#### Definition of NP
- The set of problems whose solution can be **verified** in polynomial time.
- A problem is called NP (nondeterministic polynomial) if its solution can be guessed and verified in polynomial time; nondeterministic means that no particular rule is followed to make the guess.

a) Verification of TSP (distance travelled)
Given permutation, is its length less than some value `B`

b) Verification of satisfiability
Given a settings of the boolean variables, is the formula(statement) true?

c) Verification of sorting
Given a list of numbers, is it already in sorted order? 4,5,1,3

#### So what is non-determinism here saying?

The non-determinism here comes from the fact that you can verify some solution that appear out of nowhere (maybe luck, maybe guess), but you cannot always replicate finding the solution quickly.

Also, the algorithm used can be different.
We have 2 programs. 1 for verification, 1 for solution.However it is still 1 problem, an NP problem.


#### Moving on, NP-Completeness

This is a quest to seek the holy grail of P=NP, ie. can we solve NP quickly?

However, there are many different NP problems. Can we designate a "master problem", `M` of all NP problems so that if the master problem is solved, all NP problems are solved? This master problem is in the set of `NP Complete`. To be in `NP Complete`, `M` is already in NP, and every other problems in NP is quickly(in polynomial time) reducible/transformable to `M`. So if `M` is solved quickly, everything in NP will be solved quickly.

#### P != NP ?
Unsolved problem in computer science: If the solution to a problem is easy to check for correctness, must the problem be easy to solve? The P versus NP problem is a major unsolved problem in theoretical computer science.


