Due to its simplicity Lomuto's partitioning method might be easier to implement. 
There is a nice anecdote in Jon Bentley's Programming Pearl on Sorting:

“*Most discussions of Quicksort use a partitioning scheme based on two approaching indices [...] [i.e. Hoare's]. Although the basic idea of that scheme is straightforward, I have always found the details tricky - I once spent the better part of two days chasing down a bug hiding in a short partitioning loop. A reader of a preliminary draft complained that the standard two-index method is in fact simpler than Lomuto's and sketched some code to make his point; I stopped looking after I found two bugs.*”


# **Performance Dimension:**

For practical use, ease of implementation might be sacrificed for the sake of efficiency. On a theoretical basis, we can determine the number of element comparisons and swaps to compare performance. Additionally, actual running time will be influenced by other factors, such as caching performance and branch mispredictions.

As shown below, the algorithms behave very similar on random permutations except for the number of swaps. There Lomuto needs thrice as many as Hoare! 

# **Number of Comparisons:**

Both methods can be implemented using n−1 comparisons to partition an array of length n. This is essentially optimal, since we need to compare every element to the pivot for deciding where to put it.

# **Number of Swaps:**

The number of swaps is random for both algorithms, depending on the elements in the array. If we assume random permutations, i.e. all elements are distinct and every permutation of the elements is equally likely, we can analyze the expected number of swaps.

As only relative order counts, we assume that the elements are the numbers 1,…,n. That makes the discussion below easier since the rank of an element and its value coincide.

# Lomuto's Method:

The index variable j scans the whole array and whenever we find an element A[j] smaller than pivot x, we do a swap. Among the elements 1,…,n, exactly x−1 ones are smaller than x, so we get x−1 swaps if the pivot is x.

The overall expectation then results by averaging over all pivots. Each value in {1,…,n} is equally likely to become pivot (namely with prob. 1/n), so we have

\frac1n \sum_{x=1}^n (x-1) = \frac n2 - \frac12\;
summation of (x-1) from x=1 to x=n is equal to n/2-1/2

swaps on average to partition an array of length n with Lomuto's method.

# Hoare's Method:

Here, the analysis is slightly more tricky: Even fixing pivot x, the number of swaps remains random.
More precisely: The indices i and j run towards each other until they cross, which always happens at x (by correctness of Hoars partitioning algorithm!). This effectively divides the array into two parts: A left part which is scanned by i and a right part scanned by j. Now, a swap is done exactly for every pair of “misplaced” elements, i.e. a large element (larger than x ,thus belonging in the right partition) which is currently located in the left part and a small element located in the right part. Note that this pair forming always works out, i.e. there the number of small elements initially in the right part equals the number of large elements in the left part.

One can show that the number of these pairs is hypergeometrically Hyp(n−1,n−x,x−1) distributed: For the n−x large elements we randomly draw their positions in the array and have x−1 positions in the left part. Accordingly, the expected number of pairs is (n−x)(x−1)/(n−1) given that the pivot is x.

Finally, we average again over all pivot values to obtain the overall expected number of swaps for Hoare's partitioning:

\frac1n \sum_{x=1}^n \frac{(n-x)(x-1)}{n-1} = \frac n6 - \frac13\;
summation of (n-x)(x-1)/(n-1) for x=1 to x=n is equal to n/6-1/3.

Both algorithms use two pointers into the array that scan it sequentially. Therefore both behave almost optimal w.r.t. caching.
Equal Elements and Already Sorted Lists

As already mentioned by Wandering Logic, the performance of the algorithms differs more drastically for lists that are not random permutations. On an array that is already sorted, Hoare's method never swaps, as there are no misplaced pairs (see above), whereas Lomuto's method still does its roughly n/2 swaps!

The presence of equal elements requires special care in Quicksort. (I stepped into this trap myself; see my master's thesis, page 36, for a “Tale on Premature Optimization”) Consider as extreme example an array which filled with 0
s. On such an array, Hoare's method performs a swap for every pair of elements - which is the worst case for Hoare's partitioning - but i and j always meet in the middle of the array. Thus, we have optimal partitioning and the total running time remains in O(nlogn).

Lomuto's method behaves much more stupidly on the all 0 array: The comparison A[j] <= x will always be true, so we do a swap for every single element! But even worse: After the loop, we always have i=n, so we observe the worst case partitioning, making the overall performance degrade to Θ(n2) !

# **Conclusion:**

Lomuto's method is simple and easier to implement, but should not be used for implementing a library sorting method. 
