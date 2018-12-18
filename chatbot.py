from bottle import route,run,request,abort,static_file
from transitions.extensions import GraphMachine
import requests
import random
import os

GRAPH_URL="https://graph.facebook.com/v2.6"
VERIFY_TOKEN=os.environ["VERIFY_TOKEN"]
PAGE_TOKEN=os.environ["PAGE_TOKEN"]

def send_text_message(name,text):
	url="{0}/me/messages?access_token={1}".format(GRAPH_URL,PAGE_TOKEN)
	ctx={
			"recipient":{"id":name},
			"message":{"text":text}
			}
	response=requests.post(url,json=ctx)
	if response.status_code!=200:
		print("Unable to send message: "+response.text)
	return response
def send_image_message(name,text):
	url="{0}/me/messages?access_token={1}".format(GRAPH_URL,PAGE_TOKEN)
	ctx={
			"recipient":{"id":name},
			"message":{"attachment":{"type":"image","payload":{"url":text}}}
			}
	response=requests.post(url,json=ctx)
	if response.status_code!=200:
		print("Unable to send message: "+response.text)
	return response
#不知道為什麼只傳一次，他會一直進來???
class TocMachine(GraphMachine):
	def __init__(self,**machine_configs):
		self.machine=GraphMachine(model=self,**machine_configs)

	def is_going_to_state0(self,event):
		print("\nis going to state0\n")
		if event.get("message"):
			text=event["message"]
			if text.get("text"):
				if text["text"].lower()=="universe":
					return True
		return False

	def is_going_to_state1(self,event):
		print("\nis going to state1\n")
		if event.get("message"):
			text=event["message"]
			if text.get("text"):
				if text["text"].lower()=="奇經八脈":
					return True
		return False
	def is_going_to_state1_1(self,event):
		print("\nis going to state1_1\n")
		if event.get("message"):
			text=event["message"]
			if text.get("text"):
				if text["text"].lower()=="任脈":
					return True
		return False
	def is_going_to_state1_2(self,event):
		print("\nis going to state1_2\n")
		if event.get("message"):
			text=event["message"]
			if text.get("text"):
				if text["text"].lower()=="督脈":
					return True
		return False
	def is_going_to_state1_3(self,event):
		print("\nis going to state1_3\n")
		if event.get("message"):
			text=event["message"]
			if text.get("text"):
				if text["text"].lower()=="帶脈":
					return True
		return False
	def is_going_to_state1_4(self,event):
		print("\nis going to state1_4\n")
		if event.get("message"):
			text=event["message"]
			if text.get("text"):
				if text["text"].lower()=="衝脈":
					return True
		return False
	def is_going_to_state1_5(self,event):
		print("\nis going to state1_5\n")
		if event.get("message"):
			text=event["message"]
			if text.get("text"):
				if text["text"].lower()=="陰蹻脈":
					return True
		return False
	def is_going_to_state1_6(self,event):
		print("\nis going to state1_6\n")
		if event.get("message"):
			text=event["message"]
			if text.get("text"):
				if text["text"].lower()=="陽蹻脈":
					return True
		return False
	def is_going_to_state1_7(self,event):
		print("\nis going to state1_7\n")
		if event.get("message"):
			text=event["message"]
			if text.get("text"):
				if text["text"].lower()=="陰維脈":
					return True
		return False
	def is_going_to_state1_8(self,event):
		print("\nis going to state1_8\n")
		if event.get("message"):
			text=event["message"]
			if text.get("text"):
				if text["text"].lower()=="陽維脈":
					return True
		return False

	def is_going_to_state2(self,event):
		print("\nis going to state2\n")
		if event.get("message"):
			text=event["message"]
			if text.get("text"):
				if text["text"].lower()=="八卦":
					return True
		return False
	def is_going_to_state2_1(self,event):
		print("\nis going to state2_1\n")
		if event.get("message"):
			text=event["message"]
			if text.get("text"):
				if text["text"].lower()=="乾":
					return True
		return False
	def is_going_to_state2_2(self,event):
		print("\nis going to state2_2\n")
		if event.get("message"):
			text=event["message"]
			if text.get("text"):
				if text["text"].lower()=="兌":
					return True
		return False
	def is_going_to_state2_3(self,event):
		print("\nis going to state2_3\n")
		if event.get("message"):
			text=event["message"]
			if text.get("text"):
				if text["text"].lower()=="離":
					return True
		return False
	def is_going_to_state2_4(self,event):
		print("\nis going to state2_4\n")
		if event.get("message"):
			text=event["message"]
			if text.get("text"):
				if text["text"].lower()=="震":
					return True
		return False
	def is_going_to_state2_5(self,event):
		print("\nis going to state2_5\n")
		if event.get("message"):
			text=event["message"]
			if text.get("text"):
				if text["text"].lower()=="巽":
					return True
		return False
	def is_going_to_state2_6(self,event):
		print("\nis going to state2_6\n")
		if event.get("message"):
			text=event["message"]
			if text.get("text"):
				if text["text"].lower()=="坎":
					return True
		return False
	def is_going_to_state2_7(self,event):
		print("\nis going to state2_7\n")
		if event.get("message"):
			text=event["message"]
			if text.get("text"):
				if text["text"].lower()=="艮":
					return True
		return False
	def is_going_to_state2_8(self,event):
		print("\nis going to state2_8\n")
		if event.get("message"):
			text=event["message"]
			if text.get("text"):
				if text["text"].lower()=="坤":
					return True
		return False

	def is_going_to_state3(self,event):
		print("\nis going to state3\n")
		if event.get("message"):
			text=event["message"]
			if text.get("text"):
				if text["text"].lower()=="猜拳":
					return True
		return False
	def is_going_to_state3_1(self,event):
		print("\nis going to state3_1\n")
		if event.get("message"):
			text=event["message"]
			if text.get("text"):
				if text["text"].lower()=="剪刀":
					return True
		return False
	def is_going_to_state3_2(self,event):
		print("\nis going to state3_2\n")
		if event.get("message"):
			text=event["message"]
			if text.get("text"):
				if text["text"].lower()=="石頭":
					return True
		return False
	def is_going_to_state3_3(self,event):
		print("\nis going to state3_3\n")
		if event.get("message"):
			text=event["message"]
			if text.get("text"):
				if text["text"].lower()=="布":
					return True
		return False

	def on_enter_state0(self, event):
		print("\nI'm entering state0\n")
		sender_id=event['sender']['id']
		responese=send_text_message(sender_id,"想了解宇宙的神奇嗎?\r\n輸入:奇經八脈 八卦 猜拳\r\n(輸入:universe 回到這裡)")

	def on_enter_state1(self, event):
		print("\nI'm entering state1\n")
		sender_id=event['sender']['id']
		send_text_message(sender_id,"奇經八脈是指十二經脈之外的八條經脈\r\n奇者，異也，因其異于十二正經，故稱\"奇經\"\r\n既不直屬臟腑，又無表裡配合\r\n其生理功能，主要是對十二經脈的氣血運行起著溢蓄、調節作用\r\n十二經脈猶如\"江河\"，奇經八脈猶如\"湖澤\"\r\n任->總任 督->總督 帶->約束 衝->衝要 蹻->蹻捷 維->維繫\r\n八脈介紹輸入:任脈 督脈 帶脈 衝脈 陰蹻脈 陽蹻脈 陰維脈 陽維脈")
	def on_enter_state1_1(self, event):
		print("\nI'm entering state1_1\n")
		sender_id=event['sender']['id']
		send_text_message(sender_id,"任脈三八起會陰，曲骨中極關元銳，石門氣海陰交仍，神闕水分下腕配。建里中上腕相連，巨闕鳩尾蔽骨下，中庭膻中慕玉堂，紫宮華蓋璇璣收。天突結喉是廉泉，唇下宛宛承漿舍。")
		send_image_message(sender_id,"https://www.dharmazen.org/X3LogoB/MagRen1.GIF")
		send_text_message(sender_id,"任脈詳細介紹\r\nhttps://www.dharmazen.org/X1Chinese/D32Health/H516MagRen.htm")
	def on_enter_state1_2(self, event):
		print("\nI'm entering state1_2\n")
		sender_id=event['sender']['id']
		send_text_message(sender_id,"督脈中行二十七，長強腰俞陽關密，命門懸樞追脊中，筋縮至陽靈臺逸。神道身柱陶道長，大椎平肩二十一，瘂門風府腦戶深，強間後頂百會率。前頂囟會上星圓，神庭素髎水溝窟，兌端開口唇中央，齦交唇內任督畢。")
		send_image_message(sender_id,"https://www.dharmazen.org/X3LogoB/MagDo1.GIF")
		send_text_message(sender_id,"督脈詳細介紹\r\nhttps://www.dharmazen.org/X1Chinese/D32Health/H515MagDo.htm")
	def on_enter_state1_3(self, event):
		print("\nI'm entering state1_3\n")
		sender_id=event['sender']['id']
		send_image_message(sender_id,"https://www.dharmazen.org/X3LogoB/MagDio1.gif")
		send_text_message(sender_id,"帶脈詳細介紹\r\nhttps://www.dharmazen.org/X1Chinese/D32Health/H522MagRing.htm")
	def on_enter_state1_4(self, event):
		print("\nI'm entering state1_4\n")
		sender_id=event['sender']['id']
		send_image_message(sender_id,"https://www.dharmazen.org/X3LogoB/MagChong1.gif")
		send_text_message(sender_id,"衝脈詳細介紹\r\nhttps://www.dharmazen.org/X1Chinese/D32Health/H517MagChong.htm")
	def on_enter_state1_5(self, event):
		print("\nI'm entering state1_5\n")
		sender_id=event['sender']['id']
		send_image_message(sender_id,"https://www.dharmazen.org/X3LogoB/MagNChout1.gif")
		send_text_message(sender_id,"陰蹻脈詳細介紹\r\nhttps://www.dharmazen.org/X1Chinese/D32Health/H519MagNChout.htm")
	def on_enter_state1_6(self, event):
		print("\nI'm entering state1_6\n")
		sender_id=event['sender']['id']
		send_image_message(sender_id,"https://www.dharmazen.org/X3LogoB/MagYChout1.gif")
		send_text_message(sender_id,"陽蹻脈詳細介紹\r\nhttps://www.dharmazen.org/X1Chinese/D32Health/H518MagYChout.htm")
	def on_enter_state1_7(self, event):
		print("\nI'm entering state1_7\n")
		sender_id=event['sender']['id']
		send_image_message(sender_id,"https://www.dharmazen.org/X3LogoB/MagNwei1.gif")
		send_text_message(sender_id,"陰維脈詳細介紹\r\nhttps://www.dharmazen.org/X1Chinese/D32Health/H521MagNwei.htm")
	def on_enter_state1_8(self, event):
		print("\nI'm entering state1_8\n")
		sender_id=event['sender']['id']
		send_image_message(sender_id,"https://www.dharmazen.org/X3LogoB/MagYwei1.gif")
		send_text_message(sender_id,"陽維脈詳細介紹\r\nhttps://www.dharmazen.org/X1Chinese/D32Health/H520MagYwei.htm")

	def on_enter_state2(self, event):
		print("\nI'm entering state2\n")
		sender_id=event['sender']['id']
		send_text_message(sender_id,"易有太極，是生兩儀，兩儀生四象，四象生八卦，八卦定吉凶，吉凶生大業\r\n乾三連，坤六斷，震仰盂，艮覆碗，離中虛，坎中滿，兌上缺，巽下斷\r\n八卦介紹輸入:乾 兌 離 震 巽 坎 艮 坤")
	def on_enter_state2_1(self, event):
		print("\nI'm entering state2_1\n")
		sender_id=event['sender']['id']
		send_text_message(sender_id,"乾為天，天風姤，天山遁，天地否，風地觀，山地剝，火地晉，火天大有。\r\n八八六十四，是不是更想了解六十四卦阿?!\r\nhttps://www.eee-learning.com/article/2076")
	def on_enter_state2_2(self, event):
		print("\nI'm entering state2_2\n")
		sender_id=event['sender']['id']
		send_text_message(sender_id,"兌為澤，澤水困，澤地萃，澤山鹹，水山蹇，地山謙，雷山小過，雷澤歸妹。\r\n八八六十四，是不是更想了解六十四卦阿?!\r\nhttps://www.eee-learning.com/article/2076")
	def on_enter_state2_3(self, event):
		print("\nI'm entering state2_3\n")
		sender_id=event['sender']['id']
		send_text_message(sender_id,"離為火，火山旅，火風鼎，火水未濟，山水蒙，風水渙，天水訟，天火同人。\r\n八八六十四，是不是更想了解六十四卦阿?!\r\nhttps://www.eee-learning.com/article/2076")
	def on_enter_state2_4(self, event):
		print("\nI'm entering state2_4\n")
		sender_id=event['sender']['id']
		send_text_message(sender_id,"震為雷，雷地豫，雷水解，雷風恆；地風升，水風井，澤風大過，澤雷隨。\r\n八八六十四，是不是更想了解六十四卦阿?!\r\nhttps://www.eee-learning.com/article/2076")
	def on_enter_state2_5(self, event):
		print("\nI'm entering state2_5\n")
		sender_id=event['sender']['id']
		send_text_message(sender_id,"巽為風，風天小畜，風火家人，風雷益，天雷無妄，火雷噬嗑，山雷頤，山風蠱。\r\n八八六十四，是不是更想了解六十四卦阿?!\r\nhttps://www.eee-learning.com/article/2076")
	def on_enter_state2_6(self, event):
		print("\nI'm entering state2_6\n")
		sender_id=event['sender']['id']
		send_text_message(sender_id,"坎為水，水澤節，水雷屯，水火既濟，澤火革，雷火豐，地火明夷，地水師。\r\n八八六十四，是不是更想了解六十四卦阿?!\r\nhttps://www.eee-learning.com/article/2076")
	def on_enter_state2_7(self, event):
		print("\nI'm entering state2_7\n")
		sender_id=event['sender']['id']
		send_text_message(sender_id,"艮為山，山火贲，山天大畜，山澤損，火澤睽，天澤履，風澤中孚，風山漸。\r\n八八六十四，是不是更想了解六十四卦阿?!\r\nhttps://www.eee-learning.com/article/2076")
	def on_enter_state2_8(self, event):
		print("\nI'm entering state2_8\n")
		sender_id=event['sender']['id']
		send_text_message(sender_id,"坤為地，地雷復，地澤臨，地天泰，雷天大壯，澤天夬，水天需，水地比。\r\n八八六十四，是不是更想了解六十四卦阿?!\r\nhttps://www.eee-learning.com/article/2076")

	def on_enter_state3(self, event):
		print("\nI'm entering state3\n")
		sender_id=event['sender']['id']
		send_text_message(sender_id,"規則:\r\n就是剪刀石頭布\r\n遊戲輸入:剪刀 石頭 布")
	def on_enter_state3_1(self, event):
		print("\nI'm entering state3_1\n")
		sender_id=event['sender']['id']
		x=random.randint(1,3)
		print("\nx:%d\n" % x)
		if x==1:
			send_text_message(sender_id,"剪刀\r\n平手呦~~~\r\n(可繼續遊戲)")
		elif x==2:
			send_text_message(sender_id,"石頭\r\n輸了呦~~~\r\n(可繼續遊戲)")
		else:
			send_text_message(sender_id,"布\r\n贏了呦~~~\r\n(可繼續遊戲)")
		self.go_back(event)
	def on_enter_state3_2(self, event):
		print("\nI'm entering state3_2\n")
		sender_id=event['sender']['id']
		x=random.randint(1,3)
		print("\nx:%d\n" % x)
		if x==1:
			send_text_message(sender_id,"剪刀\r\n贏了呦~~~\r\n(可繼續遊戲)")
		elif x==2:
			send_text_message(sender_id,"石頭\r\n平手呦~~~\r\n(可繼續遊戲)")
		else:
			send_text_message(sender_id,"布\r\n輸了呦~~~\r\n(可繼續遊戲)")
		self.go_back(event)
	def on_enter_state3_3(self, event):
		print("\nI'm entering state3_3\n")
		sender_id=event['sender']['id']
		x=random.randint(1,3)
		print("\nx:%d\n" % x)
		if x==1:
			send_text_message(sender_id,"剪刀\r\n輸了呦~~~\r\n(可繼續遊戲)")
		elif x==2:
			send_text_message(sender_id,"石頭\r\n贏了呦~~~\r\n(可繼續遊戲)")
		else:
			send_text_message(sender_id,"布\r\n平手呦~~~\r\n(可繼續遊戲)")
		self.go_back(event)

