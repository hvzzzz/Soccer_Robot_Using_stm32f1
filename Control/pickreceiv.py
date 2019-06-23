import pickle
favorite_color = pickle.load( open( "save.p", "rb" ) )
print(type(favorite_color['xcoord']))
