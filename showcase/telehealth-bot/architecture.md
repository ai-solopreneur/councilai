# Architecture Overview

The HealthAI Telehealth system is designed as a robust, secure, and scalable mobile application that serves two user types: patients and healthcare providers. The architecture is built around a frontend interface, a backend consisting of several microservices, and cloud-based data storage. The system is designed to handle sensitive health data, with a focus on HIPAA and GDPR compliance.

# Component Diagram

The system consists of the following components:

- **Frontend Mobile Application:** The frontend interface for both patients and healthcare providers. It includes features such as user registration, symptom input, telehealth appointments, and messaging.

- **Backend Services:**
  - **Authentication Service:** Handles user registration, login, and session management.
  - **Triage Service:** Uses AI to assess and prioritize patients based on reported symptoms.
  - **Telehealth Service:** Manages video call appointments between patients and healthcare providers.
  - **Messaging Service:** Provides secure communication between patients and healthcare providers.
  
- **Data Stores:**
  - **User Database:** Stores user profiles and authentication data.
  - **Health Records Database:** Stores patient health records and symptom reports.

- **Third-Party Integrations:**
   - **Cloud Storage Provider:** For storing patient health records.
   - **Video Call Provider:** For facilitating video call appointments.

# Data Model

The data model consists of two main entities:

- **User:** Attributes include UserID, Name, PasswordHash, Role (Patient or Provider), and Contact Information.

- **Health Record:** Attributes include RecordID, UserID, Reported Symptoms, AI Triage Result, and Appointment Details. 

Health Record is associated with User through the UserID attribute. 

The data is classified as sensitive since it includes personal health information.

# Security Strategy

- **Authentication:** The system uses a secure authentication service that manages user registration, login, and session management.

- **Authorization:** Role-based access control is implemented. Patients can only access their own health records and appointment details, while healthcare providers can access the records of patients assigned to them.

- **Encryption:** All data, both at rest and in transit, is encrypted. Communication between the frontend application and backend services is secured using SSL/TLS. 

- **Trust Boundaries:** Trust boundaries are established between the frontend application, backend services, and data stores. Each service has its own set of permissions and cannot access data outside its scope.

# Architecture Risk Declaration

- **Security Risk:** If the third-party video call provider is compromised, patient data could be at risk. 

- **Compliance Trade-off:** Storing health data in the cloud may raise data residency concerns under GDPR, depending on the location of the data centers.

- **Scalability Risk:** The AI Triage Service could potentially become a bottleneck if the system scales up and many users are reporting symptoms at the same time.

- **Vendor Lock-in Risk:** Relying on a specific cloud storage provider and video call provider could lead to vendor lock-in. 

- **Deferred Architectural Decision:** The choice of AI model for the Triage Service is deferred until more information on the specific requirements and constraints of the triage process is available. This decision impacts the accuracy and reliability of the triage system. 

All identified risks will be registered and reviewed in the next Council review.