def makeSparseHash(n_sparse_hash, n_rounds, window_lengths):
    sparse_hash = range(n_sparse_hash)
    current_idx = 0
    skip_size = 0

    for current_round in range(n_rounds):
        for window_length in window_lengths:
            for idx in range(window_length // 2):
                left_idx = (current_idx + idx) % n_sparse_hash
                right_idx = (current_idx + window_length - idx - 1) % n_sparse_hash

                temp = sparse_hash[left_idx]
                sparse_hash[left_idx] = sparse_hash[right_idx]
                sparse_hash[right_idx] = temp

            current_idx = (current_idx + window_length + skip_size) % n_sparse_hash
            skip_size = skip_size + 1

    return sparse_hash



def makeDenseHash(n_dense_hash, sparse_hash):
    n_bytes = len(sparse_hash) // n_dense_hash
    dense_hash = [0 for _ in range(n_dense_hash)]

    for dense_idx in range(n_dense_hash):
        sparse_idx = dense_idx * n_bytes
        dense_hash[dense_idx] = sparse_hash[sparse_idx]

        for byte_idx in range(1, n_bytes):
            dense_hash[dense_idx] = dense_hash[dense_idx] ^ sparse_hash[sparse_idx + byte_idx]

    return dense_hash



def makeKnotHash(dense_hash):
    knot_hash = ["" for _ in range(len(dense_hash))]
    for idx in range(len(dense_hash)):
        hex_string = hex(dense_hash[idx]).replace("0x", "")
        n_zeros = 2 - len(hex_string)
        knot_hash[idx] = ("0" * n_zeros) + hex_string
    return "".join(knot_hash)



filename = "./day10/day10_input.txt"
input_file = open(filename)
lines = input_file.readlines()

in_string = lines[0] if len(lines) > 0 else ""
window_lengths = [ord(character) for character in in_string]
window_lengths = window_lengths + [17, 31, 73, 47, 23]

sparse_hash = makeSparseHash(256, 64, window_lengths)
dense_hash = makeDenseHash(16, sparse_hash)
knot_hash = makeKnotHash(dense_hash)

print("The knot hash is", knot_hash)