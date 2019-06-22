---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.1'
      jupytext_version: 1.1.1
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

Q01 Bubble sort algorithm


Worst case: O(n^2) comparisons, O(n^2) swaps

Average: O(n^2) comparisons, O(n^2) swaps

Best: O(n) comparisons, $O(1) swaps


Q02 Selection sort algorithm


Worst case: O(n^2) comparisons, O(n) swaps

Average: O(n^2) comparisons, O(n) swaps

Best: O(n^2) comparisons, O(n) swaps

Used when swaps are expensive


Q03 Insertion sort algorithm


Worst case: O(n^2) comparisons, O(n^2) swaps

Average: O(n^2) comparisons, O(n^2) swaps

Best: O(n) comparisons, O(1) swaps

Simple implementation

Efficient for data sets that are substantially sorted


Q04 Quicksort sort algorithm


Worst case: O(n^2) comparisons

Average: O(n log n) comparisons

Best: O(n log n) simple partition, O(n) 3-way partition

Efficient

In-place


Q05 Merge sort algorithm


Worst case: O(n log n) comparisons

Average: O(n log n) comparisons

Best: O(n log n) typical, O(n) natural variant

Efficient, better than quick sort worst case

Needs O(n) as not in-place sort


Q06 Binary search algorithm


Worst case: O(log n) comparisons

Average: O(log n) comparisons

Best: O(1)


Q07 Binary search tree data structure


Sorted binary trees is a data structure with keys in sorted order. It allows fast lookup, insertion and deletion of items.

Algorithm, Average, Worst

Search O(log n) O(n)

Insert O(log n) O(n)

Delete O(log n) O(n)


Q08 B-tree data structure


Self-balancing tree data structure that maintains sorted data and allows searches, sequential access, insertions, and deletions in logarithmic time. A node can have more than two children.

Algorithm, Average, Worst

Search O(log n) O(log n)

Insert O(log n) O(log n)

Delete O(log n) O(log n)


Q09 Red-black tree structure


A red–black tree is a kind of self-balancing binary search tree. Each node of the binary tree has an extra bit, and that bit is often interpreted as the color (red or black) of the node. These color bits are used to ensure the tree remains approximately balanced during insertions and deletions.

Algorithm, Average, Worst

Search O(log n) O(log n)

Insert O(log n) O(log n)

Delete O(log n) O(log n)


Q10 Bloom filter data structure


A Bloom filter is a space-efficient probabilistic data structure, that is used to test whether an element is a member of a set. False positive matches are possible, but false negatives are not
