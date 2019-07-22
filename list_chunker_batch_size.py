def chunker(seq, size):
    # return chunks of the sequence of selected size
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))

# prepare list with some data numbers/strings
big_list = [i for i in range(1,100)]

# the chunk you want to get a time from big list
i_want_chunk = 20

# lets call chunker function, so we can get a chunk of 20 elements from a big list
for chunk in chunker(big_list, i_want_chunk):
    print(chunk)