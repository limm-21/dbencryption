# Database Encryption: A Focus on Symmetric Encryption Algorithms

This Python script is structured into two main phases:  

## Phases Overview  
1. **Phase 1: Symmetric Encryption Algorithm Performance Evaluation**  
   - Evaluates the performance of various symmetric encryption algorithms

2. **Phase 2: Real-world Scenario Simulation with Field-level Encryption**  
   - Simulates the use of encryption in real-world applications, such as protecting sensitive user data

---

## Script Description

### Phase 1: Encryption Test Data Generation  
- **File Name**: Python files labeled starting with `1`.  
- **Purpose**: Inserts data into the `encryption_test_data` table with the following attributes:  

  | **Attribute**          | **Description**                       |
  |------------------------|---------------------------------------|
  | `id`                   | Unique identifier                     |
  | `plain_text`           | Input data to be encrypted            |
  | `encrypted_data`       | Resulting encrypted output            |
  | `encryption_algorithm` | Encryption algorithm used             |
  | `key_size`             | Size of the encryption key            |
  | `encryption_time`      | Time taken for encryption             |
  | `decryption_time`      | Time taken for decryption             |
  | `encryption_key`       | Key used for encryption               |  

- **Algorithms Used**:  

  | **Algorithm** | **Key Sizes**        |
  |---------------|----------------------|
  | AES           | 128, 192, 256 bits   |
  | DES           | 192 bits             |
  | Blowfish      | 128, 256, 448 bits   |
  | RC4           | 40, 128, 256 bits    |
  | ChaCha20      | 256 bits             |  

- **Plain Text Used**

   |                | **Numeric**                                         | **Alphabetic**                                      | **Alphanumeric**                                                   |
   |----------------|-----------------------------------------------------|----------------------------------------------------|--------------------------------------------------------------------|
   | **Short**      | • 1234567890<br>• 9876543210                       | • HelloWorld<br>• Encryption                       | • P@ssw0rd!1<br>• A1B2C3D4E5                                      |
   | **Medium**     | • 12345678901234567890<br>• 09876543210987654321   | • DataEncryptionTest<br>• SecureDataTesting       | • P@ssw0rd2023!Secure<br>• Test123!Encryption                     |
   | **Long**       | •12345678901234567890123456789012345678901234567890<br>•98765432109876543210987654321098765432109876543210 | •ThisIsALongPlaintextForEncryptionTestingPurposes<br>•SecureYourDatabaseWithProperEncryptionMethods | •LongP@ssw0rd123!SecureDataEncryptionTest2023!#<br>•Encryption$Mix123!DataTestForAnalysis2023!AB |

- **Supported Databases**:  
  - MySQL  
  - SQLite  
  - MongoDB  
  - Apache Cassandra  

---

### Phase 2: Real-world Scenario Simulation  
- **File Name**:  
  - Files labeled starting with `2` and `3`.  
- **Details**:  
  - **Files Starting with `2`**:  
    - Inserts 1000 random unencrypted user data into the `unencrypted_users` table with the following attributes:  

      | **Attribute** | **Description**        |
      |---------------|------------------------|
      | `id`          | Unique identifier      |
      | `name`        | User's name            |
      | `email`       | User's email address   |
      | `creditcard`  | User's credit card     |  
  
  - **Files Starting with `3`**:  
    - Inserts 1000 random user data into the `users` table with **field-level encryption** for attributes `email` and `creditcard` using different databases and algorithms.  
    - Attributes:  

      | **Attribute** | **Description**        |
      |---------------|------------------------|
      | `id`          | Unique identifier      |
      | `name`        | User's name            |
      | `email`       | Encrypted email        |
      | `creditcard`  | Encrypted credit card  |

    - Key Sizes Used:
      | **Algorithm** | **Key Sizes**        |
      |---------------|----------------------|
      | AES           | 256 bits   |
      | DES           | 192 bits             |
      | Blowfish      | 448 bits   |
      | RC4           | 256 bits    |
      | ChaCha20      | 256 bits             |  
