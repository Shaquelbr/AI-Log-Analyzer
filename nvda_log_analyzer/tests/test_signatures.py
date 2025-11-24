from analyzer.patterns.signatures import match_signatures

def test_match_signatures_disk_issue():
    lines = [
        "Finder: DRDeviceCopyDeviceForBSDName failed(disk4s1) failed"
    ]
    matches = match_signatures(lines)
    assert len(matches) == 1
    assert matches[0]["category"] == "disk_issue"