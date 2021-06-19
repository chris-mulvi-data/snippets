# IP address regex string
ip_regex = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"


# Finding and removing comon prefixes from a pandas series
prefix = os.path.commonprefix(df['vector'].to_list())
df['vector'].apply(lambda x: str.replace(x, prefix, '')
