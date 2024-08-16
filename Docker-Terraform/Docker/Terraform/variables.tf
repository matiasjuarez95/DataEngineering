variable "credentials" {
  description = "Path to the GCP credentials JSON file"
  default     = ""  # No default value for security reasons
}

variable "project" {
  description = "Project-Homework-1"
  default = "big-silo-365814"
}

variable "region" {
  description = "Region"
  default = "us-central1"
}

variable "gcs_bucket_name" {
  description = "Buckets Homework 1"
  default = "Homework-1-terra-bucket-matias"
}

variable "location" {
  description = "Project Location"
  default = "US"
}

variable "bq_dataset_name" {
  description = "Dataset Homework 1"
  default = "Homework_1"
}


variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default = "STANDARD"
}