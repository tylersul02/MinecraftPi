#You Know I Had To Do It To Em.

from mcpi.minecraft import Minecraft
from mcpi import block
from mcpi import event
from time import sleep
import time



def init():
	mc = Minecraft.create("10.183.3.5", 4711)
	mc.postToChat("You Know I Had To Do It To Em.")
	return mc

mc = init();


x, y, z = mc.player.getPos()
h=5;k=5;l=5

zz = z + 2

def clear_with_air(mc,x,y,z,h,k,l):
	air=0;
	mc.setBlocks(x-h,y-k,z-l,x+h,y+k,z+l,air)
	
def posta(mc,x,y,zz):
	
	
	time.sleep(1)

	#layer 1
	mc.setBlock(x-3,y, zz, block.WOOD_PLANKS.id)
	mc.setBlock(x-2,y, zz, block.WOOD_PLANKS.id)
	mc.setBlock(x-1,y, zz, block.WOOD_PLANKS.id)
	mc.setBlock(x+1,y, zz, block.WOOD_PLANKS.id)
	mc.setBlock(x+2,y, zz, block.WOOD_PLANKS.id)
	mc.setBlock(x+3,y, zz, block.WOOD_PLANKS.id)
	#layer 2
	mc.setBlock(x-3,y+1, zz, block.WOOD_PLANKS.id)
	mc.setBlock(x-2,y+1, zz, block.WOOD_PLANKS.id)
	mc.setBlock(x-1,y+1, zz, block.WOOD_PLANKS.id)
	mc.setBlock(x+1,y+1, zz, block.WOOD_PLANKS.id)
	mc.setBlock(x+2,y+1, zz, block.WOOD_PLANKS.id)
	mc.setBlock(x+3,y+1, zz, block.WOOD_PLANKS.id)
	#layer 3	
	mc.setBlock(x-3,y+2, zz, block.WOOL.id,6)
	mc.setBlock(x-2,y+2, zz, block.WOOL.id,6)
	mc.setBlock(x-1,y+2, zz, block.WOOL.id,6)
	mc.setBlock(x+1,y+2, zz, block.WOOL.id,6)
	mc.setBlock(x+2,y+2, zz, block.WOOL.id,6)
	mc.setBlock(x+3,y+2, zz, block.WOOL.id,6)
	#layer 4
	mc.setBlock(x-3,y+3, zz, block.WOOL.id,6)
	mc.setBlock(x-2,y+3, zz, block.WOOL.id,6)
	mc.setBlock(x-1,y+3, zz, block.WOOL.id,6)
	mc.setBlock(x+1,y+3, zz, block.WOOL.id,6)
	mc.setBlock(x+2,y+3, zz, block.WOOL.id,6)
	mc.setBlock(x+3,y+3, zz, block.WOOL.id,6)
	#layer 5
	mc.setBlock(x-3,y+4, zz, block.WOOL.id,6)
	mc.setBlock(x-2,y+4, zz, block.WOOL.id,6)
	mc.setBlock(x-1,y+4, zz, block.WOOL.id,6)
	mc.setBlock(x+1,y+4, zz, block.WOOL.id,6)
	mc.setBlock(x+2,y+4, zz, block.WOOL.id,6)
	mc.setBlock(x+3,y+4, zz, block.WOOL.id,6)
	#layer 6
	mc.setBlock(x-3,y+5, zz, block.WOOL.id,6)
	mc.setBlock(x-2,y+5, zz, block.WOOL.id,6)
	mc.setBlock(x-1,y+5, zz, block.WOOL.id,6)
	mc.setBlock(x+1,y+5, zz, block.WOOL.id,6)
	mc.setBlock(x+2,y+5, zz, block.WOOL.id,6)
	mc.setBlock(x+3,y+5, zz, block.WOOL.id,6)
	#layer 7
	mc.setBlock(x-3,y+6, zz, block.WOOL.id,6)
	mc.setBlock(x-2,y+6, zz, block.WOOL.id,6)
	mc.setBlock(x-1,y+6, zz, block.WOOL.id,6)
	mc.setBlock(x,y+6, zz, block.WOOL.id,6)
	mc.setBlock(x+1,y+6, zz, block.WOOL.id,6)
	mc.setBlock(x+2,y+6, zz, block.WOOL.id,6)
	mc.setBlock(x+3,y+6, zz, block.WOOL.id,6)
	#layer 8
	mc.setBlock(x-3,y+7, zz, block.WOOL.id,6)
	mc.setBlock(x-2,y+7, zz, block.WOOL.id,6)
	mc.setBlock(x-1,y+7, zz, block.WOOL.id,6)
	mc.setBlock(x,y+7, zz, block.WOOL.id,6)
	mc.setBlock(x+1,y+7, zz, block.WOOL.id,6)
	mc.setBlock(x+2,y+7, zz, block.WOOL.id,6)
	mc.setBlock(x+3,y+7, zz, block.WOOL.id,6)
	#layer 9
	mc.setBlock(x-3,y+8, zz, block.WOOD.id,1)
	mc.setBlock(x-2,y+8, zz, block.WOOD.id,1)
	mc.setBlock(x-1,y+8, zz, block.WOOD.id,1)
	mc.setBlock(x,y+8, zz, block.IRON_BLOCK.id)
	mc.setBlock(x+1,y+8, zz, block.WOOD.id,1)
	mc.setBlock(x+2,y+8, zz, block.WOOD.id,1)
	mc.setBlock(x+3,y+8, zz, block.WOOD.id,1)
	#layer 10
	mc.setBlock(x-3,y+9, zz, block.WOOL.id,6)
	mc.setBlock(x-2,y+9, zz, block.WOOL.id,6)
	mc.setBlock(x-1,y+9, zz, block.WOOL.id,6)
	mc.setBlock(x,y+9, zz, block.WOOL.id,2)
	mc.setBlock(x+1,y+9, zz, block.WOOL.id,6)
	mc.setBlock(x+2,y+9, zz, block.WOOL.id,6)
	mc.setBlock(x+3,y+9, zz, block.WOOL.id,6)
	#layer 11
	mc.setBlock(x-3,y+10, zz, block.WOOL.id,6)
	mc.setBlock(x-2,y+10, zz, block.WOOL.id,6)
	mc.setBlock(x-1,y+10, zz, block.WOOL.id,6)
	mc.setBlock(x,y+10, zz, block.WOOL.id,2)
	mc.setBlock(x+1,y+10, zz, block.WOOL.id,6)
	mc.setBlock(x+2,y+10, zz, block.WOOL.id,6)
	mc.setBlock(x+3,y+10, zz, block.WOOL.id,6)
	#layer 12
	mc.setBlock(x-5,y+11, zz, block.WOOD_PLANKS.id)
	mc.setBlock(x-4,y+11, zz, block.WOOD_PLANKS.id)
	mc.setBlock(x-3,y+11, zz, block.WOOD_PLANKS.id)
	mc.setBlock(x-2,y+11, zz, block.GOLD_BLOCK.id)	
	mc.setBlock(x-1,y+11, zz, block.WOOD_PLANKS.id)
	mc.setBlock(x,y+11, zz, block.WOOL.id,1)
	mc.setBlock(x+1,y+11, zz, block.WOOD_PLANKS.id)
	mc.setBlock(x+2,y+11, zz, block.WOOD_PLANKS.id)
	mc.setBlock(x+3,y+11, zz, block.WOOD_PLANKS.id)
	mc.setBlock(x+4,y+11, zz, block.WOOD_PLANKS.id)
	mc.setBlock(x+5,y+11, zz, block.WOOD_PLANKS.id)
	#layer 13
	mc.setBlock(x-6,y+12, zz, block.WOOL.id,6)
	mc.setBlock(x-5,y+12, zz, block.WOOL.id,6)
	mc.setBlock(x-4,y+12, zz, block.WOOD_PLANKS.id)
	mc.setBlock(x-3,y+12, zz, block.WOOD_PLANKS.id)
	mc.setBlock(x-2,y+12, zz, block.GOLD_BLOCK.id)
	mc.setBlock(x-1,y+12, zz, block.WOOD_PLANKS.id)
	mc.setBlock(x,y+12, zz, block.WOOD_PLANKS.id)
	mc.setBlock(x+1,y+12, zz, block.WOOL.id,1)
	mc.setBlock(x+2,y+12, zz, block.WOOD_PLANKS.id)
	mc.setBlock(x+3,y+12, zz, block.WOOD_PLANKS.id)
	mc.setBlock(x+4,y+12, zz, block.WOOD_PLANKS.id)
	mc.setBlock(x+5,y+12, zz, block.WOOL.id,6)
	mc.setBlock(x+6,y+12, zz, block.WOOL.id,6)
	#layer 14
	mc.setBlock(x-6,y+13, zz, block.WOOL.id,6)
	mc.setBlock(x-5,y+13, zz, block.WOOL.id,6)
	mc.setBlock(x-4,y+13, zz, block.AIR.id)
	mc.setBlock(x-3,y+13, zz, block.WOOL.id,6)
	mc.setBlock(x-2,y+13, zz, block.WOOL.id,6)
	mc.setBlock(x-1,y+13, zz, block.WOOL.id,6)
	mc.setBlock(x,y+13, zz, block.WOOL.id,2)
	mc.setBlock(x+1,y+13, zz, block.WOOL.id,6)
	mc.setBlock(x+2,y+13, zz, block.WOOL.id,6)
	mc.setBlock(x+3,y+13, zz, block.WOOL.id,6)
	mc.setBlock(x+4,y+13, zz, block.AIR.id)
	mc.setBlock(x+5,y+13, zz, block.WOOL.id,6)
	mc.setBlock(x+6,y+13, zz, block.WOOL.id,6)
	#layer 15
	mc.setBlock(x-6,y+14, zz, block.WOOL.id,6)
	mc.setBlock(x-5,y+14, zz, block.WOOL.id,6)
	mc.setBlock(x-4,y+14, zz, block.WOOL.id,6)
	mc.setBlock(x-3,y+14, zz, block.WOOL.id,6)
	mc.setBlock(x-2,y+14, zz, block.WOOL.id,6)
	mc.setBlock(x-1,y+14, zz, block.WOOL.id,6)
	mc.setBlock(x,y+14, zz, block.WOOL.id,2)
	mc.setBlock(x+1,y+14, zz, block.WOOL.id,6)
	mc.setBlock(x+2,y+14, zz, block.WOOL.id,6)
	mc.setBlock(x+3,y+14, zz, block.WOOL.id,6)
	mc.setBlock(x+4,y+14, zz, block.WOOL.id,6)
	mc.setBlock(x+5,y+14, zz, block.WOOL.id,6)
	mc.setBlock(x+6,y+14, zz, block.WOOL.id,6)
	#layer 16	
	mc.setBlock(x-6,y+15, zz, block.WOOL.id,6)
	mc.setBlock(x-5,y+15, zz, block.WOOL.id,6)	
	mc.setBlock(x-4,y+15, zz, block.WOOL.id,6)
	mc.setBlock(x-3,y+15, zz, block.WOOL.id,6)
	mc.setBlock(x-2,y+15, zz, block.WOOL.id,6)
	mc.setBlock(x-1,y+15, zz, block.WOOL.id,6)
	mc.setBlock(x,y+15, zz, block.WOOL.id,2)
	mc.setBlock(x+1,y+15, zz, block.WOOL.id,6)
	mc.setBlock(x+2,y+15, zz, block.WOOL.id,6)
	mc.setBlock(x+3,y+15, zz, block.WOOL.id,6)
	mc.setBlock(x+4,y+15, zz, block.WOOL.id,6)
	mc.setBlock(x+5,y+15, zz, block.WOOL.id,6)
	mc.setBlock(x+6,y+15, zz, block.WOOL.id,6)
	#layer 17
	mc.setBlock(x-5,y+16, zz, block.WOOL.id,6)
	mc.setBlock(x-4,y+16, zz, block.WOOL.id,6)
	mc.setBlock(x-3,y+16, zz, block.WOOL.id,6)
	mc.setBlock(x-2,y+16, zz, block.WOOL.id,6)
	mc.setBlock(x-1,y+16, zz, block.WOOL.id,6)
	mc.setBlock(x,y+16, zz, block.WOOL.id,2)
	mc.setBlock(x+1,y+16, zz, block.WOOL.id,6)
	mc.setBlock(x+2,y+16, zz, block.WOOL.id,6)
	mc.setBlock(x+3,y+16, zz, block.WOOL.id,6)
	mc.setBlock(x+4,y+16, zz, block.WOOL.id,6)
	mc.setBlock(x+5,y+16, zz, block.WOOL.id,6)
	#layer 18
	mc.setBlock(x-5,y+17, zz, block.WOOL.id,6)
	mc.setBlock(x-4,y+17, zz, block.WOOL.id,6)
	mc.setBlock(x-3,y+17, zz, block.WOOL.id,6)
	mc.setBlock(x-2,y+17, zz, block.WOOL.id,6)
	mc.setBlock(x-1,y+17, zz, block.WOOL.id,6)
	mc.setBlock(x,y+17, zz, block.WOOL.id,2)
	mc.setBlock(x+1,y+17, zz, block.WOOL.id,6)
	mc.setBlock(x+2,y+17, zz, block.WOOL.id,6)
	mc.setBlock(x+3,y+17, zz, block.WOOL.id,6)
	mc.setBlock(x+4,y+17, zz, block.WOOL.id,6)
	mc.setBlock(x+5,y+17, zz, block.WOOL.id,6)
	#layer 19
	mc.setBlock(x-3,y+18, zz, block.WOOL.id,6)
	mc.setBlock(x-2,y+18, zz, block.WOOL.id,6)
	mc.setBlock(x-1,y+18, zz, block.WOOL.id,2)
	mc.setBlock(x,y+18, zz, block.WOOD_PLANKS.id)
	mc.setBlock(x+1,y+18, zz, block.WOOL.id,2)
	mc.setBlock(x+2,y+18, zz, block.WOOL.id,6)
	mc.setBlock(x+3,y+18, zz, block.WOOL.id,6)
	#layer 20
	mc.setBlock(x-2,y+19, zz, block.WOOL.id,2)
	mc.setBlock(x-1,y+19, zz, block.WOOD_PLANKS.id)
	mc.setBlock(x,y+19, zz, block.WOOD_PLANKS.id)
	mc.setBlock(x+1,y+19, zz, block.WOOD_PLANKS.id)
	mc.setBlock(x+2,y+19, zz, block.WOOL.id,2)
	#layer 21
	mc.setBlock(x-1,y+20, zz, block.WOOD_PLANKS.id)
	mc.setBlock(x,y+20, zz, block.WOOD_PLANKS.id)
	mc.setBlock(x+1,y+20, zz, block.WOOD_PLANKS.id)
	#layer 22
	mc.setBlock(x-2,y+21, zz, block.WOOD_PLANKS.id)
	mc.setBlock(x-1,y+21, zz, block.WOOL.id,1)
	mc.setBlock(x,y+21, zz, block.WOOL.id,1)
	mc.setBlock(x+1,y+21, zz, block.WOOL.id,1)
	mc.setBlock(x+2,y+21, zz, block.WOOD_PLANKS.id)
	#layer 23
	mc.setBlock(x-2,y+22, zz, block.WOOD_PLANKS.id)
	mc.setBlock(x-1,y+22, zz, block.WOOD_PLANKS.id)
	mc.setBlock(x,y+22, zz, block.WOOD_PLANKS.id)
	mc.setBlock(x+1,y+22, zz, block.WOOD_PLANKS.id)
	mc.setBlock(x+2,y+22, zz, block.WOOD_PLANKS.id)
	#layer 24
	mc.setBlock(x-2,y+23, zz, block.WOOD_PLANKS.id)	
	mc.setBlock(x-1,y+23, zz, block.WOOL.id,15)
	mc.setBlock(x,y+23, zz, block.WOOD_PLANKS.id)
	mc.setBlock(x+1,y+23, zz, block.WOOL.id,15)
	mc.setBlock(x+2,y+23, zz, block.WOOD_PLANKS.id)
	#layer 25
	mc.setBlock(x-2,y+24, zz, block.WOOD.id,1)
	mc.setBlock(x-1,y+24, zz, block.WOOD_PLANKS.id)
	mc.setBlock(x,y+24, zz, block.WOOD_PLANKS.id)
	mc.setBlock(x+1,y+24, zz, block.WOOD_PLANKS.id)
	mc.setBlock(x+2,y+24, zz, block.WOOD.id,1)
	#layer 26
	mc.setBlock(x-1,y+25, zz, block.WOOD.id,1)
	mc.setBlock(x,y+25, zz, block.WOOD.id,1)
	mc.setBlock(x+1,y+25, zz, block.WOOD.id,1)

def main():
		x,y,z= mc.player.getPos()
		h=5;k=5;l=5;
		clear_with_air(mc,x,y,z,h,k,l)
		posta(mc,x,y,zz)
    	
main()
