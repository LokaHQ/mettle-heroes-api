# Provisioning request: Support desk plugin

Built from `rollout-brief.md` and `tools-inventory.md`.

To the Claude Owner in Engineering, from Chloe Dubois, plugin owner.

## What to publish

Mettle Support desk (`mettle-support-desk`), version 1.0.0. Weekly ticket triage, reply drafting and call follow-up. Tested on December's tickets. It holds no keys or passwords. The connectors it includes are Slack and Notion.

## Who gets it

| Group | Level | Why |
|---|---|---|
| Customer Support | Installed by default | Nobody on the team should have to install anything. People can still switch it off and tell Chloe why |
| Everyone else | Not available | Client names and call notes stay inside Customer Support |

Not Required: the first version needs room for the team to say what doesn't work.

## Connectors

| Tool | What the Owner does | Until then |
|---|---|---|
| Zendesk | Add the Zendesk connector in Organization settings > Connectors | The weekly triage runs from the Monday CSV export |
| Slack, Notion | Nothing. Already added for the organisation | Each person signs in from the plugin's Connectors tab |
| Booking and dispatch service | Nothing for launch. It needs a custom connector | Not used by the plugin |

The Zendesk contract renews on 31 December. If Support changes tool, the plugin still works: only the tool behind `~~support platform` changes.

## Versions

- Chloe owns what's in the plugin. Every change raises `version` in `plugin.json` and goes up as a new version, so it can be compared with the current one and reverted.
- First quarterly curation review three months after launch.

## Until it's published

Chloe has shared the plugin with the two daily Claude users on Ravi Chandran's shift. They run the weekly triage next Monday and report what's wrong or missing.