machine=TocMachine(
		states=[
			"user",
			"state0",
			"state1",
			"state1_1",
			"state1_2",
			"state1_3",
			"state1_4",
			"state1_5",
			"state1_6",
			"state1_7",
			"state1_8",
			"state2",
			"state2_1",
			"state2_2",
			"state2_3",
			"state2_4",
			"state2_5",
			"state2_6",
			"state2_7",
			"state2_8",
			"state3",
			"state3_1",
			"state3_2",
			"state3_3"
			],
		transitions=[
			{
				"trigger":"wakeup",
				"source":"user",
				"dest":"state0"
				},
			{
				"trigger":"advance",
				"source":[
					"user",
					"state0",
					"state1",
					"state1_1",
					"state1_2",
					"state1_3",
					"state1_4",
					"state1_5",
					"state1_6",
					"state1_7",
					"state1_8",
					"state2",
					"state2_1",
					"state2_2",
					"state2_3",
					"state2_4",
					"state2_5",
					"state2_6",
					"state2_7",
					"state2_8",
					"state3"
					],
				"dest":"state0",
				"conditions":"is_going_to_state0"
				},
			{
				"trigger":"advance",
				"source":"state0",
				"dest":"state1",
				"conditions":"is_going_to_state1"
				},
			{
				"trigger":"advance",
				"source":"state1",
				"dest":"state1_1",
				"conditions":"is_going_to_state1_1"
				},
			{
				"trigger":"advance",
				"source":"state1",
				"dest":"state1_2",
				"conditions":"is_going_to_state1_2"
				},
			{
				"trigger":"advance",
				"source":"state1",
				"dest":"state1_3",
				"conditions":"is_going_to_state1_3"
				},
			{
				"trigger":"advance",
				"source":"state1",
				"dest":"state1_4",
				"conditions":"is_going_to_state1_4"
				},
			{
				"trigger":"advance",
				"source":"state1",
				"dest":"state1_5",
				"conditions":"is_going_to_state1_5"
				},
			{
				"trigger":"advance",
				"source":"state1",
				"dest":"state1_6",
				"conditions":"is_going_to_state1_6"
				},
			{
				"trigger":"advance",
				"source":"state1",
				"dest":"state1_7",
				"conditions":"is_going_to_state1_7"
				},
			{
				"trigger":"advance",
				"source":"state1",
				"dest":"state1_8",
				"conditions":"is_going_to_state1_8"
				},
			{
				"trigger":"advance",
				"source":"state0",
				"dest":"state2",
				"conditions":"is_going_to_state2"
				},
			{
				"trigger":"advance",
				"source":"state2",
				"dest":"state2_1",
				"conditions":"is_going_to_state2_1"
				},
			{
				"trigger":"advance",
				"source":"state2",
				"dest":"state2_2",
				"conditions":"is_going_to_state2_2"
				},
			{
				"trigger":"advance",
				"source":"state2",
				"dest":"state2_3",
				"conditions":"is_going_to_state2_3"
				},
			{
				"trigger":"advance",
				"source":"state2",
				"dest":"state2_4",
				"conditions":"is_going_to_state2_4"
				},
			{
				"trigger":"advance",
				"source":"state2",
				"dest":"state2_5",
				"conditions":"is_going_to_state2_5"
				},
			{
				"trigger":"advance",
				"source":"state2",
				"dest":"state2_6",
				"conditions":"is_going_to_state2_6"
				},
			{
				"trigger":"advance",
				"source":"state2",
				"dest":"state2_7",
				"conditions":"is_going_to_state2_7"
				},
			{
				"trigger":"advance",
				"source":"state2",
				"dest":"state2_8",
				"conditions":"is_going_to_state2_8"
				},
			{
				"trigger":"advance",
				"source":"state0",
				"dest":"state3",
				"conditions":"is_going_to_state3"
				},
			{
				"trigger":"advance",
				"source":"state3",
				"dest":"state3_1",
				"conditions":"is_going_to_state3_1"
				},
			{
				"trigger":"advance",
				"source":"state3",
				"dest":"state3_2",
				"conditions":"is_going_to_state3_2"
				},
			{
				"trigger":"advance",
				"source":"state3",
				"dest":"state3_3",
				"conditions":"is_going_to_state3_3"
				},
			{
				"trigger":"go_back",
				"source":[
					"state3_1",
					"state3_2",
					"state3_3"
					],
				"dest":"state3",
				}
			],
		initial="user",
		auto_transitions=False,
		show_conditions=True,
		)

@route("/webhook",method=["GET","POST"])
def webhook():
#method="GET"
	if request.method == "GET":
		mode=request.GET.get("hub.mode")
		verify_token=request.GET.get("hub.verify_token")
		challenge=request.GET.get("hub.challenge")
		if mode=="subscribe" and verify_token==VERIFY_TOKEN:
			print("WEBHOOK_VERIFIED")
			return challenge
		else:
			abort(403)
#method="POST"
	else:
		body=request.json
		print("\nFSM state: "+machine.state+"\n")
		if body["object"]=="page":
			event=body["entry"][0]["messaging"][0]
			if machine.state=="user":
				machine.wakeup(event)
			else:
				machine.advance(event)
			return "OK"
@route("/show-fsm",method=["GET"])
def show_fsm():
	machine.get_graph().draw("fsm.png",prog="dot",format="png")
	return static_file("fsm.png",root="./",mimetype="image/png")
if __name__ == "__main__":
	show_fsm()
	run(host="localhost",port=5000,debug=True)
