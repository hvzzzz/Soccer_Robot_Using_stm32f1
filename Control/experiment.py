import pickle
run=True
outs=''
while run:
        x=int(input('enter x: '))
        y=int(input('enter y: '))
        coords = { "xcoord": x, "ycoord": y } 
        pickle.dump( coords, open( "save.p", "wb" ) )
        #print(play2[name])
        outs=input('continue?')
        if outs=='salir':
                run=False