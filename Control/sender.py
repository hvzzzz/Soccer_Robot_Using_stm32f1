book ={}
book['play2']={
    'xcoord':0
    'ycoord':0
}
book['play3']={
    'xcoord':0
    'ycoord':0
}
import json
s=json.dumps(book)
with open("C://Users//hanan//Google Drive//P//Soccer Robot//Soccer_Robot_Using_stm32f1//Control"."w") as f:
    f.write(s)