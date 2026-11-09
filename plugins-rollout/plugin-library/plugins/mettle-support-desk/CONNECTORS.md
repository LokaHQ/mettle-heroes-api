# Connectors

The skills in this plugin name tool categories with a `~~` placeholder instead of a product, so the plugin works with whichever tool the team uses in that category.

Installing the plugin doesn't connect anything. Each connector shows on the plugin's Connectors tab as Connected, Not connected or Not added. On Team and Enterprise plans, an Owner adds a connector for the organisation first. Then each person connects their own account.

## Categories this plugin uses

| Category | Placeholder | Mettle & Co uses | Included in `.mcp.json` | Other options |
|---|---|---|---|---|
| Support platform | `~~support platform` | Zendesk | No. An Owner has to add it for the organisation first | Intercom, Freshdesk, HubSpot Service Hub |
| Chat | `~~chat` | Slack | Yes | Microsoft Teams |
| Knowledge base | `~~knowledge base` | Notion | Yes | Confluence, Guru |

## When nothing is connected

Every skill also works on files. Attach or drop in:

- the week's ticket export as a CSV (`~~support platform` export)
- the FAQ as a Markdown or Word file (`~~knowledge base` page)
- a call transcript or notes

The skills say which source they used, so a reader knows whether the figures came from the live tool or an export.
