import sys

print("Chat logger started. It will now search for a file called 'latest.log', and open 'output.log'")

log=open("latest.log", "r")
output=open("output.log", "w")
print("Opened files")

while True:
    logline=log.readline()
    if (logline.find('[main/INFO]: [CHAT]') != -1 or logline.find("[main/INFO] (Minecraft) [CHAT]") != -1):
        print(logline+"Chat line found! Converting...")
        output.write(logline)
    elif (logline.find("[main/INFO]: Stopping!") != -1 or logline.find("[main/INFO] (Minecraft) Stopping!") != -1):
        print(logline+"Line denotes end of process, stopping!")
        log.close
        output.close
        exit()
    else:
        print(logline+"No actions were taken")
