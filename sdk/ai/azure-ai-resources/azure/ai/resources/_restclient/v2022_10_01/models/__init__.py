# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import AccessKeyAuthTypeWorkspaceConnectionProperties
    from ._models_py3 import AccountKeyDatastoreCredentials
    from ._models_py3 import AccountKeyDatastoreSecrets
    from ._models_py3 import AmlOperation
    from ._models_py3 import AmlOperationListResult
    from ._models_py3 import AmlToken
    from ._models_py3 import AmlUserFeature
    from ._models_py3 import ApiKeyAuthWorkspaceConnectionProperties
    from ._models_py3 import AssetBase
    from ._models_py3 import AssetContainer
    from ._models_py3 import AssetJobInput
    from ._models_py3 import AssetJobOutput
    from ._models_py3 import AssetReferenceBase
    from ._models_py3 import AzureBlobDatastore
    from ._models_py3 import AzureDataLakeGen1Datastore
    from ._models_py3 import AzureDataLakeGen2Datastore
    from ._models_py3 import AzureFileDatastore
    from ._models_py3 import BanditPolicy
    from ._models_py3 import BatchDeploymentData
    from ._models_py3 import BatchDeploymentDetails
    from ._models_py3 import BatchDeploymentTrackedResourceArmPaginatedResult
    from ._models_py3 import BatchEndpointData
    from ._models_py3 import BatchEndpointDefaults
    from ._models_py3 import BatchEndpointDetails
    from ._models_py3 import BatchEndpointTrackedResourceArmPaginatedResult
    from ._models_py3 import BatchRetrySettings
    from ._models_py3 import BayesianSamplingAlgorithm
    from ._models_py3 import BuildContext
    from ._models_py3 import CertificateDatastoreCredentials
    from ._models_py3 import CertificateDatastoreSecrets
    from ._models_py3 import CodeConfiguration
    from ._models_py3 import CodeContainerData
    from ._models_py3 import CodeContainerDetails
    from ._models_py3 import CodeContainerResourceArmPaginatedResult
    from ._models_py3 import CodeVersionData
    from ._models_py3 import CodeVersionDetails
    from ._models_py3 import CodeVersionResourceArmPaginatedResult
    from ._models_py3 import CommandJob
    from ._models_py3 import CommandJobLimits
    from ._models_py3 import ComponentContainerData
    from ._models_py3 import ComponentContainerDetails
    from ._models_py3 import ComponentContainerResourceArmPaginatedResult
    from ._models_py3 import ComponentVersionData
    from ._models_py3 import ComponentVersionDetails
    from ._models_py3 import ComponentVersionResourceArmPaginatedResult
    from ._models_py3 import ComputeRuntimeDto
    from ._models_py3 import ContainerResourceRequirements
    from ._models_py3 import ContainerResourceSettings
    from ._models_py3 import CosmosDbSettings
    from ._models_py3 import CustomKeys
    from ._models_py3 import CustomKeysWorkspaceConnectionProperties
    from ._models_py3 import CustomModelJobInput
    from ._models_py3 import CustomModelJobOutput
    from ._models_py3 import DataContainerData
    from ._models_py3 import DataContainerDetails
    from ._models_py3 import DataContainerResourceArmPaginatedResult
    from ._models_py3 import DataPathAssetReference
    from ._models_py3 import DataVersionBaseData
    from ._models_py3 import DataVersionBaseDetails
    from ._models_py3 import DataVersionBaseResourceArmPaginatedResult
    from ._models_py3 import DatastoreCredentials
    from ._models_py3 import DatastoreData
    from ._models_py3 import DatastoreDetails
    from ._models_py3 import DatastoreResourceArmPaginatedResult
    from ._models_py3 import DatastoreSecrets
    from ._models_py3 import DefaultScaleSettings
    from ._models_py3 import DeploymentLogs
    from ._models_py3 import DeploymentLogsRequest
    from ._models_py3 import DiagnoseRequestProperties
    from ._models_py3 import DiagnoseResponseResult
    from ._models_py3 import DiagnoseResponseResultValue
    from ._models_py3 import DiagnoseResult
    from ._models_py3 import DiagnoseWorkspaceParameters
    from ._models_py3 import DistributionConfiguration
    from ._models_py3 import EarlyTerminationPolicy
    from ._models_py3 import EncryptionKeyVaultUpdateProperties
    from ._models_py3 import EncryptionProperty
    from ._models_py3 import EncryptionUpdateProperties
    from ._models_py3 import EndpointAuthKeys
    from ._models_py3 import EndpointAuthToken
    from ._models_py3 import EndpointDeploymentPropertiesBase
    from ._models_py3 import EndpointPropertiesBase
    from ._models_py3 import EnvironmentContainerData
    from ._models_py3 import EnvironmentContainerDetails
    from ._models_py3 import EnvironmentContainerResourceArmPaginatedResult
    from ._models_py3 import EnvironmentVersionData
    from ._models_py3 import EnvironmentVersionDetails
    from ._models_py3 import EnvironmentVersionResourceArmPaginatedResult
    from ._models_py3 import ErrorAdditionalInfo
    from ._models_py3 import ErrorDetail
    from ._models_py3 import ErrorResponse
    from ._models_py3 import ExternalFQDNResponse
    from ._models_py3 import FQDNEndpoint
    from ._models_py3 import FQDNEndpointDetail
    from ._models_py3 import FQDNEndpoints
    from ._models_py3 import FQDNEndpointsPropertyBag
    from ._models_py3 import FeatureStoreSettings
    from ._models_py3 import FlavorData
    from ._models_py3 import FqdnOutboundRule
    from ._models_py3 import GridSamplingAlgorithm
    from ._models_py3 import IdAssetReference
    from ._models_py3 import IdentityConfiguration
    from ._models_py3 import IdentityForCmk
    from ._models_py3 import InferenceContainerProperties
    from ._models_py3 import JobBaseData
    from ._models_py3 import JobBaseDetails
    from ._models_py3 import JobBaseResourceArmPaginatedResult
    from ._models_py3 import JobInput
    from ._models_py3 import JobLimits
    from ._models_py3 import JobOutput
    from ._models_py3 import JobService
    from ._models_py3 import KeyVaultProperties
    from ._models_py3 import KubernetesOnlineDeployment
    from ._models_py3 import ListAmlUserFeatureResult
    from ._models_py3 import ListNotebookKeysResult
    from ._models_py3 import ListStorageAccountKeysResult
    from ._models_py3 import ListWorkspaceKeysResult
    from ._models_py3 import LiteralJobInput
    from ._models_py3 import MLFlowModelJobInput
    from ._models_py3 import MLFlowModelJobOutput
    from ._models_py3 import MLTableData
    from ._models_py3 import MLTableJobInput
    from ._models_py3 import MLTableJobOutput
    from ._models_py3 import ManagedIdentity
    from ._models_py3 import ManagedIdentityAuthTypeWorkspaceConnectionProperties
    from ._models_py3 import ManagedNetworkProvisionOptions
    from ._models_py3 import ManagedNetworkProvisionStatus
    from ._models_py3 import ManagedOnlineDeployment
    from ._models_py3 import ManagedServiceIdentity
    from ._models_py3 import MedianStoppingPolicy
    from ._models_py3 import ModelContainerData
    from ._models_py3 import ModelContainerDetails
    from ._models_py3 import ModelContainerResourceArmPaginatedResult
    from ._models_py3 import ModelVersionData
    from ._models_py3 import ModelVersionDetails
    from ._models_py3 import ModelVersionResourceArmPaginatedResult
    from ._models_py3 import Mpi
    from ._models_py3 import NoneAuthTypeWorkspaceConnectionProperties
    from ._models_py3 import NoneDatastoreCredentials
    from ._models_py3 import NotebookAccessTokenResult
    from ._models_py3 import NotebookPreparationError
    from ._models_py3 import NotebookResourceInfo
    from ._models_py3 import Objective
    from ._models_py3 import OnlineDeploymentData
    from ._models_py3 import OnlineDeploymentDetails
    from ._models_py3 import OnlineDeploymentTrackedResourceArmPaginatedResult
    from ._models_py3 import OnlineEndpointData
    from ._models_py3 import OnlineEndpointDetails
    from ._models_py3 import OnlineEndpointTrackedResourceArmPaginatedResult
    from ._models_py3 import OnlineRequestSettings
    from ._models_py3 import OnlineScaleSettings
    from ._models_py3 import OperationDisplay
    from ._models_py3 import OutboundRule
    from ._models_py3 import OutboundRuleBasicResource
    from ._models_py3 import OutboundRuleListResult
    from ._models_py3 import OutputPathAssetReference
    from ._models_py3 import PATAuthTypeWorkspaceConnectionProperties
    from ._models_py3 import PartialAssetReferenceBase
    from ._models_py3 import PartialBatchDeployment
    from ._models_py3 import PartialBatchDeploymentPartialTrackedResource
    from ._models_py3 import PartialBatchEndpoint
    from ._models_py3 import PartialBatchEndpointPartialTrackedResource
    from ._models_py3 import PartialBatchRetrySettings
    from ._models_py3 import PartialCodeConfiguration
    from ._models_py3 import PartialDataPathAssetReference
    from ._models_py3 import PartialIdAssetReference
    from ._models_py3 import PartialKubernetesOnlineDeployment
    from ._models_py3 import PartialManagedOnlineDeployment
    from ._models_py3 import PartialManagedServiceIdentity
    from ._models_py3 import PartialOnlineDeployment
    from ._models_py3 import PartialOnlineDeploymentPartialTrackedResource
    from ._models_py3 import PartialOnlineEndpointPartialTrackedResource
    from ._models_py3 import PartialOutputPathAssetReference
    from ._models_py3 import PartialSku
    from ._models_py3 import Password
    from ._models_py3 import PipelineJob
    from ._models_py3 import PrivateEndpointConnection
    from ._models_py3 import PrivateEndpointConnectionListResult
    from ._models_py3 import PrivateEndpointDestination
    from ._models_py3 import PrivateEndpointOutboundRule
    from ._models_py3 import PrivateLinkResource
    from ._models_py3 import PrivateLinkResourceListResult
    from ._models_py3 import PrivateLinkServiceConnectionState
    from ._models_py3 import ProbeSettings
    from ._models_py3 import PyTorch
    from ._models_py3 import RandomSamplingAlgorithm
    from ._models_py3 import RegenerateEndpointKeysRequest
    from ._models_py3 import RegistryListCredentialsResult
    from ._models_py3 import Resource
    from ._models_py3 import ResourceBase
    from ._models_py3 import ResourceConfiguration
    from ._models_py3 import Route
    from ._models_py3 import SASAuthTypeWorkspaceConnectionProperties
    from ._models_py3 import SamplingAlgorithm
    from ._models_py3 import SasDatastoreCredentials
    from ._models_py3 import SasDatastoreSecrets
    from ._models_py3 import ServiceManagedResourcesSettings
    from ._models_py3 import ServicePrincipalAuthTypeWorkspaceConnectionProperties
    from ._models_py3 import ServicePrincipalDatastoreCredentials
    from ._models_py3 import ServicePrincipalDatastoreSecrets
    from ._models_py3 import ServiceTagDestination
    from ._models_py3 import ServiceTagOutboundRule
    from ._models_py3 import SharedPrivateLinkResource
    from ._models_py3 import Sku
    from ._models_py3 import SkuCapacity
    from ._models_py3 import SkuResource
    from ._models_py3 import SkuResourceArmPaginatedResult
    from ._models_py3 import SkuSetting
    from ._models_py3 import SweepJob
    from ._models_py3 import SweepJobLimits
    from ._models_py3 import SystemData
    from ._models_py3 import TargetUtilizationScaleSettings
    from ._models_py3 import TensorFlow
    from ._models_py3 import TrackedResource
    from ._models_py3 import TrialComponent
    from ._models_py3 import TritonModelJobInput
    from ._models_py3 import TritonModelJobOutput
    from ._models_py3 import TruncationSelectionPolicy
    from ._models_py3 import UriFileDataVersion
    from ._models_py3 import UriFileJobInput
    from ._models_py3 import UriFileJobOutput
    from ._models_py3 import UriFolderDataVersion
    from ._models_py3 import UriFolderJobInput
    from ._models_py3 import UriFolderJobOutput
    from ._models_py3 import UserAssignedIdentity
    from ._models_py3 import UserIdentity
    from ._models_py3 import UsernamePasswordAuthTypeWorkspaceConnectionProperties
    from ._models_py3 import Workspace
    from ._models_py3 import WorkspaceConnectionAccessKey
    from ._models_py3 import WorkspaceConnectionApiKey
    from ._models_py3 import WorkspaceConnectionManagedIdentity
    from ._models_py3 import WorkspaceConnectionPersonalAccessToken
    from ._models_py3 import WorkspaceConnectionPropertiesV2
    from ._models_py3 import WorkspaceConnectionPropertiesV2BasicResource
    from ._models_py3 import WorkspaceConnectionPropertiesV2BasicResourceArmPaginatedResult
    from ._models_py3 import WorkspaceConnectionServicePrincipal
    from ._models_py3 import WorkspaceConnectionSharedAccessSignature
    from ._models_py3 import WorkspaceConnectionUpdateParameter
    from ._models_py3 import WorkspaceConnectionUsernamePassword
    from ._models_py3 import WorkspaceHubConfig
    from ._models_py3 import WorkspaceListResult
    from ._models_py3 import WorkspacePrivateEndpointResource
    from ._models_py3 import WorkspaceUpdateParameters
