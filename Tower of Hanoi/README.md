# 🏯 Tower of Hanoi: Recursive Logic & Math

This project is a visual and mathematical exploration of the Tower of Hanoi algorithm, featured on the [Bug and Code LLC YouTube Channel](https://youtube.com).



![Tower of Hanoi Logic Breakdown](images/hanoi.png)

## 🚀 [View the Live Interactive Demo](https://bugandcode-io.github.io/Data-Structures-and-Algorithms/tower_of_hanoi.html)

---

## 🧠 Understanding the Algorithm

The Tower of Hanoi is a classic recursive problem. To move $n$ disks from a **Source** to a **Target**, we follow a three-step recursive pattern:

1. **Move** $n-1$ disks from Source to Helper.
2. **Move** the largest disk ($n$) from Source to Target.
3. **Move** the $n-1$ disks from Helper to Target.

![Tower of Hanoi Logic Breakdown](images/hanoi-logic.png)

---

## 🔢 The Mathematical Proof: $2^n - 1$

The minimum number of moves required to solve the puzzle follows an exponential pattern. As the number of disks ($n$) increases, the moves required grows by $2^n - 1$.

| Disks ($n$) | Calculation ($2^n - 1$) | Total Moves |
| :--- | :--- | :--- |
| 3 | $2^3 - 1$ | 7 |
| 4 | $2^4 - 1$ | 15 |
| 5 | $2^5 - 1$ | 31 |

![Mathematical Pattern Visualization](images/hanoi-math.png)

---

## 💻 The Code Implementation

The beauty of recursion is how few lines of code it takes to solve such a complex-looking problem.

```javascript
function hanoi(n, source, helper, target) {
  if (n <= 0) return;
  
  // Phase 1: Move n-1 to helper
  hanoi(n - 1, source, target, helper);
  
  // Phase 2: Move the big disk to target
  console.log(`Move disk ${n}: ${source} -> ${target}`);
  
  // Phase 3: Move n-1 to target
  hanoi(n - 1, helper, source, target);
}