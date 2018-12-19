# TOC-chatbot
<p> 跟chatbot互動過程
<p> 輸入任意文字進入到state0
<p> 然後chatbot會印出資訊和進入到下一個state的提示，根據提示去對話即可，若在無提示出現，代表進入到了支線的終點，可隨時輸入universe回到state0
<p> bonus: creative design(play game with chatbot), sending images or video, deploy heroku, parsing website(BeautifulSoup)
<img src=https://github.com/314159265358979323846/TOC-chatbot/blob/master/fsm.png>
<p> 初始state(user) with (任意文字) -> state0
<p> state0 with (奇經八脈 || 八卦 || 猜拳 || 爬蟲) -> (state1 || state2 || state3 || state4)
<p> state1 with (任脈 || 督脈 || 帶脈 || 衝脈 || 陰蹻脈 || 陽蹻脈 || 陰維脈 || 陽維脈) -> (state1 _ 1 ~ state1 _ 8)
<p> state2 with (乾 || 兌 || 離 || 震 || 巽 || 坎 || 艮 || 坤) -> (state2 _ 1 ~ state2 _ 8)
<p> state3 with (開始遊戲) -> state3 _ 0
<p> state3 _ 0 with (查看規則) -> state3
<p> state3 _ 0 with (現在是 WHAT TIME || CAN NOT 帶煙來 || GO TO 吃雞飯) -> (state3 _ 1 ~ state3 _ 3) -> 無論勝負回到state3 _ 0繼續遊戲
<p> state4 with (yahoo新聞) -> state4 _ 1 (避免冗長只爬五篇)
<p> 每一個state with (universe) -> state0
