import streamlit as st

st.write('歡迎進入猜數字遊戲，玩家們準備好了嗎？')
GuessGame = st.number_input('是否要進入遊戲？(YES/NO)')
confirm_input=st.button('輸入確認')
if (GuessGame.lower() == "no"):
    exit()
elif (GuessGame.lower() == "yes"):
    st.write("遊戲正式開始！")
else:
    exit()

rang1 = st.number_input("請設定本局遊戲的最小值:")
rang2 = st.number_input("請設定本局遊戲的最大值:")
num = random.randint(rang1,rang2)
guess = "guess"
i = 0
while guess != num:
    i += 1
    guess = st.number_input(input("你猜數字多少：")
    if guess = num:
        st.write("恭喜，你猜對了！")
    elif guess < num:
        st.write("再大一點！！")
    else:
        st.write("再小一點！！")
st.write("你總共猜了%d" %i + "次"",快點再來一局！！！")
