# K1 = IIIXXXX, K2 = XIXIXIX, K3 = IXXIIXX, K4 = IIIZZZZ, K5 = ZIZIZIZ , K6 = IZZIIZZ. 

# k_1 = 0001111 , k_2 = 1010101 ,k_3 = 0110011
stabilizer_list = [0b0001111 , 0b1010101 , 0b0110011]

# |ψ> =α[|0000000> + |0010000> + |01000000>  + |0110000> + |0001000> + |0011000> + |0101000> + |0111000>]
# +β[|1110000>+ |1000000> + |1010000>+ |1100000> + |1001000> + |1011000>+ |1101000> + |1111000>]
# K_5 K_6 (IIXIIII) 0b0010000 0b1100000
# K_6 (IXIIIII)0b01000000 0b1010000
# K_5 (IXXIIII)0b0110000 0b1000000
# K_4 (IIIXIII)0b0001000 0b1111000
# K_4 K_5 K_6 (IIXXIII)0b0011000 0b1101000
# K_4 K_6 (IXIXIII)0b0101000 0b1011000
# K_4 K_5 (IXXXIII)0b0111000 0b1001000
# bit_list_0 = [0b0000000, 0b0010000, 0b0100000 , 0b0110000, 0b0001000 , 0b0011000, 0b0101000 , 0b0111000]
# bit_list_0 = [0b1110000, 0b1100000, 0b1010000 , 0b1000000, 0b1111000 , 0b1101000, 0b1011000 , 0b1001000]

# |ψ> =α[|0000000> + |0000010> + |0001000>+ |0001010>]+β[|0101010> + |0101000> + |0100010>+ |0100000>]
# |0000000> |0101010>
# |0000010> |0101000> IIIIIXI
# |0001000> |0100010> IIIXIII
# |0001010> |0100000> IIIXIXI
# bit_list_0 = [0b0000000, 0b0000010, 0b0001000 , 0b0001010]
bit_list_0 = [0b0101010, 0b0101000, 0b0100010 , 0b0100000]

bit_list_1 = []
bit_list_2 = []
bit_list_3 = []


# 1/2 to be positive and 1/2 to be negative
# postive term
def new_bit_list(bit_list_before,bit_list_after,stabilizer_in_use):
   for i in bit_list_before:
      bit_list_after.append(i)
      bit_list_after.append(i ^ stabilizer_list[stabilizer_in_use])
   return bit_list_after
      
print(new_bit_list(bit_list_0,bit_list_1,0))
print(new_bit_list(bit_list_1,bit_list_2,1))
print(new_bit_list(bit_list_2,bit_list_3,2))

# coversion
def convert_binary_list(bit_list_input):
   binary_bit_list = []
   for i in bit_list_input:
      binary_bit_list.append(bin(i))
   return binary_bit_list

print(convert_binary_list(bit_list_1))
print(convert_binary_list(bit_list_2))
print(convert_binary_list(bit_list_3))

# negative term
recovery_bit_list_1 = [term for term in bit_list_1 if term not in bit_list_0]
recovery_bit_list_2 = [term for term in bit_list_2 if term not in bit_list_1]
recovery_bit_list_3 = [term for term in bit_list_3 if term not in bit_list_2]
print(convert_binary_list(recovery_bit_list_1))
print(convert_binary_list(recovery_bit_list_2))
print(convert_binary_list(recovery_bit_list_3))

# # recovery 
# # K_5 K_6 (IIXIIII) 0b0010000
# # K_6 (IXIIIII)0b01000000
# # K_5 (IXXIIII)0b0110000
# # K_4 (IIIXIII)0b0001000
# # K_4 K_5 K_6 (IIXXIII)0b0011000
# # K_4 K_6 (IXIXIII)0b0101000
# # K_4 K_5 (IXXXIII)0b0111000

# # incidently they are the same as bit_list_0
# recovery_list = [0b0000000, 0b0010000, 0b0100000 , 0b0110000, 0b0001000 , 0b0011000, 0b0101000 , 0b0111000]

# # test recovery for bit_list_3

# # create sub_list
# sub_list_0 = bit_list_3[0:8]
# sub_list_1 = bit_list_3[8:16]
# sub_list_2 = bit_list_3[16:24]
# sub_list_3 = bit_list_3[24:32]
# sub_list_4 = bit_list_3[32:40]
# sub_list_5 = bit_list_3[40:48]
# sub_list_6 = bit_list_3[48:56]
# sub_list_7 = bit_list_3[56:64]

# # check recovery for sub_list
# def check_recovery_list(sub_list,recovery_in_use):
#    recovery_sub_list = []
#    for i in sub_list:
#       recovery_sub_list.append(i ^ recovery_list[recovery_in_use])
#    return recovery_sub_list == sub_list_0

# print(check_recovery_list(sub_list_1,1))
# print(check_recovery_list(sub_list_2,2))
# print(check_recovery_list(sub_list_3,3))
# print(check_recovery_list(sub_list_4,4))
# print(check_recovery_list(sub_list_5,5))
# print(check_recovery_list(sub_list_6,6))
# print(check_recovery_list(sub_list_7,7))

# K4 = IIIZZZZ, K5 = ZIZIZIZ , K6 = IZZIIZZ
# |0000000> |0101010>
# |0000010> |0101000> IIIIIXI K4 K6
# |0001000> |0100010> IIIXIII K4 
# |0001010> |0100000> IIIXIXI K6

# incidently they are the same as bit_list_0
recovery_list = [0b0000000, 0b0000010, 0b0001000 , 0b0001010]

# test recovery for bit_list_3

# create sub_list
sub_list_0 = bit_list_3[0:8]
sub_list_1 = bit_list_3[8:16]
sub_list_2 = bit_list_3[16:24]
sub_list_3 = bit_list_3[24:32]

# check recovery for sub_list
def check_recovery_list(sub_list,recovery_in_use):
   recovery_sub_list = []
   for i in sub_list:
      recovery_sub_list.append(i ^ recovery_list[recovery_in_use])
   return recovery_sub_list == sub_list_0

print(check_recovery_list(sub_list_1,1))
print(check_recovery_list(sub_list_2,2))
print(check_recovery_list(sub_list_3,3))










