{
  "flags": [
    {
      "kind": "worth_spreading",
      "title": "Engineer A found that banning internal counts made the Agent drop other numbers",
      "context": "While fixing how the Agent explains a degraded external job, Engineer A tested four prompt wordings against an unrelated lesson-writing eval. Naming counts or tallies as things to hide caused ordinary timing figures to disappear too.",
      "moment": [
        {
          "line": 75,
          "speaker": "Engineer A",
          "quote": "This scored **worst (0/3)**. Priming does not read disclaimers; a reassurance names the class as loudly as a ban."
        },
        {
          "line": 78,
          "speaker": "Engineer A",
          "quote": "So the variable is the **word class**, not the placement or the phrasing."
        }
      ],
      "why": "You get a measured prompt-review heuristic: ban the opaque artifact, not a broad category the Agent still needs elsewhere.",
      "strategy_quote": null,
      "reaction_inferred": null,
      "options": [],
      "people": [
        "Engineer A"
      ],
      "confidence": 0.86,
      "id": "reading-20260916-codex-g03-word-class-priming",
      "meeting_id": "GPM16-03",
      "face": "Engineer A tried four ways to stop provider diagnostics from leaking into replies. Naming counts or tallies as withholdable pushed unrelated timing details out too: main scored 3/3; variants scored 1/3, 0/3, and 1/3. Even “never overrides the numbers rule” did worst. The PR’s takeaway: ban opaque artifacts such as stage names, not a broad class like numbers."
    },
    {
      "kind": "worth_spreading",
      "title": "Person Q found argument ingredients without the connective logic",
      "context": "Person Q spot-checked Polaris, Quasar, and Wisp on essay introductions and social formats using Every's writing bench, then tested social-idea generation. Across both passes, she found material from the source but not a legible path for the reader.",
      "moment": [
        {
          "line": 61,
          "speaker": "Person Q",
          "quote": "The recurring issue is coherence: I can recognize the ingredients of the argument, but the writing often leaves me to reconstruct how the ideas connect."
        },
        {
          "line": 23,
          "speaker": "Person Q",
          "quote": "the pitches are all very navel-gazey - buried in my own context, not extracting what a reader can learn from or apply"
        }
      ],
      "why": "You get a sharper diagnosis than “bad prose”: the models found material but failed to build the reader’s route through it.",
      "strategy_quote": null,
      "reaction_inferred": null,
      "options": [],
      "people": [
        "Person Q"
      ],
      "confidence": 0.82,
      "id": "reading-20260916-codex-s02-connective-logic",
      "meeting_id": "SPM16-02",
      "face": "Testing Polaris, Quasar, and Wisp on Every’s writing bench, Person Q could recognize the argument’s ingredients but had to reconstruct how they connected. Her social-idea follow-up found the same failure: pitches stayed inside her context instead of extracting what a reader could learn or apply. The useful diagnosis is not “bad prose”; the models found material but failed to build the reader’s path through it."
    },
    {
      "kind": "room_texture",
      "title": "UC Davis’s IT lead wanted private-first testing in a 30,000-person Slack",
      "context": "During an Every Agent onboarding call, Person M, the executive director of IT for UC Davis Engineering, installed the beta in the university's large Slack workspace. He was willing to test, but immediately looked for a contained starting point.",
      "moment": [
        {
          "line": 84,
          "speaker": "Person M",
          "quote": "I would want to add it to private channels first. Um, We have about 30,000 people in the Slack workspace."
        },
        {
          "line": 94,
          "speaker": "Person M",
          "quote": "We're a public institution and we get a lot of, we're kind of risk averse. But I am in a position of taking on risk for my college and this is an appropriate risk for now."
        },
        {
          "line": 115,
          "speaker": "Person M",
          "quote": "I will invite it to a channel with a few of my peers and we'll play around and then grow it from there."
        }
      ],
      "why": "You see an external IT operator’s preferred adoption sequence: accept the experiment, contain visibility, then widen from a trusted peer group.",
      "strategy_quote": null,
      "reaction_inferred": null,
      "options": [],
      "people": [
        "Person M",
        "Person B",
        "Person D"
      ],
      "confidence": 0.77,
      "id": "reading-20260916-codex-n05-private-first",
      "meeting_id": "NPM16-05",
      "face": "While installing the Agent, Person M—UC Davis Engineering’s IT director—rejected a public-channel-first path: “I would want to add it to private channels first. We have about 30,000 people in the Slack workspace.” He still accepted the experiment as an appropriate risk, but planned to start with a few peers. The reaction suggests a concrete enterprise adoption shape: bounded visibility before broad context."
    },
    {
      "kind": "worth_spreading",
      "title": "Person P separates what another agent claims from how it actually performs",
      "context": "Person P's merged external-agent profile change gives another Slack bot separate fields for its interview answers and its observed behavior after handoffs. The product keeps the two visible as different kinds of evidence.",
      "moment": [
        {
          "line": 161,
          "speaker": "Person P",
          "quote": "An agent's self-description is a claim, not evidence."
        }
      ],
      "why": "You get a clean trust primitive for multi-agent systems: preserve what an agent says about itself without mistaking that for a track record.",
      "strategy_quote": null,
      "reaction_inferred": null,
      "options": [],
      "people": [
        "Person P"
      ],
      "confidence": 0.73,
      "id": "reading-20260916-codex-g04-claims-vs-observation",
      "meeting_id": "GPM16-04",
      "face": "Person P’s merged external-agent profiles separate interview claims from actual handoffs: “An agent’s self-description is a claim, not evidence.” A workspace admin adds another Slack bot on the Employees page, records its routing profile, then asks @Every in a shared channel to hand it a brief. After the bot replies, failures or quirks update only Observed behavior, preventing its promises from silently becoming its reputation."
    }
  ],
  "reading_notes": [
    {
      "meeting_id": "NPM16-01",
      "substance": "The launch team reviewed the Agent landing page's personas, skills, compounding animation, permissions example, pricing presentation, and remaining launch assets.",
      "selection_reason": "Not selected: most choices were resolved or delegated, and the remaining pricing work was routine launch execution rather than an open strategic tiebreaker."
    },
    {
      "meeting_id": "NPM16-02",
      "substance": "Ghostwriter Person K installed the Agent, accepted a call-prep automation, and explored client-operations work that might replace some virtual-assistant overhead.",
      "selection_reason": "Not selected: the interest was concrete but exploratory, with no observed automation outcome or test of the current company-level Agent message."
    },
    {
      "meeting_id": "NPM16-03",
      "substance": "Person L and Person E planned an All Access Agent office hour and traded examples for explaining nontechnical knowledge work and shared Slack visibility.",
      "selection_reason": "Not selected: it mostly rehearsed the current Agent story internally, without the external reaction required for message_tested."
    },
    {
      "meeting_id": "NPM16-04",
      "substance": "Person B and Person D challenged the Agent roadmap's causal link between better automation suggestions, activation, skills, and eventual membership conversion.",
      "selection_reason": "Not selected: the automation-activation baseline was already carded, while the fresh causal questions remain unresolved and did not yet produce a distinct finding."
    },
    {
      "meeting_id": "NPM16-05",
      "substance": "UC Davis Engineering IT leader Person M installed the Agent in a roughly 30,000-person Slack and described a private-first, peer-group rollout shaped by institutional risk.",
      "selection_reason": "Selected for the unusually concrete texture of a large-workspace operator choosing bounded adoption while still accepting the experiment."
    },
    {
      "meeting_id": "SPM16-01",
      "substance": "Person N shared one-shot Claude game builds whose unprompted camera work, course variety, and absurd details impressed Person O and Person P.",
      "selection_reason": "Not selected: the strongest evidence lived in uninspected videos, and the text reactions did not establish a durable claim beyond delight."
    },
    {
      "meeting_id": "SPM16-02",
      "substance": "Person Q's writing-bench and social-idea tests found coherence, information hierarchy, instruction-following, and reader-context failures across several new models.",
      "selection_reason": "Selected for the precise, reusable distinction between finding argument ingredients and building connective logic for a reader."
    },
    {
      "meeting_id": "SPM16-03",
      "substance": "A privacy-policy review exposed category-specific retention schedules, missing subprocessors, disabled deletion automation, and browser profiles without a deletion path.",
      "selection_reason": "Not selected: severity was concrete, but named owners were already changing settings and ticketing containment rather than leaving ownership missing."
    },
    {
      "meeting_id": "SPM16-04",
      "substance": "The Agent dashboard briefly went down during an environment-variable restart; an initial theory blaming a 30,000-member install was corrected, though that install also showed timeouts.",
      "selection_reason": "Not selected: the outage recovered and the thread explicitly undercut the tempting shared-cause inference."
    },
    {
      "meeting_id": "SPM16-05",
      "substance": "Slack Agent mode added a native panel, persistent transcript, suggested prompts, and a DM-only stop button, with typed stop remaining necessary in channels.",
      "selection_reason": "Not selected: Reader A reacted in the thread, and this was familiar internal product progress rather than an added perspective."
    },
    {
      "meeting_id": "SPM16-06",
      "substance": "Person S created Reader A's benchmark, Person T explained the MCP ownership flow, and Person T opened a fix when Reader A found the site render broken.",
      "selection_reason": "Not selected: Reader A directly participated and the remaining material was implementation follow-through he had just requested."
    },
    {
      "meeting_id": "SPM16-07",
      "substance": "The team compared evals to replaying past attempts and to reference checks, then Reader A requested checks conditioned on an explicit audience brief.",
      "selection_reason": "Not selected: the framing was useful but familiar to Reader A from his active participation, and stronger measured eval findings were available elsewhere."
    },
    {
      "meeting_id": "SPM16-08",
      "substance": "Studio-product tax integration moved toward Kintsugi, with a correction that only main Every history—not app-account history—had yet been imported centrally.",
      "selection_reason": "Not selected: the corrected route remained an operational implementation detail with no decision for Reader A."
    },
    {
      "meeting_id": "SPM16-09",
      "substance": "The team kept a prelaunch All Access Agent preview and sought product makers for it, while planning a postlaunch group-agent camp.",
      "selection_reason": "Not selected: staffing and event positioning were largely settled, and no external audience reaction had occurred."
    },
    {
      "meeting_id": "SPM16-10",
      "substance": "Person H asked to judge buttons in product context and ultimately chose sharp corners for both buttons and cards rather than mixing treatments.",
      "selection_reason": "Not selected: the design disagreement resolved inside the thread and did not leave a meaningful choice for Reader A."
    },
    {
      "meeting_id": "SPM16-11",
      "substance": "Person Q said the Rebuilding Compound Engineering story needed more time, while Person G's question of a one- or two-week delay remained unanswered.",
      "selection_reason": "Not selected: the open choice was routine scheduling, explicitly below the tiebreaker bar."
    },
    {
      "meeting_id": "SPM16-12",
      "substance": "Person F said pausing a Quasar goal is confusing because task agents may keep working, and Reader A connected that mismatch to longer-running agents.",
      "selection_reason": "Not selected: Reader A was already in the exchange and the card would mainly recap the observation he had just made."
    },
    {
      "meeting_id": "SPM16-13",
      "substance": "Person I said sponsor opt-in was live for the afterparty but the next setup awaited sponsor names and could not use a blanket opt-in.",
      "selection_reason": "Not selected: this was a narrow operational dependency without a new route or decision for Reader A."
    },
    {
      "meeting_id": "SPM16-14",
      "substance": "Person T reported that Person AG at a16z wanted to test the Agent and asked how to enroll him in beta.",
      "selection_reason": "Not selected: the interest was secondhand, with no captured reply, enrollment, or committed experiment."
    },
    {
      "meeting_id": "SPM16-15",
      "substance": "Person D proposed that workspace onboarding infer department contacts from Slack job titles while letting the installer override the choices.",
      "selection_reason": "Not selected: it remained an early onboarding proposal without a committed test or demonstrated outcome."
    },
    {
      "meeting_id": "GPM16-01",
      "substance": "Checks rejected a codebase import for Reader A's benchmark and instead merged a flow where a new account's AI creates and owns a benchmark through MCP.",
      "selection_reason": "Not selected: Reader A was already exercising the adjacent workflow, and the item was primarily internal product implementation."
    },
    {
      "meeting_id": "GPM16-02",
      "substance": "Person D's reply-shape experiment found five descriptive prompt edits inert, while a worked example moved footer use from 0/15 to 5/5 and recency shortened replies further.",
      "selection_reason": "Not selected: it was high-signal, but overlapped with the deeper prompt-behavior experiment selected from GPM16-03 in a four-card batch."
    },
    {
      "meeting_id": "GPM16-03",
      "substance": "Engineer A added a degraded-job retry branch and documented how broad prohibitions, branch order, and unsafe retry shapes produced unrelated regressions.",
      "selection_reason": "Selected for the measured finding that naming a broad class as withholdable altered unrelated replies even when scope and disclaimers said otherwise."
    },
    {
      "meeting_id": "GPM16-04",
      "substance": "Person P merged external-agent profiles that preserve routing claims separately from observed behavior after real handoffs.",
      "selection_reason": "Selected for the crisp trust rule and its concrete shipped workflow: another agent's self-description is not its track record."
    },
    {
      "meeting_id": "GPM16-05",
      "substance": "Person P merged Slack-to-Slack agent handoffs that park the current turn, wait for another bot's thread reply, and resume that same turn.",
      "selection_reason": "Not selected: the architecture was substantial but overlapped with the selected external-agent profile and was less legible as a five-second card."
    }
  ],
  "notes": "All 25 complete source units were read. Slack authors and GitHub accounts are labelled; Notion transcripts are unlabelled, so Person M is attributed from the meeting title, direct address, self-identification, and turn continuity. GitHub measurements are author-reported and were not independently rerun; merged code is not proof of production deployment. No generated summaries, linked screenshots, videos, or other readers' outputs were used."
}
