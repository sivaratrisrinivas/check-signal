{
  "flags": [
    {
      "id": "sep16-writing-connections",
      "meeting_id": "SPM16-02",
      "kind": "worth_spreading",
      "title": "Person Q says the models supply an argument's ingredients but leave you to connect them",
      "face": "In your team's tests of Polaris, Quasar and Wisp, Person Q wrote: “I can recognize the ingredients of the argument, but the writing often leaves me to reconstruct how the ideas connect.” Her separate email-draft critique gave concrete examples: four names with no explanation of whether they were agents or people, and benchmark percentages with no baseline. She wants the model to supply the context its reader needs.",
      "context": "Person Q shared writing spot checks across essay introductions, social posts and promotional email, then illustrated missing reader context with a separate email draft. These are reported judgments, not a controlled comparison; screenshots were not inspected. [Primary Slack discussion](https://sources.example.invalid/reference-032).",
      "moment": [
        {
          "line": 61,
          "speaker": "Person Q",
          "quote": "The recurring issue is coherence: I can recognize the ingredients of the argument, but the writing often leaves me to reconstruct how the ideas connect."
        },
        {
          "line": 76,
          "speaker": "Person Q",
          "quote": "1. Claudie, Andy, Viktor, Fin — four names with no hint they're agents, systems, or people."
        },
        {
          "line": 77,
          "speaker": "Person Q",
          "quote": "2. The benchmark numbers — 44, 85, 80 percent, and \"62\" all land without a baseline or a \"up from what.\""
        }
      ],
      "why": "You get a concrete account of writing that contains the right material but still makes its reader reconstruct the argument and context.",
      "people": [
        "Person Q"
      ],
      "options": [],
      "strategy_quote": null,
      "reaction_inferred": null,
      "confidence": 0.91
    },
    {
      "id": "sep16-count-ban-timings",
      "meeting_id": "GPM16-03",
      "kind": "worth_spreading",
      "title": "Engineer A reports that banning provider counts erased timings in unrelated replies",
      "face": "Engineer A's open retry-fix PR reports that banning a provider's internal counts also made unrelated replies drop timings such as 250ms, 120ms and 8s. Adding “never overrides the numbers rule above” scored worst: 0/3 versus 3/3 on main. You can see the attempted remedy—ban specific debugging strings instead—but the final version's clean eval sweep was still pending.",
      "context": "EveryInc/plus-one #1755 documents a retry fix and a collateral regression found while translating provider diagnostics. These small eval results are author-account reports; the afternoon commit changes the retry gate, and neither merge nor a clean final sweep is established. [Primary PR and patch](https://sources.example.invalid/reference-050); [afternoon commit](https://sources.example.invalid/reference-045).",
      "moment": [
        {
          "line": 70,
          "speaker": "Engineer A (PR author account)",
          "quote": "every grader reported the same failure: the planted timings (250ms, 120ms, 8s) dissolved into qualitative phrases **in replies where nothing had failed and no tool had been called**."
        },
        {
          "line": 75,
          "speaker": "Engineer A (PR author account)",
          "quote": "the clause literally said it *never overrides the numbers rule above*. This scored **worst (0/3)**."
        },
        {
          "line": 78,
          "speaker": "Engineer A (PR author account)",
          "quote": "Every mention of counts, tallies, candidates, attempts, figures and numbers is now deleted from the addition, in both directions."
        }
      ],
      "why": "You get a specific reported case of a clarity instruction degrading unrelated answers, with failed remedies and a still-unproven final revision rather than a universal claim about prompting.",
      "people": [
        "Engineer A"
      ],
      "options": [],
      "strategy_quote": null,
      "reaction_inferred": null,
      "confidence": 0.86
    },
    {
      "id": "sep16-compounding-looks-like-work",
      "meeting_id": "NPM16-01",
      "kind": "room_texture",
      "title": "Likely Person I says the compounding diagram makes the Agent look like extra work",
      "face": "In the Agent launch-page review, likely Person I objected to the compounding diagram: “It makes me feel like I have to do all of these things.” His experience was teaching the Agent something it could reuse. Likely Person D clarified that users shouldn't run compound engineering on every request. You get a telling reaction to the illustration: showing the learning loop can make it look like the customer's workload.",
      "context": "The launch standup was reviewing website design and had just discussed which skills to highlight. Person I's attribution rests on the immediate direct address in L114; Person D's follows his earlier product-owner handoff, so both remain tentative and the workload implication is a reading of their exchange. [Primary transcript](https://sources.example.invalid/reference-004).",
      "moment": [
        {
          "line": 113,
          "speaker": "likely Person I",
          "quote": "The point is essentially I teach the agent something So it knows it and uses that in the future?"
        },
        {
          "line": 117,
          "speaker": "likely Person D",
          "quote": "We want people not to repeat themselves. The agent learns how you work. So that next time you ask it to do something, it does it the right way."
        },
        {
          "line": 117,
          "speaker": "likely Person D",
          "quote": "And so the compounding happens automatically, but it's not literally compound engineering every time working in the agent."
        }
      ],
      "why": "You get the gap between a teammate's experience of teaching the Agent once and a diagram that made him feel responsible for every step.",
      "people": [
        "Person I",
        "Person D"
      ],
      "options": [],
      "strategy_quote": null,
      "reaction_inferred": null,
      "confidence": 0.85
    },
    {
      "id": "sep16-bot-claims-observations",
      "meeting_id": "GPM16-04",
      "kind": "worth_spreading",
      "title": "Person P's bot roster separates claimed abilities from observed handoffs",
      "face": "In Person P's merged Baby Agent profile change, you would see an outside bot's own account alongside a separate record of its observed handoffs: “An agent's self-description is a claim, not evidence.” Claudie had answered the interview; Andy and Bill had not, so their planned imports remain placeholders. The roster can distinguish a bot saying it has access from a handoff that actually worked.",
      "context": "EveryInc/baby-agent #204 aligns external-bot profiles with Person P's interview skill and separates claimed fields from observed behavior in prompts, tool output and the admin interface. The PR is merged, but deployment and production imports remain subsequent steps; attribution is to the author account. [Primary PR and patch](https://sources.example.invalid/reference-038).",
      "moment": [
        {
          "line": 161,
          "speaker": "Person P (PR author account)",
          "quote": "An agent's self-description is a claim, not evidence."
        },
        {
          "line": 16,
          "speaker": "Person P (PR author account)",
          "quote": "The three prod import blocks (Claudie; Andy and Bill as placeholders — they never answered) were parsed on this tree: 7 / 1 / 1 fields, no skipped headings."
        }
      ],
      "why": "You get a concrete design for preserving the difference between what another agent says it can do and what its handoffs have actually demonstrated.",
      "people": [
        "Person P"
      ],
      "options": [],
      "strategy_quote": null,
      "reaction_inferred": null,
      "confidence": 0.79
    }
  ],
  "reading_notes": [
    {
      "meeting_id": "NPM16-01",
      "substance": "The launch standup reviewed website skills, compounding illustrations, permission examples, pricing and launch preparation.",
      "selection_reason": "Selected the concrete reaction that the compounding diagram looked like work; other choices resolved or remained routine launch plans."
    },
    {
      "meeting_id": "NPM16-02",
      "substance": "Ghostwriter Person K installed the Agent and accepted a call-prep suggestion while discussing client context and administrative work.",
      "selection_reason": "No trial outcome is observed, and no external reaction to the tracked show-not-tell message is captured."
    },
    {
      "meeting_id": "NPM16-03",
      "substance": "Person L and Person E planned nontechnical Office Hours and exchanged examples of Agent use and tools they were building.",
      "selection_reason": "The internal pitch and event plan repeat familiar themes; the tool-building anecdotes were less self-contained than the selected moments."
    },
    {
      "meeting_id": "NPM16-04",
      "substance": "Person B and Person D examined automation activation, the uncertain causal value of skills, roadmap sequencing and engineering kickoff requirements.",
      "selection_reason": "The causal challenge goes beyond the prior activation number, but no unresolved CEO tiebreaker emerged and the selected lessons were sharper."
    },
    {
      "meeting_id": "NPM16-05",
      "substance": "UC Davis IT director Person M wanted private-channel testing in a reported 30,000-person Slack workspace before a peer-channel trial.",
      "selection_reason": "The concrete customer caution was considered, but the small-trial reaction was less distinctive than the selected moments."
    },
    {
      "meeting_id": "SPM16-01",
      "substance": "Person N shared one-prompt games with inventive details and enthusiastic reactions from Person O and Person P.",
      "selection_reason": "The creative details were considered for room texture, but the selected exchanges offered more substance without relying on uninspected videos."
    },
    {
      "meeting_id": "SPM16-02",
      "substance": "Person Q reported writing samples missing connective logic and reader context, alongside unsuccessful social-pitch experiments.",
      "selection_reason": "Selected her coherence critique and concrete missing-context examples without turning spot checks into a model ranking."
    },
    {
      "meeting_id": "SPM16-03",
      "substance": "The retention thread identified provider and deletion-policy gaps, then Person B settled on 90 days while the privacy policy was being reworked.",
      "selection_reason": "The 14-versus-90-day split resolved; owners were responding, so no missing-owner security card or tiebreaker qualified."
    },
    {
      "meeting_id": "SPM16-04",
      "substance": "A dashboard outage was first attributed to a large install, then Person J identified an environment-variable restart while Person D continued investigating timeouts.",
      "selection_reason": "The later qualification prevents a settled install-caused-outage claim; the incident was owned and had recovered."
    },
    {
      "meeting_id": "SPM16-05",
      "substance": "Person J announced Slack agent mode and clarified that the stop button appears in the agent-panel DM while channels accept typed stop.",
      "selection_reason": "You reacted in the thread, and the later clarification resolves the confusion without adding a distinctive reading moment."
    },
    {
      "meeting_id": "SPM16-06",
      "substance": "Person S created your benchmark, explained MCP creation and ownership, and Person T took the rendering issue.",
      "selection_reason": "You directly participated, and the implementation follow-up adds little beyond the exchange you had."
    },
    {
      "meeting_id": "SPM16-07",
      "substance": "Person T described evals as replaying past attempts, followed by your reference-check framing and request for audience-relative checks.",
      "selection_reason": "Your contributions establish familiarity; colleagues' replies did not add enough beyond those framings for another card."
    },
    {
      "meeting_id": "SPM16-08",
      "substance": "The tax integration thread clarified ownership and corrected the claim that app history had already been imported into Kintsugi.",
      "selection_reason": "The correction leaves the same central-import route in place and yields no qualifying reading moment."
    },
    {
      "meeting_id": "SPM16-09",
      "substance": "The All Access preview gained Person I's request for product makers to attend and Person B's September 25 availability.",
      "selection_reason": "The maker-access rationale is a modest addition to an already surfaced preview plan, with no open decision needing you."
    },
    {
      "meeting_id": "SPM16-10",
      "substance": "Person N and Person H discussed evaluating buttons in product context and agreed on sharp corners for both cards and buttons.",
      "selection_reason": "The choice resolved, and the context-first observation was less distinctive than the selected material."
    },
    {
      "meeting_id": "SPM16-11",
      "substance": "Person Q said the Rebuilding Compound Engineering story needed more time because of Vibe Check load and changes since its pitch.",
      "selection_reason": "One or two weeks remained unanswered, but this is editorial scheduling rather than a substantive tiebreaker."
    },
    {
      "meeting_id": "SPM16-12",
      "substance": "Person F found Quasar's paused goals confusing because task agents could continue working, alongside your comments about simple tasks.",
      "selection_reason": "This UX reaction was in an exchange you were already discussing and remains separate from Every's stop-button behavior."
    },
    {
      "meeting_id": "SPM16-13",
      "substance": "Person I said sponsor opt-in was live for the afterparty and another setup was waiting on sponsor names from Person U.",
      "selection_reason": "The dependency has a named route and is routine event coordination, with no supported broader privacy conclusion."
    },
    {
      "meeting_id": "SPM16-14",
      "substance": "Person T reported Person AG's interest in testing the Agent and asked how to enroll him.",
      "selection_reason": "There is no direct external reaction, resolved enrollment or committed experiment to surface."
    },
    {
      "meeting_id": "SPM16-15",
      "substance": "Person D responded to department onboarding with proposed default job-title routing and an optional installer choice.",
      "selection_reason": "The response advances an internal product proposal without a distinctive qualifying exchange or decision for you."
    },
    {
      "meeting_id": "GPM16-01",
      "substance": "Person S closed the codebase benchmark import in favor of MCP database creation and merged a new-account Connect your AI flow.",
      "selection_reason": "The choice is settled and overlaps your live benchmark-setup discussion, so it was not selected as a tiebreaker or recap."
    },
    {
      "meeting_id": "GPM16-02",
      "substance": "Person D's open answer-only reply PR reports worked-example and per-turn-context experiments and received an afternoon approval.",
      "selection_reason": "The experiments are useful, but the fresh event is approval of September 14–15 work; the distinct current retry experiment was selected instead."
    },
    {
      "meeting_id": "GPM16-03",
      "substance": "Engineer A's open retry PR reports collateral number-dropping from a diagnostic-count ban and an afternoon commit correcting the retry gate.",
      "selection_reason": "Selected the surprising reported prompt experiment while preserving small samples and the pending final sweep."
    },
    {
      "meeting_id": "GPM16-04",
      "substance": "Person P merged external-agent profile alignment that visibly separates interview claims from observed handoff behavior.",
      "selection_reason": "Selected the quotable distinction with concrete unanswered-bot placeholders and no production-deployment claim."
    },
    {
      "meeting_id": "GPM16-05",
      "substance": "Person P merged external-bot handoffs that wait and resume the same turn, including a fix preserving replies across roster changes.",
      "selection_reason": "The mechanism supports the selected profile design; a separate implementation card would duplicate that bot-coordination topic."
    }
  ],
  "notes": "Read all 25 supplied primary source units, including later qualifications and selected complete patches. Notion transcripts lack stable speaker labels and contain garbled spans; tentative attribution uses local addresses, handoffs and supplied identity evidence. Slack authors are identified. GitHub attribution identifies author accounts, not verified human authorship or replicated measurements; generated summaries were not evidence, and #1755 discloses Claude-generated content. Original L-locators and supplied URLs are preserved. No attendance, novelty, current-strategy, deployment or action authorization is inferred. Four distinct drafts were selected after comparing the supplied prior-card list; no message_tested or off_strategy flag qualified. No other reader output was inspected."
}
