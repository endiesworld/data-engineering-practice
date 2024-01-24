terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.13.0"
    }
  }
}

provider "google" {
  # Configuration options
  project = "dtc-de-course-01-2024"
  region  = "us-central1"
}


resource "google_storage_bucket" "local-bucket" {
  name          = "dtc-de-course-01-2024-auto-expiring-bucket"
  location      = "US"
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}