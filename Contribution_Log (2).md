# AI Contribution Log

**Course:** 02AML204 – Introduction to Artificial Intelligence  
**PRN:** 25UAM133  
**Name:** Sanchit Sachin Magdum  
**Division:** B  
**GitHub:** https://github.com/sanchitmagdum17/IAI-SLE-25UAM133

## AI Tool Used

AI assistance was used during the development, profiling, visualization, and documentation of the SLE-2 BFS vs DFS 8-Puzzle experiment.

## Contribution Log

| Task | AI Assistance | Student Work / Verification |
|---|---|---|
| Problem selection | Helped adapt the SLE-2 experiment to the 8-Puzzle and BFS vs DFS comparison | Reviewed the selected problem and SLE-2 requirements |
| BFS implementation | Assisted with organizing the queue-based BFS search | Reviewed and executed the program |
| DFS implementation | Assisted with organizing the stack-based DFS search | Reviewed and executed the program |
| State generation | Helped structure the 8-Puzzle neighbor-state generation | Checked the puzzle moves and goal state |
| Node counting | Helped add the expanded-node counter | Verified the reported node counts |
| Timing | Helped add `time.perf_counter()` and repeated trials | Ran the program and checked measured timings |
| Best/Average/Worst cases | Helped organize three fixed 8-Puzzle test cases | Reviewed the selected cases and results |
| Path measurement | Helped reconstruct and measure solution paths | Checked the resulting path lengths |
| Result diagrams | Helped prepare the puzzle/result visualization | Reviewed the generated figures |
| Profiling | Helped prepare the cProfile-based flame-style visualization | Reviewed the profiling output |
| README | Helped document the experiment, algorithms and project files | Reviewed the final README |
| Report | Helped organize the SLE-2 report structure and explanations | Reviewed and finalized the report |

## Profiling Method

The experiment uses Python's `time.perf_counter()` for direct wall-clock measurement. A node counter is incremented when a state is removed from the BFS queue or DFS stack and expanded.

Repeated runs are used to calculate average execution time. The profiling visualization is generated separately with cProfile.

## AI Usage Statement

AI assistance was used as a development and documentation aid. It helped with code structure, profiling setup, visualization, and report organization.

The student is responsible for reviewing the generated code, running the experiment, checking the numerical results, and preparing the final submission.

## Verification

The numerical results used in the report are intended to come from actual execution of the Python program. Timing values may vary slightly between runs because of normal system-load differences.

## Note on Best/Average/Worst Labels

The Best, Average, and Worst labels refer to the selected experimental 8-Puzzle cases used for comparison. They should not be interpreted as a formal proof of the theoretical best, average, or worst-case complexity of BFS or DFS.
