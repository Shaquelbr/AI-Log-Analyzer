from analyzer.parser import parse_log

def test_parse_log_extracts_errors():
    log_text = """INFO normal
ERROR Something failed
Exception something bad happened
"""
    path = "test.log"
    with open(path, "w") as f:
        f.write(log_text)

    result = parse_log(path)
    assert len(result["raw"]) == 2
    assert "failed" in result["raw"][0].lower()