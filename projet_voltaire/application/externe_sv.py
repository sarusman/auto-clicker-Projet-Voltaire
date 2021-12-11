import pyautogui,time
import random, datetime
import request, json
dtc=json.load(request.get("LINK").text)

while True:
	dtc=json.load(request.get("LINK").text)

	if datetime.datetime.now().strftime("%H:%M")!=dtc["time"] and dtc["did_i_click?"]:
		try:
			pyautogui.click(500,500)
			time.sleep(1)
			pyautogui.click(930,730)
			time.sleep(1)
			t, v=750,random.randint(500, 690)

			pyautogui.click(930,v) #compris
			time.sleep(1)

			pyautogui.click(t, v)

			time.sleep(1)
			pyautogui.click(t, v+50)

			time.sleep(1)
			pyautogui.click(750, v+100)

			time.sleep(1)

			pyautogui.click(910, v+140)
			time.sleep(1)

		except:
	 		print("erreur")


