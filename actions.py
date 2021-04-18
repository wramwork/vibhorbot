from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import smtplib
import pandas as pd
import json
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

ZomatoData = pd.read_csv('zomato.csv')
ZomatoData = ZomatoData.drop_duplicates().reset_index(drop=True)
WeOperate = ['New Delhi', 'Gurgaon', 'Noida', 'Faridabad', 'Allahabad', 'Bhubaneshwar', 'Mangalore', 'Mumbai', 'Ranchi', 'Patna', 'Mysore', 'Aurangabad', 'Amritsar', 'Puducherry', 'Varanasi', 'Nagpur', 'Vadodara', 'Dehradun', 'Vizag', 'Agra',
             'Ludhiana', 'Kanpur', 'Lucknow', 'Surat', 'Kochi', 'Indore', 'Ahmedabad', 'Coimbatore', 'Chennai', 'Guwahati', 'Jaipur', 'Hyderabad', 'Bangalore', 'Nashik', 'Pune', 'Kolkata', 'Bhopal', 'Goa', 'Chandigarh', 'Ghaziabad', 'Ooty', 'Gangtok', 'Shimla']


def RestaurantSearch(City, Cuisine, price_max, price_min):
	return ZomatoData[
            (ZomatoData['Cuisines'].apply(
            	lambda x: Cuisine.lower() in x.lower()))
            & (ZomatoData['City'].apply(lambda x: City.lower() in x.lower()))
            & (ZomatoData['Average Cost for two'].apply(lambda x: price_max > x))
            & (ZomatoData['Average Cost for two'].apply(lambda x: price_min < x))
        ][['Restaurant Name', 'Address', 'Average Cost for two', 'Aggregate rating']]