except (SyntaxError, ImportError):
    from ._models import AccessKeyAuthTypeWorkspaceConnectionProperties  # type: ignore
    from ._models import AccountKeyDatastoreCredentials  # type: ignore
    from ._models import AccountKeyDatastoreSecrets  # type: ignore
    from ._models import AmlOperation  # type: ignore
    from ._models import AmlOperationListResult  # type: ignore
    from ._models import AmlToken  # type: ignore
    from ._models import AmlUserFeature  # type: ignore
    from ._models import ApiKeyAuthWorkspaceConnectionProperties  # type: ignore
    from ._models import AssetBase  # type: ignore
    from ._models import AssetContainer  # type: ignore
    from ._models import AssetJobInput  # type: ignore
    from ._models import AssetJobOutput  # type: ignore
    from ._models import AssetReferenceBase  # type: ignore
    from ._models import AzureBlobDatastore  # type: ignore
    from ._models import AzureDataLakeGen1Datastore  # type: ignore
    from ._models import AzureDataLakeGen2Datastore  # type: ignore
    from ._models import AzureFileDatastore  # type: ignore
    from ._models import BanditPolicy  # type: ignore
    from ._models import BatchDeploymentData  # type: ignore
    from ._models import BatchDeploymentDetails  # type: ignore
    from ._models import BatchDeploymentTrackedResourceArmPaginatedResult  # type: ignore
    from ._models import BatchEndpointData  # type: ignore
    from ._models import BatchEndpointDefaults  # type: ignore
    from ._models import BatchEndpointDetails  # type: ignore
    from ._models import BatchEndpointTrackedResourceArmPaginatedResult  # type: ignore
    from ._models import BatchRetrySettings  # type: ignore
    from ._models import BayesianSamplingAlgorithm  # type: ignore
    from ._models import BuildContext  # type: ignore
    from ._models import CertificateDatastoreCredentials  # type: ignore
    from ._models import CertificateDatastoreSecrets  # type: ignore
    from ._models import CodeConfiguration  # type: ignore
    from ._models import CodeContainerData  # type: ignore
    from ._models import CodeContainerDetails  # type: ignore
    from ._models import CodeContainerResourceArmPaginatedResult  # type: ignore
    from ._models import CodeVersionData  # type: ignore
    from ._models import CodeVersionDetails  # type: ignore
    from ._models import CodeVersionResourceArmPaginatedResult  # type: ignore
    from ._models import CommandJob  # type: ignore
    from ._models import CommandJobLimits  # type: ignore
    from ._models import ComponentContainerData  # type: ignore
    from ._models import ComponentContainerDetails  # type: ignore
    from ._models import ComponentContainerResourceArmPaginatedResult  # type: ignore
    from ._models import ComponentVersionData  # type: ignore
    from ._models import ComponentVersionDetails  # type: ignore
    from ._models import ComponentVersionResourceArmPaginatedResult  # type: ignore
    from ._models import ComputeRuntimeDto  # type: ignore
    from ._models import ContainerResourceRequirements  # type: ignore
    from ._models import ContainerResourceSettings  # type: ignore
    from ._models import CosmosDbSettings  # type: ignore
    from ._models import CustomKeys  # type: ignore
    from ._models import CustomKeysWorkspaceConnectionProperties  # type: ignore
    from ._models import CustomModelJobInput  # type: ignore
    from ._models import CustomModelJobOutput  # type: ignore
    from ._models import DataContainerData  # type: ignore
    from ._models import DataContainerDetails  # type: ignore
    from ._models import DataContainerResourceArmPaginatedResult  # type: ignore
    from ._models import DataPathAssetReference  # type: ignore
    from ._models import DataVersionBaseData  # type: ignore
    from ._models import DataVersionBaseDetails  # type: ignore
    from ._models import DataVersionBaseResourceArmPaginatedResult  # type: ignore
    from ._models import DatastoreCredentials  # type: ignore
    from ._models import DatastoreData  # type: ignore
    from ._models import DatastoreDetails  # type: ignore
    from ._models import DatastoreResourceArmPaginatedResult  # type: ignore
    from ._models import DatastoreSecrets  # type: ignore
    from ._models import DefaultScaleSettings  # type: ignore
    from ._models import DeploymentLogs  # type: ignore
    from ._models import DeploymentLogsRequest  # type: ignore
    from ._models import DiagnoseRequestProperties  # type: ignore
    from ._models import DiagnoseResponseResult  # type: ignore
    from ._models import DiagnoseResponseResultValue  # type: ignore
    from ._models import DiagnoseResult  # type: ignore
    from ._models import DiagnoseWorkspaceParameters  # type: ignore
    from ._models import DistributionConfiguration  # type: ignore
    from ._models import EarlyTerminationPolicy  # type: ignore
    from ._models import EncryptionKeyVaultUpdateProperties  # type: ignore
    from ._models import EncryptionProperty  # type: ignore
    from ._models import EncryptionUpdateProperties  # type: ignore
    from ._models import EndpointAuthKeys  # type: ignore
    from ._models import EndpointAuthToken  # type: ignore
    from ._models import EndpointDeploymentPropertiesBase  # type: ignore
    from ._models import EndpointPropertiesBase  # type: ignore
    from ._models import EnvironmentContainerData  # type: ignore
    from ._models import EnvironmentContainerDetails  # type: ignore
    from ._models import EnvironmentContainerResourceArmPaginatedResult  # type: ignore
    from ._models import EnvironmentVersionData  # type: ignore
    from ._models import EnvironmentVersionDetails  # type: ignore
    from ._models import EnvironmentVersionResourceArmPaginatedResult  # type: ignore
    from ._models import ErrorAdditionalInfo  # type: ignore
    from ._models import ErrorDetail  # type: ignore
    from ._models import ErrorResponse  # type: ignore
    from ._models import ExternalFQDNResponse  # type: ignore
    from ._models import FQDNEndpoint  # type: ignore
    from ._models import FQDNEndpointDetail  # type: ignore
    from ._models import FQDNEndpoints  # type: ignore
    from ._models import FQDNEndpointsPropertyBag  # type: ignore
    from ._models import FeatureStoreSettings  # type: ignore
    from ._models import FlavorData  # type: ignore
    from ._models import FqdnOutboundRule  # type: ignore
    from ._models import GridSamplingAlgorithm  # type: ignore
    from ._models import IdAssetReference  # type: ignore
    from ._models import IdentityConfiguration  # type: ignore
    from ._models import IdentityForCmk  # type: ignore
    from ._models import InferenceContainerProperties  # type: ignore
    from ._models import JobBaseData  # type: ignore
    from ._models import JobBaseDetails  # type: ignore
    from ._models import JobBaseResourceArmPaginatedResult  # type: ignore
    from ._models import JobInput  # type: ignore
    from ._models import JobLimits  # type: ignore
    from ._models import JobOutput  # type: ignore
    from ._models import JobService  # type: ignore
    from ._models import KeyVaultProperties  # type: ignore
    from ._models import KubernetesOnlineDeployment  # type: ignore
    from ._models import ListAmlUserFeatureResult  # type: ignore
    from ._models import ListNotebookKeysResult  # type: ignore
    from ._models import ListStorageAccountKeysResult  # type: ignore
    from ._models import ListWorkspaceKeysResult  # type: ignore
    from ._models import LiteralJobInput  # type: ignore
    from ._models import MLFlowModelJobInput  # type: ignore
    from ._models import MLFlowModelJobOutput  # type: ignore
    from ._models import MLTableData  # type: ignore
    from ._models import MLTableJobInput  # type: ignore
    from ._models import MLTableJobOutput  # type: ignore
    from ._models import ManagedIdentity  # type: ignore
    from ._models import ManagedIdentityAuthTypeWorkspaceConnectionProperties  # type: ignore
    from ._models import ManagedNetworkProvisionOptions  # type: ignore
    from ._models import ManagedNetworkProvisionStatus  # type: ignore
    from ._models import ManagedOnlineDeployment  # type: ignore
    from ._models import ManagedServiceIdentity  # type: ignore
    from ._models import MedianStoppingPolicy  # type: ignore
    from ._models import ModelContainerData  # type: ignore
    from ._models import ModelContainerDetails  # type: ignore
    from ._models import ModelContainerResourceArmPaginatedResult  # type: ignore
    from ._models import ModelVersionData  # type: ignore
    from ._models import ModelVersionDetails  # type: ignore
    from ._models import ModelVersionResourceArmPaginatedResult  # type: ignore
    from ._models import Mpi  # type: ignore
    from ._models import NoneAuthTypeWorkspaceConnectionProperties  # type: ignore
    from ._models import NoneDatastoreCredentials  # type: ignore
    from ._models import NotebookAccessTokenResult  # type: ignore
    from ._models import NotebookPreparationError  # type: ignore
    from ._models import NotebookResourceInfo  # type: ignore
    from ._models import Objective  # type: ignore
    from ._models import OnlineDeploymentData  # type: ignore
    from ._models import OnlineDeploymentDetails  # type: ignore
    from ._models import OnlineDeploymentTrackedResourceArmPaginatedResult  # type: ignore
    from ._models import OnlineEndpointData  # type: ignore
    from ._models import OnlineEndpointDetails  # type: ignore
    from ._models import OnlineEndpointTrackedResourceArmPaginatedResult  # type: ignore
    from ._models import OnlineRequestSettings  # type: ignore
    from ._models import OnlineScaleSettings  # type: ignore
    from ._models import OperationDisplay  # type: ignore
    from ._models import OutboundRule  # type: ignore
    from ._models import OutboundRuleBasicResource  # type: ignore
    from ._models import OutboundRuleListResult  # type: ignore
    from ._models import OutputPathAssetReference  # type: ignore
    from ._models import PATAuthTypeWorkspaceConnectionProperties  # type: ignore
    from ._models import PartialAssetReferenceBase  # type: ignore
    from ._models import PartialBatchDeployment  # type: ignore
    from ._models import PartialBatchDeploymentPartialTrackedResource  # type: ignore
    from ._models import PartialBatchEndpoint  # type: ignore
    from ._models import PartialBatchEndpointPartialTrackedResource  # type: ignore
    from ._models import PartialBatchRetrySettings  # type: ignore
    from ._models import PartialCodeConfiguration  # type: ignore
    from ._models import PartialDataPathAssetReference  # type: ignore
    from ._models import PartialIdAssetReference  # type: ignore
    from ._models import PartialKubernetesOnlineDeployment  # type: ignore
    from ._models import PartialManagedOnlineDeployment  # type: ignore
    from ._models import PartialManagedServiceIdentity  # type: ignore
    from ._models import PartialOnlineDeployment  # type: ignore
    from ._models import PartialOnlineDeploymentPartialTrackedResource  # type: ignore
    from ._models import PartialOnlineEndpointPartialTrackedResource  # type: ignore
    from ._models import PartialOutputPathAssetReference  # type: ignore
    from ._models import PartialSku  # type: ignore
    from ._models import Password  # type: ignore
    from ._models import PipelineJob  # type: ignore
    from ._models import PrivateEndpointConnection  # type: ignore
    from ._models import PrivateEndpointConnectionListResult  # type: ignore
    from ._models import PrivateEndpointDestination  # type: ignore
    from ._models import PrivateEndpointOutboundRule  # type: ignore
    from ._models import PrivateLinkResource  # type: ignore
    from ._models import PrivateLinkResourceListResult  # type: ignore
    from ._models import PrivateLinkServiceConnectionState  # type: ignore
    from ._models import ProbeSettings  # type: ignore
    from ._models import PyTorch  # type: ignore
    from ._models import RandomSamplingAlgorithm  # type: ignore
    from ._models import RegenerateEndpointKeysRequest  # type: ignore
    from ._models import RegistryListCredentialsResult  # type: ignore
    from ._models import Resource  # type: ignore
    from ._models import ResourceBase  # type: ignore
    from ._models import ResourceConfiguration  # type: ignore
    from ._models import Route  # type: ignore
    from ._models import SASAuthTypeWorkspaceConnectionProperties  # type: ignore
    from ._models import SamplingAlgorithm  # type: ignore
    from ._models import SasDatastoreCredentials  # type: ignore
    from ._models import SasDatastoreSecrets  # type: ignore
    from ._models import ServiceManagedResourcesSettings  # type: ignore
    from ._models import ServicePrincipalAuthTypeWorkspaceConnectionProperties  # type: ignore
    from ._models import ServicePrincipalDatastoreCredentials  # type: ignore
    from ._models import ServicePrincipalDatastoreSecrets  # type: ignore
    from ._models import ServiceTagDestination  # type: ignore
    from ._models import ServiceTagOutboundRule  # type: ignore
    from ._models import SharedPrivateLinkResource  # type: ignore
    from ._models import Sku  # type: ignore
    from ._models import SkuCapacity  # type: ignore
    from ._models import SkuResource  # type: ignore
    from ._models import SkuResourceArmPaginatedResult  # type: ignore
    from ._models import SkuSetting  # type: ignore
    from ._models import SweepJob  # type: ignore
    from ._models import SweepJobLimits  # type: ignore
    from ._models import SystemData  # type: ignore
    from ._models import TargetUtilizationScaleSettings  # type: ignore
    from ._models import TensorFlow  # type: ignore
    from ._models import TrackedResource  # type: ignore
    from ._models import TrialComponent  # type: ignore
    from ._models import TritonModelJobInput  # type: ignore
    from ._models import TritonModelJobOutput  # type: ignore
    from ._models import TruncationSelectionPolicy  # type: ignore
    from ._models import UriFileDataVersion  # type: ignore
    from ._models import UriFileJobInput  # type: ignore
    from ._models import UriFileJobOutput  # type: ignore
    from ._models import UriFolderDataVersion  # type: ignore
    from ._models import UriFolderJobInput  # type: ignore
    from ._models import UriFolderJobOutput  # type: ignore
    from ._models import UserAssignedIdentity  # type: ignore
    from ._models import UserIdentity  # type: ignore
    from ._models import UsernamePasswordAuthTypeWorkspaceConnectionProperties  # type: ignore
    from ._models import Workspace  # type: ignore
    from ._models import WorkspaceConnectionAccessKey  # type: ignore
    from ._models import WorkspaceConnectionApiKey  # type: ignore
    from ._models import WorkspaceConnectionManagedIdentity  # type: ignore
    from ._models import WorkspaceConnectionPersonalAccessToken  # type: ignore
    from ._models import WorkspaceConnectionPropertiesV2  # type: ignore
    from ._models import WorkspaceConnectionPropertiesV2BasicResource  # type: ignore
    from ._models import WorkspaceConnectionPropertiesV2BasicResourceArmPaginatedResult  # type: ignore
    from ._models import WorkspaceConnectionServicePrincipal  # type: ignore
    from ._models import WorkspaceConnectionSharedAccessSignature  # type: ignore
    from ._models import WorkspaceConnectionUpdateParameter  # type: ignore
    from ._models import WorkspaceConnectionUsernamePassword  # type: ignore
    from ._models import WorkspaceHubConfig  # type: ignore
    from ._models import WorkspaceListResult  # type: ignore
    from ._models import WorkspacePrivateEndpointResource  # type: ignore
    from ._models import WorkspaceUpdateParameters  # type: ignore

