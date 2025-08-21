function bubbleSort(arr) {
  let len = arr.length;
  let swapped;
  
  do {
    swapped = false;
    
    for (let i = 0; i < len - 1; i++) {
      if (arr[i] > arr[i + 1]) {
        // Swap elements
        let temp = arr[i];
        arr[i] = arr[i + 1];
        arr[i + 1] = temp;
        swapped = true;
      }
    }
    
    // Optimization: reduce the length since the largest element is bubbled to the end
    len--;
  } while (swapped);
  
  return arr;
}

// Export the function for testing or use in other modules
module.exports = bubbleSort;
