# UBuildOS LinkedIn Public Campaign Post Standard v1.1.0

CLASSIFICATION: OWNER PRIVATE / PROTECTED
STATUS: OWNER-APPROVED / BYTE-LOCKED
DATE: 2026-09-25
SCOPE: UBuildOS 30-Day LinkedIn public-build campaign posts and successor campaign posts unless the owner explicitly authorizes an exception.
CALIBRATION SOURCE: Owner-provided Day 1 post, identified by the owner as the strongest benchmark.

## 1. Permanent naming rule

Do not add the trademark symbol (`™`) to any new title, product name, feature, artifact, campaign phrase, or public-facing label unless the owner has explicitly established that exact trademarked form.

Rules:
- Preserve an existing owner-established trademark exactly when supplied.
- Never infer trademark status from capitalization, importance, product status, naming style, or prior use of `™` on a different name.
- New names default to plain text.
- Do not retroactively rewrite historical artifacts solely to remove an already-published mark; preserve history and correct successors.

## 2. Canonical post objective

A campaign post must do more than announce a product. It must make the release inspectable and place the individual build inside the larger 30-day proof.

Canonical narrative spine:

HOOK -> WHY THIS BOUNDED BUILD -> NARROW PROBLEM -> WHAT WAS BUILT -> CAMPAIGN MEANING -> WHAT IT PROVES -> WHAT IT DOES NOT PROVE -> LIVE REVIEW FINDING -> FORWARD MOTION -> CTA -> DAY SIGNATURE

The exact wording changes by day. The spine does not.

## 3. Required opening / hook

Default first-line construction:

`Day X of building in public: <specific contrast, decision, or lesson>.`

The opening must:
- state a real tension, choice, problem, or counterintuitive point;
- sound human and specific;
- earn the next line;
- avoid generic launch language;
- avoid opening with QA status, internal process, or administrative completion.

The second line may be a short contrast such as:
`That was the point.`

Do not use empty clickbait, fake urgency, or broad praise.

## 4. Narrow-problem block

Every daily post must identify one bounded operational problem and, when natural, one narrow question the build answers.

Preferred pattern:

`So I built <Product Name> around one deliberately narrow question:`

`"<one concrete question>"`

The question must describe the actual product job, not a marketing abstraction.

## 5. Product explanation

Explain the product in plain language.

Include only the minimum useful mechanics:
- what goes in;
- what comes out;
- what the user can see/do;
- the explicit logic/state/reasoning if that is part of the proof.

Use short negative-claim lines when they materially clarify the boundary, for example:
- No black-box recommendation.
- No hidden scoring.
- No real customer data.
- No fake AI magic.

Do not invent these lines when they are not true or relevant.

## 6. Intent / why simplicity is deliberate

When the build is intentionally small or bounded, say so.

Preferred pattern:

`The simplicity is intentional.`

Then explain why the day's proof matters beyond the demo itself.

This is a core Day 1 lesson and should remain available as a recurring campaign device, but it should not be mechanically repeated when it does not fit the build.

## 7. Campaign-meaning block

Each post should connect the day's product to the wider campaign when material.

Preferred framing:

`Because Day X is not really about proving I can build <small demo description>.`

`It is about proving the full path:`

Then show the relevant end-to-end path in simple public language.

Default public path language may use:
`problem -> working product -> visible reasoning/state -> testing -> independent QA -> freeze -> public evidence -> live review`

Do not expose protected internal governance details, hashes, prompts, or private control mechanics.

## 8. Mandatory proof section

Heading:

`What Day X proves`

Use concise bullets containing only supported, externally meaningful facts.

Typical eligible proof classes:
- synthetic-input count or bounded test case count;
- visible reasoning or explicit workflow/state;
- deterministic behavior where actually proven;
- runtime dependency boundary;
- Fresh Independent QA: PASS when true;
- frozen/public package availability when true;
- live public surface when true;
- a presentation/publication repair that preserved frozen product bytes when true;
- security/history checks when materially relevant.

Do not put SHA-256 hashes, internal package IDs, or dense governance language in the main post.

## 9. Mandatory non-claims section

Heading:

`What it does NOT prove`

This section is required unless the day's subject genuinely has no material public overclaim risk.

