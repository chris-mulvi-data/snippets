# IP address regex string
ip_regex = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"


# Finding and removing comon prefixes from a pandas series
# this works well if all elements in the the vectore follow the same naming
# conventions fore each item.  If there is any difference, it will not return
# the prifix.
prefix = os.path.commonprefix(df['vector'].to_list())
df['vector'].apply(lambda x: str.replace(x, prefix, '')
