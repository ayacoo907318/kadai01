import pandas as pd
source=["ねずこ","たんじろう","いのすけ","ぎゆう"]

def search():
    df=pd.read_csv("./input2.csv")
    source=list(df["name"])

df=pd.read_csv("./input2.csv")
source=list(df["name"])

while True:
    word=input("鬼滅の登場人物を入力　＞＞　")
    if word in source:
        print("『{}』が見つかりました".format(word))
    else:
        print("『{}』は見つかりませんでした".format(word))
        # 追加
        add_flg=input("追加登録しますか？(0:しない 1:する)　＞＞　")
        if add_flg=="1":
            source.append(word)

    # # 検索
    # if word in source:
    #     print("『{}』はあります".format(word))
    # else:
    #     print("『{}』はありません".format(word))
    #     # 追加
    #     add_flg=input("追加登録しますか？(0:しない 1:する)　＞＞　")
    #     if add_flg=="1":
    #         source.append(word)

    df=pd.DataFrame(source,columns=["name"])
    df.to_csv("./input2.csv",encoding="utf_8-sig")
    print(source)

#for s in source:
#    if "ねずこ"==s:
#        print("『ねずこ』はあります") 
if __name__ == "__main__":
    search()