Use 3-5 concise bullets identifying important boundaries, such as:
- revenue lift;
- conversion improvement;
- production-scale readiness;
- universal optimality;
- suitability for confidential/regulated data;
- generalized results beyond the demonstrated scope.

Never convert a target, hypothesis, demo result, modeled metric, or bounded proof into a broader claim.

## 10. Live-review finding

Every post should include one honest finding from live review when available.

Preferred pattern:

`And the live review mattered.`

Then state:
- what worked;
- what was exposed as the next improvement;
- what remains deliberately visible instead of being polished out of the story.

Do not manufacture a defect or improvement merely to satisfy the template. If live review produced no material new finding, say so briefly or omit this block with evidence.

## 11. Forward-motion block

Use a short forward-looking paragraph when it adds value.

Eligible content:
- how the next days increase difficulty;
- how evidence expectations rise;
- planned versus surprise releases;
- one relevant next-step theme.

Do not repeat the full 30-day campaign description every day.

## 12. CTA standard

Default CTA family:

`Inspect the product. Challenge the reasoning.`

For workflow/state products, allowed adaptation:

`Inspect the product. Challenge the workflow.`

For other products, the second noun may change only when it precisely matches the proof subject.

CTA requirements:
- one primary CTA;
- live/public evidence link immediately follows;
- repository/evidence link may follow when useful;
- no engagement-bait questions;
- no vague `Thoughts?`, `What do you think?`, or `Would you use this?` by default.

## 13. Day signature

Required closing form:

`Day X/30.`

Follow with a three-line summary modeled on Day 1:

`One <bounded thing>.`
`One <inspectable proof>.`
`One verified release.`

The first two nouns may change to match the day's product and proof.

A final short campaign-progress line may follow when earned, e.g.:
`The floor is now set.`
`The standard is getting harder.`

Do not reuse the same final line mechanically every day.

## 14. Hashtag baseline

Default campaign hashtag block, inherited from the Day 1 benchmark:

`#BuildInPublic #AI #ArtificialIntelligence #ProductDevelopment #SoftwareEngineering #Automation #AIAgents #SaaS #Startup #Founder #UBuildOS`

Use this exact baseline unless:
- LinkedIn/platform behavior materially changes;
- a later campaign-specific standard explicitly supersedes it; or
- the owner directs a different hashtag set.

Do not add unrelated trending hashtags.

## 15. Main-post exclusions

Do NOT put the following in the main LinkedIn copy unless they are specifically necessary to the public story:
- SHA-256 hashes;
- internal lifecycle state names such as `TERMINAL_VERIFIED_DONE`;
- internal handoff/checkpoint IDs;
- detailed governance or controller mechanics;
- dense QA replay details;
- private/protected evidence;
- unpublished credentials, paths, prompts, or internal system details;
- unsupported performance claims;
- fake AI hype;
- generic corporate launch language;
- invented trademark symbols;
- multiple competing CTAs;
- excessive disclaimers that belong in the repo/docs/carousel.

## 16. Carousel relationship

The LinkedIn post and carousel must not duplicate each other mechanically.

POST role:
HOOK + WHY + NARROW PROBLEM + CAMPAIGN MEANING + PROOF/NON-CLAIMS + LIVE FINDING + CTA

CAROUSEL role:
PROBLEM -> MODEL/WORKFLOW -> HOW IT WORKS -> PROOF -> LIMITATION/BOUNDARY -> LIVE CTA

The carousel should explain visually what the post frames narratively.

Carousel/PDF is part of the campaign distribution package when planned for that day. Its product-closure status must remain separately classified by the governing project plan.

## 17. Day 4 application

Day 4 must follow this standard using the product name exactly as owner-established/currently approved, with no newly invented trademark mark.

Canonical Day 4 hook direction:

`Day 4 of building in public: follow-up problems are usually not about remembering the lead.`

`They are about losing the state.`

Canonical narrow question:

`"What state is every follow-up in — and what needs attention now?"`

Canonical CTA:

`Inspect the product. Challenge the workflow.`

Day 4 must include:
- explicit NEW -> WAITING -> DUE -> WON / LOST state model;
- concise local-only behavior description;
- `What Day 4 proves`;
- `What it does NOT prove`;
- the live-review lesson that shipping the product is not the same as finishing the public release;
- live URL;
- public repository link;
- `Day 4/30.` signature;
- the standard hashtag baseline.

