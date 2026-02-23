# Product Requirements Document

## 1. Product Overview
- **Product Name:** My Bottle
- **Target Users:** Frequent bar-goers, bar staff, and bar owners
- **Primary Value Proposition:** To provide a convenient and cost-effective solution for bar-goers to enjoy premium spirits at bars and track their consumption, while also offering a robust system for bars to manage bottle inventory and enhance customer retention.
- **Business Objective:** Increase the sales of premium spirits at bars and improve customer retention

## 2. Goals & Non-Goals

**Goals**
1. Facilitate customers to purchase full bottles at bars for a better value
2. Allow customers to track their consumption and continue with the same bottle across visits
3. Provide bar staff a system to manage bottle inventory and customer consumption

**Non-Goals**
1. Payment gateway integration
2. Multi-bar support
3. Bottle sharing between customers
4. Automated pour tracking
5. Loyalty points/rewards

## 3. User Personas

**Bar Customer**
- Role: Regular visitor at pubs/bars
- Primary Needs: Wants to save money on premium spirits without feeling pressured to finish the bottle in one visit
- Key Pain Points: High per-peg pricing and wasteful consumption

**Bar Staff**
- Role: On-floor staff managing customer interactions and bar operations
- Primary Needs: Efficiently manage bottle inventory, verify customer bottles, update consumption
- Key Pain Points: Difficulty in tracking customer consumption and bottle inventory

**Bar Owner**
- Role: Owner of the bar
- Primary Needs: Track bottle sales, inventory, and customer retention
- Key Pain Points: Losing potential revenue from premium bottle sales, no tracking mechanism for customer retention

## 4. User Journeys

**Bar Customer Journey**
- Entry Point: Registering and logging in to the app
- Steps:
   1. Purchase a bottle at the bar
   2. Track consumption using the app
   3. View remaining quantity and consumption history
   4. Resume drinking from the same bottle on the next visit
- Success Condition: Successfully track consumption and resume drinking in the next visit
- Failure Conditions: Unable to track consumption or view remaining quantity

**Bar Staff Journey**
- Entry Point: Login to the admin panel
- Steps:
   1. Verify customer bottles
   2. Update consumption in the system
   3. Manage bottle inventory
- Success Condition: Successfully manage bottle inventory and update customer consumption
- Failure Conditions: Unable to update consumption or manage inventory

**Bar Owner Journey**
- Entry Point: Login to the dashboard
- Steps:
   1. View sales reports
   2. Manage inventory
   3. Track customer retention metrics
- Success Condition: Successfully manage sales, inventory and track customer retention
- Failure Conditions: Unable to view reports or manage inventory

## 5. Functional Requirements
1. The system must allow customers to register and log in
2. The system must facilitate bottle purchase and assignment
3. The system must allow manual entry of consumption by bar staff
4. The system must display remaining quantity to customers
5. The system must generate a unique QR code for each bottle
6. The system must provide an admin panel for bar staff
7. The system must track visit history

## 6. Non-Functional Requirements
- Performance: The system must handle simultaneous requests from multiple users
- Scalability: The system must be scalable to accommodate growing user base and bottle inventory
- Availability: The system must be available 24/7 as bars operate late hours
- Security: The system must protect sensitive user and business data
- Observability: The system must provide real-time tracking of bottle inventory and customer consumption
- Accessibility: The customer app should be mobile-first, and the staff panel must work offline

## 7. Compliance & Governance Requirements
- Age Verification: Ensure all customers are above the legal drinking age
- Data Privacy: Protect customer consumption data according to privacy laws
- Liquor Licensing: Comply with local liquor laws
- PCI DSS: Prepare for future integration of payment gateways

## 8. MVP Definition
- MUST have: Customer registration, Bottle purchase and assignment, Consumption tracking, Remaining quantity display, QR code generation, Bar-side admin panel
- SHOULD have: Visit history tracking
- WON’T have: Payment gateway integration, Multi-bar support, Bottle sharing, Automated pour tracking, Loyalty points/rewards

## 9. Success Metrics
- Product Success Metrics: 50+ customer registrations in the first month, 80% of bottle purchases tracked via app, Customers return within 30 days to consume remaining bottle, 20% increase in premium bottle sales
- Technical Success Metrics: System handles peak load, System uptime of 99.9%, No data breaches
- Compliance Success Criteria: Zero violations in age verification and licensing

## 10. Risks & Open Issues
- Product Risks: Low adoption by customers, Bars unwilling to store bottles securely
- Technical Risks: System downtime, Data breaches
- Compliance Risks: Violation of age verification and alcohol laws, Data privacy breaches

**Note:** These risks need to be flagged for council review.