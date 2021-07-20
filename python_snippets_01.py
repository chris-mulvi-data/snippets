# IP address regex string
ip_regex = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"


# Finding and removing comon prefixes from a pandas series
# this works well if all elements in the the vectore follow the same naming
# conventions fore each item.  If there is any difference, it will not return
# the prifix.
prefix = os.path.commonprefix(df['vector'].to_list())
df['vector'].apply(lambda x: str.replace(x, prefix, '')


# To use lookup dictionary to apply a value to a new column of a dataframe
df['new_vector'] = df['reference_vector'].apply(
    lambda x: dictionary[x].get('key') if x in dictionary.keys() else 'none'
)

# Function to run binary search 
def binary_search(data, answer):
    '''
    simple bynary search algorithm from scratch
    takes a data set in the form of a list and seachres 
    for the provided value within the list
    '''
    # ordering the data 
    data = sorted(data)
    # define botom index
    low = 0
    # define top index
    high = len(data) - 1
    # setting a count for the number of opperations
    count = 0
    while low <= high:
        count += 1 # increment the count by 1
        # find the mid point in the sorted data
        mid = round((low + high) / 2)
        # define the 'guess' value from the midpoint of the data
        guess = data[mid]
        # check the guess against the desired value
        if guess == answer:  
            return [count, guess]
        if guess > answer:
            high = mid - 1
        else: 
            low = mid + 