## 19. Human-first marketing / retention rule

This rule is mandatory for every future UBuildOS public campaign post and campaign-facing derivative unless the owner explicitly authorizes an exception.

### Primary communication objective

`READER_RETENTION_WITHOUT_MESSAGE_LOSS`

The first few seconds must give a real person a reason to keep reading. Optimize for immediate comprehension and relevance without stripping out the substance, proof, limitations, or larger UBuildOS story.

Default communication mode:
- ELI5;
- Minimal Reading;
- plain language;
- real-world use cases;
- concrete people, jobs, tasks, consequences, and problems.

Use additional detail only when the subject genuinely requires it. Minimal Reading means remove friction and unnecessary words; it does not mean reduce or weaken the message.

### First-seconds hook

The opening must quickly answer at least one of:
- Why should I care?
- Have I had this problem?
- What goes wrong today?
- What becomes easier or safer?
- What surprising thing is being tested?

Prefer a concrete human situation over an abstract product statement.

Example pattern:
`A salesperson has 20 people to follow up with. Five look urgent. Which one actually comes first — and why?`

Avoid opening with:
- architecture;
- governance;
- QA terminology;
- product taxonomy;
- technical implementation;
- abstract AI capability;
- campaign administration.

### Real-world use-case requirement

Every post must anchor the day's build in at least one believable real-world use case when the product has a human/business use case.

Preferred construction:
`PERSON + REAL JOB/TASK + REAL PROBLEM + CONSEQUENCE + HOW THE BUILD HELPS`

Examples of eligible framing:
- a salesperson deciding who to call first;
- a recruiter keeping candidate follow-ups from disappearing;
- a small-business owner seeing which customer follow-up is overdue;
- a project lead seeing which commitment is waiting, due, won, lost, blocked, or otherwise requires action;
- an operator turning scattered notes into one visible next-action queue.

Use examples only when they accurately fit the product. Do not fabricate customer adoption, outcomes, testimonials, revenue, savings, or production usage.

### Jargon prohibition

Public campaign copy must use ordinary language first.

Do not use technical/internal terms when a normal phrase communicates the same idea. Internal evidence may support the public statement without appearing in the public wording.

Examples:
- prefer `tested independently` over internal lifecycle terminology when the distinction is not needed;
- prefer `works the same way from the same inputs` over `deterministic` when explaining the concept to a general reader;
- prefer `can be rebuilt/recovered if something breaks` over recovery architecture terminology;
- prefer `a clear record of what was tested and released` over ledger/governance terminology.

Exact technical terms remain allowed when:
- the term itself is material to the proof;
- replacing it would make the statement inaccurate;
- the audience needs the term;
- it appears in a compact proof/evidence section after the human explanation.

### UBuildOS story through a human lens

The mandatory UBuildOS Story Brief from v1.1.0 must also be understandable through real work.

Do not merely say UBuildOS surrounds code with process.

Explain the practical consequence:
- the requested problem should be understood before building;
- the finished product should match what was requested;
- important behavior should be visible and testable;
- mistakes should be caught rather than hidden;
- failures should be recoverable;
- public claims should match the evidence;
- the release should have a clear completion record.

For intentionally simple builds, make the distinction explicit:
`The screen may be simple. The test is whether the whole path from problem to verified release can be repeated without losing the requirements, evidence, or truth along the way.`

### Complexity / moat claim discipline

Do not defend a simple build by pretending its code is difficult.

When a build could be coded quickly, say so when useful. The campaign proof is not raw coding difficulty.

The public thesis being tested is the repeatable quality of the complete path:
`UNDERSTAND -> BUILD -> SHOW THE REASONING/STATE -> TEST -> INDEPENDENTLY CHECK -> RECOVER -> PUBLISH -> REVIEW -> RECORD COMPLETION`

Do not call this a `moat`, competitive advantage, superior system, or other commercial superiority claim unless separately supported by evidence and authorized for public use.

### Post construction priority

Future posts should be composed in this order:

`HUMAN HOOK -> REAL-WORLD EXAMPLE -> PROBLEM/CONSEQUENCE -> DAY'S BUILD -> SIMPLE EXPLANATION -> UBUILDOS STORY/WHY -> PROOF -> NON-CLAIMS -> LIVE FINDING -> CTA -> DAY SIGNATURE`

