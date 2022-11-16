// Search on an array
// Linear search
// Big O of linear linear search is O(n)


// Path: practice.ts
// Always ask if the array is ordered
// We can do better than linear search
// Binary search
// Big O of binary search is O(log n)

// Bubble Sort
// Big O of bubble sort is O(n^2)
// xi <= xi + 1
// A singular iteration would always have the largest element bubble to the end
// A bubble sort checks if the next element is larger than the current element

// Recursion
// 1. Base case
// 2. Recurse
// recurse step can be broken down into 3 steps
// 1. pre
// 2. recurse
// 3. post



function foo(n: number): number {
    if (n === 1 ){
        return 1;
    }
    return n * foo(n - 1);
}

console.log(foo(5));