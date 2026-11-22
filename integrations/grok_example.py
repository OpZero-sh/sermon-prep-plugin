"""Ask Grok a question using this product's hosted tools, or preview the request locally."""
import argparse
import json
import os
from pathlib import Path
import sys
from urllib.error import HTTPError
from urllib.request import Request, urlopen

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("question")
    parser.add_argument("--dry-run", action="store_true", help="Print a credential-free preview without calling xAI")
    parser.add_argument("--model", default=os.environ.get("XAI_MODEL", "grok-4.7"))
    args = parser.parse_args()
    settings = json.loads(Path(__file__).with_name("grok-servers.json").read_text())
    tools = []
    missing = []
    for key, server in settings.items():
        entry = {"type": "mcp", "server_label": key.replace("-", "_"), "server_url": server["url"],
                 "allowed_tools": server["allowed_tools"]}
        variable = server.get("token_env")
        if variable:
            if args.dry_run:
                entry["headers"] = {"Authorization": "Bearer <user access token>"}
            elif os.environ.get(variable):
                entry["headers"] = {"Authorization": "Bearer " + os.environ[variable]}
            else:
                missing.append(variable)
                continue
        tools.append(entry)
    if missing:
        print("Connections needing a signed-in user's access token: " + ", ".join(missing), file=sys.stderr)
    if not tools:
        parser.exit(2, "No connected servers available for this request.\n")
    payload = {"model": args.model, "input": args.question, "tools": tools}
    if args.dry_run:
        print(json.dumps(payload, indent=2))
        return
    if not os.environ.get("XAI_API_KEY"):
        parser.exit(2, "Set XAI_API_KEY to run this example.\n")
    request = Request("https://api.x.ai/v1/responses", data=json.dumps(payload).encode(),
                      headers={"Content-Type": "application/json", "Authorization": "Bearer " + os.environ["XAI_API_KEY"]})
    try:
        with urlopen(request, timeout=120) as response:
            result = json.load(response)
    except HTTPError as exc:
        parser.exit(1, f"xAI returned HTTP {exc.code}. Check your model access and server authorization.\n")
    messages = [part["text"] for item in result.get("output", []) if item.get("type") == "message"
                for part in item.get("content", []) if part.get("type") == "output_text"]
    if not messages:
        parser.exit(1, f"No final text returned (response status: {result.get('status', 'unknown')}).\n")
    print("\n".join(messages))

if __name__ == "__main__":
    main()
