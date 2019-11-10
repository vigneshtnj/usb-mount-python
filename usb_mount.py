import time
import commands

# ASSUMED THAT THIS COMMAND HAS ALREADY BEEN RUN
# sudo mkdir /mnt/usb_stick

MOUNT_DIR = "/media/pi/"

def run_command(command):
    # start = time.time()
    ret_code, output = commands.getstatusoutput(command)
    if ret_code == 1:
        raise Exception("FAILED: %s" % command)
    # end = time.time()
    # print "Finished in %s seconds" % (end - start)
    return output.splitlines() 


def uuid_from_line(line):
    for x in line:
	if x[-4:-2] == "sd":
		return x[-4:] 
    return False

output = run_command("ls -l /dev/disk/by-uuid/")

if uuid_from_line(output) != False:
    print("drive found!")
    command = "sudo mount /dev/"+(uuid_from_line(output)+" "+MOUNT_DIR)
    run_command(command)
else:
	print("no drive found")


