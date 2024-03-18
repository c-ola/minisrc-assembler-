minisrc = {
    "name": "elec374-minisrc",
    "word_size": 32,
    "conditions": [
        {
            "name": "brzr",
            "value": 0
        },
        {
            "name": "brnz",
            "value": 1
        },
        {
            "name": "brpl",
            "value": 2
        },
        {
            "name": "brmi",
            "value": 3
        }
    ],
    "formats": [
        {
            "name": "R",
            "fields": [
                {
                    "name": "opcode",
                    "msb" : 31,
                    "lsb" : 27
                },
                {
                    "name": "Ra",
                    "msb" : 26,
                    "lsb" : 23
                },
                {
                    "name": "Rb",
                    "msb" : 22,
                    "lsb" : 19
                },
                {
                    "name": "Rc",
                    "msb" : 18,
                    "lsb" : 15
                }
            ]
        },
        {
            "name": "I",
            "fields": [
                {
                    "name": "opcode",
                    "msb" : 31,
                    "lsb" : 27
                },
                {
                    "name": "Ra",
                    "msb" : 26,
                    "lsb" : 23
                },
                {
                    "name": "Rb",
                    "msb" : 22,
                    "lsb" : 19
                },
                {
                    "name": "C",
                    "msb" : 18,
                    "lsb" : 0
                }
            ]
        },
        {
            "name": "B",
            "fields": [
                {
                    "name": "opcode",
                    "msb" : 31,
                    "lsb" : 27
                },
                {
                    "name": "Ra",
                    "msb" : 26,
                    "lsb" : 23
                },
                {
                    "name": "condition",
                    "msb" : 22,
                    "lsb" : 19
                },
                {
                    "name": "C",
                    "msb" : 18,
                    "lsb" : 0
                }
            ]
        },
        {
            "name": "J",
            "fields": [
                {
                    "name": "opcode",
                    "msb" : 31,
                    "lsb" : 27
                },
                {
                    "name": "Ra",
                    "msb" : 26,
                    "lsb" : 23
                }
            ]
        },
        {
            "name": "M",
            "fields": [
                {
                    "name": "opcode",
                    "msb" : 31,
                    "lsb" : 27
                }
            ]
        }
    ],
    "instructions": [
        {
            "name": "ld",
            "opcode": 0,
            "format": "I"
        },
        {
            "name": "ldi",
            "opcode": 1,
            "format": "I"
        },
        {
            "name": "st",
            "opcode": 2,
            "format": "I"
        },
        {
            "name": "add",
            "opcode": 3,
            "format": "R"
        },
        {
            "name": "sub",
            "opcode": 4,
            "format": "R"
        },
        {
            "name": "shr",
            "opcode": 5,
            "format": "R"
        },
        {
            "name": "shra",
            "opcode": 6,
            "format": "R"
        },
        {
            "name": "shl",
            "opcode": 7,
            "format": "R"
        },
        {
            "name": "ror",
            "opcode": 8,
            "format": "R"
        },
        {
            "name": "rol",
            "opcode": 9,
            "format": "R"
        },
        {
            "name": "and",
            "opcode": 10,
            "format": "R"
        },
        {
            "name": "or",
            "opcode": 11,
            "format": "R"
        },
        {
            "name": "addi",
            "opcode": 12,
            "format": "I"
        },
        {
            "name": "andi",
            "opcode": 13,
            "format": "I"
        },
        {
            "name": "ori",
            "opcode": 14,
            "format": "I"
        },
        {
            "name": "mul",
            "opcode": 15,
            "format": "I"
        },
        {
            "name": "div",
            "opcode": 16,
            "format": "I"
        },
        {
            "name": "neg",
            "opcode": 17,
            "format": "I"
        },
        {
            "name": "not",
            "opcode": 18,
            "format": "I"
        },
        {
            "name": "brzr",
            "opcode": 19,
            "format": "B"
        },
        {
            "name": "brnz",
            "opcode": 19,
            "format": "B"
        },
        {
            "name": "brpl",
            "opcode": 19,
            "format": "B"
        },
        {
            "name": "brmi",
            "opcode": 19,
            "format": "B"
        },
        {
            "name": "jr",
            "opcode": 20,
            "format": "J"
        },
        {
            "name": "jal",
            "opcode": 21,
            "format": "J"
        },
        {
            "name": "in",
            "opcode": 22,
            "format": "J"
        },
        {
            "name": "out",
            "opcode": 23,
            "format": "J"
        },
        {
            "name": "mfhi",
            "opcode": 24,
            "format": "J"
        },
        {
            "name": "mflo",
            "opcode": 25,
            "format": "J"
        },
        {
            "name": "nop",
            "opcode": 26,
            "format": "M"
        },
        {
            "name": "halt",
            "opcode": 27,
            "format": "M"
        }
    ]
}
