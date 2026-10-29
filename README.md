# fbzkr

Automates two Facebook Messenger tasks with a real browser session:

- **`main.py`** — picks a random zekr from `zeker.xlsx` and sends it to a fixed conversation.
- **`quran.py`** — fetches a random ayah from [alquran.cloud](https://alquran.cloud) and sends it with its tafsir.

Both are driven by GitHub Actions cron.

## How the session works

The scripts reuse a logged-in browser session instead of a hardcoded password.
`cookies.pkl` is **never committed** — it is restored at runtime from the
`FB_COOKIES_B64` repository secret (base64 of a pickle of Playwright/Selenium
cookies).

To refresh it, run `save_cookies.py` locally, log in manually, then:

```bash
base64 -w0 cookies.pkl | gh secret set FB_COOKIES_B64
```

Changing the Facebook password invalidates the stored session — re-run the step above.

## Schedule

| Workflow | Cron (UTC) |
|---|---|
| `Run Python Script` | every 2 hours |
| `Send Quran Verse` | 00:00, 08:00, 18:00 |

`Run Python Script` also commits a one-line `.heartbeat` on the 1st of each month.
Public repositories have scheduled workflows disabled after 60 days without
repository activity, and that commit is what keeps the schedule alive.

## Local run

```bash
pip install -r requirements.txt
python save_cookies.py   # log in once, writes cookies.pkl
python main.py
```

Requires Chrome/Chromium and `xvfb` on headless machines.
