import requests
import hashlib
import optparse
from urllib3.exceptions import InsecureRequestWarning

# Command line arguments
parser = optparse.OptionParser()
parser.add_option('-l', '--list', dest="list_file", help='File containing the list of target IPs/Domains')
parser.add_option('-c', '--compare', dest='origin_hash', help='Origin hash to compare with')
parser.add_option('-p', '--protocol', dest='protocol', help='Send http or https requests')
(options, arguments) = parser.parse_args()

list_file = options.list_file
origin_hash = options.origin_hash
protocol = options.protocol

matching_hosts = []

# Comapring the new hashes to the origin hash
def compare_hash(file, target_url):
    target_hash = hashlib.md5(file).hexdigest()
    if target_hash == origin_hash:
        matching_hosts.append(target_url)
    else:
        pass

# Sending HTTP/HTTPS requests for getting favicon hash
def get_favi_hash(target):
    try:
        requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
        file_hash = requests.get(target, verify=False, timeout=4).content
        if file_hash:
            compare_hash(file_hash, target)
        else:
            pass
    except:
        print('\n[X] Could not send requests to target:', target)

# Extracting each IP/Domain from provided list
def get_favicon(list_file):
    try:
        with open(list_file, 'r') as target_list:
            for line in target_list:
                target = line.strip()
                target_url = protocol + "://" + target + "/favicon.ico"
                get_favi_hash(target_url)
    except:
        print('\n[X] Could not open mentioned file')
        print('[!] Please verify the list file location and try again')

get_favicon(list_file)

# Check if there found results and finish the script
if len(matching_hosts) == 0:
    print('\n[!] No matching favicons were found')
else:
    print('\n[RESULTS] Match List:')
    for host in matching_hosts:
        print('\t[+] Matching Host:', host)
    print('\n[+] Done')
