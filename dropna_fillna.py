import pandas as pd
import pandas as pd 

data=pd.read_csv("my_file1.csv")
# print(data)    #ab is data k ander kuch empty values hn, jin ki jga NaN likha hua h

# Drop NaN vali poori row:
new_data=data.dropna()      #ab vo rows jin m NaN tha, vo poori row hi drop ho gi, ab us 
# print(new_data)           # row ka index bhi nhi mily ga.

# by- default dropna row k across drop krta , but hm chahty n k vo NaN jhan ho to us
# ki poori row ki bijay vo poora column hi drop ho jay to axis = 1 daal do simple:
n_data=data.dropna(axis=1)
# print(n_data)

# --------  agar mery data m koi poori row hi esi a gai jis m NaN tha, to m us poori
# row ko htany k liye how="any" kru gi

print(data.dropna(how="any"))   #esy krny s mery pas mojood poori empty row or saath saath
    # baki rows jin m NaN tha , vo bhi drop ho jay gi
print(data.dropna(how="all"))   # esy krny s just vo poori row drop ho gi jo empty thi
    # but baki rows jin m ek ya 2 ya kuch NaN tha, vo rhy gi. (yani vo row drop
    #                   kro jis k ander all NaN hn)


# -------  agar m chahti hu k kisi column m jo bhi NaN values hn, to us NaN vali saari 
    # row drop ho lekin bas usi column m jo empty hon vhi row drop ho, baki na ho:

print()
print()
print(data.dropna(subset="City"))  #ab city valy m jo bhi NaN hn, us NAN vali poori 
            # row drop ho gi, is s ab city valy column m koi bhi NaN nhi rhy


# --------  Agar ap chahty ho k NaN values drop ho kr purana dataset new saaf dataset m
#   convert ho jay to hm inplace  parameter ko use kryn gy:
print()
print()
# data.dropna(inplace=True)
# print(data)    # ab data k name s hi nia saath suthra NaN k bagher vala dataset create ho gya


# ------- thresh = 3 ka matlab y h k un rows ko drop kro jin k ander non-NaN values 3 
            # s km hn, thresh=2 ka matlab y h k un rows ko drop kro jin k ander non_NaN
            # values 2 s km hn.   


# print(data.dropna(thresh=2))
print(data.dropna(thresh=2, axis=1))  #ab esa ho ga k vo column drop ho ga jis m
                # non-NaN values 2 s km hon gi,,,,, vesy koi column bhi is data set m
                # condition pr nhi utr rha.
print()
print()

# ---------------------  fillna   -------------------------
print(data.fillna("PYTHON"))    #yani jhan pr bhi NaN values hon gi vo sab values
            # "PYTHON" s fill ho jay gi

print(data.fillna({"Brand":"LIMELIGHT",  "City":"SARGODHA"}))  #yani "brand" m jhan bhi NaN
        # ay us ki jga "LIMELIGHT" a jay ga, or jhan jhan "City" m NaN aya us ki jga "SARGODHA"
        # a jay ga
    
print(data.fillna(method="ffill"))   # is s NaN vali value m forwardfill ho ga yani NaN s 
            # peechy vali value (yani ooper valy cell ki value) is NaN ko fill kry gi,
            #  yani peechy valy m or is NaN m same value ho gi
print(data.fillna(method="bfill"))  #backward fill, yani NaN s agli vali value
            # yani NaN s neechy valy cell ki value is NaN ko fill kry gi

print(data.fillna(method="ffill", axis=0))  # yani row vis, yani NaN k left side pr jo value
        # ho gi vo forward shift ho gi yani NaN ko fill kry gi, agar us k left side pr koi
        # value na hui to NaN kisi value s fill nhi ho ga

# print(data.fillna(methd="bfill", axis=0, inplace=True))  #inplace = true same 
                # functionality as for dropna
    
print(data.fillna("PYTHON", limit=2)) # limit=2 krny s esa ho ga k agar ek column m 5
            # NaN values hn to just phli 2 ki jga PYTHON ay ga, baki m kuch nhi ho ga
            # agar limit=1 h to just hr column m just 1st 1st (yani phly phly) NaN ki
            #  jga PYTHON ay ga




# dropna, axis, how, subset, inplace, thresh
# fillna, 


# The 'inplace=True' argument stands for the data frame has to make changes permanent



