# Commercial Ontology — Commas × CommaForge

**Status:** Active working ontology (Phase 1–scoped)  
**As of:** 2026-07-22  
**Authority:** Derived from CANONICAL-STATE, DECISION-001/002/003, live Commas product surface, session research  
**Not:** A full knowledge graph, embeddings layer, or multi-agent world model (explicitly deferred — DECISION-003, SUPERSEDED-IDEAS)

## Correct first-principles question

| Question | Verdict |
|---|---|
| “Build a complete ontology of Commas and CommaForge” | **Wrong primary question** if it delays a paid sale |
| “What is the smallest true map of Commas + our offer that unblocks received £ through Commas?” | **Correct Phase 1 question** |
| “How does money actually clear on Commas rails for our SKU?” | Correct operational sub-question |
| “What does the codebase already encode vs invent?” | Correct cross-reference sub-question |

Research exists to improve a commercial decision (docs/RESEARCH-METHOD.md). Ontology here = **typed commercial objects + relations + money paths**, not academic taxonomy theatre.

---

## A. Entity types

### A1. Platform layer (Commas / FanBasis Inc.)

| ID | Type | Definition | Status |
|---|---|---|---|
| PLAT-COMMAS | Platform brand | Public product brand at commas.com | FACT |
| PLAT-FANBASIS | Legacy brand | Prior brand; support host still fanbasis.com | FACT |
| ENT-FANBASIS-INC | Legal entity | Operates under both names (terms) | FACT |
| RAIL-PAY | Payment rail | Checkout, routing, BNPL, retries, invoices, payouts | FACT — core wedge |
| SURF-FUNNEL | Conversion surface | Vibe Funnels (AI funnel builder) | FACT |
| SURF-WEBINAR | Conversion surface | In-room checkout webinars | FACT |
| SURF-STUDIO | Hosting surface | Courses + paid community in one Studio | FACT |
| SURF-AFF | Growth surface | Affiliate Center (native to payment rails) | FACT |
| SURF-QUAL | Sales intel | Qualifier — financial enrichment of leads | FACT |
| SURF-ENT | Enterprise | APIs, SDKs, MCP beta, embedded checkout | FACT |
| OBJ-PRODUCT-LINK | Sellable object | One-time or recurring priced checkout URL | FACT |
| OBJ-CHECKOUT | Transaction | Buyer payment attempt / capture | FACT |
| OBJ-PAYOUT | Settlement | Seller balance → bank/rail | FACT |
| ACTOR-SELLER | Role | Account that lists offers and receives GMV | FACT |
| ACTOR-BUYER | Role | Pays for offer | FACT |
| ACTOR-AFFILIATE | Role | Promotes; earns commission on rails | FACT |

### A2. CommaForge layer (this repo)

| ID | Type | Definition | Status |
|---|---|---|---|
| CF-SYSTEM | System | Commercial intelligence + experiment system for first £1k through Commas | FACT (CANONICAL-STATE) |
| CF-NORTH | Metric | Gross customer sales **received through Commas** ≥ £1,000 | FACT (DECISION-001) |
| CF-EXP-001 | Experiment | Solo Founder AI Operator Sprint | FACT (DECISION-002) |
| CF-OFFER | Offer | £250 guided one-workstream sprint; pay before delivery | FACT (OFFER.md) |
| CF-CUSTOMER | ICP | Solo founder with AI operator / context continuity pain | FACT (EXPERIMENT.md) |
| CF-DELIVERY | Protocol | Manual deliverables package | FACT (DELIVERY-PROTOCOL.md) |
| CF-OUTREACH | Process | 20 personal founder approaches | FACT (OUTREACH.md) |
| CF-SCORE | Ledger | scoreboard/SCOREBOARD.md | FACT |
| CF-INTEL | Intelligence | commas/fanbasis/mappings sources | FACT |
| CF-DECISION | Decision record | decisions/DECISION-*.md | FACT |

### A3. Money states (critical)

| State | Counts as north-star £? | Notes |
|---|---|---|
| Intent / chat | No | Conversation only |
| Checkout started | No | Abandoned possible |
| Captured on Commas | **Yes** (gross received) | DECISION-001 definition |
| Available balance | Ops, not milestone | After holds/reserves |
| Paid out to bank | Ops | Fees/FX separate |
| Refunded / charged back | Reduces effective | Track on scoreboard |

---

## B. Relations (edges that matter)

