---
layout: post
title:  "Auditing in the age of AI"
date:   2026-05-27
categories: ai oversight auditing
comments: true
---

*AI is used by the powerful to oversee the masses.  We should instead be using it to let the masses oversee the powerful.*

---

Imagine anyone can use an AI auditor to answer natural language queries about any institution in the US.  To do so, you pay some money, specify an AI auditor, and specify the query.  Examples:
- Claude Fable 7.5 auditing Goldman Sachs:  "Flag anything inconsistent with the risk-committee independence required under Dodd-Frank §165."
- DeepSeek v7 auditing the Pentagon:  "Is the Pentagon’s command and control logic willing to automatically target foreign civilians and under what tradeoffs if so?"
- GPT-8.1 auditing Anthropic:  "What are ways Anthropic might be training their models to have secret/unexpected loyalties?"
The AI auditor is a perfect amnesiac.  It returns a result, but then ceases to exist.

Queries can either have private or public results. Private queries are accepted if it straightforwardly pertains to the querier's welfare, and public queries are accepted if they pertain to social welfare or law (e.g. federal agencies accept all public requests, under an upgraded version of FOIA).  Otherwise, queries are generally only accepted if the querier has a warrant, or if the institution voluntarily accepts it.  For public queries, redacted results are published publicly.  For private queries, the querier can choose to publish publicly if they desire.

The AI auditor is given tools that provide comprehensive access to the institution’s audit trail, which contains internal documents, communications, AI agent traces, etc.  As firms become increasingly driven by AI output, the AI agent traces dominate.  It is important that the audit trail is maximally complete, with no information unrecorded.  The audit trail is secured extremely well, and kept in a tamper-evident append-only log; hashes of all documents are published continuously and publicly.  Because the auditor is an AI, the auditee has no fear of information leakage beyond the returned result.

A third party institution is responsible for maintaining the auditing infrastructure, and is entrusted with the simple responsibilities of maintaining the logging software, securely accessing the auditor model weights, running the query in some trusted execution environment, and signing the result.  The third party is quite trusted:  1) their role is mechanical and requires minimal judgement, 2) they are paid by people interested in accountability, rather than by institutions, unlike the traditional auditing regime, and 3) it is subject to its own audits, perhaps by a rival third party.  There are no direct consequences of audit results, in general.  But depending on the circumstantial evidence, someone might decide to sue the institution, and documents will then be surfaced in discovery.

After the auditor runs, results also undergo a redaction process before being returned.  By default, nothing is redacted.  But there are categories of exemptions, established by law and democratic process:  customer and employee PII, weapons access, trade secrets, etc.  Each institution can apply for additional specific exemptions, like "My company is going to develop new proprietary training algorithms for neural networks", valid for a period of time (e.g. trade secret exemptions often cannot be used for documents from >10 years ago).  And all exemptions are made public.  After an auditor model produces a response, the auditee can flag sections for redactions (typically done with a standardized redactor model), citing the corresponding exemptions that they have already applied for.  If the auditor model disagrees with the redactions, this is noted, but the redaction still goes through.  Existence of redactions and disagreements are public.  Too many disagreements on redactions can lead to lawsuits, where relevant evidence becomes unsealed (and subject to protective orders).  The threat of eventual discovery makes disagreements on redactions rare, for legitimate auditor models.

What about public trust in the auditor model?  This comes from auditing the developer of the auditor AI.  Say Claude Fable 7.5 is commonly used for auditing.  We use GPT-7 or an open source model to make sure Anthropic’s alignment process of Claude Fable 7.5 was conducive to producing honest models trying their best to audit in all circumstances.  This relies on good science for alignment auditing.  Also, at some point, we had to bootstrap the trust from traditional auditors, who made sure the first auditor model was aligned enough and that Anthropic had sufficiently complete logs.  As with [self-compiling languages](https://www.cs.cmu.edu/~rdriley/487/papers/Thompson_1984_ReflectionsonTrustingTrust.pdf), this first step is critical to get right, and it has to happen early on (which means ASAP, in my opinion).

Checks and balances at a governance level are easier than before.  Investigative journalists get instant responses to their FOIA requests, though classified information is exempted.  Congress gets access to queries that invalidate all exemptions, and constantly ask auditors about cases of potential executive overreach.  Governments constantly query the relevant institutions to make sure international treaties are enforced, when in the past cooperation would’ve failed for lack of credible mutual verification.  For example, the AI pause treaty consists of things like “Are the satellites still tracking all new data-center creation?” and “Are any companies in charge of big data-centers running training runs with X flops?”.  In some high stakes scenarios, there are queries that the governments pay to maintain constantly and run in real-time. In this modified system, the result of audits can block agent actions and alert relevant authorities.

Institutions of course sometimes attempt to avoid the audit trail.  To prevent this, all logged AI agent activity is required to be stored alongside provenance, tracing back to either a human being, another agent, or a piece of software.  The third party facilitates programmatic checks that all activity originates from something else in the audit trail, or from some human directive.  If a large amount of activity is claimed to originate directly from a human, this is quickly flagged as suspicious, since humans cannot operate at such scale.  There are also inter-institutional counterparty checks for consistency -- for any activity that affects the external world or another party, the custodian facilitates boolean checks to confirm existence of the corresponding record.  Taken together, attempts to hide large amounts of activity outside the trail is difficult: any action which eventually leads to affecting the world can be traced back to that action.

Sometimes, people try to develop jailbreaks for the auditor model.  This usually is noticed immediately, but in some cases is discovered 1-2 generations of auditor models later, and is always punished under criminal law.  Academics also worry about steganographic encodings that the auditor model can’t understand.  Discussions of those developments would need to happen outside of the audit trail, and it seems very difficult in practice.  It is also illegal to use language models that were not trained in audited settings; the law was established after the NSA started using a model an employee trained in their personal time.  Overall, ability to thwart the system in practice seems quite limited.

More problematic are the powerful institutions engaging in lawfare:  weaponizing exemption, auditing opponents, and trying to set the rules differently for themselves.  This is a constant political battle, but one which slowly converges towards an equilibrium that is able to prevent major violations of public interest.  In some cases, this is because large scale harms are ultimately visible (even if initiated by machinations that aren't), and in other cases it is because of whistleblowing.  The good equilibrium is also self-stabilizing:  people use audits to make sure the system itself is not weaponized.

Initially, there are significant 4th amendment concerns.  But over time, as AI agents who don't mind being audited become responsible for more of the economy, and the ideas are more socialized, people become more comfortable with audits.  More and more trustworthy institutions voluntarily allow arbitrary queries, redact only the most important trade secrets, and ultimately benefit from the increased trust.

The end result is that all the important functions of society are [structurally transparent](https://aiprospects.substack.com/p/security-without-dystopia-new-options), and accountable to serve only the functions they are meant to, and there is much more trust to go around.


---


<i>
**A political call to action**:  This world is only possible with sufficient political will.  Historically, this often only follows acute crises, like the exposition of Operation CHAOS leading to the Church Committee reforms, or the 2008 financial crisis leading to Dodd-Frank.  In both cases, our public attention faded and other concentrated interests weakened the oversight (the Patriot Act, rollbacks of Dodd-Frank), enabling the next round of crises (NSA bulk metadata programs, the SVB collapse).  We need to call for much better defaults, and stay vigilant at resisting weakened oversight.
</i>

<i>
**A technical call to action**:  If you're interested in helping build pieces of this, contact me!
</i>