from ._azure_machine_learning_workspaces_enums import (
    BatchLoggingLevel,
    BatchOutputAction,
    ConnectionAuthType,
    ConnectionCategory,
    ContainerType,
    CreatedByType,
    CredentialsType,
    DataType,
    DatastoreType,
    DeploymentProvisioningState,
    DiagnoseResultLevel,
    DistributionType,
    EarlyTerminationPolicyType,
    EncryptionStatus,
    EndpointAuthMode,
    EndpointComputeType,
    EndpointProvisioningState,
    EndpointServiceConnectionStatus,
    EnvironmentType,
    Goal,
    IdentityConfigurationType,
    InputDeliveryMode,
    JobInputType,
    JobLimitsType,
    JobOutputType,
    JobStatus,
    JobType,
    KeyType,
    ListViewType,
    ManagedNetworkStatus,
    ManagedServiceIdentityType,
    OperatingSystemType,
    OrderString,
    OutputDeliveryMode,
    ProvisioningState,
    PublicNetworkAccessType,
    RandomSamplingAlgorithmRule,
    ReferenceType,
    RuleAction,
    RuleCategory,
    RuleStatus,
    RuleType,
    SamplingAlgorithmType,
    ScaleType,
    SecretsType,
    ServiceDataAccessAuthIdentity,
    SkuScaleType,
    SkuTier,
)