```
ACTOR-SELLER --lists--> OBJ-PRODUCT-LINK
ACTOR-BUYER  --pays-->  OBJ-CHECKOUT
OBJ-CHECKOUT --clears_on--> RAIL-PAY
OBJ-CHECKOUT --may_use--> BNPL / routing / retry
RAIL-PAY --credits--> seller balance
seller balance --payout--> OBJ-PAYOUT

CF-OFFER --implemented_as--> OBJ-PRODUCT-LINK   (required, not yet done)
CF-OUTREACH --drives--> ACTOR-BUYER candidates
CF-OFFER --fulfilled_by--> CF-DELIVERY (manual, offline)
CF-EXP-001 --measures--> CF-SCORE
CF-SCORE --aggregates--> captured OBJ-CHECKOUT for CF-OFFER

SURF-* --increases--> checkout attempts / close rate on RAIL-PAY
PLAT-COMMAS --rebrands--> PLAT-FANBASIS (same ENT)
```

**First-principles claim (INFERENCE):**  
Every SURF-* is a **demand or conversion amplifier on RAIL-PAY**. The scarce platform capability is payment conversion for high-ticket digital offers, not LMS novelty.

---

## C. Commas product map (sitemap 2026-07-13, dogfood 2026-07-22)

### Products (`/products/*`)

| Path | Name | Job-to-be-done | Wedge class | Phase 1 need |
|---|---|---|---|---|
| /products/payments | Payments | Clear more £, pay out on many rails | **Core** | Required (link + payout) |
| /products/vibe-funnels | Vibe Funnels | AI-built funnel → same payment rails | Amplifier | No |
| /products/webinars | Webinars | In-room checkout + BNPL | Amplifier | No |
| /products/studios | Studios | Course + community hosting with native pay | Hosting | No |
| /products/affiliate-systems | Affiliate systems | Recruit/track/pay affiliates on same rails | Growth | No |
| /products/affiliate-center | (sitemap alias) | Same family; URL 404 at dogfood time | UNKNOWN alias | No |
| /products/qualifier | Qualifier | Bureau-level lead finance enrichment | Sales filter | No |

Note: bare `/products/` → 404. There is no index page; products are a flat set.

### Solutions (`/solutions/*`) — ICP marketing cuts

digital-services, agencies, coaching, online-courses, enterprises, webinars, paid-groups, software-saas, affiliate-marketing  

These are **positioning pages**, not separate engines. Same RAIL-PAY underneath.

### Legal/marketing pages

/, /terms, /privacy-policy; /pricing → 404 at research time (UNKNOWN fee schedule from public HTML).

### Claimed quantitative hooks (marketing — treat as HYPOTHESIS until account-level proof)

- 12–15% failed payments recovered via routing/retry  
- Up to 38% revenue lift on stack move  
- BNPL $30–$465k; orders up to 3×  
- Subscription Saver recovers cancellations  
- Live in under 5 days white-glove  

---

## D. Cross-reference: ontology ↔ this codebase

