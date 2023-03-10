# Five Letter Words Problem
## Problem Description

**A.** Consider the dataset SGB Words dataset at :
http://www-cs-faculty.stanford.edu/~knuth/sgb-words.txt

This dataset contains mostly English words of length 5. From this data, we build a graph G<V,E> with vertex set V = "Every word in dataset" and between 2 words u and v in G, there is an edge join if u,v differ in exactly 1 position. 

Example: `after` - `great`, 2 words have 4 common characters(`a`, `t`, `e`, `r`), so they have the connection.

It is easy to see, in graph G, the sequence of words: `words`, `wolds`, ` golds`, `goads`, `grads`, `grade`, `grape`, `graph`  is a path with starting vertex from `words` and an ending vertex from `graph` .

(a) Write a program to count the number of connected components of a graph G

(b) Write a program to input the word starting u and ending v, display screen the shortest path from u to v

**B.** Still from the data set sgb-words, we build a directed graph D with the vertex set of "every word in sgb-words”, and a word u has an arc connected to another v if the last four letters of u appear in v (including the number of occurrences). The directed graph D has **94,084** arcs and **5757** vertices. The shortest directional path from words to graph is:
 `words` → `dross` → `soars` → `orcas` → `chars` → `sharp` → `graph` and we can get back to words in five steps, `graph` → `harps` → `prats` → `astro` → `trows` → `words`

(a) Write a program to count the number of strongly connected components of graph D.

(b) Write a program that inputs the word u and displays the words with the same element on the screen strongly associated with the word u.

(c) Write a program to input the word starting u and ending v; display screen the shortest path from u to v.

## Algorithms

- Breath First Search (BFS)
- Depth First Search (DFS)
- Dijkstra Algorithms 

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Contact
[T] : (+84) 97 987 01 56

[E] : dtruong46.me@gmail.com/ truong.pd214937@sis.hust.edu.vn

[A] : Hanoi University of Science and Technology

[F] : https://www.facebook.com/dtruong46.me

## Reference
[How to write file README.md](https://viblo.asia/helps/cach-su-dung-markdown-bxjvZYnwkJZ)

[Mini Project Five Letter Words](https://github.com/charlesreid1/five-letter-words)
