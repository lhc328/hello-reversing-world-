a = [0xC9,0x68,0x8A,0xC8,0x6F,0x07,0x06,0x0F,0x07,0xC6,0xEB,0x86,0x6E,0x6E,0x66,0xAD,0x4C,0x8D,0xAC,0xEB,0x26,0x6E,0xEB,0xCC,0xAE,0xCD,0x8C,0x86,0xAD,0x66,0xCD,0x8E,0x86,0x8D,0xAF]

flag=''
for i in a:
	for s in range(0,0x7f):
		if (((s<<5)&0xff)^((s>>3)&0x1f))==i:
			flag+=chr(s)
			break
print flag