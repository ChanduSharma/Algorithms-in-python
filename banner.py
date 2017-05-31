import sys


a = ('    #    ',
     '   # #   ',
     '  #####  ',
     ' #     # ',
     '#       #')

b = ('######## ',
     '#       #',
     '######## ',
     '#       #',
     '######## ')
	 
c = ('#########',
     '#        ',
     '#        ',
     '#        ',
     '#########')

d = ('######## ',
     '#       #',
     '#       #',
     '#       #',
     '######## ')

e = ('#########',
     '#        ',
     '#########',
     '#        ',
     '#########')
	 
f = ('#########',
     '#        ',
     '######   ',
     '#        ',
     '#        ')
	 
g = (' ########',
     '#        ',
     '#   #### ',
     '#       #',
     ' ####### ')
	 
h = ('#       #',
     '#       #',
     '#########',
     '#       #',
     '#       #')
	 
i = ('#########',
     '    #    ',
     '    #    ',
     '    #    ',
     '#########')

j = ('#########',
     '    #    ',
     '    #    ',
     '#   #    ',
     ' ###     ')
	 
k = ('#       #',
     '#      # ',
     '#######  ',
     '#      # ',
     '#       #')
     
l = ('#        ',
     '#        ',
     '#        ',
     '#        ',
     '#########')
	 
m = ('##     ##',
     '# #   # #',
     '#  ###  #',
     '#       #',
     '#       #') 

n = ('###     #',
     '# #     #',
     '#  #    #',
     '#   #   #',
     '#    ####')

o = (' ####### ',
     '#       #',
     '#       #',
     '#       #',
     ' ####### ')
	 
p = ('#########',
     '#       #',
     '#########',
     '#        ',
     '#        ')
	 
q =  (' ####### ',
      '#       #',
      '#    #  #',
      '#     # #',
      ' ####### ')

r = ('######## ',
     '#       #',
     '######## ',
     '#    ##  ',
     '#      ##')
	 
s = (' ########',
     '#        ',
     ' ####### ',
     '        #',
     '######## ')
	 
t = ('#########',
     '    #    ',
     '    #    ',
     '    #    ',
     '    #    ')

u = ('#       #',
     '#       #',
     '#       #',
     '#       #',
     ' ####### ')
	 
v = ('#       #',
     ' #     # ',
     '  #   #  ',
     '   # #   ',
     '    #    ')
w = ('#       #',
     '#       #',
     '#  ###  #',
     '#  ###  #',
     '#### ####')
     
x = ('#       #',
     ' #     # ',
     '  #####  ',
     ' #     # ',
     '#       #')

y = ('#       #',
     ' #     # ',
     '  #####  ',
     '   ###   ',
     '   ###   ')
     
z = ('#########',
     '     ### ',
     '    ###  ',
     '   ###   ',
     '  ###    ',
     '#########')
	 
	 
#A dictionary which maps character to their corresponding display tuples.	 
mylist = {'a':a,'b':b,'c':c,'d':d,'e':e,'f':f,'g':g,'h':h,
	  'i':i,'j':j,'k':k,'l':l,'m':m,'n':n,'o':o,'p':p,
	  'q':q,'r':r,'s':s,'t':t,'u':u,'v':v,'w':w,'x':x,
	  'y':y,'z':z} 

#first argument of the command line
#So it will not read space separated name in command line
if len(sys.argv) > 1:
	name_list = sys.argv[1:];
	itr = 0 
	coloumn = 0
	for name in name_list:
		while itr < 5:
		#Iteration is taken as five because the display I used 
		# is a 5 segment display tuple.
			line = []
	
			for i in name.lower():
				line.append(mylist[i][coloumn])
	
			coloumn += 1
			print('  '.join(line))
	
			itr += 1
		print('\n')
else:
	print('Usage : banner.py [name]')
	print('And Yeah!Ofcourse name without brackets.')
