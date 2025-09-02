env = input("Enter your environment: ")

if env == "aws" or env == "AWS":
    print("You are in AWS environment")
elif env == "azure" or env == "AZURE":
    print("You are in Azure environment")
elif env=="gcp"   or env=="GCP":
    print("You are not in AWS or Azure environment")