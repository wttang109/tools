# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 09:47:30 2019

@author: Sunny
"""
import modbus_tk
import modbus_tk.modbus_tcp as mt
import modbus_tk.defines as md
import modbus_tk.defines as cst

# 远程连接到slave端（从）
#master = mt.TcpMaster("192.168.1.100", 502)
#master = mt.TcpMaster("10.0.0.75", 502)
master = mt.TcpMaster("127.0.0.1", 502)


master.set_timeout(5.0)

# @slave=1 : identifier of the slave. from 1 to 247.  0为广播所有的slave
# @function_code=READ_HOLDING_REGISTERS：功能码
# @starting_address=1：开始地址
# @quantity_of_x=3：寄存器/线圈的数量
# @output_value：一个整数或可迭代的值：1/[1,1,1,0,0,1]/xrange(12)
# @data_format
# @expected_length
#aa = master.execute(slave=1, function_code=md.READ_HOLDING_REGISTERS,
#                    starting_address=10, quantity_of_x=6)
#print(aa[:])  # 取到的所有寄存器的值
#print(aa[0:10])    # 获取第一个寄存器的值`

#logger = modbus_tk.utils.create_logger("console")
#a=22
#b=33
#c=580
##logger.info(master.execute(4, cst.READ_INPUT_REGISTERS, 0, 4))
#master.execute(1, cst.WRITE_MULTIPLE_REGISTERS,  starting_address=2, output_value=[a,b])
#aa = master.execute(slave=1, function_code=md.READ_HOLDING_REGISTERS,
#                    starting_address=10, quantity_of_x=6)
#print(aa[:])
a=master.execute(1, cst.WRITE_MULTIPLE_REGISTERS,  starting_address=0,
                   output_value=[0,11.1,0], quantity_of_x=3)
print(a[1])






