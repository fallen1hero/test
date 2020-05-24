print ("Updater")
ver = urllib.request.urlopen("https://raw.githubusercontent.com/fallen1hero/test/master/.version").read().decode('utf-8')
verl = ""
try:
	verl = open(".version", 'r').read()
except Exception:
	pass
if ver != verl:
	print("Update Verfügbar")
else:
	print("Aktuellste Version")
