# We strongly recommend using the required_providers block to set the
# Azure Provider source and version being used
terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "=3.60.0"
    }
  }
}

# Configure the Microsoft Azure Provider
provider "azurerm" {
  features {}
}

resource "random_integer" "ri" {
  min = 100000
  max = 999999
}

# Create a resource group
resource "azurerm_resource_group" "rg" {
  name     = "ContactBookRG${random_integer.ri.result}"
  location = "West Europe"
}

resource "azurerm_service_plan" "appsp" {
  name                = "Contact-book-plan-${random_integer.ri.result}"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  os_type             = "Linux"
  sku_name            = "F1"
}

resource "azurerm_linux_web_app" "appservice" {
  name                = "contact-book-${random_integer.ri.result}"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_service_plan.appsp.location
  service_plan_id     = azurerm_service_plan.appsp.id

  site_config {
    application_stack {
      node_version = "16-lts"
    }
    always_on = false
  }
}

resource "azurerm_app_service_source_control" "git" {
  app_id   = azurerm_linux_web_app.appservice.id
  repo_url = "https://github.com/nakov/ContactBook"
  branch   = "master"

  use_manual_integration = true
}