This is additive to the existing narrative spine. Where the two overlap, the human-first construction governs presentation while all existing proof, non-claim, naming, evidence, CTA, and closeout rules remain mandatory.

### Retention editing test

Before a campaign post is release-ready, perform this readback:

1. Can a nontechnical reader understand the first three lines without knowing UBuildOS?
2. Is there a recognizable person/job/problem early enough to create relevance?
3. Does the reader understand what the product actually does without technical knowledge?
4. Does the post explain why a simple build matters to the larger UBuildOS experiment?
5. Has jargon been removed or translated wherever possible?
6. Is the message still complete rather than oversimplified?
7. Are proof and non-claims preserved?
8. Does each paragraph earn the next paragraph?
9. Is there one clear CTA?
10. Would removing another sentence lose useful meaning? If not, tighten it.

A post does not pass campaign copy review when it is technically accurate but difficult, abstract, repetitive, jargon-heavy, or slow to reveal why a real person should care.

### Carousel and derivative rule

The same human-first standard applies to:
- carousel/PDF copy;
- document titles;
- captions;
- public README opening summaries when campaign-facing;
- launch snippets and campaign distribution derivatives.

Lead with the human problem. Explain the mechanism simply. Put deeper evidence after comprehension, not before it.


## 21. Permanent Daily Post Structure — Day 4 Calibrated Baseline

This section is the mandatory daily-post structure for Day 5 and every later planned campaign day unless the owner explicitly authorizes a successor.

Calibration source:
- owner-approved Day 4 rewrite produced after the v1.2.0 Human-First Marketing / Retention Rule;
- owner assessment: `perfect`;
- this structure supersedes looser prior day-specific composition patterns while preserving all existing proof, non-claim, naming, CTA, human-first, and evidence rules.

### Canonical sequence

Every daily LinkedIn campaign post must follow this order:

1. `DAY X OF BUILDING IN PUBLIC + HUMAN HOOK`
2. `REAL PERSON / REAL JOB / REAL PROBLEM`
3. `PLAIN-LANGUAGE CONSEQUENCE`
4. `ONE NARROW QUESTION`
5. `WHAT THE BUILD DOES`
6. `SHORT NEGATIVE BOUNDARIES` when useful
7. `THE BUILD IS INTENTIONALLY BOUNDED / SIMPLE` when true
8. `THAT IS NOT THE CLAIM`
9. `THE BIGGER UBUILDOS EXPERIMENT`
10. `WHAT DAY X PROVES`
11. `WHAT IT DOES NOT PROVE`
12. `HONEST LIVE-REVIEW LESSON`
13. `WHAT CARRIES FORWARD`
14. `ONE CTA`
15. `LIVE BUILD`
16. `PUBLIC REPOSITORY / EVIDENCE LINK` when available
17. `DAY X/30`
18. `THREE-LINE DAY SIGNATURE`
19. `ONE SHORT FORWARD-PROGRESSION LINE`
20. `CAMPAIGN HASHTAG BASELINE`

The post must feel like one story, not a checklist. Headings are allowed only where they improve scanability, especially `What Day X proves` and `What it does NOT prove`.

### Length / retention requirement

The Day 4 calibrated length is the default maximum target.

Rules:
- Keep the complete message.
- Remove repetition before removing meaning.
- Prefer short sentences and short paragraphs.
- Do not expand merely to demonstrate rigor.
- Do not compress proof, limitations, or the UBuildOS story below the point of understanding.
- If a post exceeds the practical LinkedIn character limit, tighten wording first; do not remove the human hook, UBuildOS story, proof, non-claims, or CTA.
- Minimal Reading means `minimum sufficient words`, not `minimum substance`.

### Human hook pattern

Default opening:
`Day X of building in public: <real person or role> has <real situation/problem>.`

Then:
- show 2–4 recognizable states/examples;
- state the actual problem in one short sentence;
- make the reader understand the problem before naming the build.

Preferred example style:
`A salesperson has 20 people to follow up with.`
`Some are waiting.`
`Some are due today.`
`Some are already won or lost.`
`The problem isn't remembering names.`
`It's knowing what needs attention now.`

Do not mechanically reuse the salesperson example. Use the real role/problem appropriate to that day's build.

### Narrow-question requirement

Every post should reduce the day's build to one understandable question when possible.