| Ontology node | Repo path | Implementation state |
|---|---|---|
| CF-SYSTEM soul | CANONICAL-STATE.md, README.md, AGENTS.md | Present |
| CF-NORTH | decisions/DECISION-001-NORTH-STAR.md | Present |
| CF-EXP-001 | decisions/DECISION-002, experiments/001-*/EXPERIMENT.md | Present |
| CF-OFFER | experiments/001-*/OFFER.md | Spec only — **not live on Commas** |
| CF-DELIVERY | experiments/001-*/DELIVERY-PROTOCOL.md | Spec only |
| CF-OUTREACH | experiments/001-*/OUTREACH.md | Empty register (20 blank rows) |
| CF-SCORE | scoreboard/SCOREBOARD.md | £0 / 0 customers / 0 approaches |
| Results | experiments/001-*/RESULTS.md | Empty / pre-run |
| Platform intel | intelligence/commas/PRODUCT-SURFACE.md | Thin; needs refresh from this ontology |
| Transition | intelligence/fanbasis/TRANSITION-NOTES.md | Partial |
| Mapping | intelligence/mappings/MAPPING-001-*.md | Partial |
| Provenance | intelligence/SOURCE-REGISTER.md | Present through 2026-07-18 |
| Principles | docs/PRINCIPLES.md, docs/PHASE1.md, docs/RESEARCH-METHOD.md | Present |
| Sequencing guard | decisions/DECISION-003-SEQUENCING.md | Present — blocks graph theatre |
| Deferred graph | archive/SUPERSEDED-IDEAS.md | Explicitly deferred |
| schema/ | schema/COMMERCIAL-ONTOLOGY.md (this file) | **Was empty .gitkeep** |
| src/ | .gitkeep only | No product code |
| wiki/ | .gitkeep only | Empty |
| research/ | empty content dir | Empty |
| scripts/validate_repo.py | repo hygiene | Only real code besides tools/ |
| tools/llm-wiki-mcp-runtime | tooling stub | Not commercial path |
| Hermes launchers | ~/.hermes/scripts/commaforge/* | Outside repo; Expert/Heavy/Council |

**Gap that blocks north star:**  
`CF-OFFER --implemented_as--> OBJ-PRODUCT-LINK` is missing in the world. Everything else in-repo is preparation.

---

## E. Money paths ranked (CommaForge operator, not Commas Inc.)

Score = fit to DECISION-001 × speed × controllable by us × uses existing skills.

| Rank | Path | Mechanism on Commas | E[£] near-term | Notes |
|---:|---|---|---|---|
| 1 | EXP-001 direct sell | Product link £250 × 4 | Highest | Only path with written experiment + kill gate |
| 2 | Higher-ticket same skill | Product link £750–£2.5k | High £/win | Use if £250 gets talk not pay |
| 3 | Help a seller go live on Commas | Service billed as product link | Medium | Adjacent; can distract |
| 4 | Low-ticket digital pack | Product link £49–£149 | Low | Tests rails; weak signal |
| 5 | Commas seller referral | 10% of what Commas makes | Low for £1k | Side income; not customer GMV of our offer |
| 6 | Studio/course/webinar/funnel own brand | Full SURF stack | Low now | Needs audience/ads |
| 7 | Qualifier/enterprise/API | SURF-QUAL / SURF-ENT | Near zero | Wrong stage |

**Commas Inc. money model (INFERENCE for platform):** GMV × take-rate + BNPL/payout economics + enterprise. Open free accounts = top-of-funnel for rails volume.

**Our money model (FACT for Phase 1):** 4 × £250 captured on our product link.

---

## F. Wedge vs theatre (Commas marketing)

| They say | Between the lines |
|---|---|
| All-in-one internet business OS | Payment spine + conversion surfaces |
| Shopify for minds / anyone can start | Mass brand; P&L still high-ticket sellers |
| AI funnels / co-pilot | Acquisition + roadmap wrap on payment moat |
| Open to everyone | Scale after invite-only underwriting era |
| 2× revenue / 15× growth | Performance story for referral loop |
| Escape 9-5 / AI job displacement | Identity demand gen, not product core |

**True user wedge:** collect more of the money buyers already almost paid (routing, BNPL, in-room checkout, retries).  
**Anti-customer:** no offer, no demand, hopes platform creates buyers.

---

## G. Competitive contrast (sketch)

| System | Seat/fee bias | Payment bias | Best for |
|---|---|---|---|
| Stripe | DIY | Commodity rails | Devs who assemble stack |
| Kajabi | High monthly, low % | Fine for courses | Content + email all-in-one |
| Skool | Low monthly + % tiers | Community-first | Paid groups |
| Whop | Low seat, % on gated | Discord/community commerce | Info + community drops |
| Gumroad | % heavy | Simple digital goods | Simple files |
| **Commas** | Free entry, volume rails | **Aggressive conversion + BNPL + routing** | High-ticket digital + webinar/funnel close |

---

## H. Open unknowns (do not invent)

1. Exact fees / reserves / payout timing for Richard’s UK account  
2. Whether £250 service SKU is best product type in UI (service vs digital vs other)  
3. BNPL eligibility and currency (GBP native vs FX)  
4. MCP beta availability on this account  
5. affiliate-center vs affiliate-systems canonical URL  
6. Public pricing page absence (/pricing 404)

Resolve only via authenticated seller UI or support — then update SOURCE-REGISTER + this file.

---

## I. Ontology update rule

1. New durable claim → source in intelligence/SOURCE-REGISTER.md  
2. New platform object → section C  
3. New experiment/offer → section A2 + D  
4. Payment/refund/outreach → CF-SCORE only for money facts  
5. Do not expand into embeddings/graph/multi-agent without DECISION superseding DECISION-003  

## J. Immediate actions implied by this ontology

1. Create OBJ-PRODUCT-LINK for CF-OFFER on Commas  
2. Enable OBJ-PAYOUT path (KYC/bank)  
3. Fill CF-OUTREACH rows 1–20 and send  
4. On first capture, update CF-SCORE  
5. Refresh intelligence/commas/PRODUCT-SURFACE.md from sections C–F  

Ontology complete enough for Phase 1 when step 1–3 are in motion — not when more nodes are added.
