# 1. Number of buckets = round(sqrt(#elements))
# 2. Distribute elements to the indices = ceil(value * #buckets/max_value)
# 3. Sort each buckets one by one
# 4. Merge all elements into the one array

def bucketSorting(arr):
    numberOfBuckets = round(math.sqrt(len(arr))) # Define the number of buckets using the formula
    max_value = max(arr) # Find the max value in the array

    buckets = [] # Array to hold buckets as sub-array(bucket)

    # Create buckets (sub-arrays are buckets)
    for i in range(numberOfBuckets): 
        buckets.append([])
    
    # Distribute values in the unsorted array into buckets using the index formula
    for j in arr:
        index = math.ceil(j*(numberOfBuckets/max_value))-1 # Index formula
        
        # Append the values into the appropirate buckets
        buckets[index].append(j) 

        # Sort each individual bucket
        buckets[index].sort() 
    
    k = 0 # Index for our array

    # Replace the initial array with sorted values
    for i in range(numberOfBuckets):
        for j in buckets[i]:
            arr[k] = j
            k+=1

    return arr