Pattern:
`So I built <Product Name> around one simple question:`
`"<question a real user would actually ask>"`

The question must be comprehensible without technical background.

### Product explanation rule

Explain the product as a person would experience it:
- what they see;
- what they can do;
- what problem becomes easier to manage.

Prefer:
`Move a follow-up when its status changes.`
`See overdue work.`
`Keep a note with it.`
`Export the board when needed.`

Avoid:
- implementation architecture;
- framework names;
- system internals;
- dense technical descriptions.

### Boundary lines

Use brief negative lines when they help the reader understand what is intentionally absent:
`No account.`
`No analytics.`
`No cloud database.`
`No real customer data.`

Only include lines that are factually true for that release.

### Simple-build / larger-test bridge

When the build is intentionally easy to reproduce, the post must say so plainly rather than hiding it.

Required concept:
`A capable developer could recreate parts of this quickly. That isn't the claim.`

Then explain the larger UBuildOS experiment in normal language.

Public meaning to preserve:
- understand the problem correctly;
- build the intended thing;
- make important behavior visible;
- test it;
- independently check it;
- recover when something breaks;
- make public claims match the evidence;
- keep an exact record of what was released.

Preferred framing:
`The screen may be simple. The test is the whole path around it.`

Do not call this a moat, superiority, or competitive advantage without separate evidence and public-claim authorization.

### Proof section

Heading:
`What Day X proves`

Requirements:
- concise bullets;
- externally understandable;
- evidence-supported;
- plain language first;
- use exact technical labels only when materially useful, such as `Fresh Independent QA: PASS`.

### Non-claims section

Heading:
`What it does NOT prove`

Requirements:
- 3–5 important boundaries;
- prevent overreading the demo;
- do not bury this in legalistic wording.

### Live-review lesson

Each post should surface the most useful honest lesson discovered during live review.

Pattern:
`The live review exposed another lesson:`
`<one simple lesson>`

Then explain what changes going forward.

Do not invent a flaw merely to satisfy the structure.

### CTA

Default:
`Inspect the product. Challenge the <reasoning/workflow/result>.`

One CTA only.

Then:
`Live build:`
`<verified URL>`

Then, when available:
`Public repository:`
`<verified URL>`

### Day signature

Required:
`Day X/30.`

Then three short lines:
`One <real problem>.`
`One <bounded/inspectable proof>.`
`One verified release.`

Then one forward line, specific to current campaign progress.

Example:
`The builds get harder from here. The standard doesn't get easier.`

Do not mechanically reuse the exact forward line every day.

### Exact Day 4 calibration example

The following is the approved structural calibration source. Future posts should preserve its pacing and information density without copying its product-specific wording:

`Day 4 of building in public: a salesperson has 20 people to follow up with.`

`Some are waiting.`
`Some are due today.`
`Some are already won or lost.`

`The problem isn't remembering names.`

`It's knowing what needs attention now.`

Then:
- narrow question;
- simple product actions;
- short boundary lines;
- explicit acknowledgment that the app is intentionally simple;
- `That isn't the claim.`;
- plain-language UBuildOS experiment;
- `The screen may be simple. The test is the whole path around it.`;
- proof bullets;
- non-claims;
- one live-review lesson;
- one carry-forward lesson;
- one CTA;
- live link;
- repo link;
- Day X/30;
- three-line signature;
- one forward line;
- hashtags.

### Release-readiness test

Before any daily post is approved for publication, answer YES to all:

1. Does the first screenful describe a person/job/problem rather than the system?
2. Can a nontechnical reader understand what is wrong in under a few seconds?
3. Is there one clear narrow question?
4. Does the reader understand what the build does without jargon?
5. If the build is simple, does the post explain why simplicity is intentional?
6. Does the post explain what UBuildOS is actually testing?
7. Are proof and non-claims both present?
8. Is there one honest live-review lesson?
9. Is there exactly one CTA?
10. Are the live/evidence links correct?
11. Is the day signature present?
12. Has unnecessary repetition been removed?
13. Is the message still complete?
14. Were no unapproved trademark symbols invented?

Any `NO` blocks campaign-post readiness until repaired.


## 22. Governance / change control

This artifact is the byte-locked v1.1.0 successor for campaign LinkedIn post structure. It preserves v1.0.0 and adds the mandatory UBuildOS story brief.

