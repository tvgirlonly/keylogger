⚠️ WARNING:
Keyloggers are illegal to use without explicit consent and violate GitHub's Acceptable Use Policy if deployed maliciously. This README is provided strictly for educational purposes to demonstrate cybersecurity concepts. Do not use this code on systems you do not own.

Educational Keylogger Demonstration 🔒
Disclaimer: This project is for learning purposes only. Use it only on your own devices with full consent. Misuse may result in legal consequences.

Purpose
This project demonstrates:

How keyloggers capture keyboard input

Why process monitoring is critical for cybersecurity

Methods attackers use to steal sensitive data

Intended for:

Cybersecurity students learning defense mechanisms


Features

Logs keystrokes to a local file (keystrokes.log)

Timestamps each recorded event

Handles special keys (e.g., [Shift], [Ctrl])

Terminates with ESC key (for educational safety)

Prerequisites
Python 3.6+

pynput library

Installation
Install dependencies:
pip install pynput

Usage ⚠️
Run in a controlled environment (e.g., virtual machine):

bash
Copy
python keylogger.py
To stop:

Press the ESC key

Logs will be saved to:

bash
Copy
keystrokes.log
Legal Disclaimer
