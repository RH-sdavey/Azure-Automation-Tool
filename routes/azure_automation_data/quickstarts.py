azure_quickstarts = {
    "Analysis Services": [
        {
            "action": "Azure Analysis Services Server",
            "description": "This template allows you to deploy a new Azure Analysis Services server with a simple firewall rule",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.analysisservices%2Fanalysis-services-create%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.analysisservices%2Fanalysis-services-create%2Fazuredeploy.json"
        }
    ],
    "API Management": [
        {
            "action": "API Management instance and all sub resources",
            "description": "This template provides an example of how to create API Management service and configure all sub-entities",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.apimanagement%2Fapi-management-create-all-resources%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.apimanagement%2Fapi-management-create-all-resources%2Fazuredeploy.json"
        },
        {
            "action": "API Management with an external Azure Cache for Redis",
            "description": "Creates an instance of Azure API Management in the Consumption tier with an external Azure Cache for Redis instance",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.apimanagement%2Fapi-management-create-with-external-redis-cache%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.apimanagement%2Fapi-management-create-with-external-redis-cache%2Fazuredeploy.json"
        },
        {
            "action": "Deploy API Management in external VNet with public IP",
            "description": "Creates an instance of Azure API Management in the Premium tier within your virtual network's subnet in external mode and configure recommended NSG rules on the subnet. The instance is deployed to two availability zones. The template also configures a public IP address from your subscription.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.apimanagement%2Fapi-management-create-with-external-vnet-publicip%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.apimanagement%2Fapi-management-create-with-external-vnet-publicip%2Fazuredeploy.json"
        },
        {
            "action": "Create an API Management instance with custom hostnames",
            "description": "Creates an instance of Azure API Management with a custom hostname for the portal and multiple custom hostnames for the proxy. Creates API Management service in Premium tier since the feature to configure multiple custom hostnames in the proxy in API Management is only available in Premium tier of API Management. However, you can configure a single proxy custom hostname in any API Management tier.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.apimanagement%2Fapi-management-create-with-hostname%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.apimanagement%2Fapi-management-create-with-hostname%2Fazuredeploy.json"
        },
        {
            "action": "Create API Management in Internal VNet with App Gateway",
            "description": "Creates an instance of Azure API Management on a private network protected by Azure Application Gateway. This template also demonstrates how to configure integration with Application Insights and Azure Monitor Log Analytics. Because the concept being demonstrated in this template requires VNet integration, only Developer or Premium tier Azure API Management tiers can be selected.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.apimanagement%2Fapi-management-create-with-internal-vnet-application-gateway%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.apimanagement%2Fapi-management-create-with-internal-vnet-application-gateway%2Fazuredeploy.json"
        },
        {
            "action": "Deploy API Management in internal VNet with public IP",
            "description": "Creates an instance of Azure API Management in the Premium tier within your virtual network's subnet in internal mode and configure recommended NSG rules on the subnet. The instance is deployed to two availability zones. The template also configures a public IP address from your subscription.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.apimanagement%2Fapi-management-create-with-internal-vnet-publicip%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.apimanagement%2Fapi-management-create-with-internal-vnet-publicip%2Fazuredeploy.json"
        },
        {
            "action": "Create an API Management instance having MSI Identity",
            "description": "Creates a developer instance of Azure API Management having an MSI Identity.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.apimanagement%2Fapi-management-create-with-msi%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.apimanagement%2Fapi-management-create-with-msi%2Fazuredeploy.json"
        },
        {
            "action": "Create a multiregion Premium tier API Management instance",
            "description": "Creates an API Management instance with additional locations. The primary location is the same as the location of the resource group. For additional locations, the template shows NorthCentralUs and East US2. The primary location should be different from additional locations.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.apimanagement%2Fapi-management-create-with-multiregion%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.apimanagement%2Fapi-management-create-with-multiregion%2Fazuredeploy.json"
        },
        {
            "action": "Create API Management with custom proxy SSL using KeyVault",
            "description": "Creates an Azure API Management service with SSL Certificate from KeyVault as Resource Manager Reference.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.apimanagement%2Fapi-management-create-with-reference-keyvault%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.apimanagement%2Fapi-management-create-with-reference-keyvault%2Fazuredeploy.json"
        },
        {
            "action": "Create an API Management service with SSL from KeyVault",
            "description": "Deploys an API Management service configured with User Assigned Identity. It uses this identity to fetch an SSL certificate from KeyVault and keeps it updated by checking every 4 hours.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.apimanagement%2Fapi-management-key-vault-create%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.apimanagement%2Fapi-management-key-vault-create%2Fazuredeploy.json"
        },
        {
            "action": "Create and monitor API Management instance",
            "description": "Creates an instance of Azure API Management service and Log Analytics workspace and sets up monitoring for your API Management service with Log Analytics.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.apimanagement%2Fapi-management-logs-oms-integration%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.apimanagement%2Fapi-management-logs-oms-integration%2Fazuredeploy.json"
        },
        {
            "action": "Create an API Management service with a private endpoint",
            "description": "This template will create a virtual network, an API Management service, and a private endpoint exposing the API Management service to the virtual network.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.apimanagement%2Fapi-management-private-endpoint%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.apimanagement%2Fapi-management-private-endpoint%2Fazuredeploy.json"
        },
        {
            "action": "Deploy API Management into Availability Zones",
            "description": "Creates a premium instance of Azure API Management and deploys it into an Availability Zone.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.apimanagement%2Fapi-management-simple-zones%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.apimanagement%2Fapi-management-simple-zones%2Fazuredeploy.json"
        },
        {
            "action": "Create an API Management instance using a template",
            "description": "Creates a developer instance of Azure API Management.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.apimanagement%2Fazure-api-management-create%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.apimanagement%2Fazure-api-management-create%2Fazuredeploy.json"
        }
    ],
    "App": [
        {
            "action": "Create a Container App Environment with a basic Container App from an Azure Container Registry",
            "description": "Creates a Container App Environment with a basic Container App from an Azure Container Registry. It also deploys a Log Analytics Workspace to store logs.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.app%2Fcontainer-app-acr%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.app%2Fcontainer-app-acr%2Fazuredeploy.json"
        },
        {
            "action": "Create a two Container App Environment with a basic Container App",
            "description": "Creates two Container Apps in a Container App Environment. It also deploys a Log Analytics Workspace to store logs.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.app%2Fcontainer-app-azurevote%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.app%2Fcontainer-app-azurevote%2Fazuredeploy.json"
        },
        {
            "action": "Create a Container App Environment with a basic Container App",
            "description": "Creates a Container App Environment with a basic Container App. It also deploys a Log Analytics Workspace to store logs.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.app%2Fcontainer-app-create%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.app%2Fcontainer-app-create%2Fazuredeploy.json"
        },
        {
            "action": "Create a Dapr microservices app using Container Apps",
            "description": "Deploys a Dapr microservice application as a Container App in a Container App Environment.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.app%2Fcontainer-app-dapr-blob%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.app%2Fcontainer-app-dapr-blob%2Fazuredeploy.json"
        },
        {
            "action": "Create a Dapr pub-sub servicebus app using Container Apps",
            "description": "Deploys a Dapr pub-sub servicebus application as a Container App in a Container App Environment.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.app%2Fcontainer-app-dapr-pubsub-servicebus%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.app%2Fcontainer-app-dapr-pubsub-servicebus%2Fazuredeploy.json"
        },
        {
            "action": "Create a Container App Environment with a basic Container App that scales based on HTTP traffic",
            "description": "This template provides a way to deploy a Container App that scales based on HTTP traffic in a Container App Environment.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.app%2Fcontainer-app-scale-http%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.app%2Fcontainer-app-scale-http%2Fazuredeploy.json"
        },
        {
            "action": "Creates an external Container App environment with a VNET",
            "description": "Deploys an external Azure Container Apps environment with a virtual network.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.app%2Fcontainer-app-vnet-external-environment%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.app%2Fcontainer-app-vnet-external-environment%2Fazuredeploy.json"
        },
        {
            "action": "Creates an internal Container App environment with a VNET",
            "description": " an internal Azure Container Apps environment with a virtual network.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.app%2Fcontainer-app-vnet-internal-environment%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.app%2Fcontainer-app-vnet-internal-environment%2Fazuredeploy.json"
        }
    ],
    "App Configuration": [
        {
            "action": "Create an App Configuration Store with Feature Flag",
            "description": "Creates an Azure App Configuration store, then creates a feature flag inside the new store.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.appconfiguration%2Fapp-configuration-store-ff%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.appconfiguration%2Fapp-configuration-store-ff%2Fazuredeploy.json"
        },
        {
            "action": "Create an App Configuration Store with Key Vault Reference",
            "description": "Creates an Azure App Configuration store, then creates a Key Vault reference inside the new store.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.appconfiguration%2Fapp-configuration-store-keyvaultref%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.appconfiguration%2Fapp-configuration-store-keyvaultref%2Fazuredeploy.json"
        },
        {
            "action": "Create an Azure App Configuration Store with Key Values",
            "description": "Creates an Azure App Configuration store, then creates two key-values inside the new store via a copy function. This can also deploy key-values that link to an Azure Key Vault.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.appconfiguration%2Fapp-configuration-store-kv-copy%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.appconfiguration%2Fapp-configuration-store-kv-copy%2Fazuredeploy.json"
        },
        {
            "action": "Create an Azure App Configuration Store with Key Values",
            "description": "Creates an Azure App Configuration store, then creates two key-values inside the new store.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.appconfiguration%2Fapp-configuration-store-kv%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.appconfiguration%2Fapp-configuration-store-kv%2Fazuredeploy.json"
        },
        {
            "action": "Create an Azure App Configuration Store",
            "description": "Creates an Azure App Configuration store.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.appconfiguration%2Fapp-configuration-store%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.appconfiguration%2Fapp-configuration-store%2Fazuredeploy.json"
        },
        {
            "action": "Reference existing key-value configurations from an existing config store",
            "description": "This template references existing key-value configurations from an existing config store and uses retrieved values to set properties of the resources the template creates.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.appconfiguration%2Fapp-configuration%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.appconfiguration%2Fapp-configuration%2Fazuredeploy.json"
        }
    ],
    "Attestation": [
        {
            "action": "Create an Attestation provider",
            "description": "This template creates an Attestation provider.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.attestation%2Fattestation-provider-create%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.attestation%2Fattestation-provider-create%2Fazuredeploy.json"
        }
    ],
    "Authorization": [
        {
            "action": "Assign a built-in policy to an existing resource group",
            "description": "This template assigns a built-in policy to an existing resource group. You must be an owner of the scope (subscription, resourceGroup) to apply a policy.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.authorization%2Fazurepolicy-assign-builtinpolicy-resourcegroup%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.authorization%2Fazurepolicy-assign-builtinpolicy-resourcegroup%2Fazuredeploy.json"
        },
        {
            "action": "RBAC - Grant Built-In Role Access for multiple existing VMs in a Resource Group",
            "description": "This template assigns Owner, Reader, Contributor, Virtual Machine Contributor access to multiple VMs in a resource group. Inputs to this template are following fields.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.authorization%2Frbac-builtinrole-multiplevms%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.authorization%2Frbac-builtinrole-multiplevms%2Fazuredeploy.json"
        },
        {
            "action": "Assign an RBAC role to a Resource Group",
            "description": "This template assigns Owner, Reader or Contributor access to an existing resource group. To learn more about how to deploy the template, see the quickstart article linked below.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.authorization%2Frbac-builtinrole-resourcegroup%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.authorization%2Frbac-builtinrole-resourcegroup%2Fazuredeploy.json"
        },
        {
            "action": "Assign RBAC roles to an existing VM",
            "description": "This template assigns Owner, Reader, Contributor, and Virtual Machine Contributor access to an existing VM in a resource group. To learn more about how to deploy the template, see the quickstart article linked below.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.authorization%2Frbac-builtinrole-virtualmachine%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.authorization%2Frbac-builtinrole-virtualmachine%2Fazuredeploy.json"
        },
        {
            "action": "Create Managed Identity Access on Azure Maps account",
            "description": "This template assigns Azure Maps Data Reader access for a Managed Identity on an Azure Maps account in a resource group. It does not assign the identity to an Azure resource such as Azure App Service or Azure Virtual Machines. To enable Service to Service authentication to Azure Maps, this template grants a service principal access to Azure Maps using an Azure Managed Identity. Inputs to this template include a GUID, and for automation on role assignments, you must assign 'User Access Administrator' to enable automation scenarios without a user's principal.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.authorization%2Frbac-managedidentity-maps%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.authorization%2Frbac-managedidentity-maps%2Fazuredeploy.json"
        }
    ],
    "Automation": [
        {
            "action": "Create Azure Automation account",
            "description": "This template demonstrates the creation of an Azure Automation account and links it to a new or existing Azure Monitor Log Analytics workspace that you specify. It provides an example of how to create an Azure Automation account and configure its integration with Log Analytics. The template allows you to specify the details of the Automation account and the Log Analytics workspace.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.automation%2F101-automation%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.automation%2F101-automation%2Fazuredeploy.json"
        },
        {
            "action": "Create Managed Virtual Machine",
            "description": "This template demonstrates a managed virtual machine where the configuration will be maintained by Azure for the life of the node. The template includes examples of nested templates that create an automation account, publish a configuration script and supporting modules from the PowerShell Gallery, compile the configuration, bootstrap the machine to the service, and wait for the initial delivery of the configuration to complete, all from a single deployment.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.automation%2Fautomation-configuration%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.automation%2Fautomation-configuration%2Fazuredeploy.json"
        }
    ],
    "Azure Purview": [
        {
            "action": "Deploy Microsoft Purview account",
            "description": "This template deploys a Microsoft Purview account using an Azure Resource Manager (ARM) template.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.azurepurview%2Fazure-purview-deployment%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.azurepurview%2Fazure-purview-deployment%2Fazuredeploy.json"
        }

    ],
    "Azure Stack HCI": [
        {
            "action": "Create Azure Stack HCI Image from Azure Marketplace",
            "description": "This template allows you to deploy a new Azure Stack HCI Image from the referenced Azure Marketplace image. See Azure Stack HCI Images for a list of supported images.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.azurestackhci%2Fimage-from-azure-marketplace%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.azurestackhci%2Fimage-from-azure-marketplace%2Fazuredeploy.json"
        },
        {
            "action": "Create Azure Stack HCI Storage Path/Container",
            "description": "This template creates a Storage Path/Container in Azure, representing a physical path in your on-prem Azure Stack HCI cluster. This resource is used in the creation of VMs and images to target a specific path rather than any CSV with space.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.azurestackhci%2Fstorage-container%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.azurestackhci%2Fstorage-container%2Fazuredeploy.json"
        },
        {
            "action": "Create a VM from the referenced Azure Marketplace image on Azure Stack HCI",
            "description": "This template allows you to deploy a new Windows Virtual Machine on an on-premises Azure Stack HCI cluster using the referenced Azure Marketplace image. The article walks you through the process and prerequisites.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.azurestackhci%2Fvm-simple-windows%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.azurestackhci%2Fvm-simple-windows%2Fazuredeploy.json"
        },
        {
            "action": "Create a VM from the referenced image on Azure Stack HCI",
            "description": "This template allows you to deploy a new Windows Virtual Machine on an on-premises Azure Stack HCI cluster using the referenced image. The article walks you through the process and prerequisites.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.azurestackhci%2Fvm-windows-storage-container%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.azurestackhci%2Fvm-windows-storage-container%2Fazuredeploy.json"
        }
    ],
    "Batch": [
        {
            "action": "Azure Batch pool without public IP addresses",
            "description": "This module will create Azure Batch account with node management private endpoint enabled, and provision a pool without public IP addresses in a virtual network.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.batch%2Fbatch-pool-no-public-ip%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.batch%2Fbatch-pool-no-public-ip%2Fazuredeploy.json"
        },
        {
            "action": "Existing Azure Batch Service with Pfx from Keyvault",
            "description": "This template demostrates use of pfx certificate from keyvault in Azure batch service.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.batch%2Fbatch-with-keyvault-pfx-password%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.batch%2Fbatch-with-keyvault-pfx-password%2Fazuredeploy.json"
        },
        {
            "action": "Create a Batch Account using a template",
            "description": "This Azure Resource Manager template (ARM template) creates a batch account resource in Azure. To learn more about how to deploy the template, see the quickstart article.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.batch%2Fbatchaccount-with-storage%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.batch%2Fbatchaccount-with-storage%2Fazuredeploy.json"
        }
    ],
    "Cache": [
        {
            "action": "Create a Redis Cache with Microsoft Entra Authentication",
            "description": "This template creates an Azure Cache for Redis instance with Microsoft Entra authentication and custom access policies for Microsoft Entra Service Principals or Managed Identities.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.cache%2Fredis-cache-microsoft-entra-authentication%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.cache%2Fredis-cache-microsoft-entra-authentication%2Fazuredeploy.json"
        },
        {
            "action": "Create an Azure Redis Cache with diagnostics data kept in a storage account",
            "description": "This template creates an Azure Redis Cache with diagnostics data stored in a storage account.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.cache%2Fredis-cache%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.cache%2Fredis-cache%2Fazuredeploy.json"
        },
        {
            "action": "Create a Redis Cluster on Ubuntu VMs with Azure Redis Cache",
            "description": "This template deploys a Redis cluster on Ubuntu virtual machine images with well-known optimizations and best practices applied.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.cache%2Fredis-high-availability%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.cache%2Fredis-high-availability%2Fazuredeploy.json"
        },
        {
            "action": "Create a Premium Redis Cache with Clustering",
            "description": "Create and configure clustering in premium Azure Redis Cache using a template.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.cache%2Fredis-premium-cluster-diagnostics%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.cache%2Fredis-premium-cluster-diagnostics%2Fazuredeploy.json"
        },
        {
            "action": "Create Premium Redis Cache with data persistence",
            "description": "Create and configure persistence in a premium Azure Redis Cache instance using a template.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.cache%2Fredis-premium-persistence%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.cache%2Fredis-premium-persistence%2Fazuredeploy.json"
        },
        {
            "action": "Create Premium Redis Cache deployed into a Virtual Network",
            "description": "Create a premium Redis Cache inside a Virtual Network using a template.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.cache%2Fredis-premium-vnet%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.cache%2Fredis-premium-vnet%2Fazuredeploy.json"
        },
        {
            "action": "Create two geo-replicated caches in a Virtual Network",
            "description": "Create two Premium tier Azure Cache for Redis instances inside separate Virtual Networks and link them with Geo-Replication using a template.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.cache%2Fredis-vnet-geo-replication%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.cache%2Fredis-vnet-geo-replication%2Fazuredeploy.json"
        }
    ],
    "CDN": [
        {
            "action": "Create a CDN Profile and a CDN Endpoint with parameters",
            "description": "Create a CDN Profile and a CDN Endpoint with parameterized configuration settings.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.cdn%2Fcdn-customize%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.cdn%2Fcdn-customize%2Fazuredeploy.json"
        },
        {
            "action": "Create a CDN Profile and a CDN Endpoint with custom origin",
            "description": "Create a CDN Profile and a CDN Endpoint with a user-specified origin and all commonly used settings on CDN.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.cdn%2Fcdn-with-custom-origin%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.cdn%2Fcdn-with-custom-origin%2Fazuredeploy.json"
        },
        {
            "action": "Create a CDN Endpoint with cache override through Rules",
            "description": "Create a CDN Profile and a CDN Endpoint with a user-specified origin and all commonly used settings on CDN. This template also configures rules engine with a path-based rule and overrides cache expiration.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.cdn%2Fcdn-with-ruleseengine-cacheoverride%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.cdn%2Fcdn-with-ruleseengine-cacheoverride%2Fazuredeploy.json"
        },
        {
            "action": "Create a CDN Endpoint with response header addition",
            "description": "Create a CDN Profile and a CDN Endpoint with a user-specified origin and all commonly used settings on CDN. This template also configures rules engine with a Remote address based match and adds corresponding response headers.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.cdn%2Fcdn-with-ruleseengine-responseheader%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.cdn%2Fcdn-with-ruleseengine-responseheader%2Fazuredeploy.json"
        },
        {
            "action": "Create a CDN Endpoint with rewrite and redirect rules",
            "description": "Create a CDN Profile and a CDN Endpoint with a user-specified origin and all commonly used settings on CDN. This template also configures rules engine device-based path rewrite and request scheme-based redirect.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.cdn%2Fcdn-with-ruleseengine-rewriteandredirect%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.cdn%2Fcdn-with-ruleseengine-rewriteandredirect%2Fazuredeploy.json"
        },
        {
            "action": "Create a CDN Endpoint with UrlSigning action",
            "description": "Create a CDN Profile and a CDN Endpoint with a user-specified origin and commonly used settings on CDN. This template also configures rules engine UrlSigning action for default and override parameters.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.cdn%2Fcdn-with-ruleseengine-urlsigning%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.cdn%2Fcdn-with-ruleseengine-urlsigning%2Fazuredeploy.json"
        },
        {
            "action": "Create a CDN Profile, Endpoint and a Storage Account",
            "description": "Create a CDN Profile and a CDN Endpoint with origin as a Storage Account. Note that the user needs to create a public container in the Storage Account for the CDN Endpoint to serve content from the Storage Account.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.cdn%2Fcdn-with-storage-account%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.cdn%2Fcdn-with-storage-account%2Fazuredeploy.json"
        },
        {
            "action": "Apply a WAF Policy with custom rules to a CDN Endpoint",
            "description": "Create a CDN Profile and a CDN Endpoint with a user specified origin and all of the most commonly used settings on CDN. This template also links a CDN WAF Policy to the Endpoint which applies example custom rules for blocking and redirecting requests based on geo-location, IP address, and SESSIONID header.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.cdn%2Fcdn-with-waf-custom-rules%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.cdn%2Fcdn-with-waf-custom-rules%2Fazuredeploy.json"
        },
        {
            "action": "Apply a WAF Policy for the OWASP top 10 to a CDN Endpoint",
            "description": "Create a CDN Profile and a CDN Endpoint with a user specified origin and all of the most commonly used settings on CDN. This template also enables a CDN WAF Policy on the Endpoint which applies the managed rule set DefaultRuleSet_1.0.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.cdn%2Fcdn-with-waf-managed-rules%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.cdn%2Fcdn-with-waf-managed-rules%2Fazuredeploy.json"
        },
        {
            "action": "Apply a WAF Policy with rate limit rules to a CDN Endpoint",
            "description": "Create a CDN Profile and a CDN Endpoint with a user specified origin and all of the most commonly used settings on CDN. This template also links a CDN WAF Policy to the Endpoint which applies example rate limit rules for blocking and redirecting rate-limited requests.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.cdn%2Fcdn-with-waf-rate-limit-rules%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.cdn%2Fcdn-with-waf-rate-limit-rules%2Fazuredeploy.json"
        },
        {
            "action": "Create a CDN Profile and a CDN Endpoint with a Web App as the origin",
            "description": "This template creates a CDN Profile and a CDN Endpoint with a Web App as the origin.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.cdn%2Fcdn-with-web-app%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.cdn%2Fcdn-with-web-app%2Fazuredeploy.json"
        },
        {
            "action": "Create a Front Door Premium and an App Service with a Private Link",
            "description": "This template deploys a Front Door Standard/Premium with an App Service origin, using a private endpoint to access the App Service application.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.cdn%2Ffront-door-premium-app-service-private-link%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.cdn%2Ffront-door-premium-app-service-private-link%2Fazuredeploy.json"
        },
        {
            "action": "Create a Front Door Premium and an Azure Storage blob container with a Private Link",
            "description": "This template deploys a Front Door Premium with an Azure Storage blob container origin, using a private endpoint to access the storage account.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.cdn%2Ffront-door-premium-storage-blobs-private-link%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.cdn%2Ffront-door-premium-storage-blobs-private-link%2Fazuredeploy.json"
        },
        {
            "action": "Create a Front Door Premium with a virtual machine web server origin using Private Link service",
            "description": "This template deploys a Front Door Standard/Premium with a virtual machine web server origin. Front Door uses a private endpoint, configured with Private Link service, to access the web application.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.cdn%2Ffront-door-premium-vm-private-link%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.cdn%2Ffront-door-premium-vm-private-link%2Fazuredeploy.json"
        },
        {
            "action": "Create a Front Door Premium with a Web Application Firewall (WAF) and Microsoft-managed rule sets",
            "description": "This template deploys a Front Door Premium with a Web Application Firewall (WAF) and Microsoft-managed rule sets.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.cdn%2Ffront-door-premium-waf-managed%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.cdn%2Ffront-door-premium-waf-managed%2Fazuredeploy.json"
        },
        {
            "action": "Create a Front Door Standard/Premium with an API Management origin",
            "description": "This template deploys a Front Door Standard/Premium with an API Management origin using external VNet connectivity for the API Management instance.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.cdn%2Ffront-door-standard-premium-api-management-external%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.cdn%2Ffront-door-standard-premium-api-management-external%2Fazuredeploy.json"
        },
        {
            "action": "Create a Front Door Standard/Premium with an App Service origin",
            "description": "This template deploys a Front Door Standard/Premium with an App Service origin, using the App Service public endpoint.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.cdn%2Ffront-door-standard-premium-app-service-public%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.cdn%2Ffront-door-standard-premium-app-service-public%2Fazuredeploy.json"
        },
        {
            "action": "Create a Front Door Standard/Premium with an Application Gateway origin",
            "description": "This template deploys a Front Door Standard/Premium with an Application Gateway origin, using the Application Gateway's public endpoint.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.cdn%2Ffront-door-standard-premium-application-gateway-public%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.cdn%2Ffront-door-standard-premium-application-gateway-public%2Fazuredeploy.json"
        },
        {
            "action": "Create a Front Door with Container Instances and Application Gateway",
            "description": "This template deploys a Front Door Standard/Premium with Azure Container Instances and Application Gateway.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.cdn%2Ffront-door-standard-premium-container-instances-application-gateway-public%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.cdn%2Ffront-door-standard-premium-container-instances-application-gateway-public%2Fazuredeploy.json"
        },
        {
            "action": "Create a Front Door with Azure Container Instances",
            "description": "This template deploys a Front Door Standard/Premium with an Azure Container Instances origin, using a public IP address for the container group.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.cdn%2Ffront-door-standard-premium-container-instances-public%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.cdn%2Ffront-door-standard-premium-container-instances-public%2Fazuredeploy.json"
        },
        {
            "action": "Create a Front Door with Azure DNS and custom domain",
            "description": "This template deploys a Front Door Standard/Premium with custom domain managed through an Azure DNS zone, and a Microsoft-managed TLS certificate.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.cdn%2Ffront-door-standard-premium-custom-domain-azure-dns%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.cdn%2Ffront-door-standard-premium-custom-domain-azure-dns%2Fazuredeploy.json"
        },
        {
            "action": "Create a Front Door with a custom domain and customer-managed certificate",
            "description": "This template deploys a Front Door Standard/Premium with a custom domain and customer-managed TLS certificate.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.cdn%2Ffront-door-standard-premium-custom-domain-customer-certificate%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.cdn%2Ffront-door-standard-premium-custom-domain-customer-certificate%2Fazuredeploy.json"
        },
        {
            "action": "Create a Front Door with a custom domain and Microsoft-managed certificate",
            "description": "This template deploys a Front Door Standard/Premium with a custom domain and Microsoft-managed TLS certificate.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.cdn%2Ffront-door-standard-premium-custom-domain%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.cdn%2Ffront-door-standard-premium-custom-domain%2Fazuredeploy.json"
        },
        {
            "action": "Create a Front Door with an Azure Functions origin",
            "description": "This template deploys a Front Door Standard/Premium with an Azure Functions (HTTP trigger) origin, using the Azure Functions public endpoint.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.cdn%2Ffront-door-standard-premium-function-public%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.cdn%2Ffront-door-standard-premium-function-public%2Fazuredeploy.json"
        },
        {
            "action": "Create a Front Door with Geo-Filtering Policy",
            "description": "This template deploys a Front Door Standard/Premium with a geo-filtering policy.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.cdn%2Ffront-door-standard-premium-geo-filtering%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.cdn%2Ffront-door-standard-premium-geo-filtering%2Fazuredeploy.json"
        },
        {
            "action": "Create a Front Door with Rate Limit",
            "description": "This template deploys a Front Door Standard/Premium with a rate limit.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.cdn%2Ffront-door-standard-premium-rate-limit%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.cdn%2Ffront-door-standard-premium-rate-limit%2Fazuredeploy.json"
        },
        {
            "action": "Create a Front Door with Rule Set",
            "description": "This template deploys a Front Door Standard/Premium with a rule set.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.cdn%2Ffront-door-standard-premium-rule-set%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.cdn%2Ffront-door-standard-premium-rule-set%2Fazuredeploy.json"
        },
        {
            "action": "Create a Front Door with Storage Static Website",
            "description": "This template deploys a Front Door Standard/Premium with an Azure Storage static website origin.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.cdn%2Ffront-door-standard-premium-storage-static-website%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.cdn%2Ffront-door-standard-premium-storage-static-website%2Fazuredeploy.json"
        },
        {
            "action": "Create a Front Door with WAF and Custom Rule",
            "description": "This template deploys a Front Door Standard/Premium with a Web Application Firewall (WAF) and a custom rule set.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.cdn%2Ffront-door-standard-premium-waf-custom%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.cdn%2Ffront-door-standard-premium-waf-custom%2Fazuredeploy.json"
        },
        {
            "action": "Create a Front Door Standard/Premium",
            "description": "This template deploys a Front Door Standard/Premium.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.cdn%2Ffront-door-standard-premium%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.cdn%2Ffront-door-standard-premium%2Fazuredeploy.json"
        }
    ],
    "Cognitive Services": [
        {
            "action": "Deploy a Cognitive Services Computer Vision API",
            "description": "This template deploys a Cognitive Services Computer Vision API, which allows you to process visual data with features like image analytics, tagging, face recognition, text extraction, and more.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.cognitiveservices%2Fcognitive-services-Computer-vision-API%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.cognitiveservices%2Fcognitive-services-Computer-vision-API%2Fazuredeploy.json"
        },
        {
            "action": "Deploy a Cognitive Services Translate API",
            "description": "This template deploys a Cognitive Services Translate API, which enables text translation and language detection in applications, websites, and other solutions.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.cognitiveservices%2Fcognitive-services-translate%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.cognitiveservices%2Fcognitive-services-translate%2Fazuredeploy.json"
        },
        {
            "action": "Deploy a Cognitive Service Universal key",
            "description": "This template deploys a Cognitive Services Universal Key, enabling developers to access a wide range of AI services, such as vision, speech, language, search, and more, through a single key.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.cognitiveservices%2Fcognitive-services-universalkey%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.cognitiveservices%2Fcognitive-services-universalkey%2Fazuredeploy.json"
        }
    ],
    "Compute": [
        {
            "action": "Create a VM with multiple NICs and RDP accessible",
            "description": "This template allows you to create a Virtual Machine with multiple (2) network interfaces (NICs), and RDP connectable with a configured load balancer and an inbound NAT rule. More NICs can easily be added with this template. This template also deploys a Storage Account, Virtual Network, Public IP address, and 2 Network Interfaces (front-end and back-end).",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2F1-vm-loadbalancer-2-nics%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2F1-vm-loadbalancer-2-nics%2Fazuredeploy.json"
        },
        {
            "action": "Create a VM with two NICs and two subnets within the same VNet",
            "description": "This template creates a new VM with two NICs which connect to two different subnets within the same VNet.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2F1vm-2nics-2subnets-1vnet%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2F1vm-2nics-2subnets-1vnet%2Fazuredeploy.json"
        },
        {
            "action": "Create 2 VMs in a VNET under an Internal Load Balancer",
            "description": "This template allows you to create 2 Virtual Machines in a VNET under an internal Load Balancer and configure a load balancing rule on Port 80. This template also deploys a Storage Account, Virtual Network, Public IP address, Availability Set, and Network Interfaces.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2F2-vms-internal-load-balancer%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2F2-vms-internal-load-balancer%2Fazuredeploy.json"
        },
        {
            "action": "Create 2 VMs under a Load Balancer with load balancing rules on Port 80",
            "description": "This template allows you to create 2 Virtual Machines under a Load balancer and configure a load balancing rule on Port 80. This template also deploys a Storage Account, Virtual Network, Public IP address, Availability Set, and Network Interfaces. In this template, we use the resource loops capability to create the network interfaces and virtual machines.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2F2-vms-loadbalancer-lbrules%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2F2-vms-loadbalancer-lbrules%2Fazuredeploy.json"
        },
        {
            "action": "Create 2 VMs in an Availability Set and configure NAT rules through the Load Balancer",
            "description": "This template allows you to create 2 Virtual Machines in an Availability Set and configure NAT rules through the Load Balancer. This template also deploys a Storage Account, Virtual Network, Public IP address, and Network Interfaces. In this template, we use the resource loops capability to create the network interfaces and virtual machines.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2F2-vms-loadbalancer-natrules%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2F2-vms-loadbalancer-natrules%2Fazuredeploy.json"
        },
        {
            "action": "Create an Availability Set with 3 Fault Domains",
            "description": "This template creates an Availability Set and configures it for 3 Fault Domains and 20 Update Domains. 3 FDs are very useful when you're building a quorum-based solution or simply to ensure high availability of your service.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Favailability-set-create-3FDs-20UDs%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Favailability-set-create-3FDs-20UDs%2Fazuredeploy.json"
        },
        {
            "action": "Create an encrypted managed disk from an encrypted VHD",
            "description": "This template creates a new encrypted managed disk provided a pre-encrypted VHD and its corresponding encryption settings.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fcreate-encrypted-managed-disk%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fcreate-encrypted-managed-disk%2Fazuredeploy.json"
        },
        {
            "action": "Custom Script extension on a Ubuntu VM",
            "description": "This template creates a Ubuntu VM and installs the CustomScript extension. CustomScript Extension allows the owner of the Azure Virtual Machines to run customized scripts in the VM.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fcustomscript-extension-public-storage-on-ubuntu%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fcustomscript-extension-public-storage-on-ubuntu%2Fazuredeploy.json"
        },
        {
            "action": "Disable encryption on Windows VM encrypted without AAD",
            "description": "This template disables encryption on a running Windows VM which was encrypted without using AAD application.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fdecrypt-running-windows-vm-without-aad%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fdecrypt-running-windows-vm-without-aad%2Fazuredeploy.json"
        },
        {
            "action": "Disable encryption on a running Linux VM.",
            "description": "This template disables encryption on a running Linux VM. This template assumes that the VM is located in the same region as the resource group. If not, please edit the template to pass the appropriate location for the VM sub-resources.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fdecrypt-running-linux-vm%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fdecrypt-running-linux-vm%2Fazuredeploy.json"
        },
        {
            "action": "Disable encryption on an existing Linux VMSS",
            "description": "This template disables encryption on a running VM scale set of Linux VMs.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fdecrypt-vmss-linux%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fdecrypt-vmss-linux%2Fazuredeploy.json"
        },
        {
            "action": "Disable encryption on a running Windows VM Scale Set",
            "description": "This template disables encryption on a running VM Scale Set of Windows VMs.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fdecrypt-vmss-windows%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fdecrypt-vmss-windows%2Fazuredeploy.json"
        },
        {
            "action": "Discover Private IP dynamically",
            "description": "This template allows you to discover a private IP for a NIC. It passes the private IP of NIC0 to VM1 using custom script extensions which writes it to a file on VM1.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fdiscover-private-ip-dynamically%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fdiscover-private-ip-dynamically%2Fazuredeploy.json"
        },
        {
            "action": "Create new encrypted managed disks Windows VM from gallery image",
            "description": "This template creates a new encrypted managed disks Windows VM using the Windows Server 2012 gallery image.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fencrypt-create-new-vm-gallery-image-managed-disks%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fencrypt-create-new-vm-gallery-image-managed-disks%2Fazuredeploy.json"
        },
        {
            "action": "Create a new encrypted Windows VM from gallery image",
            "description": "This template creates a new encrypted Windows VM using the Windows Server 2012 gallery image.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fencrypt-create-new-vm-gallery-image%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fencrypt-create-new-vm-gallery-image%2Fazuredeploy.json"
        },
        {
            "action": "Enable encryption on a running Linux VM without needing AAD application details",
            "description": "This template enables encryption with no AD requirement on a running Linux VM.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fencrypt-running-linux-vm-without-aad%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fencrypt-running-linux-vm-without-aad%2Fazuredeploy.json"
        },
        {
            "action": "Enable encryption on a running Linux VM using AAD client secret",
            "description": "This template enables encryption on a running Linux VM using AAD client secret. This template assumes that the VM is located in the same region as the resource group. If not, please edit the template to pass appropriate location for the VM sub-resources.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fencrypt-running-linux-vm%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fencrypt-running-linux-vm%2Fazuredeploy.json"
        },
        {
            "action": "Enable data volume encryption on a running Linux VMSS",
            "description": "This template enables encryption on a running VM Scale Set of Linux VMs.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fencrypt-running-vmss-linux%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fencrypt-running-vmss-linux%2Fazuredeploy.json"
        },
        {
            "action": "Enable encryption on a running Windows VMSS",
            "description": "This template enables encryption on a running VM Scale Set of Windows VMs.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fencrypt-running-vmss-windows%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fencrypt-running-vmss-windows%2Fazuredeploy.json"
        },
        {
            "action": "Enable encryption on a running Windows VM & AAD",
            "description": "This template enables encryption on a running windows vm using AAD client cert thumbprint. The certificate should have been deployed to the VM before running this template.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fencrypt-running-windows-vm-aad-client-cert%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fencrypt-running-windows-vm-aad-client-cert%2Fazuredeploy.json"
        },

        {
            "action": "Create and encrypt a new Linux VMSS with jumpbox",
            "description": "This template deploys a Linux VMSS using the latest Linux image, adds data volumes, and then encrypts the data volumes of each Linux VMSS instance. It also deploys a jumpbox with a public IP address in the same virtual network as the Linux VMSS instances with private IP addresses.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fencrypt-vmss-linux-jumpbox%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fencrypt-vmss-linux-jumpbox%2Fazuredeploy.json"
        },
        {
            "action": "GlassFish on SUSE",
            "description": "This template deploys GlassFish application server onto multiple load balanced SUSE Linux VMs. It is possible to select either OpenSUSE or SLES for the OS, and any release package associated with version 3 or 4 of GlassFish.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fglassfish-on-suse%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fglassfish-on-suse%2Fazuredeploy.json"
        },
        {
            "action": "List Storage Account keys-Windows Custom Script extension",
            "description": "This template creates a Windows Server 2012 R2 VM and runs a PowerShell script using the custom script extension. It also uses the listKeys function to get the Azure Storage Account keys. The PowerShell script for this sample must be hosted in an Azure Storage account. (Note: For other samples custom script can also be hosted in Github)",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Flist-storage-keys-windows-vm%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Flist-storage-keys-windows-vm%2Fazuredeploy.json"
        },
        {
            "action": "VMs in Availability Zones with a Load Balancer and NAT",
            "description": "This template allows you to create Virtual Machines distributed across Availability Zones with a Load Balancer and configure NAT rules through the load balancer. This template also deploys a Virtual Network, Public IP address, and Network Interfaces. In this template, we use the resource loops capability to create the network interfaces and virtual machines.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fmulti-vm-lb-zones%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fmulti-vm-lb-zones%2Fazuredeploy.json"
        },
        {
            "action": "Virtual Machine Scaleset example using Availability Zones",
            "description": "This template creates a VMSS placed in separate Availability Zones with a load balancer.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fmulti-vmss-linux-lb-zones%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fmulti-vmss-linux-lb-zones%2Fazuredeploy.json"
        },
        {
            "action": "Deploy multiple VM Scale Sets of Linux VMs.",
            "description": "This template allows you to deploy multiple VM Scale Sets of Linux VMs.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fmulti-vmss-linux%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fmulti-vmss-linux%2Fazuredeploy.json"
        },
        {
            "action": "Deploy multiple VM Scale Sets of Windows VMs.",
            "description": "This template allows you to deploy multiple VM Scale Sets of Windows VMs.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fmulti-vmss-windows%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fmulti-vmss-windows%2Fazuredeploy.json"
        },
        {
            "action": "Deploy the OS Patching extension on an Ubuntu VM",
            "description": "Azure Linux OSPatching extension enables the Azure VM administrators to automate the VM OS updates with customized configurations. This template shows a simple example to deploy the OSPatching Extension on a Linux VM.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fospatching-extension-on-ubuntu%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fospatching-extension-on-ubuntu%2Fazuredeploy.json"
        },
        {
            "action": "Deploy a Premium Windows VM",
            "description": "This template allows you to deploy a premium Windows VM using a few different options for the Windows version, using the latest patched version.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fpremium-storage-windows-vm%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fpremium-storage-windows-vm%2Fazuredeploy.json"
        },
        {
            "action": "Create an Azure Compute Gallery",
            "description": "This template allows you to create an Azure Compute Gallery.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fsig-create%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fsig-create%2Fazuredeploy.json"
        },
        {
            "action": "Create an Image Definition in an Azure Compute Gallery",
            "description": "This template allows you to create an Image Definition in an Azure Compute Gallery. Please ensure you have run the Shared Image Gallery 101 Template before you deploy this.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fsig-image-definition-create%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fsig-image-definition-create%2Fazuredeploy.json"
        },
        {
            "action": "Create an Image Version in an Azure Compute Gallery",
            "description": "This template allows you to create an Image Version in an Azure Compute Gallery. Please ensure that you have run the Azure Compute Gallery 101 Template and the Image Definition 101 Template before you deploy this.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fsig-image-version-create%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fsig-image-version-create%2Fazuredeploy.json"
        },
        {
            "action": "Create an ultra managed disk with a specific sector size",
            "description": "This template creates a new ultra managed disk allowing the user to specify a sector size of either 512 or 4096.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fultra-managed-disk%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fultra-managed-disk%2Fazuredeploy.json"
        },
        {
            "action": "Deploy a simple Linux VM and update private IP to static",
            "description": "This template allows you to deploy a simple Linux VM using Ubuntu from the marketplace. This will deploy a VNET, Subnet, and an A1 size VM in the resource group location with a dynamically assigned IP address and then convert it to static IP.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-automatic-static-ip%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-automatic-static-ip%2Fazuredeploy.json"
        },
        {
            "action": "Create VMs in Availability Sets using Resource Loops",
            "description": "This template allows you to create 'N' number of Virtual Machines in an availability set based on the 'numberOfInstances' parameter specified during the template deployment. This template also deploys a Virtual Network, a network security group and places the VMs in availability sets.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-copy-index-loops%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2%2Fquickstarts%2Fmicrosoft.compute%2Fvm-copy-index-loops%2Fazuredeploy.json"
        },
        {
            "action": "Multi VM Template with Managed Disk",
            "description": "This template will create N number of VM's with managed disks, public IPs and network interfaces. They will be provisioned in a single Availability Set and a Virtual Network will be created as part of the deployment.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-copy-managed-disks%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-copy-managed-disks%2Fazuredeploy.json"
        },
        {
            "action": "Azure Dedicated Hosts",
            "description": "This template will deploy an isolated environment using Azure Dedicated Hosts for you to provision VMs.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-dedicated-hosts%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-dedicated-hosts%2Fazuredeploy.json"
        },
        {
            "action": "Deploy a Premium Windows VM with diagnostics",
            "description": "This template allows you to deploy a Premium Windows VM using a few different options for the Windows version, using the latest patched version. In addition, it will provision the Diagnostics Extension on your behalf in a new, non-Premium Storage Account.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-diagnostics-extension-windows%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-diagnostics-extension-windows%2Fazuredeploy.json"
        },
        {
            "action": "Create a VM in a VNET in a different Resource Group",
            "description": "This template creates a VM in a VNET which is in a different Resource Group. You'll need to have the VNET created before running this template and pass the VNET name and its resource group name as input to this parameter.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-different-rg-vnet%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-different-rg-vnet%2Fazuredeploy.json"
        },
        {
            "action": "Join an existing Windows VM to AD Domain",
            "description": "This template allows you to join an existing Windows virtual machine into an existing Windows Active Directory Domain. For this template to work, we need certain prerequisites to be met, such as having one or more virtual machines to join to a domain, an Active Directory Forest with a accessible Domain Controller, and the necessary rights to join computers to the Active Directory Domain.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-domain-join-existing%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-domain-join-existing%2Fazuredeploy.json"
        },
        {
            "action": "Create a VM with a dynamic selection of data disks",
            "description": "This template allows the user to create a VM with a dynamic selection of data disks without creating a per size template with different numbers of data disks. It takes advantage of a copy property loop in the template to construct the desired number of data disks.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-dynamic-data-disks-selection%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-dynamic-data-disks-selection%2Fazuredeploy.json"
        },
        {
            "action": "Create a VM from a EfficientIP VHD",
            "description": "This template creates a VM from a EfficientIP VHD and lets you connect it to an existing VNET that can reside in another Resource Group than the virtual machine. Prerequisites include having an EfficientIP VHD file in a storage account, the name of the existing VNET and subnet to connect the new virtual machine to, the name of the Resource Group that the VNET resides in, and the name of the Network Security Group to attach to the virtual NIC.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-efficientip-vhd%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-efficientip-vhd%2Fazuredeploy.json"
        },
        {
            "action": "Create a VM from User Image",
            "description": "This template allows you to create a Virtual Machine from an unmanaged User image VHD. The template also deploys a Virtual Network, Public IP addresses, and a Network Interface. Prerequisites include having the generalized image VHD, a Storage Account for boot diagnostics, and other necessary resources.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-from-user-image%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-from-user-image%2Fazuredeploy.json"
        },
        {
            "action": "Create a VM from a Generalized VHD",
            "description": "This template creates a VM from a generalized VHD and allows you to connect it to a new or existing VNET. Prerequisites include having a generalized VHD file in a storage account and the name of the resource group, existing VNET, and subnet you want to connect the VM to if you're using an existing VNET.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-generalized-vhd-new-or-existing-vnet%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-generalized-vhd-new-or-existing-vnet%2Fazuredeploy.json"
        },
        {
            "action": "Create VM with Dynamic Data Disks and Docker",
            "description": "This template creates a single instance CentOS or Ubuntu Server with a configurable number of data disks, configurable sizes, and the latest Docker, Docker Compose, and Docker Machine. It also includes an Azure CLI container. The MDADM RAID0 Array is automounted and survives restarts.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-linux-dynamic-data-disks%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-linux-dynamic-data-disks%2Fazuredeploy.json"
        },
        {
            "action": "Create Linux VM with Serial Output",
            "description": "This template creates a simple Linux VM with minimal parameters and serial/console configured to output to storage.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-linux-serial-output%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-linux-serial-output%2Fazuredeploy.json"
        },
        {
            "action": "Deploy a Windows VM with Monitoring and Diagnostics",
            "description": "This template deploys a Windows VM along with the diagnostics extension, enabling monitoring and diagnostics for the VM.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-monitoring-diagnostics-extension%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-monitoring-diagnostics-extension%2Fazuredeploy.json"
        },
        {
            "action": "Deploy a Terraform Workstation as a Linux VM with Managed Identity",
            "description": "This template creates a Linux VM with a Managed Identity, installs Terraform, Azure CLI, and pre-configures Terraform remote state with the Azure backend. Optionally, it installs the Ubuntu Mate Desktop environment for development.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-msi-linux-terraform%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-msi-linux-terraform%2Fazuredeploy.json"
        },
        {
            "action": "Deploy a Linux VM with Managed Identity Accessing Storage",
            "description": "This template deploys a Linux VM (Ubuntu) with a system assigned managed identity (MSI) that has the necessary role assignment to access a storage account in a different resource group.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-msi-storage%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-msi-storage%2Fazuredeploy.json"
        },
        {
            "action": "Deploy a Linux or Windows VM with Managed Service Identity (MSI)",
            "description": "This template allows you to deploy a Linux or Windows VM with a Managed Service Identity (MSI). It demonstrates how to create a VM with a system-assigned identity, install the MSI extension to issue OAuth tokens for Azure resources, assign RBAC permissions to the Managed Identity, and run scripts using Azure CLI or PowerShell to log in using the MSI.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-msi%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-msi%2Fazuredeploy.json"
        },
        {
            "action": "Create a Windows Virtual Machine with 4 Empty Data Disks",
            "description": "This template creates a Windows Virtual Machine from a specified image, installs the VM Diagnostics Extension, and attaches 4 empty data disks. You can specify the size of each data disk during deployment. The template also provisions a Storage Account, Virtual Network, Public IP addresses, and a Network Interface.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-multiple-data-disk%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-multiple-data-disk%2Fazuredeploy.json"
        },
        {
            "action": "Deploy a VM with Multiple IP Configurations",
            "description": "This template deploys a Linux/Windows VM named myVM1 with 3 IP configurations: IPConfig-1, IPConfig-2, and IPConfig-3.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-multiple-ipconfig%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-multiple-ipconfig%2Fazuredeploy.json"
        },
        {
            "action": "Deploy a Linux VM (Ubuntu) with Multiple NICs",
            "description": "This template creates a VNet with multiple subnets and deploys a Ubuntu VM with multiple NICs.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-multiple-nics-linux%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-multiple-nics-linux%2Fazuredeploy.json"
        },
        {
            "action": "Deploy a Linux VM with Conditional Resources",
            "description": "This template allows deploying a Linux VM using new or existing resources for the Virtual Network, Storage, and Public IP Address. It also allows for choosing between SSH and Password authentication. The template uses conditions and logic functions to remove the need for nested deployments.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-new-or-existing-conditions%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-new-or-existing-conditions%2Fazuredeploy.json"
        },
        {
            "action": "Create VM from Existing VHDs and Connect to Existing VNET",
            "description": "This template creates a VM from specialized VHD and a data disk and lets you connect it to an existing VNET that can reside in another Resource Group than the virtual machine.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-os-disk-and-data-disk-existing-vnet%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-os-disk-and-data-disk-existing-vnet%2Fazuredeploy.json"
        },
        {
            "action": "Push a Certificate onto a Windows VM",
            "description": "This template allows you to push a certificate onto a Windows VM. It requires the URL of the secret in a Key Vault, which must be a secret (not a certificate or key). You can use a script to create a new certificate and put it into the vault. The script can be easily modified to work with an existing certificate.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-push-certificate-windows%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-push-certificate-windows%2Fazuredeploy.json"
        },
        {
            "action": "Secure VM Password with Key Vault",
            "description": "This template allows you to deploy a simple Windows VM by retrieving the password stored in a Key Vault. As a result, the password is never put in plain text in the template parameter file.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-secure-password%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-secure-password%2Fazuredeploy.json"
        },
        {
            "action": "Deploy a simple Linux VM with Accelerated Networking",
            "description": "This template allows you to deploy a simple Linux VM with Accelerated Networking using Ubuntu version 18.04-LTS with the latest patched version. This will deploy a D3_v2 size VM in the resource group location and return the FQDN of the VM.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-simple-linux-with-accelerated-networking%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-simple-linux-with-accelerated-networking%2Fazuredeploy.json"
        },
        {
            "action": "Deploy a simple Ubuntu Linux VM 18.04-LTS",
            "description": "This template deploys a Linux VM Ubuntu using the latest patched version. This will deploy a Standard_B2s size VM and a 18.04-LTS Version as defaultValue in the resource group location and will return the admin user name, Virtual Network Name, Network Security Group Name and FQDN.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-simple-linux%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-simple-linux%2Fazuredeploy.json"
        },
        {
            "action": "Red Hat Enterprise Linux VM (RHEL 7.8)",
            "description": "This template allows deploying a Red Hat Enterprise Linux VM (RHEL 7.8), using the latest image for the selected RHEL version. This will deploy a Standard A1_v2 VM in the location of your chosen resource group with an additional 100 GiB data disk attached to the VM.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-simple-rhel%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-simple-rhel%2Fazuredeploy.json"
        },
        {
            "action": "Deploy a Windows Server VM with Visual Studio.",
            "description": "This template deploys a Windows Server Datacenter 2019 VM with Visual Studio 2019 Community Edition, using the latest patched version. This will deploy a Standard_D2_v2 size VM in the resource group location and return the admin user name, networkSecurityGroupName, virtualNetworkName, and hostname.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-simple-windows-visualstudio2019%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-simple-windows-visualstudio2019%2Fazuredeploy.json"
        },
        {
            "action": "Deploy a simple Windows VM",
            "description": "This template allows you to deploy a simple Windows Generation 2 VM using a few different options for the Windows version, using the latest patched version. This will deploy a D2s_v3 size VM in the resource group location and return the fully qualified domain name of the VM.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-simple-windows%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-simple-windows%2Fazuredeploy.json"
        },
        {
            "action": "Deploy a VM into an Availability Zone",
            "description": "This template allows you to deploy a simple VM (Windows or Ubuntu), using the latest patched version. This will deploy an A2_v2 size VM in the location specified and return the FQDN of the VM.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-simple-zones%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-simple-zones%2Fazuredeploy.json"
        },
        {
            "action": "Existing SQL Server Auto Backup setup",
            "description": "This template setup or update on an existing SQL Server Virtual Machine on Azure with the Auto Backup Configuration",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-sql-existing-autobackup-update%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-sql-existing-autobackup-update%2Fazuredeploy.json"
        },
        {
            "action": "Existing SQL Server Auto Patching setup",
            "description": "This template setup or update on an existing SQL Server Virtual Machine on Azure with the Auto Patching Configuration",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-sql-existing-autopatching-update%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-sql-existing-autopatching-update%2Fazuredeploy.json"
        },
        {
            "action": "Existing SQL Server credentials setup with Azure Key Vault",
            "description": "This template setup or update on an existing SQL Server Virtual Machine on Azure with the credentials secured by Azure Key Vault",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-sql-existing-keyvault-update%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-sql-existing-keyvault-update%2Fazuredeploy.json"
        },
        {
            "action": "This template provisions a virtual machine with SQL Server 2014 SP2 and enables the Automated Backup feature.",
            "description": "The template creates a virtual machine with SQL Server 2014 SP2 on Windows Server 2012 R2 and configures the Automated Backup feature.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-sql-full-autobackup%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-sql-full-autobackup%2Fazuredeploy.json"
        },
        {
            "action": "This template provisions a virtual machine with SQL Server 2014 SP1 and enables the Auto Patching feature.",
            "description": "The template creates a virtual machine with SQL Server 2014 SP1 on Windows Server 2012 R2 and configures the Auto Patching feature.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-sql-full-autopatching%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-sql-full-autopatching%2Fazuredeploy.json"
        },
        {
            "action": "This template provisions a virtual machine with SQL Server 2014 SP1 and enables the Azure Key Vault Integration feature.",
            "description": "The template creates a virtual machine with SQL Server 2014 SP1 on Windows Server 2012 R2 and configures Azure Key Vault Integration.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-sql-full-keyvault%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-sql-full-keyvault%2Fazuredeploy.json"
        },
        {
            "action": "Create SQL Server 2014 SP1 Enterprise edition with Azure Key Vault Integration",
            "description": "This Azure Resource Manager template provisions a virtual machine running SQL Server 2014 SP1 Enterprise edition on Windows Server 2012 R2 with Azure Key Vault Integration enabled. It also creates additional resources such as a Virtual Network, Storage Accounts, a public IP address, network interface, and network security group.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-sql-full-keyvault%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-sql-full-keyvault%2Fazuredeploy.json"
        },
        {
            "action": "Create a Linux Virtual Machine with SSH rsa public key",
            "description": "This Azure Resource Manager template allows you to create a Linux Virtual Machine with SSH Keys. It deploys a Virtual Network with an inbound rule allowing only port 22 connections, Public IP addresses, a Public domain namespace, and a Network Interface. You can use your SSH rsa public key for authentication. This template provides quick steps and references for creating and using SSH keys on Azure Linux VMs.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-sshkey%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-sshkey%2Fazuredeploy.json"
        },
        {
            "action": "Deploy a simple Windows VM with tags",
            "description": "This Azure Resource Manager template allows you to deploy a simple Windows VM with various Windows version options. The template includes tags on the Virtual Machine, Storage Account, Public IP Address, Virtual Network, and Network Interface.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-tags%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-tags%2Fazuredeploy.json"
        },
        {
            "action": "Deploy a trusted launch capable Linux virtual machine",
            "description": "This Azure Resource Manager template deploys a trusted launch capable Linux virtual machine with various options for the Linux version. It also includes the Guest Attestation extension for remote attestation by the cloud. The default configuration is a Standard_D2s_v3 size virtual machine in the resource group location.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-trustedlaunch-linux%2Fazuredeploy.json/createUIDefinitionUri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%22Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-trustedlaunch-linux%2FcreateUiDefinition.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-trustedlaunch-linux%2Fazuredeploy.json"
        },
        {
            "action": "Deploy a trusted launch capable Windows virtual machine",
            "description": "This Azure Resource Manager template allows you to deploy a trusted launch capable Windows virtual machine with various options for the Windows version, using the latest patched version. It also includes the Guest Attestation extension for remote attestation by the cloud. The default configuration is a Standard_D2_v3 size virtual machine in the resource group location.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-trustedlaunch-windows%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-trustedlaunch-windows%2Fazuredeploy.json"
        },
        {
            "action": "Deploy a Virtual Machine with User Data",
            "description": "This Azure Resource Manager template allows you to create a Virtual Machine with User Data. It also deploys a Virtual Network, Public IP addresses, and a Network Interface.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-userdata%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-userdata%2Fazuredeploy.json"
        },
        {
            "action": "Virus attack on Virtual Machines Scenario",
            "description": "This template deploys 2 virtual machines, OMS, and other network resources. It simulates a virus attack and demonstrates the mitigation and prevention of a virus attack.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-virus-attack-prevention%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-virus-attack-prevention%2Fazuredeploy.json"
        },
        {
            "action": "Deploy a Windows VM with Windows Admin Center extension",
            "description": "This template allows you to deploy a Windows VM with Windows Admin Center extension to manage the VM directly from the Azure Portal.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-windows-admincenter%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-windows-admincenter%2Fazuredeploy.json"
        },
        {
            "action": "Deploy a Windows VM with Azure secure baseline",
            "description": "This template allows you to deploy a Windows VM running Windows Server in a new virtual network with a public IP address. The Azure secure baseline for Windows Server is applied using a guest configuration extension. If the machine's configuration drifts, you can re-apply the settings by deploying the template again.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-windows-baseline%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-windows-baseline%2Fazuredeploy.json"
        },
        {
            "action": "Deploy a Windows VM with a variable number of data disks",
            "description": "This template allows you to deploy a simple VM and specify the number of data disks at deployment time using a parameter. Note that the number and size of data disks are bound by the VM size. The VM size for this sample is Standard_DS4_v2 with a default of 16 data disks.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-windows-copy-datadisks%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-windows-copy-datadisks%2Fazuredeploy.json"
        },
        {
            "action": "Deploy a single Windows VM with Open SSH enabled for key-based authentication",
            "description": "This template allows you to quickly deploy a Windows Server VM with OpenSSH preinstalled and preconfigured. You need to provide your public SSH key as only key-based authentication is allowed. The template also adds and initializes a data disk of configurable size and installs vim as a shell editor.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-windows-ssh%2Fazuredeploy.json/createUIDefinitionUri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-windows-ssh%2FcreateUiDefinition.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-windows-ssh%2Fazuredeploy.json"
        },
        {
            "action": "Create a data management gateway and install on an Azure VM",
            "description": "This template deploys a virtual machine and creates a workable data management gateway",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-with-data-management-gateway%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-with-data-management-gateway%2Fazuredeploy.json"
        },
        {
            "action": "Create a virtual machine and create a NAT rule for RDP",
            "description": "This sample template demonstrates how to create a NAT rule in load balancer to allow RDP to a VM.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-with-rdp-port%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-with-rdp-port%2Fazuredeploy.json"
        },
        {
            "action": "Create a Windows Virtual Machine with empty StandardSSD_LRS data disks",
            "description": "This template allows you to create a Windows Virtual Machine from a specified image during the template deployment. It also attaches multiple empty Standard SSD data disks. Note that you can specify the size of each of the empty data disks. This template also deploys a Virtual Network, Public IP addresses, and a Network Interface.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-with-standardssd-disk%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.compute%2Fvm-with-standardssd-disk%2Fazuredeploy.json"
        }
    ],
    "Confidential Ledger": [
        {
            "action": "Create a Confidential Ledger",
            "description": "This template uses Confidential Ledger to log to an immutable, tamper-proof ledger. Azure Confidential Ledger provides a service for logging to an immutable, tamper-proof ledger. It runs in SGX enclaves and is built on Microsoft Research's Confidential Consortium Framework.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.confidentialledger%2Fconfidential-ledger-create%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.confidentialledger%2Fconfidential-ledger-create%2Fazuredeploy.json"
        }
    ],
    "Consumption": [
        {
            "action": "Create a Budget with Filter",
            "description": "This template shows how to create a budget to track cost or usage and get notified whenever a specified threshold is met. It is available to enterprise customers with an enterprise subscription.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.consumption%2Fcreate-budget-onefilter%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.consumption%2Fcreate-budget-onefilter%2Fazuredeploy.json"
        },
        {
            "action": "Create a Simple Budget",
            "description": "This template shows how to create a budget to track cost or usage and get notified whenever a specified threshold is met. It is available to enterprise customers with an enterprise subscription.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.consumption%2Fcreate-budget-simple%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.consumption%2Fcreate-budget-simple%2Fazuredeploy.json"
        },
        {
            "action": "Create a Budget",
            "description": "This template shows how to create a budget to track cost or usage and get notified whenever a specified threshold is met. It is available to enterprise customers with an enterprise subscription.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.consumption%2Fcreate-budget%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.consumption%2Fcreate-budget%2Fazuredeploy.json"
        }
    ],
    "Container Instance": [
        {
            "action": "Deploy a Linux container with a health probe using Azure Container Instances",
            "description": "This template demonstrates a simple use case for health probe of Azure Container Instances. The container will be restarted after it runs for 30 seconds because the file /tmp/healthy is deleted.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.containerinstance%2Faci-linuxcontainer-healthprobe%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.containerinstance%2Faci-linuxcontainer-healthprobe%2Fazuredeploy.json"
        },
        {
            "action": "Deploy a single Linux container accessible via a public IP using Azure Container Instances",
            "description": "This template demonstrates a use case for Azure Container Instances. It deploys a Linux container that is accessible via a public IP address.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.containerinstance%2Faci-linuxcontainer-public-ip%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.containerinstance%2Faci-linuxcontainer-public-ip%2Fazuredeploy.json"
        },
        {
            "action": "Deploy a Linux container with secure environment variables using Azure Container Instances",
            "description": "This template demonstrates a use case for Azure Container Instances. It deploys a Linux container with secure environment variables.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.containerinstance%2Faci-linuxcontainer-secure-environmentvariables%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.containerinstance%2Faci-linuxcontainer-secure-environmentvariables%2Fazuredeploy.json"
        },
        {
            "action": "Deploy two Linux containers with an emptyDir volume using Azure Container Instances",
            "description": "This template demonstrates a use case for Azure Container Instances. It deploys two Linux containers that share an emptyDir volume.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.containerinstance%2Faci-linuxcontainer-volume-emptydir%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.containerinstance%2Faci-linuxcontainer-volume-emptydir%2Fazuredeploy.json"
        },
        {
            "action": "Deploy a Linux container with a gitRepo volume using Azure Container Instances",
            "description": "This template demonstrates a use case for Azure Container Instances. It deploys a Linux container that uses a gitRepo volume to clone source code files from a GitHub repository and mounts them into the container.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.containerinstance%2Faci-linuxcontainer-volume-gitrepo%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.containerinstance%2Faci-linuxcontainer-volume-gitrepo%2Fazuredeploy.json"
        },
        {
            "action": "Azure Container Instances - container with secrets",
            "description": "This template demonstrates a simple use case for secret volumes of Azure Container Instances. When creating a container with the image containerinstance/helloworld:ssl, it sets up HTTP connections with the certificate and password passed in as secret volumes. A PFX certificate is encoded in Base64 and mounted as a secret volume. Inside the container, the certificate is accessible as a file with the path /mnt/secrets/sslCertificateData. The password of the PFX certificate is also encoded in Base64, and mounted as a secret volume. Inside the container, the certificate is accessible as a file with the path /mnt/secrets/sslCertificatePwd. The parameters sslCertificateData and sslCertificatePwd are only for demo purposes. Please create your own certificate when creating container groups.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.containerinstance%2Faci-linuxcontainer-volume-secret%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.containerinstance%2Faci-linuxcontainer-volume-secret%2Fazuredeploy.json"
        },
        {
            "action": "On-demand SFTP Server using an existing storage account",
            "description": "This template demonstrates an on-demand SFTP server using an Azure Container Instance (ACI). This version requires an existing Storage Account and File Share to exist in the same region as the ACI to be created. This File Share is then mounted into the main ACI to provide persistent storage after the container is terminated.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.containerinstance%2Faci-sftp-files-existing-storage%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.containerinstance%2Faci-sftp-files-existing-storage%2Fazuredeploy.json"
        },
        {
            "action": "Create an on-demand SFTP Server with persistent storage",
            "description": "This template demonstrates an on-demand SFTP server using an Azure Container Instance (ACI). It creates a Storage Account and a File Share via the Azure CLI using another ACI (based on the 101-aci-storage-file-share template also in this repository). This File Share is then mounted into the main ACI to provide persistent storage after the container is terminated.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.containerinstance%2Faci-sftp-files%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.containerinstance%2Faci-sftp-files%2Fazuredeploy.json"
        },
        {
            "action": "Create a Storage Account and a File Share via az-cli in Container Instance",
            "description": "This template demonstrates creating a Storage File Share via az-cli and Azure Container Instance. Modify the template to create a blob or other similar storage operation. The Azure Container Instance and az-cli can be used to create services not directly available in an Azure Resource Manager Template.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.containerinstance%2Faci-storage-file-share%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.containerinstance%2Faci-storage-file-share%2Fazuredeploy.json"
        },
        {
            "action": "UDP Container in ACI",
            "description": "This templates deploys a public linux container into Azure Container Instances, assigns a public IP, and exposes a UDP port to the container.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.containerinstance%2Faci-udp%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.containerinstance%2Faci-udp%2Fazuredeploy.json"
        },
        {
            "action": "Azure Container Instances - VNet",
            "description": "This template demonstrates a simple use case for deploying a container instance into an Azure virtual network.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.containerinstance%2Faci-vnet%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.containerinstance%2Faci-vnet%2Fazuredeploy.json"
        },
        {
            "action": "Deploy a managed Kubernetes Cluster with AAD (AKS)",
            "description": "This ARM template demonstrates the deployment of an AKS instance with advanced networking features into an existing virtual network and Azure AD Integration. Additionally, the chosen Service Principal is assigned the Network Contributor role against the subnet that contains the AKS cluster.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.containerinstance%2Faks-advanced-networking-aad%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.containerinstance%2Faks-advanced-networking-aad%2Fazuredeploy.json"
        },
        {
            "action": "Deploy a managed Kubernetes Cluster (AKS)",
            "description": "This ARM template demonstrates the deployment of an AKS instance with advanced networking features into an existing virtual network. Additionally, the chosen Service Principal is assigned the Network Contributor role against the subnet that contains the AKS cluster.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.containerinstance%2Faks-advanced-networking%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.containerinstance%2Faks-advanced-networking%2Fazuredeploy.json"
        },
        {
            "action": "Deploy an AKS cluster for Azure ML",
            "description": "This template allows you to deploy an enterprise compliant AKS cluster which can be attached to Azure ML. The AKS cluster in this template is MSI (Managed Service Identity) enabled and fulfills the conditions to be attached with Azure ML as compute target resources.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.containerinstance%2Faks-azml-targetcompute%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.containerinstance%2Faks-azml-targetcompute%2Fazuredeploy.json"
        }
    ],
    "Container Registry": [
        {
            "action": "Azure Container Registry with Geo-replication Template",
            "description": "This template deploys an Azure Container Registry with geo-replication enabled, allowing you to create your own Docker image registry. The Azure Container Registry is set to Premium SKU, which is required to support Geo-Replication.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.containerregistry%2Fcontainer-registry-geo-replication%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.containerregistry%2Fcontainer-registry-geo-replication%2Fazuredeploy.json"
        },
        {
            "action": "Azure Container Registry with Policies and Diagnostics (bicep)",
            "description": "This module deploys an Azure Container Registry with policies and diagnostic logs. You can optionally configure system/user assigned identities, IP rules, public access, and zone redundancy.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.containerregistry%2Fcontainer-registry-with-policies-and-diagnostics%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.containerregistry%2Fcontainer-registry-with-policies-and-diagnostics%2Fazuredeploy.json"
        },
        {
            "action": "Simple Azure Container Registry Template",
            "description": "This template deploys an Azure Container Registry. Azure Container Registry is a PaaS offer for creating your own Docker image registry.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.containerregistry%2Fcontainer-registry%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.containerregistry%2Fcontainer-registry%2Fazuredeploy.json"
        }
    ],
    "Cost Management": [
        {
            "action": "FinOps Hub Template",
            "description": "This template creates a new FinOps hub instance, including Data Lake storage and a Data Factory.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.costmanagement%2Ffinops-hub%2Fazuredeploy.json/createUIDefinitionUri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.costmanagement%2Ffinops-hub%2FcreateUiDefinition.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.costmanagement%2Ffinops-hub%2Fazuredeploy.json"
        },
        {
            "action": "Cost Optimization Workbook",
            "description": "This template creates a new Azure Monitor workbook for cost optimization based on the Well-Architected Framework.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.costmanagement%2Foptimization-workbook%2Fazuredeploy.json/createUIDefinitionUri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.costmanagement%2Foptimization-workbook%2FcreateUiDefinition.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.costmanagement%2Foptimization-workbook%2Fazuredeploy.json"
        }
    ],
    "Custom Providers": [
        {
            "action": "Extend Existing Azure Resources with Custom Providers",
            "description": "This sample Azure Resource Manager template deploys a custom resource provider to Azure that extends the Azure Resource Manager API. It shows how to extend existing resources outside the resource group where the custom provider instance lives.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.customproviders%2Fcustom-rp-existing-resource-deployments%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.customproviders%2Fcustom-rp-existing-resource-deployments%2Fazuredeploy.json"
        },
        {
            "action": "Create a function app and call it using a Custom Resource",
            "description": "This sample Azure Resource Manager template deploys a custom resource provider to Azure that extends the Azure Resource Manager API set with custom abilities and then utilizes the new extension to deploy 'customResources'.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.customproviders%2Fcustom-rp-with-function%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.customproviders%2Fcustom-rp-with-function%2Fazuredeploy.json"
        },
        {
            "action": "Create a Custom Resource for templates with Custom Providers",
            "description": "This sample Azure Resource Manager template deploys a custom resource provider to Azure that extends the Azure Resource Manager API. In this sample, the custom resource provider is powered by an Azure Logic App, but any public API endpoint can be used.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.customproviders%2Fcustom-rp-with-logicapp%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.customproviders%2Fcustom-rp-with-logicapp%2Fazuredeploy.json"
        }
    ],
    "Data Bricks": [
        {
            "action": "Deploy an Azure Databricks Workspace with private endpoint, managed svc & CMK & DBFS encryption",
            "description": "This template allows you to create a Azure Databricks workspace with privateendpoint and all three forms of customer managed keys (CMK).",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.databricks%2Fdatabricks-all-in-one-template-for-privateendpoint-cmk-all-forms%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.databricks%2Fdatabricks-all-in-one-template-for-privateendpoint-cmk-all-forms%2Fazuredeploy.json"
        },
        {
            "action": "Create a network security group, Virtual Network, and Azure Databricks Workspace with Virtual Network and Private Endpoint",
            "description": "This template allows you to create a network security group, a Virtual Network, and an Azure Databricks Workspace with Virtual Network and Private Endpoint.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.databricks%2Fdatabricks-all-in-one-template-for-vnet-injection-privateendpoint%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.databricks%2Fdatabricks-all-in-one-template-for-vnet-injection-privateendpoint%2Fazuredeploy.json"
        },
        {
            "action": "Create a Virtual Network for Azure Databricks VNet injection",
            "description": "This template allows you to create a Virtual Network for Azure Databricks VNet injection.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.databricks%2Fdatabricks-vnet-for-vnet-injection%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.databricks%2Fdatabricks-vnet-for-vnet-injection%2Fazuredeploy.json"
        },
        {
            "action": "Create an Azure Databricks workspace with a custom virtual network address range",
            "description": "This template allows you to create an Azure Databricks workspace with a custom virtual network address range.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/urihttps://3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.databricks%2Fdatabricks-workspace-with-custom-vnet-address%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.databricks%2Fdatabricks-workspace-with-custom-vnet-address%2Fazuredeploy.json"
        },
        {
            "action": "Deploy an Azure Databricks workspace with all 3 forms of CMK (Customer Managed Keys)",
            "description": "This template allows you to create an Azure Databricks workspace with all three forms of customer managed keys (CMK).",
            "link": "https://portal.azure.com/#create/Microsoft.Template/urihttps://3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.databricks%2Fdatabricks-workspace-with-customer-managed-keys-all-forms%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.databricks%2Fdatabricks-workspace-with-customer-managed-keys-all-forms%2Fazuredeploy.json"
        },
        {
            "action": "Deploy an Azure Databricks workspace with CMK for DBFS root encryption",
            "description": "This template allows you to create an Azure Databricks workspace with CMK for DBFS (Databricks File System) root encryption.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.databricks%2Fdatabricks-workspace-with-dbfs-root-customer-managed-keys%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.databricks%2Fdatabricks-workspace-with-dbfs-root-customer-managed-keys%2Fazuredeploy.json"
        },
        {
            "action": "Deploy an Azure Databricks Workspace with Managed Disks CMK",
            "description": "This template allows you to create an Azure Databricks workspace with Managed Disks CMK (Customer Managed Key).",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.databricks%2Fdatabricks-workspace-with-managed-disk-customer-managed-keys%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.databricks%2Fdatabricks-workspace-with-managed-disk-customer-managed-keys%2Fazuredeploy.json"
        },
        {
            "action": "Deploy Azure Databricks Workspace with Managed Services CMK",
            "description": "This template allows you to create an Azure Databricks workspace with Managed Services CMK (Customer Managed Key).",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.databricks%2Fdatabricks-workspace-with-managed-services-customer-managed-keys%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.databricks%2Fdatabricks-workspace-with-managed-services-customer-managed-keys%2Fazuredeploy.json"
        },
        {
            "action": "Deploy Azure Databricks Workspace with VNet Injection",
            "description": "This template allows you to create an Azure Databricks workspace with VNet injection into a custom virtual network.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.databricks%2Fdatabricks-workspace-with-vnet-injection%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.databricks%2Fdatabricks-workspace-with-vnet-injection%2Fazuredeploy.json"
        },
        {
            "action": "Deploy Azure Databricks Workspace",
            "description": "This template allows you to create an Azure Databricks workspace.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.databricks%2Fdatabricks-workspace%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.databricks%2Fdatabricks-workspace%2Fazuredeploy.json"
        }
    ],
    "Data Dog": [
        {
            "action": "Create a new Datadog Organization",
            "description": "This template deploys a new Datadog – An Azure Native ISV Service resource and creates a new organization in Datadog’s US3 site to monitor resources in your Azure subscription.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.datadog%2Fdatadog%2Fazuredeploy.json/createUIDefinitionUri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.datadog%2Fdatadog%2FcreateUiDefinition.json"
        }
    ],
    "Data Factory": [
        {
            "action": "Create a Data Factory pipeline",
            "description": "This template creates a Data Factory pipeline that copies data from a file in a Blob Storage into a SQL Database table while invoking a Stored Procedure (SProc).",
            "link": "https://azure.microsoft.com/documentation/articles/data-factory-stored-proc-activity/",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.datafactory%2Fdata-factory-blob-to-sql-copy-stored-proc%2Fazuredeploy.json"
        },
        {
            "action": "Create a Data Factory pipeline",
            "description": "This template creates a Data Factory pipeline that copies data from an Azure Blob into an Azure SQL Database.",
            "link": "https://azure.microsoft.com/documentation/articles/data-factory-copy-data-from-azure-blob-storage-to-sql-database/",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.datafactory%2Fdata-factory-blob-to-sql-copy%2Fazuredeploy.json"
        },
        {
            "action": "Deploy a new Data Factory",
            "description": "This template deploys a new Data Factory and requisite objects to facilitate a two-activity chained Data Factory pipeline. The first leg of the pipeline pulls data from an on-premises SQL server source into Azure Data Lake Store in Apache ORC columnar storage format using data management gateway. The second leg of the pipeline pulls data from ORC files in Azure Data Lake Store and inserts it into Azure SQL as the final destination.",
            "link": "https://docs.microsoft.com/azure/data-factory/data-factory-data-movement-security-considerations",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.datafactory%2Fdata-factory-chained-copy-activities%2Fazuredeploy.json"
        },
        {
            "action": "Create a blob for the Data Factory Copy Data Tool quickstart",
            "description": "This template creates a blob storage and uploads a file for the copy data tool quickstart in Azure Data Factory. It sets up an Azure Storage linked service, Azure Blob dataset, and a pipeline with a copy activity.",
            "link": "https://azurequickstartsservice.blob.core.windows.net/assets/201/data-factory-copy-data-tool/azuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.datafactory%2Fdata-factory-copy-data-tool%2Fazuredeploy.json"
        },
        {
            "action": "One click to try Azure Data Factory",
            "description": "This template creates a data factory pipeline for a copy activity from Azure Blob into another Azure Blob. It demonstrates the capabilities of Azure Data Factory and includes Azure Storage linked services, Azure Blob datasets, and a pipeline with a copy activity.",
            "link": "https://azurequickstartsservice.blob.core.windows.net/assets/201/data-factory-get-started/azuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.datafactory%2Fdata-factory-get-started%2Fazuredeploy.json"
        },
        {
            "action": "Bulk copy using Azure Data Factory",
            "description": "This template creates a data factory that copies a number of tables from Azure SQL Database to Azure SQL Data Warehouse.",
            "link": "https://azurequickstartsservice.blob.core.windows.net/assets/201/data-factory-v2-azure-sql-database-to-sql-data-warehouse-copy/azuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.datafactory%2Fdata-factory-v2-azure-sql-database-to-sql-data-warehouse-copy%2Fazuredeploy.json"
        },
        {
            "action": "Create a V2 data factory",
            "description": "This template creates a data factory of version 2 with a pipeline that copies data from one folder to another in an Azure Blob Storage.",
            "link": "https://azurequickstartsservice.blob.core.windows.net/assets/201/data-factory-v2-blob-to-blob-copy/azuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.datafactory%2Fdata-factory-v2-blob-to-blob-copy%2Fazuredeploy.json"
        },
        {
            "action": "Create a V2 data factory (MySQL)",
            "description": "This template creates a data factory of version 2 with a pipeline that copies data from a folder in an Azure Blob Storage to a table in an Azure Database for MySQL.",
            "link": "https://azurequickstartsservice.blob.core.windows.net/assets/201/data-factory-v2-blob-to-mysql-copy/azuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.datafactory%2Fdata-factory-v2-blob-to-mysql-copy%2Fazuredeploy.json"
        },
        {
            "action": "Create a V2 data factory (PostgreSql)",
            "description": "This template creates a data factory of version 2 with a pipeline that copies data from a folder in an Azure Blob Storage to a table in an Azure Database for PostgreSQL.",
            "link": "https://azurequickstartsservice.blob.core.windows.net/assets/201/data-factory-v2-blob-to-postgresql-copy/azuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.datafactory%2Fdata-factory-v2-blob-to-postgresql-copy%2Fazuredeploy.json"
        },
        {
            "action": "Create an empty data factory",
            "description": "This template creates an empty data factory of version 2.",
            "link": "https://azurequickstartsservice.blob.core.windows.net/assets/201/data-factory-v2-create/azuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.datafactory%2Fdata-factory-v2-create%2Fazuredeploy.json"
        },
        {
            "action": "Create a V2 data factory (SQL On-prem)",
            "description": "This template creates a data factory of version 2 with a pipeline that copies data from an on-premises SQL Server to an Azure blob storage.",
            "link": "https://azurequickstartsservice.blob.core.windows.net/assets/201/data-factory-v2-onprem-sql-to-blob-copy/azuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.datafactory%2Fdata-factory-v2-onprem-sql-to-blob-copy%2Fazuredeploy.json"
        },
        {
            "action": "Provision SSIS runtime in Azure",
            "description": "This template creates a data factory of version 2, and then configures an Azure SSIS integration runtime in the cloud.",
            "link": "https://azurequickstartsservice.blob.core.windows.net/assets/201/data-factory-v2-provision-ssis-runtime/azuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.datafactory%2Fdata-factory-v2-provision-ssis-runtime%2Fazuredeploy.json"
        },
        {
            "action": "Create a V2 data factory (Spark)",
            "description": "This template creates a data factory of version 2 with a pipeline that copies data from one folder to another in an Azure Blob Storage.",
            "link": "https://azurequickstartsservice.blob.core.windows.net/assets/201/data-factory-v2-transform-using-spark/azuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.datafactory%2Fdata-factory-v2-transform-using-spark%2Fazuredeploy.json"
        },
        {
            "action": "Create HA data management gateway and install on an Azure VMs",
            "description": "This template deploys multiple virtual machines with a highly available data management gateway for Azure Data Factory.",
            "link": "https://azurequickstartsservice.blob.core.windows.net/assets/206/mutiple-vms-with-data-management-gateway/azuredeploy.json"
        },
        {
            "action": "Deploy Azure Data Factory VM Gateway",
            "description": "This template deploys multiple virtual machines with workable HA data management gateway.",
            "link": "Link to the Template",
            "visualize": "Visualize the Template"
        },
        {
            "action": "Create HA Data Management Gateway on Azure VMs",
            "description": "This template deploys multiple virtual machines with a workable HA data management gateway.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.datafactory%2Fmutiple-vms-with-data-management-gateway%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.datafactory%2Fmutiple-vms-with-data-management-gateway%2Fazuredeploy.json"
        }
    ],
    "Data Lake Store": [
        {
            "action": "Deploy Data Lake Analytics on a new Data Lake Store",
            "description": "This template allows you to deploy a new Data Lake Analytics account on a new Data Lake Store account.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.datalakestore%2Fdata-lake-analytics%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.datalakestore%2Fdata-lake-analytics%2Fazuredeploy.json"
        },
        {
            "action": "Deploy Azure Data Lake Store account with data encryption",
            "description": "This template allows you to deploy an Azure Data Lake Store account with data encryption enabled. This account uses the Data Lake Store account for the encryption key management.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.datalakestore%2Fdata-lake-store-encryption-adls%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.datalakestore%2Fdata-lake-store-encryption-adls%2Fazuredeploy.json"
        },
        {
            "action": "Deploy Azure Data Lake Store account with data encryption using Azure Key Vault",
            "description": "This template allows you to deploy an Azure Data Lake Store account with data encryption enabled. This account uses Azure Key Vault to manage the encryption key.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.datalakestore%2Fdata-lake-store-encryption-key-vault%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.datalakestore%2Fdata-lake-store-encryption-key-vault%2Fazuredeploy.json"
        },
        {
            "action": "Deploy Azure Data Lake Store with no data encryption",
            "description": "This template allows you to deploy an Azure Data Lake Store account with data encryption disabled.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.datalakestore%2Fdata-lake-store-no-encryption%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.datalakestore%2Fdata-lake-store-no-encryption%2Fazuredeploy.json"
        }

    ],
    "Data Migration": [
        {
            "action": "Migrate to Azure SQL database using Azure DMS",
            "description": "The Azure Database Migration Service (DMS) is designed to streamline the process of migrating on-premises databases to Azure. DMS will simplify the migration of existing on-premises SQL Server and Oracle databases to Azure SQL Database, Azure SQL Managed Instance, or Microsoft SQL Server in an Azure Virtual Machine. This template would deploy an instance of Azure Database Migration service, an Azure VM with SQL server installed on it which will act as a Source server with a pre-created database on it and a Target Azure SQL DB server which will have a pre-created schema of the database to be migrated from Source to Target server. The template will also deploy the required resources like NIC, VNET, etc for supporting the Source VM, DMS service, and Target server.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.datamigration%2Fazure-database-migration-service%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.datamigration%2Fazure-database-migration-service%2Fazuredeploy.json"
        },
        {
            "action": "Deploy Azure Database Migration Service (DMS)",
            "description": "Azure Database Migration Service is a fully managed service designed to enable seamless migrations from multiple database sources to Azure data platforms with minimal downtime (online migrations).",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.datamigration%2Fazure-database-migration-simple-deploy%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.datamigration%2Fazure-database-migration-simple-deploy%2Fazuredeploy.json"
        }

    ],
    "Data Protection": [
        {
            "action": "Create Disk & enable protection via Backup Vault",
            "description": "This template creates a disk and enables protection via Azure Backup. A disaster recovery and data protection strategy keeps your business running when unexpected events occur. The Backup service is Microsoft's born-in-the-cloud backup solution to backup data that's located on-premises and in Azure. It replaces your existing on-premises or offsite backup solution with a reliable, secure, and cost-competitive cloud backup solution. It also provides the flexibility of protecting your assets running in the cloud. Learn more at [Backup Overview](http://aka.ms/backup-learn-more/). Azure Disk Backup is a native, cloud-based backup solution that protects your data in managed disks. It's a simple, secure, and cost-effective solution that enables you to configure protection for managed disks in a few steps, assuring that you can recover your data in a disaster scenario. Learn more at [Azure Disk Backup Overview](https://docs.microsoft.com/azure/backup/disk-backup-overview).",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.dataprotection%2Fbackup-create-disk-enable-protection%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.dataprotection%2Fbackup-create-disk-enable-protection%2Fazuredeploy.json"
        },
        {
            "action": "Create Storage Account & enable protection via Backup Vault",
            "description": "This template creates a storage account and enables blobs protection via Azure Backup. A disaster recovery and data protection strategy keeps your business running when unexpected events occur. The Backup service is Microsoft's born-in-the-cloud backup solution to backup data that's located on-premises and in Azure. It replaces your existing on-premises or offsite backup solution with a reliable, secure, and cost-competitive cloud backup solution. It also provides the flexibility of protecting your assets running in the cloud. Learn more at [Backup Overview](http://aka.ms/backup-learn-more/). Operational backup for Azure Blobs is a managed, local data protection solution that lets you protect your block blobs from various data loss scenarios like blob corruptions, blob deletions, and accidental storage account deletion. The data is stored locally within the source storage account itself and can be restored to a selected point in time whenever needed. This provides a simple, secure, and cost-effective means to protect your blobs. Learn more at [Azure Blob Backup Overview](https://docs.microsoft.com/azure/backup/blob-backup-overview).",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.dataprotection%2Fbackup-create-storage-account-enable-protection%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.dataprotection%2Fbackup-create-storage-account-enable-protection%2Fazuredeploy.json"
        },
        {
            "action": "Create Backup Vault",
            "description": "This template creates a Backup Vault, which is an essential part of a disaster recovery and data protection strategy. The Backup service is Microsoft's born-in-the-cloud backup solution designed to back up data located on-premises and in Azure. It replaces existing on-premises or offsite backup solutions with a reliable, secure, and cost-competitive cloud backup solution. It also offers flexibility for protecting assets running in the cloud. Learn more at [Backup Overview](http://aka.ms/backup-learn-more/).",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.dataprotection%2Fbackup-vault-basic%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.dataprotection%2Fbackup-vault-basic%2Fazuredeploy.json"
        }

    ],
    "Data Share": [
        {
            "action": "Create a Data Share Account",
            "description": "This template creates a data share account in Azure. When you deploy this Azure Resource Manager template, a data share account is created. You can find more information about data sharing in Azure at [Azure Data Share Overview](https://docs.microsoft.com/azure/data-share/overview).",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.datashare%2Fdata-share-account%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.datashare%2Fdata-share-account%2Fazuredeploy.json"
        },
        {
            "action": "Create a Data Share from a Storage Account",
            "description": "This template creates a storage account and a data share from the storage account in Azure. It helps you share data with roles and requirements for Azure Data Share, which you can learn more about at [Roles and requirements for Azure Data Share](https://docs.microsoft.com/azure/data-share/concepts-roles-permissions#roles-and-requirements). To learn more about how to deploy the template, see the [quickstart](https://docs.microsoft.com/azure/data-share/share-your-data-arm) article.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.datashare%2Fdata-share-share-storage-account%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.datashare%2Fdata-share-share-storage-account%2Fazuredeploy.json"
        },
        {
            "action": "Create a Data Share",
            "description": "This template creates a data share provider share in Azure. It allows you to share data with roles and requirements for Azure Data Share, which you can learn more about at [Roles and requirements for Azure Data Share](https://docs.microsoft.com/azure/data-share/concepts-roles-permissions#roles-and-requirements).",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.datashare%2Fdata-share-share%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.datashare%2Fdata-share-share%2Fazuredeploy.json"
        }
    ],
    "Devcenter": [
        {
            "action": "Deploy Dev Box Service with built-in image",
            "description": "This template provides a way to deploy a Dev Box service with a built-in image including Dev Center, Dev box Project, Dev box Definition, Dev box pool, Network connection, and Virtual Network.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.devcenter%2Fdevbox-with-builtin-image%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.devcenter%2Fdevbox-with-builtin-image%2Fazuredeploy.json"
        },
        {
            "action": "Configure Dev Box service",
            "description": "This template would create all Dev Box admin resources as per Dev Box quick start guide. You can view all resources created or directly go to DevPortal.microsoft.com to create your first Dev Box.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.devcenter%2Fdevbox-with-customized-image%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.devcenter%2Fdevbox-with-customized-image%2Fazuredeploy.json"
        }

    ],
    "Devices": [
        {
            "action": "Create an IoT Hub and Ubuntu Edge Simulator",
            "description": "The purpose of this ARM Template is to deploy an IoT Hub with an Ubuntu Edge Simulator. The Linux Ubuntu virtual machine is configured to be an IoT Edge device.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.devices%2Fiot-iothub-edgeemulator-vm%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.devices%2Fiot-iothub-edgeemulator-vm%2Fazuredeploy.json"
        },
        {
            "action": "Use ARM template to create IoT Hub, route, and view messages",
            "description": "This template creates an IoT Hub instance and a storage account, and shows how to auto-route messages to storage.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.devices%2Fiothub-auto-route-messages%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.devices%2Fiothub-auto-route-messages%2Fazuredeploy.json"
        },
        {
            "action": "Create an IoT Hub Device Provisioning Service",
            "description": "This template creates an IoT hub and an IoT Hub Device Provisioning Service, and links the two services together.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.devices%2Fiothub-device-provisioning%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.devices%2Fiothub-device-provisioning%2Fazuredeploy.json"
        },
        {
            "action": "Create an IoT Hub and a Device to Cloud Consumer Group",
            "description": "This template creates an IoT Hub instance with device to cloud and cloud to device messaging configurations and a device to cloud consumer group.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.devices%2Fiothub-with-consumergroup-create%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.devices%2Fiothub-with-consumergroup-create%2Fazuredeploy.json"
        }
    ],
    "Device Update": [
        {
            "action": "Create Device Update for IoT Hub account, instance, IoT Hub.",
            "description": "This template creates an account, an instance, and a hub to link the instance with. It configures the hub with the necessary access policies, routes, and consumer group.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.deviceupdate%2Fdeviceupdate-create-account-instance-iothub%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.deviceupdate%2Fdeviceupdate-create-account-instance-iothub%2Fazuredeploy.json"
        },
        {
            "action": "Create Device Update for IoT Hub account",
            "description": "This template creates an account that provides a public DNS record and allows making REST API calls to Data Plane.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.deviceupdate%2Fdeviceupdate-create-account%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.deviceupdate%2Fdeviceupdate-create-account%2Fazuredeploy.json"
        }

    ],
    "Digital Twins": [
        {
            "action": "Azure Digital Twins with Function and Private Link service",
            "description": "This template creates an Azure Digital Twins service configured with a Virtual Network connected Azure function that can communicate through a Private Link Endpoint to Digital Twins. It also creates a Private DNS Zone to allow seamless hostname resolution of the Digital Twins Endpoint from the Virtual Network to the Private Endpoint internal subnet IP address. The hostname is stored as a setting to the Azure function with the name 'ADT_ENDPOINT'.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.digitaltwins%2Fdigitaltwins-with-function-private-link%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.digitaltwins%2Fdigitaltwins-with-function-private-link%2Fazuredeploy.json"
        },
        {
            "action": "Azure Digital Twins with Time Data History Connection",
            "description": "This template creates an Azure Digital Twins instance configured with a time series data history connection. In order to create a connection, other resources must be created such as an Event Hubs namespace, an event hub, Azure Data Explorer cluster, and a database. Data is sent to an event hub which eventually forwards the data to the Azure Data Explorer cluster. Data is stored in a database table in the cluster.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.digitaltwins%2Fdigitaltwins-with-function-time-series-database-connection%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.digitaltwins%2Fdigitaltwins-with-function-time-series-database-connection%2Fazuredeploy.json",
        }

    ],
    "Document DB": [
        {
            "action": "Create autoscale Azure Cosmos DB account for Cassandra API",
            "description": "This template creates an Azure Cosmos DB account for Cassandra API in two regions with a keyspace and table with autoscale throughput. The template allows you to configure various parameters such as consistency level, primary and secondary regions, system-managed failover, keyspace name, table name, and autoscale max throughput.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.documentdb%2Fcosmosdb-cassandra-autoscale%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.documentdb%2Fcosmosdb-cassandra-autoscale%2Fazuredeploy.json"
        },

        {
            "action": "Create an Azure CosmosDB Account",
            "description": "This ARM template is intended to create a Cosmos DB Account quickly with the minimal required values.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.documentdb%2Fcosmosdb-create-account%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.documentdb%2Fcosmosdb-create-account%2Fazuredeploy.json"
        },
        {
            "action": "Create an Azure Cosmos DB account in multiple regions",
            "description": "This template creates an Azure Cosmos DB account for any database API type with a primary and secondary region with a choice of consistency level and failover type.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.documentdb%2Fcosmosdb-create-multi-region-account%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.documentdb%2Fcosmosdb-create-multi-region-account%2Fazuredeploy.json"
        },
        {
            "action": "Create a free-tier Azure Cosmos DB account",
            "description": "This template creates a free-tier Azure Cosmos DB account for SQL API with a database with shared throughput and container.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.documentdb%2Fcosmosdb-free%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.documentdb%2Fcosmosdb-free%2Fazuredeploy.json"
        },
        {
            "action": "Create an Azure Cosmos DB account for Gremlin API autoscale",
            "description": "This template creates an Azure Cosmos DB account for Gremlin API in two regions with one database and one graph using autoscale throughput.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.documentdb%2Fcosmosdb-gremlin-autoscale%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.documentdb%2Fcosmosdb-gremlin-autoscale%2Fazuredeploy.json"
        },
        {
            "action": "Create an Azure Cosmos DB account for Gremlin API",
            "description": "This template creates an Azure Cosmos DB account for Gremlin API in two regions with one database and one graph using dedicated throughput.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.documentdb%2Fcosmosdb-gremlin%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.documentdb%2Fcosmosdb-gremlin%2Fazuredeploy.json"
        },
        {
            "action": "Create an Azure Cosmos DB account for MongoDB API",
            "description": "This template creates an Azure Cosmos DB account for MongoDB API 4.2 in two regions using shared and dedicated throughput with two collections.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.documentdb%2Fcosmosdb-mongodb%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.documentdb%2Fcosmosdb-mongodb%2Fazuredeploy.json"
        },
        {
            "action": "Create an Azure Cosmos DB Account with a private endpoint",
            "description": "This template will create a Cosmos account, a virtual network, and a private endpoint exposing the Cosmos account to the virtual network.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.documentdb%2Fcosmosdb-private-endpoint%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.documentdb%2Fcosmosdb-private-endpoint%2Fazuredeploy.json"
        },
        {
            "action": "Create an Azure Cosmos DB account for Core (SQL) API with analytical store",
            "description": "This template creates an Azure Cosmos account for Core (SQL) API with a database and container configured with autoscale and analytical store.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.documentdb%2Fcosmosdb-sql-analytical-store%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.documentdb%2Fcosmosdb-sql-analytical-store%2Fazuredeploy.json"
        },
        {
            "action": "Create an Azure Cosmos DB account for Core (SQL) API with autoscale",
            "description": "This template creates an Azure Cosmos account for Core (SQL) API, provisioned for two regions, a database, a container configured for autoscale throughput showing multiple indexing and policy options.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.documentdb%2Fcosmosdb-sql-autoscale%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.documentdb%2Fcosmosdb-sql-autoscale%2Fazuredeploy.json"
        },
        {
            "action": "Create Azure Cosmos DB Core (SQL) API stored procedures",
            "description": "This template creates an Azure Cosmos account for Core (SQL) API and a container with a stored procedure, trigger, and user-defined function.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.documentdb%2Fcosmosdb-sql-container-sprocs%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.documentdb%2Fcosmosdb-sql-container-sprocs%2Fazuredeploy.json"
        },
        {
            "action": "Create a minimal Azure Cosmos DB account for Core (SQL) API",
            "description": "This template creates an Azure Cosmos account for Core (SQL) API provisioned for a single region using the minimum required resource properties.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.documentdb%2Fcosmosdb-sql-minimal%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.documentdb%2Fcosmosdb-sql-minimal%2Fazuredeploy.json"
        },
        {
            "action": "Create Azure Cosmos with SQL API and multiple containers",
            "description": "This template creates an Azure Cosmos account for Core (SQL) API, a database, and multiple containers with names and partition keys as specified. You can keep adding containers by extending the containers array.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.documentdb%2Fcosmosdb-sql-multiple-containers%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.documentdb%2Fcosmosdb-sql-multiple-containers%2Fazuredeploy.json"
        },
        {
            "action": "Create Azure Cosmos DB SQL Account with data plane RBAC",
            "description": "This template will create a SQL Cosmos account, a natively maintained Role Definition, and a natively maintained Role Assignment for an AAD identity.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.documentdb%2Fcosmosdb-sql-rbac%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.documentdb%2Fcosmosdb-sql-rbac%2Fazuredeploy.json"
        },
        {
            "action": "Create a Serverless Azure Cosmos DB account for SQL API",
            "description": "This template will create a serverless Azure Cosmos account for Core (SQL) API provisioned for a single region.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.documentdb%2Fcosmosdb-sql-serverless%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.documentdb%2Fcosmosdb-sql-serverless%2Fazuredeploy.json"
        },
        {
            "action": "Create an Azure Cosmos DB account for Core (SQL) API",
            "description": "This template will create an Azure Cosmos DB account for Core (SQL) API, in two regions, a database and container with dedicated throughput showing multiple indexing and policy options.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.documentdb%2Fcosmosdb-sql%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.documentdb%2Fcosmosdb-sql%2Fazuredeploy.json"
        },
        {
            "action": "Create an Azure Cosmos DB account for Table API with autoscale",
            "description": "This template will create an Azure Cosmos account for Table API, provisioned for two regions, then provision a table with autoscale throughput.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.documentdb%2Fcosmosdb-table-autoscale%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.documentdb%2Fcosmosdb-table-autoscale%2Fazuredeploy.json"
        },
        {
            "action": "Create an Azure Cosmos DB account for Table API",
            "description": "This template will create an Azure Cosmos account for Table API, provisioned for two regions, then provision a table with throughput.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.documentdb%2Fcosmosdb-table%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.documentdb%2Fcosmosdb-table%2Fazuredeploy.json"
        },
        {
            "action": "Create an Azure Cosmos DB account and Azure Web App with automatic deployment",
            "description": "This template creates an Azure Cosmos DB account and Azure Web App, then automatically deploys the Cosmos DB sample To-Do ASP MVC web app hosted on GitHub and injects the Cosmos DB endpoint and auth key into the Web App's Application Settings allowing it to connect automatically upon first run.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.documentdb%2Fcosmosdb-webapp%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.documentdb%2Fcosmosdb-webapp%2Fazuredeploy.json"
        },
        {
            "action": "Create an Azure Cosmos DB account with Microsoft Defender enabled",
            "description": "Using this ARM template, you can deploy an Azure Cosmos DB Account with Microsoft Defender for Azure Cosmos DB enabled. Microsoft Defender for Azure Cosmos DB is an Azure-native layer of security that detects attempts to exploit databases in your Azure Cosmos DB accounts. Microsoft Defender for Azure Cosmos DB detects potential SQL injections, known bad actors based on Microsoft Threat Intelligence, suspicious access patterns, and potential exploitations of your database through compromised identities or malicious insiders.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.documentdb%2Fmicrosoft-defender-cosmosdb-create-account%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.documentdb%2Fmicrosoft-defender-cosmosdb-create-account%2Fazuredeploy.json"
        }
    ],
    "Elastic": [
        {
            "action": "Create an Elastic Cloud (Elasticsearch) resource",
            "description": "This QuickStart template creates a new ‘Elastic Cloud (Elasticsearch) – An Azure Native ISV Service’ resource in your Azure subscription, which you can use to create and manage your Elastic deployments, right from Azure.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.elastic%2Felastic-create%2Fazuredeploy.json/createUIDefinitionUri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.elastic%2Felastic-create%2FcreateUiDefinition.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.elastic%2Felastic-create%2Fazuredeploy.json"
        }

    ],
    "Event Grid": [
        {
            "action": "Create a custom Azure Event Grid topic with CloudEvents schema",
            "description": "Creates a custom Azure Event Grid topic, a webhook subscription having CloudEvents schema, and a Logic App as an event handler.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.eventgrid%2Fevent-grid-cloudevents%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.eventgrid%2Fevent-grid-cloudevents%2Fazuredeploy.json"
        },
        {
            "action": "Create Azure Event Grid custom topic and event hub",
            "description": "Creates an Azure Event Grid custom topic and an event hub. It creates an event subscription that sends events from the custom topic to the event hub.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.eventgrid%2Fevent-grid-event-hubs-handler%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.eventgrid%2Fevent-grid-event-hubs-handler%2Fazuredeploy.json"
        },
        {
            "action": "Create Event Grid subscription for resource events",
            "description": "Creates an Event Grid subscription for either a resource group or Azure subscription, sending events to a WebHook.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.eventgrid%2Fevent-grid-resource-events-to-webhook%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.eventgrid%2Fevent-grid-resource-events-to-webhook%2Fazuredeploy.json"
        },
        {
            "action": "Create Azure Event Grid Custom Topic and Queue Subscription",
            "description": "Creates an Event Grid custom topic and a Service Bus queue subscription on Azure.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.eventgrid%2Fevent-grid-servicebus-queue%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.eventgrid%2Fevent-grid-servicebus-queue%2Fazuredeploy.json"
        },
        {
            "action": "Create Azure Event Grid Custom Topic Subscription",
            "description": "Creates an Event Grid custom topic and a Service Bus topic subscription on Azure.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.eventgrid%2Fevent-grid-servicebus-topic%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.eventgrid%2Fevent-grid-servicebus-topic%2Fazuredeploy.json"
        },
        {
            "action": "Create Blob Storage and Event Grid subscription to the Blob",
            "description": "Creates an Azure Storage Account and then creates an Event Grid subscription to that storage account.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.eventgrid%2Fevent-grid-subscription-and-storage%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.eventgrid%2Fevent-grid-subscription-and-storage%2Fazuredeploy.json"
        },
        {
            "action": "Create Azure Event Grid Custom Topic and Subscription",
            "description": "Creates an Event Grid custom topic and webhook subscription on Azure.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.eventgrid%2Fevent-grid%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.eventgrid%2Fevent-grid%2Fazuredeploy.json"
        }

    ],
    "Event Hub": [
        {
            "action": "Create an EventHubs namespace, Event Hub, & consumer group",
            "description": "Enables you to deploy an Event Hubs Standard namespace, an Event Hub, and a consumer group.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.eventhub%2Fevent-hubs-create-event-hub-and-consumer-group%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.eventhub%2Fevent-hubs-create-event-hub-and-consumer-group%2Fazuredeploy.json"
        },
        {
            "action": "Create EventHubs authorizationRules",
            "description": "Enables you to deploy an Event Hubs Standard namespace, an Event Hub, a consumer group, and authorization rules.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.eventhub%2Feventhub-create-authrule-namespace-and-eventhub%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.eventhub%2Feventhub-create-authrule-namespace-and-eventhub%2Fazuredeploy.json"
        },
        {
            "action": "Create EventHub namespace and geo-recovery configuration",
            "description": "Enables you to deploy a Service Bus namespace with a Basic/Standard SKU and set up geo-recovery configuration.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.eventhub%2Feventhub-create-namespace-geo-recoveryconfiguration%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.eventhub%2Feventhub-create-namespace-geo-recoveryconfiguration%2Fazuredeploy.json"
        },
        {
            "action": "Create Event Hub namespace with IP Filter rule",
            "description": "Enables you to deploy a Service Bus Premium namespace with an IP Filter rule for Azure Event Hubs.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.eventhub%2Feventhub-namespace-ipfilter%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.eventhub%2Feventhub-namespace-ipfilter%2Fazuredeploy.json"
        },
        {
            "action": "Create Event Hubs namespace with Virtual Network rule",
            "description": "Enables you to deploy an Azure Event Hubs Standard namespace with a Virtual Network rule.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.eventhub%2Feventhub-namespace-vnet%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.eventhub%2Feventhub-namespace-vnet%2Fazuredeploy.json"
        },
        {
            "action": "Create Event Hubs Cluster, Namespace, and Event Hub",
            "description": "Enables you to create an Event Hubs Cluster, namespace, and event hub using an Azure Resource Manager template.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.eventhub%2Feventhubs-create-cluster-namespace-eventhub%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.eventhub%2Feventhubs-create-cluster-namespace-eventhub%2Fazuredeploy.json"
        },
        {
            "action": "Create Event Hubs Cluster and Namespace in Cluster",
            "description": "Enables you to create an Event Hubs Cluster and a namespace in the cluster using an Azure Resource Manager template.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.eventhub%2Feventhubs-create-cluster-namespace%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.eventhub%2Feventhubs-create-cluster-namespace%2Fazuredeploy.json"
        },
        {
            "action": "Create Event Hubs with Capture enabled (ADLS)",
            "description": "Enables you to create an Event Hubs namespace with an event hub and enable Capture using an Azure Resource Manager template.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.eventhub%2Feventhubs-create-namespace-and-enable-capture-for-adls%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.eventhub%2Feventhubs-create-namespace-and-enable-capture-for-adls%2Fazuredeploy.json"
        },
        {
            "action": "Create Event Hubs with Capture enabled",
            "description": "Enables you to create an Event Hubs namespace with an event hub and enable Capture using an Azure Resource Manager template.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.eventhub%2Feventhubs-create-namespace-and-enable-capture%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.eventhub%2Feventhubs-create-namespace-and-enable-capture%2Fazuredeploy.json"
        },
        {
            "action": "Create Event Hubs with Auto-Inflate",
            "description": "Enables you to create an Event Hubs Standard namespace, an Event Hub, a consumer group, and enable the auto-inflate feature using an Azure Resource Manager template.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.eventhub%2Feventhubs-create-namespace-and-enable-inflate%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.eventhub%2Feventhubs-create-namespace-and-enable-inflate%2Fazuredeploy.json"
        },
        {
            "action": "Create Event Hubs Namespace and Event Hub",
            "description": "Enables you to deploy an Event Hubs namespace with an Event Hub using an Azure Resource Manager template.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.eventhub%2Feventhubs-create-namespace-and-eventhub%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.eventhub%2Feventhubs-create-namespace-and-eventhub%2Fazuredeploy.json"
        },
        {
            "action": "Connect to Event Hubs via Private Endpoint",
            "description": "Configure a virtual network and private DNS zone to access an Event Hubs namespace via a private endpoint using an Azure Resource Manager template.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.eventhub%2Feventhubs-private-endpoint%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.eventhub%2Feventhubs-private-endpoint%2Fazuredeploy.json"
        }
    ],
    "HD Insight": [],
    "Hardware Security Modules": [],
    "Healthcare APIs": [],
    "Insights": [],
    "KeyVault": [],
    "Kubernetes": [],
    "Kusto": [],
    "Lab Services": [
        {
            "action": "Create Azure Lab Services Lab",
            "description": "Create an Azure Lab Services lab using an Azure Resource Manager template.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.labservices%2Flab%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.labservices%2Flab%2Fazuredeploy.json"
        },
        {
            "action": "Create Azure Lab Services Lab Plan",
            "description": "Create an Azure Lab Services lab plan using an Azure Resource Manager template.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.labservices%2Flab-plan%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.labservices%2Flab-plan%2Fazuredeploy.json"
        },
        {
            "action": "Create Azure Lab Services Lab using a Lab Plan",
            "description": "Create an Azure Lab Services lab using a lab plan with an Azure Resource Manager template.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.labservices%2Flab-using-lab-plan%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.labservices%2Flab-using-lab-plan%2Fazuredeploy.json"
        }

    ],
    "Logic": [],
    "Machine Learning Services": [],
    "Maps": [],
    "MariaDB": [
        {
            "action": "Deploy Azure Database for MariaDB with VNet Integration",
            "description": "This template provides a way to deploy an Azure Database for MariaDB with VNet Integration. You can learn more about how to deploy the template by referring to the [quickstart article](https://docs.microsoft.com/azure/mariadb/quickstart-create-mariadb-server-database-arm-template).",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.dbformariadb%2Fmanaged-mariadb-with-vnet%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.dbformariadb%2Fmanaged-mariadb-with-vnet%2Fazuredeploy.json"
        }
    ],
    "MySql": [
        {
            "action": "Deploy Azure Database for MySQL (Flexible) with VNet Integration",
            "description": "This template provides an easy way to deploy the Flexible server Azure database for MySQL with VNet Integration. You can learn more about how to deploy the template by referring to the [quickstart article](https://docs.microsoft.com/azure/mysql/flexible-server/quickstart-create-arm-template). For more information about the Flexible Server SKU for Azure database for MySQL and how it compares to the Single Server SKU, see the [docs](https://docs.microsoft.com/azure/mysql/select-right-deployment-type).",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.dbformysql%2Fflexible-mysql-with-vnet%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.dbformysql%2Fflexible-mysql-with-vnet%2Fazuredeploy.json"
        },
        {
            "action": "Deploy Azure Database for MySQL with VNet Integration",
            "description": "This template provides an easy way to deploy Azure database for MySQL with VNet Integration. You can learn more about how to deploy the template by referring to the [quickstart article](https://docs.microsoft.com/azure/mysql/quickstart-create-mysql-server-database-using-arm-template).",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.dbformysql%2Fmanaged-mysql-with-vnet%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.dbformysql%2Fmanaged-mysql-with-vnet%2Fazuredeploy.json"
        },
    ],
    "Media": [],
    "Migrate": [],
    "Mobile Network": [],
    "Netapp": [
{
    "action": "Create new ANF resource with NFSV3/NFSv4.1 volume",
    "description": "This template creates Azure NetApp Files account along with setting up a capacity pool to enable you to create NFSv3/NFSv4.1 volume within it. Deployed together with Azure Virtual Network and delegated subnet.",
    "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.netapp%2Fanf-nfs-volume%2Fazuredeploy.json",
    "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.netapp%2Fanf-nfs-volume%2Fazuredeploy.json"
},
{
    "action": "ORACLE Azure NetApp Files storage",
    "description": "This template deploys storage for ORACLE deployments. Storage is provided using Azure NetApp Files, built on NetApp ONTAP storage OS.",
    "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.netapp%2Fanf-oracle%2Fanf-oracle-storage%2Fazuredeploy.json",
    "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.netapp%2Fanf-oracle%2Fanf-oracle-storage%2Fazuredeploy.json"
},

    ],
    "Network": [],
    "Notification Hubs": [
{
    "action": "Create Azure Notification Hub",
    "description": "This template creates a Notification Hub on Azure. Azure Notification Hubs is a massively scalable mobile push notification engine for quickly sending millions of notifications to iOS, Android, Windows, or Kindle devices.",
    "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.notificationhubs%2Fnotification-hub%2Fazuredeploy.json",
    "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.notificationhubs%2Fnotification-hub%2Fazuredeploy.json"
},

    ],
    "Operations Management": [
{
    "action": "Enable Microsoft Sentinel",
    "description": "Enable Azure Sentinel, a scalable, cloud-native, security information event management (SIEM) and security orchestration automated response (SOAR) solution.",
    "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.operationsmanagement%2Fazure-sentinel%2Fazuredeploy.json",
    "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.operationsmanagement%2Fazure-sentinel%2Fazuredeploy.json"
},

    ],
    "Portal": [
        {
            "action": "Create Azure Portal Dashboard",
            "description": "Create an Azure portal dashboard showing the performance of an existing virtual machine in your Azure subscription.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.portal%2Fazure-portal-dashboard%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.portal%2Fazure-portal-dashboard%2Fazuredeploy.json"
        },
        {
            "action": "Create Shared Azure Dashboard",
            "description": "Create a shared dashboard providing visibility to a specific resource group. Customize the dashboard by pinning metric charts and views of your application's performance.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.portal%2Fdefault-shared-dashboard%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.portal%2Fdefault-shared-dashboard%2Fazuredeploy.json"
        }
    ],
    "PostgresQl": [
        {
            "action": "Deploy Azure Database for PostgreSQL (flexible) with AAD",
            "description": "This template provides an easy way to deploy Azure Database for PostgreSQL (flexible) with AAD (Azure Active Directory) integration. You can learn more about how to deploy the template by referring to the [quickstart article](https://docs.microsoft.com/azure/postgresql/flexible-server/quickstart-create-arm-template).",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.dbforpostgresql%2Fflexible-postgresql-with-aad%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.dbforpostgresql%2Fflexible-postgresql-with-aad%2Fazuredeploy.json"
        },
        {
            "action": "Deploy Azure Database for PostgreSQL (flexible) with VNet",
            "description": "This template provides an easy way to deploy the Flexible server Azure database for PostgreSQL with VNet Integration. To learn more about how to deploy the template, see the [quickstart article](https://docs.microsoft.com/azure/postgresql/flexible-server/quickstart-create-arm-template). For more information about the Flexible Server SKU for Azure database for PostgreSQL and how it compares to the Single Server SKU, refer to the [docs](https://docs.microsoft.com/azure/postgresql/select-right-deployment-type).",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.dbforpostgresql%2Fflexible-postgresql-with-vnet%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.dbforpostgresql%2Fflexible-postgresql-with-vnet%2Fazuredeploy.json"
        },
        {
            "action": "Deploy Azure Database for PostgreSQL with VNet",
            "description": "This template provides an easy way to deploy an Azure database for PostgreSQL with VNet Integration. To learn more about how to deploy the template, see the [quickstart article](https://docs.microsoft.com/azure/postgresql/quickstart-create-postgresql-server-database-using-arm-template).",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.dbforpostgresql%2Fmanaged-postgresql-with-vnet%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.dbforpostgresql%2Fmanaged-postgresql-with-vnet%2Fazuredeploy.json"
        }

    ],
    "PowerBI": [
{
  "action": "Create a PowerBI Workspace Collection",
  "description": "This ARM template creates a PowerBI Workspace collection resource in Azure.",
  "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.powerbi%2Fpowerbi-workspace-create%2Fazuredeploy.json",
  "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.powerbi%2Fpowerbi-workspace-create%2Fazuredeploy.json"
}

    ],
    "PowerBI Dedicated": [
{
  "action": "Create a Power BI Embedded capacity",
  "description": "This template creates a Power BI capacity in Azure, which simplifies how ISVs and developers use Power BI capabilities with embedded analytics.",
  "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.powerbidedicated%2Fpower-bi-embedded%2Fazuredeploy.json",
  "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.powerbidedicated%2Fpower-bi-embedded%2Fazuredeploy.json"
},

    ],
    "Recovery Services": [],
    "Relay": [
        {
            "action": "Create an Azure Relay namespace with all resources",
            "description": "This template enables you to deploy an Azure Relay namespace with standard SKU, a WCF Relay and a HybridConnection.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.relay%2Fazure-relay-create-all-resources%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.relay%2Fazure-relay-create-all-resources%2Fazuredeploy.json"
        },
        {
            "action": "Create an Azure Relay namespace with SAS Policies",
            "description": "This template enables you to deploy an Azure Relay namespace with standard SKU, a HybridConnection entity and authorization rules for both the namespace and HybridConnection.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.relay%2Fazure-relay-create-authrule-namespace-and-hybridconnection%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.relay%2Fazure-relay-create-authrule-namespace-and-hybridconnection%2Fazuredeploy.json"
        },
        {
            "action": "Create an Azure Relay namespace with SAS Policies and WCF",
            "description": "This template enables you to deploy an Azure Relay namespace with standard SKU, a WcfRealy entity and authorization rules for both the namespace and WcfRealy.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.relay%2Fazure-relay-create-authrule-namespace-and-wcfrelay%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.relay%2Fazure-relay-create-authrule-namespace-and-wcfrelay%2Fazuredeploy.json"
        },
        {
            "action": "Create an Azure Relay namespace and HybridConnection",
            "description": "This template enables you to deploy an Azure Relay namespace with standard SKU and a HybridConnection.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.relay%2Fazure-relay-create-hybridconnection%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.relay%2Fazure-relay-create-hybridconnection%2Fazuredeploy.json"
        },
        {
            "action": "Create an Azure Relay namespace",
            "description": "This template enables you to deploy an Azure Relay namespace with a Standard SKU.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.relay%2Fazure-relay-create-namespace%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.relay%2Fazure-relay-create-namespace%2Fazuredeploy.json"
        },
        {
            "action": "Create an Azure Relay namespace with a WCF Relay",
            "description": "This template enables you to deploy an Azure Relay namespace with standard SKU and a WCF Relay.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.relay%2Fazure-relay-create-wcfrelay%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.relay%2Fazure-relay-create-wcfrelay%2Fazuredeploy.json"
        },

    ],
    "Resources": [],
    "Search": [
        {
            "action": "Create an Azure Cognitive Search service with a private endpoint",
            "description": "This template allows you to create an Azure Cognitive Search service with a private endpoint.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.search%2Fazure-search-create-private-endpoint%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.search%2Fazure-search-create-private-endpoint%2Fazuredeploy.json"
        },
        {
            "action": "Azure Cognitive Search service",
            "description": "This template creates a new Azure Cognitive Search Service. The quickstart article describes how to deploy the template.",
            "link": "https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.search%2Fazure-search-create%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.search%2Fazure-search-create%2Fazuredeploy.json"
        },

    ],
    "Security": [
        {
            "action": "Create a Security Automation for specific Alerts",
            "description": "This template deploys an Azure Security Center Automation which will be triggered by Azure Security alerts which their display name contains a specific string. Automation is an Azure Resource which triggers a Logic App.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.security%2Fsecuritycenter-create-automation-for-alertnamecontains%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.security%2Fsecuritycenter-create-automation-for-alertnamecontains%2Fazuredeploy.json"
        },
        {
            "action": "Create a Security Automation for all Alerts",
            "description": "This template deploys an Azure Security Center Automation for any of Azure Security Center's alerts. Automation is an Azure Resource which triggers a Logic App.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.security%2Fsecuritycenter-create-automation-for-all-alerts%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.security%2Fsecuritycenter-create-automation-for-all-alerts%2Fazuredeploy.json"
        },
        {
            "action": "Create a Security Automation for any Recommendation",
            "description": "This template deploys an Azure Security Center Automation for any of Azure Security Center's recommendations. Automation is an Azure Resource which triggers a Logic App.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.security%2Fsecuritycenter-create-automation-for-all-recommendations%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.security%2Fsecuritycenter-create-automation-for-all-recommendations%2Fazuredeploy.json"
        },
        {
            "action": "Create a Security Automation for a Recommendation",
            "description": "This template deploys an Azure Security Center Automation for a specific Azure Security Center's recommendation. Automation is an Azure Resource which triggers a Logic App.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.security%2Fsecuritycenter-create-automation-for-specific-recommendations%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.security%2Fsecuritycenter-create-automation-for-specific-recommendations%2Fazuredeploy.json"
        }

    ],
    "Security Insights": [
        {
            "action": "Creates a new Microsoft Sentinel Automation Rule",
            "description": "This sample template demonstrates how to create an Automation Rule in your Microsoft Sentinel workspace. This sample automation rule triggers on incident creation and looks for specific analytic rule ID, severity, tactics, and title. If the incident matches these conditions, it then modifies incident status and adds a tag. For more information about automation rules, visit [Automation in Azure Sentinel](https://docs.microsoft.com/azure/sentinel/automation-in-azure-sentinel)",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.securityinsights%2Fsentinel-automation-rule%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.securityinsights%2Fsentinel-automation-rule%2Fazuredeploy.json"
        },
        {
            "action": "Creates a new Microsoft Sentinel Scheduled Analytics Rule",
            "description": "This sample template demonstrates how to create a Scheduled Analytics Rule in your Microsoft Sentinel workspace. For more information about analytics rules, visit [Create custom analytics rules to detect threats](https://docs.microsoft.com/azure/sentinel/detect-threats-custom)",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.securityinsights%2Fsentinel-scheduled-analytics-rule%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.securityinsights%2Fsentinel-scheduled-analytics-rule%2Fazuredeploy.json"
        }

    ],
    "Service Bus": [],
    "Service Fabric": [

        {
            "action": "Deploy a 5 Node Ubuntu Service Fabric Cluster",
            "description": "This template allows you to deploy a secure 5 node Service Fabric Cluster running Ubuntu on a Standard_D2_V2 Size VMSS. This template assumes that you already have certificates uploaded to your keyvault.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.servicefabric%2F5-vm-ubuntu-1-nodetypes-secure%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.servicefabric%2F5-vm-ubuntu-1-nodetypes-secure%2Fazuredeploy.json"
        },
        {
            "action": "Deploy a 5 Node Secure Cluster",
            "description": "This template allows you to deploy a secure 5 node Service Fabric Cluster running Windows Server 2019 Datacenter on a Standard_D2_v2 Size VMSS with Azure Diagnostics turned on. This template assumes that you already have certificates uploaded to your key vault. If you want to create a new certificate run the New-ServiceFabricClusterCertificate.ps1 file in this sample. That script will output the values necessary for deployment via the parameters file. The certificate that is created by this script is self-signed and should only be used for testing purposes.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.servicefabric%2Fservice-fabric-secure-cluster-5-node-1-nodetype%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.servicefabric%2Fservice-fabric-secure-cluster-5-node-1-nodetype%2Fazuredeploy.json"
        },
        {
            "action": "Deploy a 3 Nodetype Secure Cluster with NSGs enabled",
            "description": "Use this template as a sample for setting up a three nodetype secure cluster and to control the inbound and outbound network traffic using Network Security Groups. The template has a Network Security Group for each of the VMSS to control the traffic in and out of the VMSS. As a default, the rules are set up to allow all the traffic needed by the system services and the application ports specified in the template. Review those rules and make changes to fit your needs, including add any new ones for your applications. Although, as a default, the parameter file is set to create a 65 node cluster. So, make sure to adjust the instance counts for each of the Nodetypes in the parameter file to suit your needs. In this template, 'SF' is the primary node type and the systems services will be running in it. When deploying applications to the cluster, having a dedicated Nodetype for System services is a best practice when running clusters that are over 50 nodes and are packed for maximum utilization of VM resources. This template assumes that you already have certificates uploaded to your keyvault, else I strongly suggest you follow the links below on how to.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.servicefabric%2Fservice-fabric-secure-nsg-cluster-65-node-3-nodetype%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.servicefabric%2Fservice-fabric-secure-nsg-cluster-65-node-3-nodetype%2Fazuredeploy.json"
        }

    ],
    "SignalR Service": [
        {
            "action": "Deploy an Azure SignalR service",
            "description": "This template allows you to create an Azure SignalR Service. Azure SignalR Service is an Azure managed service that helps developers build web applications with real-time features. To learn more about how to deploy the template, see the quickstart article.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.signalrservice%2Fsignalr%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.signalrservice%2Fsignalr%2Fazuredeploy.json"
        }

    ],
    "Solutions": [
        {
            "action": "Create a managed application that deploys linked templates",
            "description": "This sample template deploys a Service catalog managed application along with the definition that creates a linked deployment for the managed application. While creating managed application packages your scenario might require a complex deployment scenario which needs the ARM template to be broken down in to simpler templates that can be called by the main template. Managed Applications allow this by utilizing linked ARM template deployments and providing a location to store your linked templates.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.solutions%2Fmanaged-application-with-linked-templates%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.solutions%2Fmanaged-application-with-linked-templates%2Fazuredeploy.json"
        },
        {
            "action": "Create a managed application with metrics and alerts",
            "description": "This sample shows how you can author a service catalog managed application definition that will allow deploying a managed application with defined metrics and alerts. This managed application will contain a single storage account as a resource, expose application metrics for the storage account including availability, success E2E latency, transactions; as well as alerts based on storage account availability and activity log alerts based on regenerating storage account keys.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.solutions%2Fmanaged-application-with-metrics-and-alerts%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.solutions%2Fmanaged-application-with-metrics-and-alerts%2Fazuredeploy.json"
        },
        {
            "action": "Create a managed application with a customized view",
            "description": "This sample template deploys a Service catalog managed application definition that creates a single storage account as an application resource. The application definition demonstrates how you can customize the default application overview: header and description.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.solutions%2Fmanaged-application%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.solutions%2Fmanaged-application%2Fazuredeploy.json"
        }

    ],
    "Sql": [],
    "Sql Virtual Machine": [
        {
            "action": "Deploy SQL Always ON setup with existing SQL Virtual Machines",
            "description": "This deployment will create a WS failover cluster with cloud witness on the provided VMs (in the same region) and enable SQL Always ON them. This will enable creating SQL Availability Groups over the created Always ON setup.",
            "link": "https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/quickstarts/microsoft.sqlvirtualmachine/sql-vm-ag-setup/azuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/quickstarts/microsoft.sqlvirtualmachine/sql-vm-ag-setup/azuredeploy.json"
        },
        {
            "action": "Create SQL AvailabilityGroup listener on existing Always ON setup.",
            "description": "This deployment will create an AG listener for a SQL Availability Group. This will also set up Load balancer rules corresponding to the Listener.",
            "link": "https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/quickstarts/microsoft.sqlvirtualmachine/sql-vm-aglistener-setup/azuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/quickstarts/microsoft.sqlvirtualmachine/sql-vm-aglistener-setup/azuredeploy.json"
        },
        {
            "action": "SQL Server VM with performance optimized storage settings",
            "description": "Create a SQL Server Virtual Machine with performance optimized storage settings on PremiumSSD.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.sqlvirtualmachine%2Fsql-vm-new-storage%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.sqlvirtualmachine%2Fsql-vm-new-storage%2Fazuredeploy.json"
        },

    ],
    "Storage": [
        {
            "action": "Connect to a storage account from a VM via private endpoint",
            "description": "Create a Linux Virtual Machine in a virtual network that privately accesses a blob storage account using an Azure Private Endpoint.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.storage%2Fblob-storage-private-endpoint%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.storage%2Fblob-storage-private-endpoint%2Fazuredeploy.json"
        },
        {
            "action": "Connect to an Azure File Share via a Private Endpoint",
            "description": "Create a Linux Virtual Machine in a virtual network that privately accesses Azure File Share and an ADLS Gen 2 blob storage account using Azure Private Endpoints.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.storage%2Ffile-share-private-endpoint%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.storage%2Ffile-share-private-endpoint%2Fazuredeploy.json"
        },
        {
            "action": "Create a Standard Storage Account",
            "description": "This template creates a standard storage account in Azure. If you're new to Azure Storage accounts, you can learn more from the provided links.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.storage%2Fstorage-account-create%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.storage%2Fstorage-account-create%2Fazuredeploy.json"
        },
        {
            "action": "Create a Storage Account with Storage Service Encryption for Data at Rest",
            "description": "This template creates a Storage account with Storage Service Encryption for data at rest in Azure. For more information, you can refer to the provided link.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.storage%2Fstorage-account-service-encryption-create%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.storage%2Fstorage-account-service-encryption-create%2Fazuredeploy.json"
        },
        {
            "action": "Deploy an Azure Storage Account with Advanced Threat Protection enabled",
            "description": "This template allows you to deploy an Azure Storage Account with Advanced Threat Protection enabled. Storage Advanced Threat Protection is a unified package for advanced Storage security capabilities. For more information on Storage Advanced Threat Protection, see the official documentation provided in the link.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.storage%2Fstorage-advanced-threat-protection-create%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.storage%2Fstorage-advanced-threat-protection-create%2Fazuredeploy.json"
        },
        {
            "action": "Create an Azure Storage Account and Blob Container on Azure",
            "description": "This template creates an Azure Storage account and a blob container. The template allows you to deploy an Azure Storage Account and Blob Container on Azure. It is originally authored by John Downs. If you are new to Azure Storage account, you can refer to the provided links for documentation and template references.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.storage%2Fstorage-blob-container%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.storage%2Fstorage-blob-container%2Fazuredeploy.json"
        },
        {
            "action": "Azure Storage Account Encryption with customer-managed key",
            "description": "This template deploys a Storage Account with a customer-managed key for encryption that's generated and placed inside a Key Vault.",
            "link": "https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.storage%2Fstorage-blob-encryption-with-cmk%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.storage%2Fstorage-blob-encryption-with-cmk%2Fazuredeploy.json"
        },
        {
            "action": "Create a storage account with file share",
            "description": "This template creates an Azure Storage account with a single file share.",
            "link": "https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/quickstarts/microsoft.storage/storage-file-share/azuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/quickstarts/microsoft.storage/storage-file-share/azuredeploy.json"
        },
        {
            "action": "Create a storage account with multiple Blob containers",
            "description": "This template creates an Azure Storage account with multiple blob containers.",
            "link": "https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/quickstarts/microsoft.storage/storage-multi-blob-container/azuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/quickstarts/microsoft.storage/storage-multi-blob-container/azuredeploy.json"
        },
        {
            "action": "Create a storage account with multiple file shares",
            "description": "This template creates an Azure Storage account with multiple file shares.",
            "link": "https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/quickstarts/microsoft.storage/storage-multi-file-share/azuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/quickstarts/microsoft.storage/storage-multi-file-share/azuredeploy.json"
        },
        {
            "action": "Create Storage Account with SFTP enabled",
            "description": "This template creates an Azure Storage account and a blob container that can be accessed using SFTP protocol. Access can be password or public-key based.",
            "link": "https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/quickstarts/microsoft.storage/storage-sftp/azuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/quickstarts/microsoft.storage/storage-sftp/azuredeploy.json"
        },

    ],
    "Storage Pool": [
        {
            "action": "Deploy an entry level Disk Pool",
            "description": "Deploy a Disk Pool with a 1TB existing Premium Disk into an existing subnet.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.storagepool%2Fdiskpool-create-entry-level%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.storagepool%2Fdiskpool-create-entry-level%2Fazuredeploy.json"
        }

    ],
    "Stream Analytics": [
        {
            "action": "Create a Standard Stream Analytics Job",
            "description": "Deploy a standard Azure Stream Analytics job to analyze and process high volumes of fast streaming data from multiple sources simultaneously.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.streamanalytics%2Fstreamanalytics-create%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.streamanalytics%2Fstreamanalytics-create%2Fazuredeploy.json"
        }

    ],
    "Synapse": [
        {
            "action": "Create Azure Synapse Proof-of-Concept Environment",
            "description": "Deploy a proof of concept environment for Azure Synapse, including SQL Pools and optional Apache Spark Pools.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.synapse%2Fsynapse-poc%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.synapse%2Fsynapse-poc%2Fazuredeploy.json"
        }

    ],
    "Time Series Insights": [
        {
            "action": "Create PAYG Time Series Insights Environment with IoT Hub",
            "description": "Create a Pay As You Go (PAYG) Time Series Insights environment configured to consume events from an IoT Hub.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.timeseriesinsights%2Ftimeseriesinsights-environment-payg-with-iothub%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.timeseriesinsights%2Ftimeseriesinsights-environment-payg-with-iothub%2Fazuredeploy.json"
        },
        {
            "action": "Create Time Series Insights Environment with Event Hub Event Source",
            "description": "Create a standard Time Series Insights environment configured to consume events from an Event Hub.",
            "link": "https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.timeseriesinsights%2Ftimeseriesinsights-environment-with-eventhub%2Fazuredeploy.json",
            "visualize": "http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.timeseriesinsights%2Ftimeseriesinsights-environment-with-eventhub%2Fazuredeploy.json"
        }

    ],
    "Web": []
}
