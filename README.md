# Spiral Matrix Traversal

This repository contains a Python solution for traversing a matrix in spiral order.

## Overview
The algorithm extracts elements from a matrix in a spiral pattern, starting from the top-left corner and moving clockwise. It continues layer-by-layer until all elements are processed.

## How It Works
1. The top row is appended directly to the result list.
2. The last element of each remaining row is appended.
3. The bottom row is appended in reverse order.
4. The first element of each remaining row (from bottom to top) is appended.
5. Repeat the process until no elements are left.

## Complexity
- **Time Complexity:** O(m × n), where m is the number of rows and n is the number of columns.
- **Space Complexity:** O(m × n) for storing the result list.
