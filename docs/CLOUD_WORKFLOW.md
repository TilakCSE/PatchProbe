# Codex Cloud and phone workflow

This records the setup and verification steps. Local GitHub access is confirmed: this checkout can read `TilakCSE/PatchProbe`, and initial commits were pushed. Codex Cloud repository access is a separate connection and is **not yet verified**. On 2026-10-17, the user reported seeing only `Base Environment` on mobile.

## Create the PatchProbe cloud environment

Follow the [official Codex Cloud guide](https://learn.chatgpt.com/docs/cloud). Environment creation is available on ChatGPT web or desktop; the mobile Codex app can select an existing one.

1. On ChatGPT web or desktop, choose **Work in → Cloud → Select environment → Create environment**. On a phone, try ChatGPT in a browser; if the mobile layout lacks the control, use the browser's desktop-site mode or finish this step when a desktop is available.
2. Search for `TilakCSE/PatchProbe`. Connect GitHub if prompted, approve repository access in the account UI, select PatchProbe, and choose **Get started**.
3. Let the setup inspect the repository. Use Python 3.11+ and the project commands below; the committed processed data permits an offline smoke check.
4. Review the setup and test output, save changes, and choose **Publish**. Wait until it says **Environment published**. Then start a task in that environment.

Suggested setup checks from the repository root:

```sh
python -m pip install -e '.[dev]'
python -m pytest
```

The test command is the setup pass criterion. Training is a later step: `python scripts/train_model.py` deliberately stops until human labels exist. The Streamlit app command is `python -m streamlit run app.py`.

Cloud tasks have separate workspaces and can continue while the laptop is off once the environment is published. The owner must complete GitHub authorization and publication in their signed-in account. Do not paste account passwords or personal access tokens into the project or chat.

## Phone approvals for local work

The [official phone walkthrough](https://developers.openai.com/training/walkthroughs/working-on-your-phone) describes desktop Settings → Connections → Control this Mac or PC → Set up/Add, then scanning the QR code with a phone. Keep the laptop awake, online, and signed into the same account/workspace to approve or follow up on **local** tasks. Local work pauses if the laptop sleeps or disconnects.

Use the cloud environment for work that must continue while away from this laptop. Keep cloud and local branches separate until reviewed and merged.
