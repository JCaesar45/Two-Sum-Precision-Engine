# Two Sum — Precision Engine

O(n) time / O(n) space hash-map solution for the classic Two Sum problem, shipped with multi-language implementations and a live interactive demo.

## Problem
Given an array of integers `nums` and an integer `target`, return the indices of two distinct elements whose values sum to `target`. Each element may be used at most once. If no solution exists, return `None` / `null`.

## Implementations
| Language     | File          | Notes                          |
|--------------|---------------|--------------------------------|
| Python       | `two_sum.py`  | Core + 8 edge-case tests       |
| TypeScript   | `twoSum.ts`   | Strict types + self-test       |
| Java         | `TwoSum.java` | HashMap version                |
| Live Demo    | `index.html`  | Single-file luxury UI + viz    |

## Quick Start
```bash
# Python
python two_sum.py

# TypeScript (requires ts-node or compile first)
npx ts-node twoSum.ts

# Java
javac TwoSum.java && java TwoSum

# Demo
open index.html
```

## Edge Cases Covered
1. Empty list  
2. Single element  
3. No valid pair  
4. Negative numbers + zero  
5. Duplicate values (distinct indices)  
6. Multiple valid pairs (first discovered is returned)  
7. Large integers near language limits  
8. All zeros with target zero  

## Complexity
- Time: O(n)  
- Space: O(n)  

## License
MIT — Independent contractor build.
