import click
from analyzer.parser import parse_log
from analyzer.patterns.signatures import match_signatures
from analyzer.ai_client import summarize_logs, analyze_with_nim


@click.group()
def main():
    """Root CLI command group"""
    pass


@main.command()
@click.argument("logfile", type=click.Path(exists=True))
def analyze(logfile):
    """Local log analysis with signature matching + summarization"""
    with open(logfile, "r") as f:
        raw = f.read()

    result = parse_log(logfile)
    raw_text = result["raw"]
    compressed = result["compressed"]

    matches = match_signatures(raw_text)

    if matches:
        out = {
            "likely_issue": "Known pattern detected",
            "details": matches
        }
    else:
        out = summarize_logs(compressed)

    print(out)


@main.command()
@click.argument("logfile", type=click.Path(exists=True))
def nim(logfile):
    """Cloud inference using NVIDIA NIM"""

    with open(logfile, "r") as f:
        raw = f.read()

    # parse_log should receive text, not the path
    parsed = parse_log(raw)

    # raw is already a string, no need to join
    combined = parsed["raw"]

    print("Sending to NVIDIA NIM cloud inference...")
    result = analyze_with_nim(combined)

    print("\nNIM Cloud Analysis Result:\n")
    print(result)