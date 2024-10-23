int: n;
int: k;

% edges
array[1..k, 1..2] of int: edges;

% colors of 3coloring
array[1..n] of var 1..3: col;

constraint
  forall(i in 1..k) (
    col[edges[i, 1]] != col[edges[i, 2]]
  );

solve satisfy;

output [
  show(col)
];