def sendmail(mail_id, data):
	sender = 'heena4415@gmail.com'
	receivers = [mail_id]

	message = MIMEMultipart("alternative")
	message["Subject"] = "Top 10 Foodie Restaurants"
	message["From"] = sender

	html = """
			<!DOCTYPE HTML PUBLIC "-//W3C//DTD XHTML 1.0 Transitional //EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
		<html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
		<head>
		<!--[if gte mso 9]>
		<xml>
		<o:OfficeDocumentSettings>
			<o:AllowPNG/>
			<o:PixelsPerInch>96</o:PixelsPerInch>
		</o:OfficeDocumentSettings>
		</xml>
		<![endif]-->
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta name="x-apple-disable-message-reformatting">
		<!--[if !mso]><!--><meta http-equiv="X-UA-Compatible" content="IE=edge"><!--<![endif]-->
		<title></title>
		
			<style type="text/css">
		@media only screen and (min-width: 570px) {
		.u-row {
			width: 550px !important;
		}
		.u-row .u-col {
			vertical-align: top;
		}

		.u-row .u-col-100 {
			width: 550px !important;
		}

		}

		@media (max-width: 570px) {
		.u-row-container {
			max-width: 100% !important;
			padding-left: 0px !important;
			padding-right: 0px !important;
		}
		.u-row .u-col {
			min-width: 320px !important;
			max-width: 100% !important;
			display: block !important;
		}
		.u-row {
			width: calc(100% - 40px) !important;
		}
		.u-col {
			width: 100% !important;
		}
		.u-col > div {
			margin: 0 auto;
		}
		}
		body {
		margin: 0;
		padding: 0;
		}

		table,
		tr,
		td {
		vertical-align: top;
		border-collapse: collapse;
		}

		p {
		margin: 0;
		}

		.ie-container table,
		.mso-container table {
		table-layout: fixed;
		}

		* {
		line-height: inherit;
		}

		a[x-apple-data-detectors='true'] {
		color: inherit !important;
		text-decoration: none !important;
		}

		@media (max-width: 480px) {
		.hide-mobile {
			display: none !important;
			max-height: 0px;
			overflow: hidden;
		}

		}
			</style>
		
		

		<!--[if !mso]><!--><link href="https://fonts.googleapis.com/css?family=Montserrat:400,700&display=swap" rel="stylesheet" type="text/css"><!--<![endif]-->

		</head>

		<body class="clean-body" style="margin: 0;padding: 0;-webkit-text-size-adjust: 100%;background-color: #ffffff">
		<!--[if IE]><div class="ie-container"><![endif]-->
		<!--[if mso]><div class="mso-container"><![endif]-->
		<table style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;min-width: 320px;Margin: 0 auto;background-color: #ffffff;width:100%" cellpadding="0" cellspacing="0">
		<tbody>
		<tr style="vertical-align: top">
			<td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top">
			<!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td align="center" style="background-color: #ffffff;"><![endif]-->
			

		<div class="u-row-container" style="padding: 0px;background-color: transparent">
		<div class="u-row" style="Margin: 0 auto;min-width: 320px;max-width: 550px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: #fc5656;">
			<div style="border-collapse: collapse;display: table;width: 100%;background-image: url('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAlgAAAN6CAYAAABSdTdVAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyhpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuNi1jMTM4IDc5LjE1OTgyNCwgMjAxNi8wOS8xNC0wMTowOTowMSAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENDIDIwMTcgKE1hY2ludG9zaCkiIHhtcE1NOkluc3RhbmNlSUQ9InhtcC5paWQ6OUZCOEY4RjlCRjc1MTFFQUFBMDNGQzVGNDQ4QThBRUYiIHhtcE1NOkRvY3VtZW50SUQ9InhtcC5kaWQ6OUZCOEY4RkFCRjc1MTFFQUFBMDNGQzVGNDQ4QThBRUYiPiA8eG1wTU06RGVyaXZlZEZyb20gc3RSZWY6aW5zdGFuY2VJRD0ieG1wLmlpZDo5RkI4RjhGN0JGNzUxMUVBQUEwM0ZDNUY0NDhBOEFFRiIgc3RSZWY6ZG9jdW1lbnRJRD0ieG1wLmRpZDo5RkI4RjhGOEJGNzUxMUVBQUEwM0ZDNUY0NDhBOEFFRiIvPiA8L3JkZjpEZXNjcmlwdGlvbj4gPC9yZGY6UkRGPiA8L3g6eG1wbWV0YT4gPD94cGFja2V0IGVuZD0iciI/PuvbmY4AAE4bSURBVHja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QGABAAgsAACBBQCAwAIAEFgAAAILAACBBQAgsAAABBYAAAILAEBgAQAILAAABBYAgMACABBYAAACCwAAgQUAILAAAAQWAAACCwBAYAEACCwAAAQWAIDAAgAQWAAAAktgAQAILAAAgQUAILAAABBYAAACCwBAYAEAILAAAAQWAIDAAgBAYAEACCwAAIEFACCwAAAQWAAAAgsAQGABACCwAAAEFgCAwAIAQGABAAgsAACBBQCAwAIAEFgAAAILAEBgAQAgsAAABBYAgMACAEBgAQAILAAAgQUAgMACABBYAAACCwAAgQUAILAAAAQWAIDAAgBAYAHAmLbwkflh3oMPhHw+v/bN4+LMijMpTnucUpxVcRbEWbGu7dRqtTBpypSw595Pt6gCCwDGtss//anwyfPPCePGT8jGXx4W51Vxnj8cWOPWuutA6rE4N8f5dpyfDodXU19vT3jBi18aPnX5Vy3qZspbAgB4aiu2FEPXuHF7dnZ1nRN/+Yo4beu5a7p99+E5Kc7P4pwb57fpi5lMJrS1tVnQUZC1BADw1LZg3rwTc7n8dfHTkzcQV4+Xi/PCOD+Oc5ZVFFgAwLBLPnr+K7//ra//V0dn566buInxcT4T59+spsACgDHvsx//6GFXfelzn+/o6uoYhXOqz49zqlUVWAAwZn33G1d1XnHppz8ybvyEyencqVGQDhmm87GeZnUFFgCMOb093eHqb37tde2dnceOUlw1tba2zr79tlveMfdv91pkgQUAY0v3mjVtD8+9/9RisTiq280XCmHxggX/uHjhgl2tssACgDHlyss+96xarXroaG83ncfV3tEx42tf+vzzrbLAAoAxZeWK5QfX640t8t/wdMhx5fLlh1hlgQUAY0o+l9uiJ6Ln83knugssABhzdniKb19gAQAgsABge7f4Kb59gQUAbFtqtdp9W3T71ep9VllgAcCYMmHSpD9ks5n6lth2ulTDhMmTf2+VBRYAjCmnnXHWbblcftQjKF2iob+vb/Epb3n7DVZZYAHAmNI1bnz/zrvudlWlXB7V7Var1TB95szvTZ8x8wGrLLAAYIwF1rjw8pNO/lpvb88v0yG90TI4MPDwAQcd/Jk99trbIgssABh7/unk03pef8ZZH1yzevWqUYqsdE7XuXHusboCCwDGrHf82wdvPPlNb3l7X0/PQDp/ajN9OM4VVlVg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');background-repeat: repeat;background-position: center top;background-color: transparent;">
			<!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding: 0px;background-color: transparent;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:550px;"><tr style="background-image: url('images/image-1.png');background-repeat: repeat;background-position: center top;background-color: #fc5656;"><![endif]-->
			
		<!--[if (mso)|(IE)]><td align="center" width="534" style="width: 534px;padding: 0px;border-top: 8px solid #000000;border-left: 8px solid #000000;border-right: 8px solid #000000;border-bottom: 0px solid transparent;" valign="top"><![endif]-->
		<div class="u-col u-col-100" style="max-width: 320px;min-width: 550px;display: table-cell;vertical-align: top;">
		<div style="width: 100% !important;">
		<!--[if (!mso)&(!IE)]><!--><div style="padding: 0px;border-top: 8px solid #000000;border-left: 8px solid #000000;border-right: 8px solid #000000;border-bottom: 0px solid transparent;"><!--<![endif]-->
		

		<table style="font-family:'Montserrat',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
		<tbody>
			<tr>
			<td style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:'Montserrat',sans-serif;" align="left">
				
		<div style="color: #ffffff; line-height: 100%; text-align: left; word-wrap: break-word;">
			<p style="line-height: 100%; text-align: center; font-size: 14px;"><span style="font-size: 44px; line-height: 44px;"><strong>Restaurants List</strong></span></p>
		</div>

			</td>
			</tr>
		</tbody>
		</table>

		<table class="hide-mobile" style="font-family:'Montserrat',sans-serif; justify-content: center; display: table-cell" role="presentation" cellpadding="0" cellspacing="0" width="80%" border="2">
		<div>
			<thead>
			<tr>
				<th>Restaurant Name</th>
				<th>Address</th>
				<th>Average Cost for two</th>
				<th>Aggregate rating</th>
			</tr>
			</thead>
			<tbody >
				--data--
			</tbody>
		</div>
		</table>

		<table style="font-family:'Montserrat',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
		<tbody>
			<tr>
			<td style="overflow-wrap:break-word;word-break:break-word;padding:20px;font-family:'Montserrat',sans-serif;" align="left">
				
		<table height="0px" align="center" border="0" cellpadding="0" cellspacing="0" width="1%" style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;border-top: 1px solid #fc5656;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
			<tbody>
			<tr style="vertical-align: top">
				<td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;font-size: 0px;line-height: 0px;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
				<span>&#160;</span>
				</td>
			</tr>
			</tbody>
		</table>

			</td>
			</tr>
		</tbody>
		</table>

		<!--[if (!mso)&(!IE)]><!--></div><!--<![endif]-->
		</div>
		</div>
		<!--[if (mso)|(IE)]></td><![endif]-->
			<!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->
			</div>
		</div>
		</div>



		<div class="u-row-container" style="padding: 0px;background-color: transparent">
		<div class="u-row" style="Margin: 0 auto;min-width: 320px;max-width: 550px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: #000000;">
			<div style="border-collapse: collapse;display: table;width: 100%;background-color: transparent;">
			<!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding: 0px;background-color: transparent;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:550px;"><tr style="background-color: #000000;"><![endif]-->
			
		<!--[if (mso)|(IE)]><td align="center" width="550" style="width: 550px;padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;" valign="top"><![endif]-->
		<div class="u-col u-col-100" style="max-width: 320px;min-width: 550px;display: table-cell;vertical-align: top;">
		<div style="width: 100% !important;">
		<!--[if (!mso)&(!IE)]><!--><div style="padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;"><!--<![endif]-->
		
		<table style="font-family:'Montserrat',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
		<tbody>
			<tr>
			<td style="overflow-wrap:break-word;word-break:break-word;padding:40px;font-family:'Montserrat',sans-serif;" align="left">
				
		<div style="color: #828388; line-height: 140%; text-align: left; word-wrap: break-word;">
			<p style="font-size: 14px; line-height: 140%; text-align: center;"><span style="font-size: 14px; line-height: 19.6px;">&copy;ChatBot </span></p>
		</div>

			</td>
			</tr>
		</tbody>
		</table>

		<!--[if (!mso)&(!IE)]><!--></div><!--<![endif]-->
		</div>
		</div>
		<!--[if (mso)|(IE)]></td><![endif]-->
			<!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->
			</div>
		</div>
		</div>


			<!--[if (mso)|(IE)]></td></tr></table><![endif]-->
			</td>
		</tr>
		</tbody>
		</table>
		<!--[if mso]></div><![endif]-->
		<!--[if IE]></div><![endif]-->
		</body>

		</html>
		"""
	html = html.replace("--data--", data)
	part2 = MIMEText(html, "html")
	message = message
	message.attach(part2)
	try:
		smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
		smtpObj.starttls()
		smtpObj.login(sender, "23071998")
		smtpObj.sendmail(sender, receivers, message.as_string())
		return "Successfully sent email"
	except SMTPException:
		return "Error: unable to send email"


