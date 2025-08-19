# Confusion Matrix, p. 8-20

Wikipedia says that a confusion matrix "is a specific table layout that allows visualization of the performance 
of an algorithm."

In the book, the author uses a binomial confusion matrix to shows a version with true positives, false negatives, 
false positives, and true negatives. One example from p. 8:

|  | Have Cancer (1,000) | Don't have Cancer (99,000) |
| --- | --- | --- |
| Test Positive | 80% of those that have cancer<br> (true positives) <br> 800 | 10% of those that don't have cancer <br>  (false positives) <br>  9,900 |
| Test Negative | 20% of those that have cancer<br> (false negatives) <br> 200 | 90% of those that don't have cancer <br> (true negatives)<br>  89,100 |

Of the 10,700 people tested (800 + 9,900), only 800 had cancer, or about 7%.

The .py file of the same name calculates several different binomial confusion matrices found in the Introduction.

## Possible expansions:
[] Add the other confusion matrices. These didn't have the same inputs as the others.
[] Plot out the confusion matrices.