import sys

if (len(sys.argv) != 2):
    print("Usage: python3 disasm.py <filename>")
    sys.exit(1)

filename = sys.argv[1]

instructions = {
    '10001011000': {"name": "ADD", "type": "R", "output": "ADD rd, rn, rm"},
    '1001000100': {"name": "ADDI", "type": "I", "output": "ADDI rd, rn, imm"},
    '1011000100': {"name": "ADDIS", "type": "I", "output": "ADDIS rd, rn, imm"},
    '10101011000': {"name": "ADDS", "type": "R", "output": "ADDS rd, rn, rm"},
    '10001010000': {"name": "AND", "type": "R", "output": "AND rd, rn, rm"},
    '1001001000': {"name": "ANDI", "type": "I", "output": "ANDI rd, rn, imm"},
    '1111001000': {"name": "ANDIS", "type": "I", "output": "ANDIS rd, rn, imm"},
    '1110101000': {"name": "ANDS", "type": "R", "output": "ANDS rd, rn, rm"},
    '000101': {"name": "B", "type": "B", "output": "B address"},
    '100101': {"name": "BL", "type": "B", "output": "BL address"},
    '11010110000': {"name": "BR", "type": "R", "output": "BR rn"},
    '10110101': {"name": "CBNZ", "type": "CB", "output": "CBNZ rt, address"},
    '10110100': {"name": "CBZ", "type": "CB", "output": "CBZ rt, address"},
    '01010100': {"name": "Bcond", "type": "CB", "output": "B.cond address"},
    '11111111110': {"name": "DUMP", "type": "R", "output": "DUMP"},
    '11001010000': {"name": "EOR", "type": "R", "output": "EOR rd, rn, rm"},
    '1101001000': {"name": "EORI", "type": "I", "output": "EORI rd, rn, imm"},
    '00011110011': {"name": "FADDD", "type": "R", "output": "FADDD rd, rn, rm"},
    '00011110001': {"name": "FADDS", "type": "R", "output": "FADDS rd, rn, rm"},
    '00011110011': {"name": "FCMPD", "type": "R", "output": "FCMPD rd, rn, rm"},
    '00011110001': {"name": "FCMPS", "type": "R", "output": "FCMPS rd, rn, rm"},
    '00011110011': {"name": "FDIVD", "type": "R", "output": "FDIVD rd, rn, rm"},
    '00011110001': {"name": "FDIVS", "type": "R", "output": "FDIVS rd, rn, rm"},
    '00011110011': {"name": "FMULD", "type": "R", "output": "FMULD rd, rn, rm"},
    '00011110001': {"name": "FMULS", "type": "R", "output": "FMULS rd, rn, rm"},
    '00011110011': {"name": "FMSUBD", "type": "R", "output": "FMSUBD rd, rn, rm"},
    '00011110001': {"name": "FMSUBS", "type": "R", "output": "FMSUBS rd, rn, rm"},
    '11111111111': {"name": "HALT", "type": "R", "output": "HALT"},
    '11111000010': {"name": "LDUR", "type": "D", "output": "LDUR rd, [rn, address]"},
    '00111000010': {"name": "LDURB", "type": "D", "output": "LDURB rd, [rn, address]"},
    '11111100010': {"name": "LDURD", "type": "D", "output": "LDURD rd, [rn, address]"},
    '01111000010': {"name": "LDURH", "type": "D", "output": "LDURH rd, [rn, address]"},
    '10111100010': {"name": "LDURS", "type": "D", "output": "LDURS rd, [rn, address]"},
    '10111000100': {"name": "LDURSW", "type": "D", "output": "LDURSW rd, [rn, address]"},
    '11010011011': {"name": "LSL", "type": "R", "output": "LSL rd, rn, rm"},
    '11010011010': {"name": "LSR", "type": "R", "output": "LSR rd, rn, rm"},
    '10011011000': {"name": "MUL", "type": "R", "output": "MUL rd, rn, rm"},
    '10101010000': {"name": "ORR", "type": "R", "output": "ORR rd, rn, rm"},
    '1011001000': {"name": "ORRI", "type": "I", "output": "ORRI rd, rn, imm"},
    '11111111100': {"name": "PRNL", "type": "R", "output": "PRNL"},
    '11111111101': {"name": "PRNT", "type": "R", "output": "PRNT rd"},
    '10011010110': {"name": "SDIV", "type": "R", "output": "SDIV rd, rn, rm"},
    '10011011010': {"name": "SMULH", "type": "R", "output": "SMULH rd, rn, rm"},
    '11111000000': {"name": "STUR", "type": "D", "output": "STUR rd, [rn, address]"},
    '00111000000': {"name": "STURB", "type": "D", "output": "STURB rd, [rn, address]"},
    '11111100000': {"name": "STURD", "type": "D", "output": "STURD rd, [rn, address]"},
    '01111000000': {"name": "STURH", "type": "D", "output": "STURH rd, [rn, address]"},
    '10111100000': {"name": "STURS", "type": "D", "output": "STURS rd, [rn, address]"},
    '10111000000': {"name": "STURSW", "type": "D", "output": "STURSW rd, [rn, imm]"},
    '11001011000': {"name": "SUB", "type": "R", "output": "SUB rd, rn, rm"},
    '1101000100': {"name": "SUBI", "type": "I", "output": "SUBI rd, rn, imm"},
    '1111000100': {"name": "SUBIS", "type": "I", "output": "SUBIS rd, rn, imm"},
    '11101011000': {"name": "SUBS", "type": "R", "output": "SUBS rd, rn, rm"},
    '10011010110': {"name": "UDIV", "type": "R", "output": "UDIV rd, rn, rm"},
    '10011011110': {"name": "UMULH", "type": "R", "output": "UMULH rd, rn, rm"},
}

