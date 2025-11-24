import re

SIGNATURES = { 
    "disk_issue": {
        "patterns": [
            re.compile(r".*DRDeviceCopyDeviceForBSDName.*failed.*", re.IGNORECASE),
            re.compile(r".*I/O error.*", re.IGNORECASE),
            re.compile(r".*read only file system.*", re.IGNORECASE)
        ],
        "explanation": "This appears to be a disk or device lookup failure. It usually occurs when a disk cannot be mounted or accessed."
    },
    "network_issue": {
        "patterns": [
            re.compile(r".*connection timed out.*", re.IGNORECASE),
            re.compile(r".*failed to establish connection.*", re.IGNORECASE)
        ],
        "explanation": "This indicates a network connection failure or unstable network conditions."
    },
    "permission_denied": {
        "patterns": [
            re.compile(r".*permission denied.*", re.IGNORECASE),
            re.compile(r".*access denited.*", re.IGNORECASE)

        ],
        "explanation": "This indicates a permission or access rights problem."
    }   
}

def match_signatures(lines):
    matches = []

    for line in lines:
        for key, entry in SIGNATURES.items():
            for pattern in entry["patterns"]:
                if pattern.search(line):
                    matches.append({
                        "category": key,
                        "line": line,
                        "explanation": entry["explanation"]

                    })

    return matches