class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'

	def run(self, dispatcher, tracker, domain):
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		price = tracker.get_slot('price')
		if price == 'high':
			price_max = sys.maxsize
			price_min = 700
		elif price == 'mid':
			price_max = 699
			price_min = 300
		else:
			price_max = 299
			price_min = 0

		results = RestaurantSearch(
			City=loc, Cuisine=cuisine, price_max=price_max, price_min=price_min)
		response = ""
		if results.shape[0] == 0:
			response = "no results"
		else:
			for restaurant in RestaurantSearch(loc, cuisine, price_max=price_max, price_min=price_min).iloc[:5].iterrows():
				restaurant = restaurant[1]
				response = response + \
					F"Found {restaurant['Restaurant Name']} in {restaurant['Address']} rated {restaurant['Address']} with avg cost {restaurant['Average Cost for two']} \n\n"

		dispatcher.utter_message("-----"+response)
		return [SlotSet('location', loc)]


class ActionSendMail(Action):
	def name(self):
		return 'action_send_email'

	def run(self, dispatcher, tracker, domain):
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		price = tracker.get_slot('price')
		MailID = tracker.get_slot('email')
		if price == 'high':
			price_max = sys.maxsize
			price_min = 700
		elif price == 'mid':
			price_max = 699
			price_min = 300
		else:
			price_max = 299
			price_min = 0

		results = RestaurantSearch(
			City=loc, Cuisine=cuisine, price_max=price_max, price_min=price_min)
		data = ""
		if results.shape[0] == 0:
			data = "no results"
		else:
			for restaurant in RestaurantSearch(loc, cuisine, price_max=price_max, price_min=price_min).iloc[:10].iterrows():
				restaurant = restaurant[1]
				# data=data + F"Found {restaurant['Restaurant Name']} in {restaurant['Address']} rated {restaurant['Address']} with avg cost {restaurant['Average Cost for two']} \n\n"
				data = data + F"<tr><td> {restaurant['Restaurant Name']} </td><td> {restaurant['Address']} </td><td> {restaurant['Average Cost for two']} </td><td> {restaurant['Aggregate rating']} </td></tr>"
		print(MailID)
		message = sendmail(MailID,data)
		dispatcher.utter_message(message)
		return [SlotSet('email', MailID)]
