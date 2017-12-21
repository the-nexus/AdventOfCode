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



hex_to_binary = {
    "0" : "0000",
    "1" : "0001",
    "2" : "0010",
    "3" : "0011",
    "4" : "0100",
    "5" : "0101",
    "6" : "0110",
    "7" : "0111",
    "8" : "1000",
    "9" : "1001",
    "a" : "1010",
    "b" : "1011",
    "c" : "1100",
    "d" : "1101",
    "e" : "1110",
    "f" : "1111",
}

filename = "./day14/day14_input.txt"
input_file = open(filename)
lines = input_file.readlines()
in_string = lines[0] if len(lines) > 0 else ""
memory = [[0 for column in range(128)] for line in range(128)]

for line_idx in range(128):
    window_lengths = [ord(character) for character in (in_string + "-" + str(line_idx))]
    window_lengths = window_lengths + [17, 31, 73, 47, 23]
    sparse_hash = makeSparseHash(256, 64, window_lengths)
    dense_hash = makeDenseHash(16, sparse_hash)
    knot_hash = makeKnotHash(dense_hash)

    for hex_idx in range(len(knot_hash)):
        binary_str = hex_to_binary[knot_hash[hex_idx]]
        for bit_idx in range(len(binary_str)):
            column_idx = len(binary_str) * hex_idx + bit_idx
            memory[line_idx][column_idx] = int(binary_str[bit_idx])

region_count = 0
for line_idx in range(128):
    for column_idx in range(128):
        used_memory = used_memory + sum(memory[line_idx])

print("Memory used:", used_memory, "squares")
