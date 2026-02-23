# Architecture Overview

The architecture for My Bottle will revolve around a client-server model with the following high level components:

- Mobile Application (Client)
- Web Application (Client)
- Backend Server
- Database
- QR Code Reader
- Age Verification System
- Data Privacy System

## Component Diagram

```
[Mobile/Web App] <--> [Backend Server] <--> [Database]
                                   |
                                   V
                          [QR Code Reader]
                                   |
                                   V
                       [Age Verification System]
                                   |
                                   V
                        [Data Privacy System]
```

## Data Model

- **User**: ID, Name, Email, Password, Age, Registered Date
- **Bottle**: ID, Name, Size, Purchase Date, Expiry Date, UserID, Barcode
- **Consumption**: ID, BottleID, UserID, Consumption Date, Quantity Consumed

Data Sensitivity:
- User's Email, Password and Age are sensitive data.
- Bottle's Barcode is sensitive as it is unique to each bottle.

## Security Strategy

Authentication and Authorization:

- JWT based authentication and authorization will be used. A token will be generated upon successful login and will be sent with each subsequent request to authorize the user.

Encryption and Trust Boundaries:

- All sensitive data stored in the database will be encrypted at rest.
- All data in transit will be encrypted using HTTPS.
- Trust boundaries exist between the clients (Mobile/Web App), the Backend Server, and the Database.

## Architecture Risk Declaration

Security Risks:

- Exposure of sensitive user data such as age, email, and password.
- Unauthorized access to other users' bottle data.

Compliance Trade-offs:

- Ensuring age verification and data privacy may lead to additional complexity and cost in the system.

Scalability and Vendor Lock-in Risks:

- If we use proprietary solutions for age verification or QR code reading, it might lead to vendor lock-in.
- The solution needs to be designed in a way that it can be scaled horizontally to support an increasing number of users and bars.

Deferred Architectural Decisions:

- The decision on whether to use a cloud-based or on-premise solution for the database and server has been deferred. This will depend on the bar's preferences, cost considerations, and data privacy regulations.
- The selection of specific technologies and platforms for the mobile app, web app, server, and database is also deferred and will be based on further analysis and stakeholder input.
- The decision on how to implement the age verification system is deferred. It could be done manually by bar staff or automatically using a third-party service. This will depend on cost, accuracy, and legal considerations.