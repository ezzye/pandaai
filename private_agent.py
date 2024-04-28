import ollama

with open('logs/2024-04-09T10_i-02d74c80628cc896b_0(4)=api-management', 'r') as file:
    log1 = file.read()
if log1:
    print("log1 loaded successfully")
    print(f"This is log1: {log1[:9000]}")
else:
    print("log1 failed to load or is empty")
print()

with open('logs/2024-04-09T10_i-02d74c80628cc896b_0(4)-nginx-tls-access', 'r') as file:
    log2 = file.read()
if log2:
    print("log1 loaded successfully")
    print(f"This is log2: {log2[:9000]}")
else:
    print("log2 failed to load or is empty")
print()

info = (
    "Toughguy is the authentication layer. Toughguy runs on EC2, with the api-management rpm installed and running to "
    "verify API keys (with commercial company) and client certificates, and forwards valid content-access "
    "requests to related component, and valid content-access.")
certs = ("EarthCert TLS server certificate and private key: Toughguy uses a EarthCert server certificate as users of "
         "the API cannot be required to install the company's CA certificates. The private key is stored in encrypted "
         "form in"
         "local-configuration, and decrypted by the component every hour using KMS, and installed if any changes have "
         "occurred.")

prompt1_01 = (f"Toughguy purpose: {info} {certs} From these Toughguy logs, what interesting useful information can you "
              f"determine. ### This is the  ```api-management log``` a javascript app running on ec2  ```{log1[:9000]}``` "
              f"### This is the ```nginx-tls-access``` log for the nginx reverse proxy server on same ec2 as api-management app.  "
              f"The nginx server is used as a reverse proxy for the api-management app ```{log2[:9000]}```")

print(f"<agent 1> Prompt: {prompt1_01}")
print()
print(f"<agent 1> Generating a response...")
print()

response_01 = ollama.chat(
    model="llama3",
    messages=[
        {
            "role": "user",
            "content": prompt1_01
        }
    ]
)

print(f"<agent 01> Response: {response_01['message']['content']}")
print()

prompt1_02 = (
    f"Toughguy purpose: {info} {certs} ### ```{response_01['message']['content']}``` This is interesting and useful information about a log file "
    f"from an aws ec2 component.  Highlight any issues that need to be fixed, how to fix issues and further "
    f"steps that maybe necessary to determine cause of issues")

print(f"<agent 2> Prompt: {prompt1_02}")
print()
print(f"<agent 2> Generating a response...")
print()

response_02 = ollama.chat(
    model="llama3",
    messages=[
        {
            "role": "user",
            "content": prompt1_02
        }
    ]
)

print(f"<agent 02> Response: {response_02['message']['content']}")
print()
