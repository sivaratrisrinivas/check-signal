{
 "flags": [
  {
   "id": "npm16-04-skills-care",
   "meeting_id": "NPM16-04",
   "kind": "room_texture",
   "title": "Likely Person B thinks nobody cares about skills; Person D keeps them for automations",
   "face": "In the Every Agent product review, likely Person B offers a “hot take”: “I don't think anyone cares about skills. Outside of maybe us, right?” He also says he doesn't want the team to “fake like being focused.” Likely Person D answers that if skill usage rises while satisfaction, revenue and memberships don't change, “then that's a failure,” yet still wants skills as the route for better automations.",
   "context": "Person D walks Person B through the Agent roadmap, whose main focus is getting more workspaces to accept an automation; the proposal is to connect automations to skills. Person B is testing whether the work would really move the metric. Speakers are unlabelled; attribution follows the roster and turn-taking.",
   "moment": [
    {
     "line": 99,
     "speaker": "likely Person B",
     "quote": "maybe a hot take, I don't think anyone cares about skills. Outside of maybe us, right?"
    },
    {
     "line": 103,
     "speaker": "likely Person B",
     "quote": "I don't want us to fake like being focused."
    },
    {
     "line": 106,
     "speaker": "likely Person D",
     "quote": "If we ship a bunch of updates to Skills and then Skill usage goes up because we like, you know, orient around that. But. like overall satisfaction, revenue. Memberships? Don't change. then that's a failure."
    }
   ],
   "why": "The strategy leans on skills as how compounding gets put into practice, and the Agent's own leads are arguing about whether users want them at all. Reading, not sourced: the real dispute is whether skills are judged by usage or by revenue and memberships.",
   "strategy_quote": null,
   "reaction_inferred": null,
   "options": [],
   "people": [
    "Person B",
    "Person D"
   ],
   "confidence": 0.7
  },
  {
   "id": "gpm16-03-priming",
   "meeting_id": "GPM16-03",
   "kind": "worth_spreading",
   "title": "Telling the agent not to relay error jargon made it drop numbers everywhere",
   "face": "An open Plus One PR from Engineer A began with the agent pasting a provider's error, “the taste lens threw a JSON parse error on its own output,” at a user who didn't follow it. The PR reports the fix surprised its author: naming a word class as withholdable “primes the model to drop it everywhere.” A line promising not to override the numbers rule scored worst, 0 of 3.",
   "context": "PR #1755 (open, unmerged; the author says not to merge until a clean eval sweep is posted) makes the agent retry once when an external job returns success with a crashed stage, and translate provider errors for the reader. The measurements are the author's own, in a Claude Code-generated description.",
   "moment": [
    {
     "line": 14,
     "speaker": "Engineer A (PR description)",
     "quote": "the taste lens threw a JSON parse error on its own output"
    },
    {
     "line": 68,
     "speaker": "Engineer A (PR description)",
     "quote": "naming a word class as withholdable primes the model to drop it everywhere"
    },
    {
     "line": 75,
     "speaker": "Engineer A (PR description)",
     "quote": "Priming does not read disclaimers; a reassurance names the class as loudly as a ban."
    }
   ],
   "why": "This is a transferable lesson for any prompt or writing skill the team maintains: naming what to avoid can spread the avoided behavior, and reassurance made it worse. It rests on one author's eval runs and hasn't been replicated.",
   "strategy_quote": null,
   "reaction_inferred": null,
   "options": [],
   "people": [
    "Engineer A"
   ],
   "confidence": 0.65
  },
  {
   "id": "npm16-05-largest-install",
   "meeting_id": "NPM16-05",
   "kind": "room_texture",
   "title": "Probably the Agent's largest Slack install: a university IT director who starts private",
   "face": "Person M, an Every subscriber who directs IT for UC Davis's College of Engineering, onboarded the Agent on a call. He says his Slack has about 30,000 people, and the host told him it's “probably the largest Slack workspace that has installed it so far.” He wanted private channels first, connected only GitHub with nothing legally protected, and said he'd “take the heat if we had some big security incident.”",
   "context": "Onboarding session with an external beta user (Person M). He narrates setup as he goes and notes the channel picker showed only public channels. The 30,000 figure is his report, not a measure of Agent users.",
   "moment": [
    {
     "line": 84,
     "speaker": "Person M",
     "quote": "I would want to add it to private channels first. Um, We have about 30,000 people in the Slack workspace."
    },
    {
     "line": 95,
     "speaker": "host (Person D or Person B)",
     "quote": "Candidly, you're probably the largest Slack workspace that has installed it so far."
    },
    {
     "line": 104,
     "speaker": "Person M",
     "quote": "would take the heat if we had some big security incident"
    }
   ],
   "why": "A concrete look at how a cautious institutional admin sizes up the Agent: trust controls, not features, shaped his first session. A ghostwriter on the earlier onboarding call (NPM16-02 L68) also raised private channels; that is a separate observation, not a measured pattern.",
   "strategy_quote": null,
   "reaction_inferred": null,
   "options": [],
   "people": [
    "Person M",
    "Person D",
    "Person B"
   ],
   "confidence": 0.6
  },
  {
   "id": "spm16-02-reader-context",
   "meeting_id": "SPM16-02",
   "kind": "worth_spreading",
   "title": "Person Q's writing check: models skip the context a reader needs to follow the argument",
   "face": "Person Q spot-checked Polaris, Quasar and Wisp on Every's writing bench and found no compelling reason to use them yet: “I can recognize the ingredients of the argument, but the writing often leaves me to reconstruct how the ideas connect.” Separately, she flagged an email draft that gave readers four unexplained names, benchmark numbers with no baseline, and a payoff “only the author can decode.”",
   "context": "Person Q posted two writing tests in Slack on Sept 16: a spot check of three pre-release models on essay intros, X and LinkedIn posts and a promo email, and one email draft she passed along as an example of the model misjudging what readers need.",
   "moment": [
    {
     "line": 61,
     "speaker": "Person Q",
     "quote": "The recurring issue is coherence: I can recognize the ingredients of the argument, but the writing often leaves me to reconstruct how the ideas connect."
    },
    {
     "line": 74,
     "speaker": "Person Q",
     "quote": "It doesn't have great judgment on the context a reader needs to make information legible to them."
    },
    {
     "line": 78,
     "speaker": "Person Q",
     "quote": "the essay's whole payoff, compressed into a phrase only the author can decode"
    }
   ],
   "why": "Named, specific failures you can hold against any claim that the new models write well; she also notes extra-high effort didn't obviously improve the samples she read. It's her firsthand read, not a matched-effort evaluation.",
   "strategy_quote": null,
   "reaction_inferred": null,
   "options": [],
   "people": [
    "Person Q"
   ],
   "confidence": 0.6
  }
 ],
 "reading_notes": [
  {
   "meeting_id": "NPM16-01",
   "substance": "Launch-page design review: Person H walked the Figma sections (skills tabs, a compounding animation, pricing), the team cut the enterprise contact-us for now, and Person D gave a roadmap and billing-rollout update.",
   "selection_reason": "Not selected: the compounding-feels-like-homework reaction (unlabelled, likely Person I) overlaps earlier compounding-positioning and pricing cards, and its attribution is uncertain."
  },
  {
   "meeting_id": "NPM16-02",
   "substance": "Onboarding call with Person K, a solo ghostwriter: she read the setup as 'mostly for teams', asked whether the credit meant a paid tool, and liked the client-ops pitch as an alternative to hiring an assistant.",
   "selection_reason": "Not selected: good customer texture but no show-not-tell message was used, and the Person M call is the stronger customer voice."
  },
  {
   "meeting_id": "NPM16-03",
   "substance": "Person L and Person E planned the Sept 25 All Access office hours around the Agent, with Person E pitching the shared-agent story and Reader A's meeting-ping workflow as his best example.",
   "selection_reason": "Not selected: the pitch is teammate to teammate, not an outside reaction, and the Person U executive-feed idea is already covered by earlier cards."
  },
  {
   "meeting_id": "NPM16-04",
   "substance": "Agent product review covering activation funnel numbers, connecting automations to skills, and the billing and reinstall rollout, with Person B pressing on whether the focus would really move the metric.",
   "selection_reason": "Selected: the skills exchange shows a real disagreement over metric versus focus, with both positions quotable."
  },
  {
   "meeting_id": "NPM16-05",
   "substance": "Onboarding call with Person M, a university IT director with a roughly 30,000-person Slack, who tested cautiously and explained his internal versus legally protected data rule.",
   "selection_reason": "Selected: a first-hand institutional customer reaction, with the host calling it probably the largest install so far."
  },
  {
   "meeting_id": "SPM16-01",
   "substance": "Person N one-shot a golf game with a flyover, a ball camera and a pelican that steals the ball, and Person P called the model output slop with taste.",
   "selection_reason": "Not selected: vivid but model identity is unverified and there is no decision or lesson beyond a fun capability sample."
  },
  {
   "meeting_id": "SPM16-02",
   "substance": "Person Q reported two writing tests: a spot check of three pre-release models on the writing bench and an email draft that ignored what a reader needs, plus Grok failing her social-pitch format.",
   "selection_reason": "Selected: named, concrete writing failures with exact examples."
  },
  {
   "meeting_id": "SPM16-03",
   "substance": "Retention audit follow-up for the lawyers: Engineer A listed vendor retention facts and the gap with the privacy page's 14-business-day promise, and Person B settled on 90 days with the policy being reworked.",
   "selection_reason": "Not selected: it fits none of the five kinds, owners are already acting, and it needs a careful legal-adjacent framing; left for the ordinary lane."
  },
  {
   "meeting_id": "SPM16-04",
   "substance": "A brief dashboard and API outage after a large-workspace install; Person J later said his env-var update restarted the server, and the service recovered within minutes.",
   "selection_reason": "Not selected: routine incident already resolved, and the large-install cause was corrected."
  },
  {
   "meeting_id": "SPM16-05",
   "substance": "Slack Agent mode launched with a native stop control that was hard to find outside DMs.",
   "selection_reason": "Not selected: Reader A already reacted to the launch, so a recap adds nothing."
  },
  {
   "meeting_id": "SPM16-06",
   "substance": "Person S built a Checks benchmark from Reader A's task dump and walked Person T and Reader A through ownership transfer and a render bug.",
   "selection_reason": "Not selected: Reader A took part, and it is a handoff walkthrough with no new perspective."
  },
  {
   "meeting_id": "SPM16-07",
   "substance": "Person T described benchmarks as replaying past attempts, Reader A offered an SAT versus reference-check framing, Person U joked 'it's math', and Reader A asked for audience-relative checks.",
   "selection_reason": "Not selected: mostly Reader A's own framing; Person T's red-flag and green-flag extension is real but thin."
  },
  {
   "meeting_id": "SPM16-08",
   "substance": "Person X corrected the tax-history import: only main Every history is in Kintsugi, app accounts still await exports, and the no-backfill guidance stands.",
   "selection_reason": "Not selected: operational status correction with no decision for Reader A."
  },
  {
   "meeting_id": "SPM16-09",
   "substance": "Planning for the Sept 25 All Access office hours and an Oct 9 camp after the Oct 6 launch, with Person I wanting product makers present for the top tier.",
   "selection_reason": "Not selected: a maker and event plan with no customer reaction, and the basic idea is already carded."
  },
  {
   "meeting_id": "SPM16-10",
   "substance": "Person N and Person H settled on sharp corners for both buttons and cards and asked for a staging environment for design iteration.",
   "selection_reason": "Not selected: small, already-settled design choice."
  },
  {
   "meeting_id": "SPM16-11",
   "substance": "Person G asked whether the Rebuilding Compound Engineering story holds for Monday; Person Q said it needs more time and Person G asked one week or two, unanswered.",
   "selection_reason": "Not selected: an editorial scheduling call for its owners, not something left open for Reader A to break."
  },
  {
   "meeting_id": "SPM16-12",
   "substance": "Reader A noticed a model using goals for simple tasks, and Person F found pausing a goal while task agents keep working confusing.",
   "selection_reason": "Not selected: Reader A took part and the confusion is about another tool's UX."
  },
  {
   "meeting_id": "SPM16-13",
   "substance": "Person I said the sponsor opt-in is live for the afterparty and that he is waiting on sponsor names before launching the next setup.",
   "selection_reason": "Not selected: narrow status update with an ambiguous referent."
  },
  {
   "meeting_id": "SPM16-14",
   "substance": "Person T said Person AG at a16z wants to test the Agent and asked how to enroll him; no reply was captured.",
   "selection_reason": "Not selected: an early external opportunity with no committed experiment or outcome."
  },
  {
   "meeting_id": "SPM16-15",
   "substance": "Person D replied that department-agent onboarding could default to job titles from Slack profiles with an optional installer choice.",
   "selection_reason": "Not selected: modest design reply to an idea already surfaced this morning."
  },
  {
   "meeting_id": "GPM16-01",
   "substance": "Person S closed Person T's PR importing Reader A's 65 candidate checks and merged a PR letting a new account create its benchmark through its own AI.",
   "selection_reason": "Not selected: Reader A is a direct participant in the benchmark, and it is internal product progress."
  },
  {
   "meeting_id": "GPM16-02",
   "substance": "Person D's PR making replies answer-only with caveats in a footer reports that worked examples moved footer use from 0 of 15 to 5 of 5 where five described rules did not; Engineer A approved it.",
   "selection_reason": "Not selected: a close second to GPM16-03 and less surprising; it is also an open PR reporting the author's own runs."
  },
  {
   "meeting_id": "GPM16-03",
   "substance": "Engineer A's open PR makes the agent retry a degraded external job once and translate provider jargon, and its writeup reports that naming a word class primed the model to drop it everywhere.",
   "selection_reason": "Selected: a surprising, transferable prompt lesson with exact quotable lines."
  },
  {
   "meeting_id": "GPM16-04",
   "substance": "Person P's merged PR reshapes the external-agent profile to eight fields and separates an agent's claims from observed behavior; two of three interviewed agents never answered.",
   "selection_reason": "Not selected: the claim-versus-evidence principle is crisp but this is an internal build detail and the batch cap was reached."
  },
  {
   "meeting_id": "GPM16-05",
   "substance": "Person P's merged PR adds external AI employees to the Agent's roster with a handoff that waits on another Slack bot and resumes the same turn.",
   "selection_reason": "Not selected: internal engineering progress with no decision needing Reader A."
  }
 ],
 "notes": "Read all 25 units in full. Four cards selected. NPM units have no speaker labels, so attribution follows the manifest's roster and turn-taking evidence and is marked likely where uncertain; Slack and GitHub authors are verified accounts. Every quotation was machine-checked as a contiguous span of the cited original line. Cross-source pointers appear only in why fields (NPM16-02 L68 on private channels) and are separate observations, not shared-cause claims. GPM16-03 figures are the PR author's own runs on an open, unmerged PR. SPM16-03 (privacy-page retention gap) is deliberately left for the ordinary lane. No message_tested flag: no outside reaction to the show-not-tell message appeared. Strategy addendum text was not in the packet; the reader-prompt paraphrase was used."
}
