start:
    ADD X1, X2, X3
    ADDI X4, X1, #1
    AND X5, X1, X2
    ANDI X6, X1, #2
    B loop
loop:
    B.EQ start
    B.NE start
    B.HS start
    B.LO start
    B.MI start
    B.PL start
    B.VS start
    B.VC start
    B.HI start
    B.LS start
    B.GE start
    B.LT start
    B.GT start
    B.LE start
    BL start
    BR X1
    CBNZ X1, start
    CBZ X2, start
    EOR X7, X1, X2
    EORI X8, X1, #3
    LDUR X9, [X1, #4]
    LSL X10, X1, #2 // Broken
    LSR X11, X1, #2  // Broken
    ORR X12, X1, X2
    ORRI X13, X1, #4
    STUR X9, [X1, #8]
    SUB X14, X1, X2
    SUBI X15, X1, #5
    SUBIS X16, X1, #6
    SUBS X17, X1, X2
    MUL X18, X1, X2
    B final
final:
    PRNT X1
    PRNL
    DUMP
    HALT
    B end
end:

