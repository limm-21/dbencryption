import random
import string
import time
import base64
from Crypto.Cipher import ARC4
from Crypto.Random import get_random_bytes
from pymongo import MongoClient
import os

def generate_rc4_key():
    """Generates a cryptographically secure random 32-byte RC4 key."""
    return get_random_bytes(32)

key = generate_rc4_key()
key_hex = key.hex()
print(f"Generated RC4 Key (Hex): {key_hex}")

key_bytes = bytes.fromhex(key_hex)

os.environ["ENCRYPTION_KEY"] = key_hex
print(os.environ.get("ENCRYPTION_KEY"))

def encrypt_data(data):
    """Encrypt data using RC4-256 and Base64 encode."""
    cipher = ARC4.new(key_bytes)
    encrypted = cipher.encrypt(data.encode())
    encoded_data = base64.b64encode(encrypted).decode('utf-8')
    return encoded_data

def decrypt_data(encoded_data):
    """Decrypt Base64 encoded data using RC4-256."""
    decoded_data = base64.b64decode(encoded_data.encode('utf-8'))
    cipher = ARC4.new(key_bytes)
    decrypted = cipher.decrypt(decoded_data)
    return decrypted.decode()

def generate_name():
    first_names = ["Alice", "Bob", "Charlie", "David", "Emma", "Fiona", "Grace", "Hannah", "Isaac", "Julia"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez",
                  "Martinez"]
    return f"{random.choice(first_names)} {random.choice(last_names)}"

def generate_email():
    domains = ["example.com", "test.com", "mail.com", "demo.com", "sample.org"]
    username = "".join(random.choices(string.ascii_lowercase, k=5))
    return f"{username}@{random.choice(domains)}"

def generate_credit_card():
    return "-".join(["".join(random.choices(string.digits, k=4)) for _ in range(4)])

def measure_time(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    return end_time - start_time, result

def mongo_operations():
    try:
        mongo_url = "mongodb://localhost:27017/"
        database_name = "EncryptionDB"
        collection_name = "users"

        client = MongoClient(mongo_url)
        db = client[database_name]
        collection = db[collection_name]

        count_time, row_count_result = measure_time(collection.estimated_document_count)
        row_count = row_count_result
        if row_count == 0:
            records = [
                {
                    "Name": generate_name(),
                    "Email": encrypt_data(generate_email()),
                    "CreditCard": encrypt_data(generate_credit_card())
                }
                for _ in range(1000)
            ]
            insert_time, _ = measure_time(collection.insert_many, records)
            print(f"Insert Time: {insert_time:.10f} seconds")
        else:
            print("Collection is not empty, skipping insertion")

        print(f"Select Time: {count_time:.10f} seconds")

        email_docs = collection.find({}, {"_id": 1, "Email": 1})
        ids_to_update = []
        for doc in email_docs:
            try:
                decrypted_email = decrypt_data(doc["Email"])
                if decrypted_email.endswith("@example.com"):
                    ids_to_update.append(doc["_id"])
            except (ValueError, TypeError, base64.binascii.Error) as e:
                print(f"Decryption error for ID {doc['_id']}: {e}")

        if ids_to_update:
            update_time, update_result = measure_time(
                collection.update_many,
                {"_id": {"$in": ids_to_update}},
                {"$set": {"Name": "James David"}}
            )
            print(f"Updated {update_result.modified_count} records. Update Time: {update_time:.10f} seconds")
        else:
            print("No emails found ending with @example.com")

        docs = collection.find().limit(5)
        for doc in docs:
            try:
                decrypted_email = decrypt_data(doc["Email"])
                decrypted_credit_card = decrypt_data(doc["CreditCard"])
                print(
                    f"ID: {doc['_id']}, Name: {doc['Name']}, Decrypted Email: {decrypted_email}, Decrypted Credit Card: {decrypted_credit_card}")
            except (ValueError, TypeError, base64.binascii.Error) as e:
                print(f"Decryption Error for ID {doc['_id']}: {e}")
                print(f"Encrypted Email: {doc['Email']}")
                print(f"Encrypted Credit Card: {doc['CreditCard']}")
                continue

    except Exception as e:
        print(f"MongoDB Error: {e}")
    finally:
        if client:
            client.close()

import secrets
key = secrets.token_bytes(32)
key_hex = key.hex()
os.environ["ENCRYPTION_KEY"] = key_hex
print(f"Generated RC4 Key (Hex): {key_hex}")

mongo_operations()
