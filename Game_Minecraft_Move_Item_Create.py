#마인크래프트 '라즈베리파이 서버'에서 파이썬으로 컨트롤 하기

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

time.sleep(3)

# 포탈 이동 시작

#좌표 세팅
x= 20.671
y= 65.00000
z= 183.566

#해당 좌표로 이동
mc.player.setTilePos(x, y, z)

time.sleep(10)

#블럭 쌓기 시작

#해당좌표에 특정 블럭을 세팅
x= 23.414
y= 71.00000
vz= 193.734
blockType = 103


# 20개의 불럭을 쌓기 Y는 높이
for i in range(1, 20):
    y = 70+i
    mc.setBlock(x, y, z, blockType)

# 블럭 쌓기 끝
