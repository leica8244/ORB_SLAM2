# -*- coding: utf-8 -*-   
import sys      
import os  

#usage:  generate assosiation.txt for ORB_SLAM2
#python generate_asso.py n


if __name__ == "__main__":
	print ('This is main of module "walkList.py"')
	n = sys.argv[1]
	f=open("xtion.txt",'w')  #pay attention here shoule be txtName
	for i in range(int(n)):
		f.write(str(i) + ' Image_ORBSLAM/rgb/color' + str(i) + '.png ' + str(i) + ' Image_ORBSLAM/depth/depth' + str(i) + '.png\n')    #rgb/1305031526.671473.png 1305031526.688356 depth/1305031526.688356.png
	# for i in range(1,100):
	# 	if i % 2 == 0:
	# 	    new_context = "C++" + '\n'
	# 	    f.write(new_context)
	# 	else:
	# 	    new_context = "Python" + '\n'  
	# 	    f.write(new_context)
	f.close()