This v1.3.0 successor preserves v1.2.0 and adds the mandatory Permanent Daily Post Structure — Day 4 Calibrated Baseline. A material semantic change requires a SemVer successor. Do not mutate these bytes in place.

Allowed without successor:
- day-specific copy instantiated from this standard;
- product-specific facts supported by evidence;
- exact URLs;
- day number;
- CTA second noun when the proof subject requires it;
- a day-specific final closing line.

Requires successor:
- changing the mandatory narrative spine;
- changing naming/trademark policy;
- removing proof/non-claims discipline;
- changing default CTA philosophy;
- changing the day-signature requirement;
- changing main-post exclusion rules;
- changing the default hashtag baseline as a permanent campaign rule.

Historical posts remain immutable evidence and are not rewritten by this standard.


## 19. Mandatory UBuildOS story brief — Day 5+ and Day 4 additive amendment

Every campaign post must explain enough of the UBuildOS story that a first-time reader can understand why the build exists and what the campaign is testing. The reader must not need prior campaign context.

The story brief is mandatory even when the day's product is technically simple. It must make clear that the small app is the visible test object, not the whole claim.

Required meaning:
- UBuildOS is being tested as a system for taking a bounded problem through a complete, repeatable path from intake to a working, inspectable, verified public release.
- The campaign is not primarily testing whether a small interface can be coded quickly. Small builds are deliberately useful because their implementation complexity cannot hide weaknesses in reasoning, requirements, evidence, QA, recovery, publication, or closeout.
- The proof target is disciplined repeatability: can the system understand the problem, bound it correctly, build the intended thing, expose how it works, test it, independently verify it, preserve evidence, recover from defects, publish it, learn from live review, and finish with an exact completion record?
- As the campaign advances, product difficulty and evidence demands may rise, but the same end-to-end discipline must continue to hold.
- The public build is evidence of the process; it is not by itself evidence of a durable competitive moat, commercial superiority, production-scale readiness, or business impact. Those claims require separate evidence.

Default public-language pattern:

`The app is intentionally small. The test is bigger than the app.`

`UBuildOS is being tested on whether it can repeatedly take a bounded problem from idea to a working, inspectable, independently verified public release — with the reasoning, evidence, recovery, live review, and completion record preserved along the way.`

`A simple build makes that harder to hide behind code. If the product can be coded quickly, then the interesting question becomes whether the whole path around the code is thoughtful, repeatable, inspectable, and trustworthy.`

This wording is a template, not mandatory verbatim copy. Preserve the meaning while avoiding mechanical repetition.

### What the story brief must NOT claim

Do not call the current campaign or these small builds proof of a `moat` unless separate evidence establishes a defensible competitive advantage. Do not imply that process rigor alone proves market demand, revenue, product-market fit, production readiness, or superiority to other development methods.

Preferred framing is `what UBuildOS is trying to prove`, `what this build tests`, and `what evidence exists so far`.

### Placement

Place the story brief after the day's product/problem explanation and before `What Day X proves`, unless the narrative reads more naturally with a shorter version immediately after `The simplicity is intentional.`

### Day 4 additive amendment

For the already-published Day 4 post, the preferred additive edit is:

`The app is intentionally small. The test is bigger than the app.`

`A capable developer could reproduce pieces of this interface quickly. That is not the claim.`

`What I am testing with UBuildOS is the path around the code: can a bounded problem be understood correctly, turned into the intended product, made inspectable, tested, independently verified, recovered when something breaks, published with evidence, reviewed live, and closed with an exact record — repeatedly?`

`Simple builds make that test cleaner. There is less product complexity to hide behind. The quality of the reasoning, requirements, verification, evidence, recovery, and release discipline has to stand on its own.`

`As the 30 days progress, the products and evidence demands get harder. The question is whether that same end-to-end discipline keeps holding.`

`That is what UBuildOS is trying to prove.`

This amendment is additive. It does not convert the Day 4 product into evidence of a competitive moat or any unsupported commercial outcome.

## 20. v1.1.0 successor lock

This v1.1.0 successor preserves all v1.0.0 rules and makes Section 19 mandatory for Day 5 and beyond. The Day 4 amendment is approved as the canonical additive correction if the owner chooses to edit the already-published post.

Future material changes require a SemVer successor. Do not mutate these bytes in place.