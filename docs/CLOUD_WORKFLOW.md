# Codex Cloud and phone workflow

This records setup steps; it does not claim an environment has already been connected.

## Codex Cloud
Official guide: https://learn.chatgpt.com/docs/cloud

1. In ChatGPT on web or mobile, open Codex Cloud and create an environment.
2. Connect GitHub when prompted. Authorize TilakCSE/PatchProbe and select that repository.
3. Let Codex inspect the repository and prepare tools. Review install/test output, save the environment, and select Publish.
4. Start a cloud task from the published environment. Cloud tasks have separate workspaces and can continue while this laptop is off.
5. Review the result on the phone. Commit or open a pull request when ready.

The owner must complete GitHub authorization and environment publication in their signed-in account. No personal access token or account password belongs in this repository or chat.

## Phone approvals for local work
Official guide: https://developers.openai.com/training/walkthroughs/working-on-your-phone

In the ChatGPT desktop app, use Settings → Connections → Control this Mac or PC → Set up or Add. Scan the QR code with the phone and select this computer. Keep the laptop awake, online, and signed in to the same account and workspace. Mobile Remote can show approvals, reviews, and follow-up prompts. Local work stops when the laptop sleeps or disconnects.

## Recommendation
Use Codex Cloud for work that should continue while away. Pair Remote as a second option when local Windows files or tools are needed. Keep cloud and local branches separate until reviewed.
