# Connector map: Mettle Support desk plugin

Built from the plugin's `CONNECTORS.md` and `tools-inventory.md`.

| Placeholder | Mettle & Co tool | In the plugin's `.mcp.json` | Organisation status | What it shows on the Connectors tab | Who acts | Fallback until then |
|---|---|---|---|---|---|---|
| `~~support platform` | Zendesk | No | Not added for the organisation | Not listed, because the plugin doesn't bundle it | An Owner adds it in Organization settings > Connectors, then each person connects their own account | Monday CSV export |
| `~~knowledge base` | Notion | Yes | Added for the organisation | Not connected until each person signs in, then Connected | Each member connects their own account | FAQ file attached to the project |
| `~~chat` | Slack | Yes | Added for the organisation | Not connected until each person signs in, then Connected | Each member connects their own account | Copy the commitments into Slack by hand |

## Not in this plugin

- Booking and dispatch service: no connector exists. Building one is custom work, so log it as a use case rather than solve it in the session.
- Salesforce: added for Sales only. Support doesn't need it for these three workflows.

## Before rollout

1. An Owner adds the Zendesk connector for the organisation, so Customer Support can connect it.
2. Check that the weekly triage still runs from the CSV export, in case the ticketing tool changes when its contract renews.
