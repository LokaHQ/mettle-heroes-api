# Review checklist: before you approve a submitted skill

For whoever reviews skills submitted for organisation publication (an owner, or anyone with Libraries set to "Can manage"). Go through this before clicking Approve.

1. **Description**: does it say both what the skill does and when Claude should use it? A description that only says what it does will under-trigger or over-trigger.
2. **Tested**: has the person who built it tried two prompts that should trigger the skill, one that shouldn't, and one borderline case? Ask to see the results if it isn't obvious from the request.
3. **Matches an example**: does the skill's own example output match what it's meant to produce, in structure and tone?
4. **Nothing sensitive hard-coded**: check every file for client names, numbers or internal shorthand that shouldn't go out to the whole organisation as a default, versus what belongs in the data the skill reads each time.
5. **Scan result**: on Enterprise, check the security scan result. Pass installs normally; Risk needs the submitter to explain the flagged behaviour before you approve; Malicious is blocked and can't be approved.
6. **Not a duplicate**: check the inventory for a similar skill already published. If two or three teams have built close versions of the same thing, promote the best one instead of approving another.
7. **How it's offered**: confirm or change the submitter's proposed offering (available to install, installed by default, not available, or required) and who it's offered to (everyone or specific groups).
8. **Owner and review date**: before you approve, make sure the submission names an owner and add a row to `skills-register.template.csv` with a review date 60 days out. A skill with no owner is the first one to go stale.

If anything on this list is missing, use "Request changes" with a short note instead of approving.
