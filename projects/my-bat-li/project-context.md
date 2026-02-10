# My Bottle — Project Context

## Product Name
**My Bottle** (Bar Bottle Management System)

## Problem
Customers at pubs and bars who want to drink premium spirits face two issues:
1. **High per-peg pricing** — Buying individual pegs is expensive
2. **Wasteful consumption** — Customers feel pressured to finish bottles in one visit

This leads to:
- Customers avoiding premium spirits due to cost
- Bars losing potential revenue from premium bottle sales
- No tracking of consumption across visits

## Solution
A mobile/web app that allows customers to:
- **Purchase full bottles** at the bar (better value than per-peg pricing)
- **Track consumption** — Record what they drink each visit
- **Resume next visit** — Continue drinking from the same bottle on future visits
- **Save money** — Pay upfront for the bottle, consume at their own pace

The bar stores the bottle with the customer's name, and the app tracks:
- Bottle purchase date
- Remaining quantity
- Consumption history
- Expiry/storage limits

## Users

### Primary Users
- **Bar customers** — People who visit pubs/bars regularly and want to save money on premium spirits

### Secondary Users
- **Bar staff** — Manage bottle inventory, verify customer bottles, update consumption
- **Bar owners** — Track bottle sales, inventory, and customer retention

## Scope

### In Scope (MVP)
- Customer registration and login
- Bottle purchase and assignment
- Consumption tracking (manual entry by staff)
- Remaining quantity display
- Visit history
- QR code for bottle identification
- Bar-side admin panel for staff

### Out of Scope (Phase 2)
- Payment gateway integration (cash/card at bar for now)
- Multi-bar support (single bar for MVP)
- Bottle sharing between customers
- Automated pour tracking (IoT devices)
- Loyalty points/rewards

## Constraints

### Regulatory
- **Age verification** — Must verify customer is 21+ (legal drinking age)
- **Alcohol licensing** — Comply with local liquor laws
- **Data privacy** — Customer consumption data is sensitive

### Technical
- Mobile-first design (customers use phones)
- Works offline for staff (bar may have poor connectivity)
- Simple QR code scanning for bottle identification
- Low-cost infrastructure (small bar budget)

### Business
- Bar must agree to store bottles securely
- Bottles expire after 90 days (or bar policy)
- Customer must show ID on first visit

## Compliance Needs
- **Age verification** (legal drinking age enforcement)
- **Data privacy** (customer consumption data)
- **Local liquor laws** (varies by region/country)
- **PCI DSS** (if payment integration added in Phase 2)

## Success Criteria
- 50+ customers register in first month
- 80% of bottle purchases are tracked via app
- Customers return within 30 days to consume remaining bottle
- Bar reports 20% increase in premium bottle sales
- Zero compliance violations (age verification, licensing)

## Risk Tolerance
**Medium** — This is a consumer-facing app with regulatory requirements (age verification, alcohol laws), but not life-critical. Focus on compliance and user trust.

---

## Additional Context

### Key Features
1. **Customer App:**
   - View my bottles (active, consumed, expired)
   - See remaining quantity
   - View consumption history
   - QR code for bottle verification

2. **Bar Staff Panel:**
   - Scan customer QR code
   - Record consumption (e.g., "2 pegs consumed")
   - Mark bottle as finished
   - View all active bottles in storage

3. **Bar Owner Dashboard:**
   - Sales reports (bottles sold)
   - Inventory management
   - Customer retention metrics

### Business Model
- Free for customers
- Bar pays monthly subscription (SaaS model)
- Or: Bar pays per bottle tracked (usage-based pricing)