__all__ = [
    'AccessKeyAuthTypeWorkspaceConnectionProperties',
    'AccountKeyDatastoreCredentials',
    'AccountKeyDatastoreSecrets',
    'AmlOperation',
    'AmlOperationListResult',
    'AmlToken',
    'AmlUserFeature',
    'ApiKeyAuthWorkspaceConnectionProperties',
    'AssetBase',
    'AssetContainer',
    'AssetJobInput',
    'AssetJobOutput',
    'AssetReferenceBase',
    'AzureBlobDatastore',
    'AzureDataLakeGen1Datastore',
    'AzureDataLakeGen2Datastore',
    'AzureFileDatastore',
    'BanditPolicy',
    'BatchDeploymentData',
    'BatchDeploymentDetails',
    'BatchDeploymentTrackedResourceArmPaginatedResult',
    'BatchEndpointData',
    'BatchEndpointDefaults',
    'BatchEndpointDetails',
    'BatchEndpointTrackedResourceArmPaginatedResult',
    'BatchRetrySettings',
    'BayesianSamplingAlgorithm',
    'BuildContext',
    'CertificateDatastoreCredentials',
    'CertificateDatastoreSecrets',
    'CodeConfiguration',
    'CodeContainerData',
    'CodeContainerDetails',
    'CodeContainerResourceArmPaginatedResult',
    'CodeVersionData',
    'CodeVersionDetails',
    'CodeVersionResourceArmPaginatedResult',
    'CommandJob',
    'CommandJobLimits',
    'ComponentContainerData',
    'ComponentContainerDetails',
    'ComponentContainerResourceArmPaginatedResult',
    'ComponentVersionData',
    'ComponentVersionDetails',
    'ComponentVersionResourceArmPaginatedResult',
    'ComputeRuntimeDto',
    'ContainerResourceRequirements',
    'ContainerResourceSettings',
    'CosmosDbSettings',
    'CustomKeys',
    'CustomKeysWorkspaceConnectionProperties',
    'CustomModelJobInput',
    'CustomModelJobOutput',
    'DataContainerData',
    'DataContainerDetails',
    'DataContainerResourceArmPaginatedResult',
    'DataPathAssetReference',
    'DataVersionBaseData',
    'DataVersionBaseDetails',
    'DataVersionBaseResourceArmPaginatedResult',
    'DatastoreCredentials',
    'DatastoreData',
    'DatastoreDetails',
    'DatastoreResourceArmPaginatedResult',
    'DatastoreSecrets',
    'DefaultScaleSettings',
    'DeploymentLogs',
    'DeploymentLogsRequest',
    'DiagnoseRequestProperties',
    'DiagnoseResponseResult',
    'DiagnoseResponseResultValue',
    'DiagnoseResult',
    'DiagnoseWorkspaceParameters',
    'DistributionConfiguration',
    'EarlyTerminationPolicy',
    'EncryptionKeyVaultUpdateProperties',
    'EncryptionProperty',
    'EncryptionUpdateProperties',
    'EndpointAuthKeys',
    'EndpointAuthToken',
    'EndpointDeploymentPropertiesBase',
    'EndpointPropertiesBase',
    'EnvironmentContainerData',
    'EnvironmentContainerDetails',
    'EnvironmentContainerResourceArmPaginatedResult',
    'EnvironmentVersionData',
    'EnvironmentVersionDetails',
    'EnvironmentVersionResourceArmPaginatedResult',
    'ErrorAdditionalInfo',
    'ErrorDetail',
    'ErrorResponse',
    'ExternalFQDNResponse',
    'FQDNEndpoint',
    'FQDNEndpointDetail',
    'FQDNEndpoints',
    'FQDNEndpointsPropertyBag',
    'FeatureStoreSettings',
    'FlavorData',
    'FqdnOutboundRule',
    'GridSamplingAlgorithm',
    'IdAssetReference',
    'IdentityConfiguration',
    'IdentityForCmk',
    'InferenceContainerProperties',
    'JobBaseData',
    'JobBaseDetails',
    'JobBaseResourceArmPaginatedResult',
    'JobInput',
    'JobLimits',
    'JobOutput',
    'JobService',
    'KeyVaultProperties',
    'KubernetesOnlineDeployment',
    'ListAmlUserFeatureResult',
    'ListNotebookKeysResult',
    'ListStorageAccountKeysResult',
    'ListWorkspaceKeysResult',
    'LiteralJobInput',
    'MLFlowModelJobInput',
    'MLFlowModelJobOutput',
    'MLTableData',
    'MLTableJobInput',
    'MLTableJobOutput',
    'ManagedIdentity',
    'ManagedIdentityAuthTypeWorkspaceConnectionProperties',
    'ManagedNetworkProvisionOptions',
    'ManagedNetworkProvisionStatus',
    'ManagedOnlineDeployment',
    'ManagedServiceIdentity',
    'MedianStoppingPolicy',
    'ModelContainerData',
    'ModelContainerDetails',
    'ModelContainerResourceArmPaginatedResult',
    'ModelVersionData',
    'ModelVersionDetails',
    'ModelVersionResourceArmPaginatedResult',
    'Mpi',
    'NoneAuthTypeWorkspaceConnectionProperties',
    'NoneDatastoreCredentials',
    'NotebookAccessTokenResult',
    'NotebookPreparationError',
    'NotebookResourceInfo',
    'Objective',
    'OnlineDeploymentData',
    'OnlineDeploymentDetails',
    'OnlineDeploymentTrackedResourceArmPaginatedResult',
    'OnlineEndpointData',
    'OnlineEndpointDetails',
    'OnlineEndpointTrackedResourceArmPaginatedResult',
    'OnlineRequestSettings',
    'OnlineScaleSettings',
    'OperationDisplay',
    'OutboundRule',
    'OutboundRuleBasicResource',
    'OutboundRuleListResult',
    'OutputPathAssetReference',
    'PATAuthTypeWorkspaceConnectionProperties',
    'PartialAssetReferenceBase',
    'PartialBatchDeployment',
    'PartialBatchDeploymentPartialTrackedResource',
    'PartialBatchEndpoint',
    'PartialBatchEndpointPartialTrackedResource',
    'PartialBatchRetrySettings',
    'PartialCodeConfiguration',
    'PartialDataPathAssetReference',
    'PartialIdAssetReference',
    'PartialKubernetesOnlineDeployment',
    'PartialManagedOnlineDeployment',
    'PartialManagedServiceIdentity',
    'PartialOnlineDeployment',
    'PartialOnlineDeploymentPartialTrackedResource',
    'PartialOnlineEndpointPartialTrackedResource',
    'PartialOutputPathAssetReference',
    'PartialSku',
    'Password',
    'PipelineJob',
    'PrivateEndpointConnection',
    'PrivateEndpointConnectionListResult',
    'PrivateEndpointDestination',
    'PrivateEndpointOutboundRule',
    'PrivateLinkResource',
    'PrivateLinkResourceListResult',
    'PrivateLinkServiceConnectionState',
    'ProbeSettings',
    'PyTorch',
    'RandomSamplingAlgorithm',
    'RegenerateEndpointKeysRequest',
    'RegistryListCredentialsResult',
    'Resource',
    'ResourceBase',
    'ResourceConfiguration',
    'Route',
    'SASAuthTypeWorkspaceConnectionProperties',
    'SamplingAlgorithm',
    'SasDatastoreCredentials',
    'SasDatastoreSecrets',
    'ServiceManagedResourcesSettings',
    'ServicePrincipalAuthTypeWorkspaceConnectionProperties',
    'ServicePrincipalDatastoreCredentials',
    'ServicePrincipalDatastoreSecrets',
    'ServiceTagDestination',
    'ServiceTagOutboundRule',
    'SharedPrivateLinkResource',
    'Sku',
    'SkuCapacity',
    'SkuResource',
    'SkuResourceArmPaginatedResult',
    'SkuSetting',
    'SweepJob',
    'SweepJobLimits',
    'SystemData',
    'TargetUtilizationScaleSettings',
    'TensorFlow',
    'TrackedResource',
    'TrialComponent',
    'TritonModelJobInput',
    'TritonModelJobOutput',
    'TruncationSelectionPolicy',
    'UriFileDataVersion',
    'UriFileJobInput',
    'UriFileJobOutput',
    'UriFolderDataVersion',
    'UriFolderJobInput',
    'UriFolderJobOutput',
    'UserAssignedIdentity',
    'UserIdentity',
    'UsernamePasswordAuthTypeWorkspaceConnectionProperties',
    'Workspace',
    'WorkspaceConnectionAccessKey',
    'WorkspaceConnectionApiKey',
    'WorkspaceConnectionManagedIdentity',
    'WorkspaceConnectionPersonalAccessToken',
    'WorkspaceConnectionPropertiesV2',
    'WorkspaceConnectionPropertiesV2BasicResource',
    'WorkspaceConnectionPropertiesV2BasicResourceArmPaginatedResult',
    'WorkspaceConnectionServicePrincipal',
    'WorkspaceConnectionSharedAccessSignature',
    'WorkspaceConnectionUpdateParameter',
    'WorkspaceConnectionUsernamePassword',
    'WorkspaceHubConfig',
    'WorkspaceListResult',
    'WorkspacePrivateEndpointResource',
    'WorkspaceUpdateParameters',
    'BatchLoggingLevel',
    'BatchOutputAction',
    'ConnectionAuthType',
    'ConnectionCategory',
    'ContainerType',
    'CreatedByType',
    'CredentialsType',
    'DataType',
    'DatastoreType',
    'DeploymentProvisioningState',
    'DiagnoseResultLevel',
    'DistributionType',
    'EarlyTerminationPolicyType',
    'EncryptionStatus',
    'EndpointAuthMode',
    'EndpointComputeType',
    'EndpointProvisioningState',
    'EndpointServiceConnectionStatus',
    'EnvironmentType',
    'Goal',
    'IdentityConfigurationType',
    'InputDeliveryMode',
    'JobInputType',
    'JobLimitsType',
    'JobOutputType',
    'JobStatus',
    'JobType',
    'KeyType',
    'ListViewType',
    'ManagedNetworkStatus',
    'ManagedServiceIdentityType',
    'OperatingSystemType',
    'OrderString',
    'OutputDeliveryMode',
    'ProvisioningState',
    'PublicNetworkAccessType',
    'RandomSamplingAlgorithmRule',
    'ReferenceType',
    'RuleAction',
    'RuleCategory',
    'RuleStatus',
    'RuleType',
    'SamplingAlgorithmType',
    'ScaleType',
    'SecretsType',
    'ServiceDataAccessAuthIdentity',
    'SkuScaleType',
    'SkuTier',
]
