
# registers: L R S T X Y M[] I O A D P
# flags: Z C G

# eg:
#   LxR = DxT
#   if Z jump long T.M[0,R]
#   jump S
#   M[Y,X] = D
#   outvga M[Y,X++]
#   outaux D
#   in S

# remove spaces, tabs, "if", "then", "|", "long", all after "#", "H" (will be detected automatically)
# substitute "jmp"/"jp"/"jump"/"j" with "P="
# substitute "outvga" with "O="
# substitute "outaux" with "A="
# substitute "in" adding "=I" at the end
# substitute "." with "x"
# finally check what is at the left and at the right of the equal sign, special treatement if P is involved (flag and autodetect long if T.), and of register M[]

"""
What register to write (from the bus):
00. none! 
01. S
02. T
03. X
04. Y
05. L and R (mixing bus and T)
06. AuxOut / Audio / Led
07. Vga / KeyRow
08. ram[Y,X]
09. ram[Y,L]
10. ram[Y,R]
11. PCL and PCH from T (jump long)
12. PCL if Zero
13. PCL if halfCarry
14. PCL if siGn
15. PCL (jump short)
... L (half bus half T), all ram[0,*], all X++
What value to put to the bus:
00. ram[0,X++]
01. ram[0,X]
02. ram[0,L]
03. ram[0,R]
04. ram[Y,X++]
05. ram[Y,X]
06. ram[Y,L]
07. ram[Y,R]
08. <reserved> (to keep bit4 for RAM signal ~WE)
09. D (numeric literal following byte)
10. R
11. S
12. AuxIn
(there are 3 signals free,  ram output enable can be taken directly from instruction bit3)
"""
# forbidden instruction: M[Y,X++] or M[Y,X] = R , since it will become M[Y,R] = R (from the pull to register behaviour)
