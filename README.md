# Advent of Code

Python solutions for [Advent of Code](https://adventofcode.com/) puzzles.

This repository is organized by year and day. Each day folder usually contains a Python solution script and the puzzle input used for that solution.

## Progress

| Year | Completed days in this repo |
| --- | --- |
| 2015 | 1, 2, 3, 5, 6 |
| 2024 | 1-15, 17 |
| 2025 | 1-12 |

## Repository Layout

```text
Advent-of-code/
+-- 2015/
|   +-- day 1/
|   |   +-- day1.py
|   |   +-- inp1.txt
|   +-- ...
+-- 2024/
|   +-- day 1/
|   |   +-- day-1.py
|   |   +-- puzzle1.txt
|   +-- ...
+-- 2025/
|   +-- day 1/
|   |   +-- day1.py
|   |   +-- inp1.txt
|   +-- ...
+-- README.md
```

Some scratch or in-progress files may live at the repository root before being moved into a year/day folder.

## Requirements

- Python 3.x
- No third-party Python packages are required for the checked-in solutions.

## Running a Solution

Clone the repository:

```bash
git clone https://github.com/abhiram-vattikonda/Advent-of-code.git
cd Advent-of-code
```

Run any day script from its folder:

```bash
cd "2024/day 1"
python day-1.py
```

For older folders that use the `day1.py` naming style:

```bash
cd "2015/day 1"
python day1.py
```

On some systems, use `python3` instead of `python`.

## Notes

- Puzzle inputs are included alongside the solution scripts where available.
- Solutions favor direct, readable Python over shared framework code.
- File and folder names preserve the style used while solving each puzzle.

## About Advent of Code

Advent of Code is an annual set of programming puzzles released each December. The puzzles are great practice for parsing, search, dynamic programming, graph traversal, simulation, and other problem-solving techniques.
