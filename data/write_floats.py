# write_floats.py
'''
import struct
import random

# Generate non-negative values
float32_vals = [random.uniform(0, 100) for _ in range(13)]
float64_vals = [random.uniform(0, 100) for _ in range(26)]
int32_val = random.randint(0, 1000)

# Format string: '<' disables padding, 'f'*13, 'd'*26, 'i'
format_str = '<' + 'f'*13 + 'd'*26 + 'i'

# Pack all values into binary
all_values = float32_vals + float64_vals + [int32_val]

with open("mixed_large.bin", "wb") as f:
    f.write(struct.pack(format_str, *all_values))

print("Written values:")
print("  float32s:", float32_vals)
print("  float64s:", float64_vals)
print("  int32:   ", int32_val)
'''

import struct
import random

num_rows = 45000000
float32_per_row = 13
float64_per_row = 26
int32_per_row = 1

# Struct format per row: 13 float32s, 26 float64s, 1 int32
format_str = '<' + 'f'*float32_per_row + 'd'*float64_per_row + 'i'
row_size = struct.calcsize(format_str)

all_data = []

with open("generated_binary.bin", "wb") as f:
    for i in range(num_rows):
        float32_vals = [random.uniform(0, 100) for _ in range(float32_per_row)]
        float64_vals = [random.uniform(0, 100) for _ in range(float64_per_row)]
        int32_val = random.randint(0, 1000)

        row_values = float32_vals + float64_vals + [int32_val]
        f.write(struct.pack(format_str, *row_values))
        all_data.append(row_values)

# Print first and last row for verification
print("Written first row:")
print("  float32s:", all_data[0][:float32_per_row])
print("  float64s:", all_data[0][float32_per_row:-1])
print("  int32:   ", all_data[0][-1])

print("\nWritten last row:")
print("  float32s:", all_data[-1][:float32_per_row])
print("  float64s:", all_data[-1][float32_per_row:-1])
print("  int32:   ", all_data[-1][-1])



