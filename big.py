import streamlit as st

rang1 = st.number_input("請設定本局遊戲的最小值:")
rang2 = st.number_input("請設定本局遊戲的最大值:")
confirm_input=st.button('輸入確認')
num = random.randint(rang1,rang2)
guess = "guess"
i = 0
while guess != num:
    i += 1
    guess = st.number_input("你猜數字多少：")
    if guess == num:
        st.write("恭喜，你猜對了！")
    elif guess < num:
        st.write("再大一點！！")
    else:
        st.write("再小一點！！")