instruction_types = {
    'R': {
        'breakdown': [[21, 0x7FF], [16, 0x1F], [10, 0x3F], [5, 0x1F], [None, 0x1F]],
        'elements': ['opcode', 'rm', 'shamt', 'rn', 'rd'],
    },
    'I': {
        'breakdown': [[22, 0x3FF], [10, 0xFFF], [5, 0x1F], [None, 0x1F]],
        'elements': ['opcode', 'imm', 'rn', 'rd'],
    },
    'D': {
        'breakdown': [[21, 0x7FF], [12, 0x1FF], [10, 0x3], [5, 0x1F], [None, 0x1F]],
        'elements': ['opcode', 'address', 'op', 'rn', 'rd'],
    },
    'B': {
        'breakdown': [[26, 0x3F], [None, 0x3FFFFFF]],
        'elements': ['opcode', 'address'],
    },
    'CB': {
        'breakdown': [[24, 0xFF], [5, 0x7FFFF], [None, 0x1F]],
        'elements': ['opcode', 'address', 'rt'],
    },
    'IW': {
        'breakdown': [[21, 0x7FF], [5, 0xFFFF], [None, 0x1F]],
        'elements': ['opcode', 'imm', 'rd'],
    }
}

conditional_codes = {
    0b0000: 'EQ',
    0b0001: 'NE',
    0b0010: 'HS',
    0b0011: 'LO',
    0b0100: 'MI',
    0b0101: 'PL',
    0b0110: 'VS',
    0b0111: 'VC',
    0b1000: 'HI',
    0b1001: 'LS',
    0b1010: 'GE',
    0b1011: 'LT',
    0b1100: 'GT',
    0b1101: 'LE',
}

instruction_matches = [
    [0b000101, 0b100101],  # size 6
    [0b10110101, 0b10110100, 0b01010100],  # size 8
    [0b1001000100, 0b1011000100, 0b1001001000, 0b1111001000, 0b1110101000,
        0b1101001000, 0b1011001000, 0b1101000100, 0b1111000100],  # size 10
]

instruction_keys = list(instructions.keys())

output_arr = []
labels = {0: "label_0"}

def twos_complement_binary_to_integer(binary_str):
    if (len(binary_str) < 19):
        return int(binary_str, 2)
    elif binary_str[0] == '0':  # Positive number
        return int(binary_str, 2)
    else:  # Negative number
        ones_complement = ''.join(
            ['1' if bit == '0' else '0' for bit in binary_str])

        twos_complement = bin(int(ones_complement, 2) + 1)[2:]

        decimal_value = int(twos_complement, 2)

        negative_integer = -decimal_value
        return negative_integer

def getOrAddLabel(i):
    if (i in labels):
        return labels[i]
    else:
        labels[i] = "label_" + str(len(labels))
        return labels[i]

