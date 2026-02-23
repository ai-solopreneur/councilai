# Compliance Scope Summary

The "My Bottle" app operates in the hospitality sector and involves the collection, storage, and processing of personal data of bar customers. It also involves the sale of alcohol, which has its own set of regulations. Considering these, the following regulations are applicable:

- **General Data Protection Regulation (GDPR)**: As the app collects and processes personal data of customers, GDPR compliance is mandatory.
- **Local Liquor Laws**: The app must adhere to local laws related to the sale and consumption of alcohol. This includes age restriction laws, which vary by country.
- **Payment Card Industry Data Security Standard (PCI DSS)**: Although not included in the MVP, the project scope indicates that a payment gateway integration might be added in Phase 2. In this case, PCI DSS compliance will be required to ensure secure handling of cardholder information.

# Data Classification Table

| Data Type            | Sensitivity Level | Storage Constraints | Retention Limits | Deletion Requirements |
|----------------------|-------------------|---------------------|------------------|-----------------------|
| Personal Data        | High              | Encrypted, secure   | 90 days          | Upon user request     |
| Financial Data       | High              | Encrypted, secure   | As per PCI DSS   | As per PCI DSS        |
| Consumption Data     | Medium            | Encrypted, secure   | 90 days          | Upon user request     |
| Operational Metadata | Low               | Standard            | Not defined      | Not defined           |

# Control Register

| Control ID | Description                              | Regulation Mapping | Enforcement Mechanism                              | Owner     |
|------------|------------------------------------------|--------------------|---------------------------------------------------|-----------|
| C1         | Age verification                         | Local Liquor Laws  | ID check on first visit                           | Bar Staff |
| C2         | Personal data encryption                 | GDPR               | Use of encryption at rest and in transit          | Developer |
| C3         | Data minimization                        | GDPR               | Collect only necessary data                       | Developer |
| C4         | Access control                           | GDPR               | Role-based access control                         | Developer |
| C5         | Compliance with PCI DSS (Phase 2)        | PCI DSS            | Adherence to all 12 PCI DSS requirements          | Developer |
| C6         | Compliance with local liquor laws        | Local Liquor Laws  | Adherence to local laws (age, serving, hours etc) | Bar Staff |

# Control → Test Mapping

| Control ID | Test Type   | Evidence                          |
|------------|-------------|-----------------------------------|
| C1         | Manual      | Age verification log              |
| C2         | Automated   | Encryption verification tests     |
| C3         | Automated   | Data collection limitation tests  |
| C4         | Automated   | Access control tests              |
| C5         | Periodic Audit | PCI DSS Compliance Certificate |
| C6         | Periodic Audit | Local Law Compliance Report    |

# Compliance Risks

1. **Insufficient age verification**: The current plan relies on bar staff to verify the age of customers. This could lead to non-compliance due to human error.
2. **Data privacy**: Ensuring the privacy and security of customer data is crucial, especially financial data (Phase 2). There is a risk if GDPR and PCI DSS requirements are not adhered to.

# Council Flags

1. **Age Verification Process**: The process of age verification needs to be revisited to ensure it is foolproof and compliant with local laws. More robust mechanisms, such as ID scanning, could be considered.
2. **Data Storage and Retention**: We need to discuss and define policies around data storage and retention, including operational metadata.
3. **Compliance with Local Liquor Laws**: The app will need to adapt to local liquor laws, which can vary significantly. This could impact features and operations.

# AI Behavioral & Ethical Risk Controls

Potential Risks:
- Over-reliance on AI without human validation in processes like age verification and consumption tracking.
  
Controls:
- Independent audit of AI systems
- Human-in-the-loop checks for sensitive operations

Validation Mechanism:
- Regular audits and quality assurance checks

Test or Audit Artifact:
- Audit reports
- Quality assurance reports

# Conflicting Compliance Resolution

In case of conflicts between different compliance requirements, the strictest applicable control should prevail. Any exceptions should be approved by the Council and documented with compensating controls.