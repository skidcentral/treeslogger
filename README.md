###TREES LOGGER VERSION 1,0###

A simple Keylogger project written in Python3.
It requires two non-standard modules: colorama and pynput.

These can be installed by running:
sudo pip3 install -r requirements.txt

You will need to enable access to less secure apps on your gmail account.
To allow the mail to be forwarded over smtp.

    1.	Open your Google Admin console (admin.google.com).
    2.	Click Security > Basic settings.
    3.	Under Less secure apps, select Go to settings for less secure apps.
    4.	In the subwindow, select the Enforce access to less secure apps for all users radio button.
	(You can also use the Allow users to manage their access to less secure apps, but don't forget to turn on the less secure apps option in users settings then!)
    5.	Click the Save button.

Once the dependencies are installed and your Gmail has the right settings, you can run the keylogger.
You will be prompted for your gmail credentials, and the email you want to send your logs to.
A copy of the keylog session will also be saved in trees-logger/logs as well.

Hit Ctrl&C in the terminal running trees-logger to end it, and trigger sending the email copy.
Feedback on Functionality is appreciated.