def parseInst(instruction, code, inst_num):
    instruction_type = instruction['type']
    instruction_breakdown = instruction_types[instruction_type]['breakdown']
    instruction_elements = instruction_types[instruction_type]['elements']
    instruction_split = {}
    output = instruction["output"] or ""
    for (j, [shift, mask]) in enumerate(instruction_breakdown):
        # Get element break e.g. opcode, address, rt
        key = instruction_elements[j]
        if shift == None:
            # End of breakdown, but still need to get bits
            instruction_split[key] = bin(int(code, 2) & mask)
        else:
            # Use breakdown array to fetch respective bits for key
            instruction_split[key] = bin(int(code, 2) >> shift & mask)
        if (instruction['name'] == "Bcond" and (key == "rt" or key == "address")):
            if (key == "rt"):
                conditional_code = int(instruction_split[key], 2)
                for (code, name) in conditional_codes.items():
                    if (conditional_code ^ code == 0):
                        s = name
                key = "cond"
            elif (key == "address"):
                label = getOrAddLabel(inst_num + twos_complement_binary_to_integer(instruction_split[key][2:]))
                s = label
        elif (key == "imm" or instruction_type == "B" or instruction_type == "BL" or (instruction_type.startswith("CB") and key == "address") or (instruction["type"] == "D" and key == "address") or (instruction['name'] == 'LSL' and key == 'rm') or (instruction['name'] == 'LSR' and key == 'rm')):
            if ((instruction_type == "B" or instruction_type == "CB") and key == "address"):
                # Calculate relative instruction line distance using inst_num
                label = getOrAddLabel(inst_num + twos_complement_binary_to_integer(instruction_split[key][2:]))
                s = label
            else:
                s = "#" + str(twos_complement_binary_to_integer(instruction_split[key][2:]))
        else:
            # Check for common registers and replace if necessary
            register = int(instruction_split[key], 2)
            if (register == 30):
                s = "LR"
            elif (register == 29):
                s = "FP"
            elif (register == 28):
                s = "SP"
            else:
                s = "X" + str(int(instruction_split[key], 2))
        # Replace key with value in output string
        output = output.replace(key, s)
    return output

f = open(filename, "rb")
data = f.read()
binary_machine_code = ''.join(format(byte, '08b') for byte in data)
split_code = [binary_machine_code[i:i+32]
              for i in range(0, len(binary_machine_code), 32)]
for (i, code) in enumerate(split_code):
    matched = False
    # Get first 6 bits using bit manipulation and check against 6 bit instructions
    for instruction_match in instruction_matches[0]:
        check = int(code, 2) >> 26 & 0x3F
        if check ^ instruction_match == 0:
            matched = True
            key = format(instruction_match, '06b')
            #print(str(i) + ": " + parseInst(instructions[key], code, i))
            output_arr.append(parseInst(instructions[key], code, i))
    # Get first 8 bits using bit manipulation and check against 8 bit instructions
    for instruction_match in instruction_matches[1]:
        check = int(code, 2) >> 24 & 0xFF
        if check ^ instruction_match == 0 and not matched:
            key = format(instruction_match, '08b')
            #print(str(i) + ": " + parseInst(instructions[key], code, i))
            output_arr.append(parseInst(instructions[key], code, i))
    # Get first 10 bits using bit manipulation and check against 10 bit instructions
    for instruction_match in instruction_matches[2]:
        check = int(code, 2) >> 22 & 0x3FF
        if check ^ instruction_match == 0 and not matched:
            key = format(instruction_match, '010b')
            #print(str(i) + ": " + parseInst(instructions[key], code, i))
            output_arr.append(parseInst(instructions[key], code, i))
    # Get first 11 bits using bit manipulation and check against 11 bit instructions
    for instruction_match in instruction_keys:
        check = int(code, 2) >> 21 & 0x7FF
        if check ^ int(instruction_match, 2) == 0 and not matched:
            #print(str(i) + ": " + parseInst(instructions[instruction_match], code, i))
            output_arr.append(parseInst(instructions[instruction_match], code, i))
f.close()

# Iterate through labels and insert into output_arr
offset = 0
for (label, name) in labels.items():
    output_arr.insert(label + offset, name + ":")
    offset += 1

# Print output_arr
for line in output_arr:
    print(line)