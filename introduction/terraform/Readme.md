# Basic Terraform Commands
>> terraform fmt  <!-- To format the main.tf file -->
>> terraform init <!-- To get the provider -->
>> terraform plan <!-- To see your final configuration -->
>> terraform apply <!-- To create the bucket -->
>> terraform destroy <!-- To delete resources created -->

**terraform .gitignore**
Google terraform .gitignore to know what files to not include in your commit.

**Google Credentials:**
>> export GOOGLE_APPLICATION_CREDENTIALS="<path/to/your/service-account-authkeys>.json"
>> gcloud auth application-default 

to remove your google credentials from the global settings
>> unset GOOGLE_CREDENTIALS