# FaviconScanner
The script takes a file containing a list of IPs/Domains in order to look for a MD5 hash that matches the provided hash of a given favicon.

This script can be used for tracking malicious websites such as phishing pages that immitates legitimate services, and for finding other apps or services as well.


# Usage:
python3 FaviScan.py -m [HTTP/HTTPS] -l [FILE_NAME] -c [HASH_TO_COMPARE]
