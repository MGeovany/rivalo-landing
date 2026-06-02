# Rivalo Landing

Minimal FastHTML marketing and policy site for Rivalo.

## Routes

- `/` — marketing page
- `/support` — Apple support URL
- `/privacy` — privacy policy URL
- `/terms` — terms of use

## Local Dev

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn api.index:app --reload
```
