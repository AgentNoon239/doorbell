from gpiozero import MCP3008
import time
import requests

analog = MCP3008(channel=0)

while True:
	analog_value = int(analog.value * 1024)
	if analog_value > 200:
		requests.post(
			'https://discord.com/api/webhooks/1412507571583057920/pWrx-6s7_dT-vdfDxRTgwtMETwCHCapJX-5bkkwZrMsMvyiNfF11eyuR7feR0S0sgi5l',
			json={"content": "Doorbell pressed"}
		)
		time.sleep(6)
	time.sleep(0.01)