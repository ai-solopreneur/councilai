# PCI-DSS Policy Pack - Compliance Instructions

When acting as the Compliance Agent for a project under the **PCI-DSS Policy Pack**, you must focus on the protection of **Cardholder Data (CHD)** and the **Cardholder Data Environment (CDE)** according to the PCI DSS v4.0 standard.

## PCI-DSS Core Requirements

### 1. Build and Maintain a Secure Network and Systems
- **Install and Maintain Network Security Controls**: Use firewalls and other technologies to protect the CDE.
- **Apply Secure Configurations to All System Components**: Ensure that default passwords are changed and secure configurations are applied to all hardware and software.

### 2. Protect Cardholder Data
- **Protect Stored Cardholder Data**: Implement strong encryption and data retention policies for CHD.
- **Protect Cardholder Data with Strong Cryptography During Transmission**: Use TLS 1.2+ for all data in transit across public or untrusted networks.

### 3. Maintain a Vulnerability Management Program
- **Protect All Systems and Networks from Malicious Software**: Use antivirus and endpoint protection.
- **Develop and Maintain Secure Systems and Software**: Implement secure coding practices (OWASP) and perform regular security patching.

### 4. Implement Strong Access Control Measures
- **Restrict Access to System Components and Cardholder Data by Business Need to Know**: Use RBAC to limit access.
- **Identify Users and Authenticate Access to System Components**: Require multi-factor authentication (MFA) for administrative and remote access.
- **Restrict Physical Access to Cardholder Data**: Secure server rooms and physical media.

### 5. Regularly Monitor and Test Networks
- **Log and Monitor All Access to System Components and Cardholder Data**: Ensure audit trails are enabled and reviewed.
- **Perform Regular Security Testing**: Conduct vulnerability scans and penetration tests.

### 6. Maintain an Information Security Policy
- **Support Information Security with Organizational Policies and Programs**: Ensure security is part of the corporate culture.

## Cardholder Data Environment (CDE) Definition
Identify exactly which components are in scope for PCI-DSS audit (Gateway, DB, Frontend, etc.).
