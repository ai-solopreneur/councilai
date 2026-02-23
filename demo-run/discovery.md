# Discovery Output

## Discovery Summary

"My Bottle" is a mobile/web app designed to address the high costs and wasteful consumption associated with purchasing premium spirits at bars by allowing customers to buy whole bottles and keep track of their consumption over multiple visits. The app's features include purchase and assignment of bottles, manual consumption entry by bar staff, remaining quantity display, visit history, and a QR code for bottle identification. The system serves bar customers primarily, as well as bar staff and owners. Compliance with age verification, local liquor laws, and data privacy is paramount. 

## Assumptions

- Bar staff will accurately and consistently update consumption data in the app.
- Bar owners are willing to store customer bottles securely and comply with the system's requirements.
- Customers are willing to trust the bar with their purchased bottles and the app with their consumption data.
- The app can legally store and display alcohol consumption data.

## Functional Requirements

1. User registration and login system
2. Functionality for customers to view active, consumed, and expired bottles
3. Bottle purchase and assignment features
4. Manual consumption entry by bar staff
5. Display of remaining bottle quantity
6. QR code generation and scanning for bottle identification
7. Visit history tracking
8. Admin panel for bar staff to manage inventory and verify customer bottles
9. Dashboard for bar owners to track sales, inventory, and customer retention

## Non-Functional Requirements

- **Performance:** The app should respond quickly to user interactions and load data efficiently.
- **Scalability:** The system should be able to handle an increasing number of users and bottles.
- **Availability:** The app should be available at all times, considering the bar's operational hours.
- **Security:** The system must protect sensitive customer data and ensure secure transactions.

## Compliance Profile

- **Applicable regulations:** Age verification laws, local liquor laws, data privacy laws, and potentially PCI-DSS if payment integration is added in the future.
- **Data sensitivity classification:** Personal data (names, contact information, and age), financial data (if payment integration is added), and sensitive customer consumption data.
- **Audit requirements:** The system should have an audit log to track all actions performed in the system by both customers and staff.

## Open Questions

- What happens if a bottle is lost or damaged while in the bar's storage?
- How will the bar handle situations where a customer disputes the remaining quantity of their bottle?
- What is the legal and regulatory stance on storing and displaying alcohol consumption data? 

## Council Flags

- The legal implications of storing and displaying alcohol consumption data need to be discussed and clarified.
- The handling of lost, damaged, or disputed bottles needs to be addressed.
- The system's dependency on manual updates by bar staff could lead to errors and disputes, and should be considered for risk mitigation measures.