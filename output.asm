label_0:
ADD X1, X2, X3
ADDI X4, X1, #1
AND X5, X1, X2
ANDI X6, X1, #2
B label_1
label_1:
B.EQ label_0
B.NE label_0
B.HS label_0
B.LO label_0
B.MI label_0
B.PL label_0
B.VS label_0
B.VC label_0
B.HI label_0
B.LS label_0
B.GE label_0
B.LT label_0
B.GT label_0
B.LE label_0
BL label_0
BR X1
CBNZ X1, label_0
CBZ X2, label_0
EOR X7, X1, X2
EORI X8, X1, #3
LDUR X9, [X1, #4]
LSL X10, X1, #0
LSR X11, X1, #0
ORR X12, X1, X2
ORRI X13, X1, #4
STUR X9, [X1, #8]
SUB X14, X1, X2
SUBI X15, X1, #5
SUBIS X16, X1, #6
SUBS X17, X1, X2
MUL X18, X1, X2
B label_2
label_2:
PRNT X1
PRNL
DUMP
HALT
B label_3
label_3:
