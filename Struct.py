#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'struct'

_author_='wangjianfeng'

import struct

#>表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。
print(struct.pack('>I',10240099))
print(struct.unpack('IH',b'\xf0\xf0\xf0\xf0\x80\x80'))

#Bmp read
def check_file(file_path):
    try:
        #with open(file_path,'rb') as f:
            #s=f.read(30)
            s=open(file_path,'rb').read(30)
            info=struct.unpack('<ccIIIIIIHH',s)
        
            if info[0]==b'B' and info[1]==b'M':
                print('该图像是windows位图\n图像大小：{}*{}\n颜色数：{}'.format(info[6],info[7],info[9]))
            elif info[0]==b'B' and info[1]==b'A':
                print('该图像是OS/2位图\n图像大小：{}*{}\n颜色数：{}'.format(info[6],info[7],info[9]))
            else :
                print('this is not bmp!')
    finally:
        print('finally!')
    
file_path=r'C:\Users\wangjianfeng2014\Desktop\a.bmp' 
check_file(file_path)   
    
    
    
