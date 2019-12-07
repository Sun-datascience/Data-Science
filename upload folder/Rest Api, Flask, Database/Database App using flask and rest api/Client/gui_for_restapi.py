from tkinter import *
import json


def viewrest():
    import http.client
    conn = http.client.HTTPConnection("localhost", 5010)
    conn.request("GET","/viewusers")

    res=conn.getresponse()
    data=res.read()
    valdict=json.loads(data)
    print(valdict['msg'])

    l=valdict['msg']
    list1.delete(0,END)
    for i in l:
        list1.insert(END,i)




'''def adduserrest():
    import requests
    url = " http://127.0.0.1:5010/adduser"
    uid=eid_val.get()
    upass=epass_val.get()
    details = {'id':uid, 'passw': upass}
    print(details)
    response = requests.post(url=url, data=details)
    print(response.text)

    #insert(eid_val.get(), epass_val.get())
    #list1.delete(0,END)
    #list1.insert(END,eid_val.get(), epass_val.get())
'''

def adduserrest():
    import http.client
    import json
    conn=http.client.HTTPConnection('localhost',5010)
    headers={'content-type':'application/json'}

    details = {'id': eid_val.get(), 'passw': epass_val.get()}
    json_data=json.dumps(details)

    conn.request('POST','/adduser',json_data,headers)
    response=conn.getresponse()
    print(response.read())

def deleteuserrest():
    import http.client
    conn=http.client.HTTPConnection('localhost',5010)

    headers={'content-type':'application/json'}
    details={'id':eid_val.get()}
    json_data=json.dumps(details)

    conn.request('POST','/deleteuser',json_data,headers)
    response=conn.getresponse()
    #response=
    print(json.loads(response.read())['msg'])
    #print(response['msg'])

window=Tk()

lid=Label(window, text='ID')
lid.grid(row=0, column=0)

eid_val=StringVar()
eid=Entry(window, textvariable=eid_val)
eid.grid(row=0, column=1)

lpass=Label(window, text='PASS')
lpass.grid(row=1, column=0)

epass_val=StringVar()
epass=Entry(window, textvariable=epass_val)
epass.grid(row=1, column=1)

list1=Listbox(window, height=6,width=30)
list1.grid(row=3, column=0, rowspan=6, columnspan=3)

binsert=Button(window, text='INSERT', command=adduserrest)
binsert.grid(row=2, column=0)

bview=Button(window, text='VIEW', command=viewrest)
bview.grid(row=2, column=1)

bdelete=Button(window,text='Delete', command=deleteuserrest)
bdelete.grid(row=2, column=2)


window.mainloop()