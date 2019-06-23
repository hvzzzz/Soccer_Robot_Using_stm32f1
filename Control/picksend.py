import pickle
x=int(input('enter x: '))
y=int(input('enter y: '))
favorite_color = { "xcoord": x, "ycoord": y } 
pickle.dump( favorite_color, open( "save.p", "wb" ) )