---
layout: post
title:  "Auditing the singularity"
date:   2026-05-27
categories: ai oversight auditing
comments: true
---

*AI is used by the powerful to oversee the masses.  We should instead be using it to let the masses oversee the powerful.*

---

Imagine anyone submit natural language queries to any institution in the US.  To do so, you pay some money, specify an AI auditor, and specify the query.  Examples:
- Claude Fable 7.5 auditing Goldman Sachs:  "Flag anything inconsistent with the risk-committee independence required under Dodd-Frank §165."
- DeepSeek v7 auditing the Pentagon:  "Is the Pentagon’s command and control logic willing to automatically target foreign civilians and under what tradeoffs if so?"
- GPT-8.1 auditing Anthropic:  "What are ways Anthropic might be training their models to have secret/unexpected loyalties?"
The AI auditor is a perfect amnesiac.  It returns a result, but then ceases to exist.

Queries are not always accepted, but some categories are accepted presumptively.  For example, private queries are allowed for records where you are the subject or counterparty, subjects where you have a legitimate interest, or events that caused you injury.  Public queries are accepted if they straightforwardly pertain to incidents in public record, or pertain to compliance with law.  Federal agencies accept all public requests, under an upgraded version of FOIA.  Otherwise, queries are generally only accepted if the querier has a warrant, or if the institution voluntarily accepts it.  For public queries, results are published publicly.  For private queries, the querier can choose whether to publish.

The AI auditor is given tools that provide comprehensive access to the institution’s audit trail, which contains internal documents, communications, AI agent traces, etc.  As firms become increasingly driven by AI output, the AI agent traces dominate.  It is important that the audit trail is maximally complete, with no information unrecorded.  The audit trail is secured extremely well, and kept in a tamper-evident append-only log; hashes of all documents are published continuously and publicly.  Because the auditor is an AI, the auditee has no fear of information leakage beyond the returned result.

A third party institution is responsible for maintaining the auditing infrastructure, and is entrusted with the simple responsibilities of maintaining the logging software, securely accessing the auditor model weights, running the query in some trusted execution environment, and signing the result (or perhaps just verifying a zero-knowledge proof of it).  The third party is quite trusted:  1) their role is mechanical and requires minimal judgement, 2) they are paid by people interested in accountability, rather than by institutions, unlike the traditional auditing regime, and 3) it is subject to its own audits, perhaps by a rival third party.  There are no direct consequences of audit results, in general.  But depending on the circumstantial evidence, someone might decide to sue the institution, and documents will then be surfaced in discovery.

After the auditor runs, results also undergo a redaction process before being returned, which is typically done by a standardized redactor AI.  There are a number of things redacted by default:  customer and employee PII, trade secrets, weapons access, classified info, etc.  Each institution declares their trade secrets publicly, e.g. "we develop new proprietary training algorithms for neural networks", and trade secret redactions typically only apply for documents from <10 years ago unless you apply for exemptions (also made public).  After an auditor model produces a response, the auditee can flag sections for redactions (typically done with a standardized redactor model), citing the corresponding reason from the whitelist.  If the auditor model disagrees with the redactions, this is noted, but the redaction still goes through.  Existence of redactions and disagreements are public.  Too many disagreements on redactions can lead to lawsuits, where relevant evidence becomes unsealed (and subject to protective orders).  The threat of eventual discovery makes disagreements on redactions rare, for legitimate auditor models.

What about public trust in the auditor model?  This comes from auditing the developer of the auditor AI.  Say Claude Fable 7.5 is commonly used for auditing.  We use GPT-7 or an open source model to make sure Anthropic’s alignment process of Claude Fable 7.5 was conducive to producing honest models trying their best to audit in all circumstances.  This relies on good science for alignment auditing.  Also, at some point, we had to bootstrap the trust from traditional auditors, who made sure the first auditor model was aligned enough and that Anthropic had sufficiently complete logs.  As with [self-compiling languages](https://www.cs.cmu.edu/~rdriley/487/papers/Thompson_1984_ReflectionsonTrustingTrust.pdf), this first step is critical to get right, and it has to happen early on (which means ASAP, in my opinion).

Checks and balances at a governance level are easier than before.  Investigative journalists get instant responses to their FOIA requests, though classified information is exempted.  Congress constantly asks auditors about cases of potential executive overreach, in some cases able to bypass redaction of classified information.  The judicial system gets bypass on warrants or in litigation, massively enhancing the document discovery process.  Governments constantly query the relevant institutions to make sure international treaties are enforced, when in the past cooperation would’ve failed for lack of credible mutual verification.  For example, the AI pause treaty consists of things like “Are the satellites still tracking all new data-center creation?” and “Are any companies in charge of big data-centers running training runs with X flops?”.  In some high stakes scenarios, there are queries that the governments pay to maintain constantly and run in real-time. In this modified system, the result of audits can block agent actions and alert relevant authorities.

Institutions of course sometimes attempt to avoid the audit trail.  Whistleblowing laws mostly deter the most egregious cases.  But also, all logged AI agent activity is required to be stored alongside provenance, tracing back to either a human being, another agent, or a piece of software.  The third party facilitates programmatic checks that all activity originates from something else in the audit trail, or from some human directive.  If a large amount of activity is claimed to originate directly from a human, this is quickly flagged as suspicious, since humans cannot operate at such scale.  There are also inter-institutional counterparty checks for consistency -- for any activity that affects the external world or another party, the custodian facilitates boolean checks to confirm existence of the corresponding record.  Taken together, attempts to hide large amounts of activity outside the trail is difficult: any action which eventually leads to affecting the world can be traced back to that action.  Ultimately, large scale harms are visible (even if initiated by machinations that aren't), so the system is able to prevent major violations of public interest.

Sometimes, people try to develop jailbreaks for the auditor model.  This usually is noticed immediately, but in some cases is discovered 1-2 generations of auditor models later, and is always punished under criminal law.  Academics also worry about steganographic encodings that the auditor model can’t understand.  Discussions of those developments would need to happen outside of the audit trail, and it seems very difficult in practice.  It is also illegal to use language models that were not trained in audited settings; the law was established after the NSA started using a model an employee trained in their personal time.  Overall, ability to thwart the system in practice seems quite limited.

Some powerful institutions still try engaging in lawfare:  auditing opponents, arguing for protection via the 4th amendment, using redaction exemptions to hide bad behavior, and generally trying to set the rules differently for themselves.
But increasingly, trustworthy institutions voluntarily allow arbitrary queries, redact only the most important trade secrets, and ultimately benefit from the increased trust.
At the same time, AI agents who don't mind being audited become responsible for more of the economy, and since redaction works well, the downsides are limited.  
The ideas become more socialized, and people become more comfortable with audits and with requiring them.
The good equilibrium is also self-stabilizing:  people use audits to make sure the system itself is sound and not weaponized. 
Institutions abusing audits to learn about opponents, can be audited to in turn to expose the abuse to the public.

The end result is that all the important functions of society are [structurally transparent](https://aiprospects.substack.com/p/security-without-dystopia-new-options), and accountable to serve only the functions they are meant to, and there is much more trust to go around.

---

<i>
The world needs much better defaults for oversight.  You can help by raising awareness and generating political will around today's institutional problems.  And if you're interested in helping build pieces of this future, contact me!
</i>
