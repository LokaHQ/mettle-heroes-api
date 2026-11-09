# Company plugin library

The organisation's Claude plugins. Claude syncs this repository into Organization settings > Plugins & skills, so a merged pull request is how a plugin is published or updated.

## Set it up (once, by a Claude Owner)

1. Create a private (or internal) repository and copy this folder's contents to its root.
2. Edit `.github/CODEOWNERS` with your reviewers. In the repository's branch rules for `main`, require a pull request, one approval, and review from Code Owners.
3. In Claude: Organization settings > Plugins & skills > Add > Sync from GitHub. Connect GitHub if asked. If the repository isn't listed, select Install the Claude GitHub App and give it access. Leave Sync automatically on, choose the default access, and select Create.
4. On the Inventory tab, set each plugin's default access: Not available, Available to install, Installed by default or Required. On Enterprise, use Group access for per-group settings.

## Change a plugin

1. Branch, edit the plugin under `plugins/`, and raise `version` in its `.claude-plugin/plugin.json`.
2. Open a pull request. The check runs `claude plugin validate`, and a code owner reviews.
3. Merge. Claude syncs on the push to `main`.

To add a plugin, put its folder under `plugins/` and add an entry to `.claude-plugin/marketplace.json`.

## Rules

- A plugin's `name` is permanent once published.
- No top-level `bin/` folder in a plugin: sync rejects it.
- No keys or passwords in any file.
- Something broke: set the plugin to Not available, revert the pull request, and let it re-sync. Synced plugins can't be reverted in Claude's settings. Never use Delete source: it removes every plugin in this library for everyone.
