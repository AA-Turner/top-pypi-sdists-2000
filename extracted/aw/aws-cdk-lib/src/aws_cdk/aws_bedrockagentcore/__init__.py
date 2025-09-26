r'''
# AWS::BedrockAgentCore Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_bedrockagentcore as bedrockagentcore
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for BedrockAgentCore construct libraries](https://constructs.dev/search?q=bedrockagentcore)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::BedrockAgentCore resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_BedrockAgentCore.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::BedrockAgentCore](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_BedrockAgentCore.html).

(Read the [CDK Contributing Guide](https://github.com/aws/aws-cdk/blob/main/CONTRIBUTING.md) and submit an RFC if you are interested in contributing to this construct library.)

<!--END CFNONLY DISCLAIMER-->
'''
from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)

import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

import typeguard
from importlib.metadata import version as _metadata_package_version
TYPEGUARD_MAJOR_VERSION = int(_metadata_package_version('typeguard').split('.')[0])

def check_type(argname: str, value: object, expected_type: typing.Any) -> typing.Any:
    if TYPEGUARD_MAJOR_VERSION <= 2:
        return typeguard.check_type(argname=argname, value=value, expected_type=expected_type) # type:ignore
    else:
        if isinstance(value, jsii._reference_map.InterfaceDynamicProxy): # pyright: ignore [reportAttributeAccessIssue]
           pass
        else:
            if TYPEGUARD_MAJOR_VERSION == 3:
                typeguard.config.collection_check_strategy = typeguard.CollectionCheckStrategy.ALL_ITEMS # type:ignore
                typeguard.check_type(value=value, expected_type=expected_type) # type:ignore
            else:
                typeguard.check_type(value=value, expected_type=expected_type, collection_check_strategy=typeguard.CollectionCheckStrategy.ALL_ITEMS) # type:ignore

from .._jsii import *

import constructs as _constructs_77d1e7e8
from .. import (
    CfnResource as _CfnResource_9df397a6,
    IInspectable as _IInspectable_c2943556,
    IResolvable as _IResolvable_da3f097b,
    ITaggableV2 as _ITaggableV2_4e6798f8,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_bedrockagentcore.BrowserCustomReference",
    jsii_struct_bases=[],
    name_mapping={"browser_id": "browserId"},
)
class BrowserCustomReference:
    def __init__(self, *, browser_id: builtins.str) -> None:
        '''A reference to a BrowserCustom resource.

        :param browser_id: The BrowserId of the BrowserCustom resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_bedrockagentcore as bedrockagentcore
            
            browser_custom_reference = bedrockagentcore.BrowserCustomReference(
                browser_id="browserId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45e545da2b3da370563839cf7802f81e77f186bac4ddee7d944e49364fcf8806)
            check_type(argname="argument browser_id", value=browser_id, expected_type=type_hints["browser_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "browser_id": browser_id,
        }

    @builtins.property
    def browser_id(self) -> builtins.str:
        '''The BrowserId of the BrowserCustom resource.'''
        result = self._values.get("browser_id")
        assert result is not None, "Required property 'browser_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BrowserCustomReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnBrowserCustomProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "network_configuration": "networkConfiguration",
        "description": "description",
        "execution_role_arn": "executionRoleArn",
        "recording_config": "recordingConfig",
        "tags": "tags",
    },
)
class CfnBrowserCustomProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        network_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnBrowserCustom.BrowserNetworkConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        description: typing.Optional[builtins.str] = None,
        execution_role_arn: typing.Optional[builtins.str] = None,
        recording_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBrowserCustom.RecordingConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnBrowserCustom``.

        :param name: The name of the browser.
        :param network_configuration: Network configuration for browser.
        :param description: The description of the browser.
        :param execution_role_arn: The Amazon Resource Name (ARN) of the IAM role.
        :param recording_config: Recording configuration for browser.
        :param tags: A map of tag keys and values.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-browsercustom.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_bedrockagentcore as bedrockagentcore
            
            cfn_browser_custom_props = bedrockagentcore.CfnBrowserCustomProps(
                name="name",
                network_configuration=bedrockagentcore.CfnBrowserCustom.BrowserNetworkConfigurationProperty(
                    network_mode="networkMode"
                ),
            
                # the properties below are optional
                description="description",
                execution_role_arn="executionRoleArn",
                recording_config=bedrockagentcore.CfnBrowserCustom.RecordingConfigProperty(
                    enabled=False,
                    s3_location=bedrockagentcore.CfnBrowserCustom.S3LocationProperty(
                        bucket="bucket",
                        prefix="prefix"
                    )
                ),
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08f9adb5e20b52bbdc47438decbd54e3ebb4b1976cbf46432a19597fc6589c39)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument network_configuration", value=network_configuration, expected_type=type_hints["network_configuration"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument execution_role_arn", value=execution_role_arn, expected_type=type_hints["execution_role_arn"])
            check_type(argname="argument recording_config", value=recording_config, expected_type=type_hints["recording_config"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "network_configuration": network_configuration,
        }
        if description is not None:
            self._values["description"] = description
        if execution_role_arn is not None:
            self._values["execution_role_arn"] = execution_role_arn
        if recording_config is not None:
            self._values["recording_config"] = recording_config
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the browser.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-browsercustom.html#cfn-bedrockagentcore-browsercustom-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def network_configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnBrowserCustom.BrowserNetworkConfigurationProperty"]:
        '''Network configuration for browser.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-browsercustom.html#cfn-bedrockagentcore-browsercustom-networkconfiguration
        '''
        result = self._values.get("network_configuration")
        assert result is not None, "Required property 'network_configuration' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnBrowserCustom.BrowserNetworkConfigurationProperty"], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the browser.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-browsercustom.html#cfn-bedrockagentcore-browsercustom-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def execution_role_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the IAM role.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-browsercustom.html#cfn-bedrockagentcore-browsercustom-executionrolearn
        '''
        result = self._values.get("execution_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def recording_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBrowserCustom.RecordingConfigProperty"]]:
        '''Recording configuration for browser.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-browsercustom.html#cfn-bedrockagentcore-browsercustom-recordingconfig
        '''
        result = self._values.get("recording_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBrowserCustom.RecordingConfigProperty"]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map of tag keys and values.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-browsercustom.html#cfn-bedrockagentcore-browsercustom-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBrowserCustomProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnCodeInterpreterCustomProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "network_configuration": "networkConfiguration",
        "description": "description",
        "execution_role_arn": "executionRoleArn",
        "tags": "tags",
    },
)
class CfnCodeInterpreterCustomProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        network_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnCodeInterpreterCustom.CodeInterpreterNetworkConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        description: typing.Optional[builtins.str] = None,
        execution_role_arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnCodeInterpreterCustom``.

        :param name: The name of the sandbox.
        :param network_configuration: Network configuration for code interpreter.
        :param description: Description of the code interpreter.
        :param execution_role_arn: The ARN of the IAM role.
        :param tags: A map of tag keys and values.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-codeinterpretercustom.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_bedrockagentcore as bedrockagentcore
            
            cfn_code_interpreter_custom_props = bedrockagentcore.CfnCodeInterpreterCustomProps(
                name="name",
                network_configuration=bedrockagentcore.CfnCodeInterpreterCustom.CodeInterpreterNetworkConfigurationProperty(
                    network_mode="networkMode"
                ),
            
                # the properties below are optional
                description="description",
                execution_role_arn="executionRoleArn",
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b5217aa9ccd0ec964b92c3a48855bb1494914c435606fcee5b0faefd790d264)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument network_configuration", value=network_configuration, expected_type=type_hints["network_configuration"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument execution_role_arn", value=execution_role_arn, expected_type=type_hints["execution_role_arn"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "network_configuration": network_configuration,
        }
        if description is not None:
            self._values["description"] = description
        if execution_role_arn is not None:
            self._values["execution_role_arn"] = execution_role_arn
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the sandbox.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-codeinterpretercustom.html#cfn-bedrockagentcore-codeinterpretercustom-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def network_configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnCodeInterpreterCustom.CodeInterpreterNetworkConfigurationProperty"]:
        '''Network configuration for code interpreter.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-codeinterpretercustom.html#cfn-bedrockagentcore-codeinterpretercustom-networkconfiguration
        '''
        result = self._values.get("network_configuration")
        assert result is not None, "Required property 'network_configuration' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnCodeInterpreterCustom.CodeInterpreterNetworkConfigurationProperty"], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Description of the code interpreter.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-codeinterpretercustom.html#cfn-bedrockagentcore-codeinterpretercustom-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def execution_role_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the IAM role.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-codeinterpretercustom.html#cfn-bedrockagentcore-codeinterpretercustom-executionrolearn
        '''
        result = self._values.get("execution_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map of tag keys and values.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-codeinterpretercustom.html#cfn-bedrockagentcore-codeinterpretercustom-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCodeInterpreterCustomProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnRuntimeEndpointProps",
    jsii_struct_bases=[],
    name_mapping={
        "agent_runtime_id": "agentRuntimeId",
        "name": "name",
        "agent_runtime_version": "agentRuntimeVersion",
        "description": "description",
        "tags": "tags",
    },
)
class CfnRuntimeEndpointProps:
    def __init__(
        self,
        *,
        agent_runtime_id: builtins.str,
        name: builtins.str,
        agent_runtime_version: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnRuntimeEndpoint``.

        :param agent_runtime_id: The ID of the parent Agent Runtime.
        :param name: 
        :param agent_runtime_version: 
        :param description: 
        :param tags: A map of tag keys and values.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-runtimeendpoint.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_bedrockagentcore as bedrockagentcore
            
            cfn_runtime_endpoint_props = bedrockagentcore.CfnRuntimeEndpointProps(
                agent_runtime_id="agentRuntimeId",
                name="name",
            
                # the properties below are optional
                agent_runtime_version="agentRuntimeVersion",
                description="description",
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03746d507f3e8e95afbebc436c73d1ac1fc643ccea60f817b99b76cb41ccf5fb)
            check_type(argname="argument agent_runtime_id", value=agent_runtime_id, expected_type=type_hints["agent_runtime_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument agent_runtime_version", value=agent_runtime_version, expected_type=type_hints["agent_runtime_version"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "agent_runtime_id": agent_runtime_id,
            "name": name,
        }
        if agent_runtime_version is not None:
            self._values["agent_runtime_version"] = agent_runtime_version
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def agent_runtime_id(self) -> builtins.str:
        '''The ID of the parent Agent Runtime.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-runtimeendpoint.html#cfn-bedrockagentcore-runtimeendpoint-agentruntimeid
        '''
        result = self._values.get("agent_runtime_id")
        assert result is not None, "Required property 'agent_runtime_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-runtimeendpoint.html#cfn-bedrockagentcore-runtimeendpoint-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def agent_runtime_version(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-runtimeendpoint.html#cfn-bedrockagentcore-runtimeendpoint-agentruntimeversion
        '''
        result = self._values.get("agent_runtime_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-runtimeendpoint.html#cfn-bedrockagentcore-runtimeendpoint-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map of tag keys and values.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-runtimeendpoint.html#cfn-bedrockagentcore-runtimeendpoint-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRuntimeEndpointProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnRuntimeProps",
    jsii_struct_bases=[],
    name_mapping={
        "agent_runtime_artifact": "agentRuntimeArtifact",
        "agent_runtime_name": "agentRuntimeName",
        "network_configuration": "networkConfiguration",
        "role_arn": "roleArn",
        "authorizer_configuration": "authorizerConfiguration",
        "description": "description",
        "environment_variables": "environmentVariables",
        "protocol_configuration": "protocolConfiguration",
        "tags": "tags",
    },
)
class CfnRuntimeProps:
    def __init__(
        self,
        *,
        agent_runtime_artifact: typing.Union[_IResolvable_da3f097b, typing.Union["CfnRuntime.AgentRuntimeArtifactProperty", typing.Dict[builtins.str, typing.Any]]],
        agent_runtime_name: builtins.str,
        network_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnRuntime.NetworkConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        role_arn: builtins.str,
        authorizer_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRuntime.AuthorizerConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        environment_variables: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]] = None,
        protocol_configuration: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnRuntime``.

        :param agent_runtime_artifact: 
        :param agent_runtime_name: 
        :param network_configuration: 
        :param role_arn: 
        :param authorizer_configuration: Configuration for the authorizer.
        :param description: 
        :param environment_variables: Environment variable attributes.
        :param protocol_configuration: 
        :param tags: A map of tag keys and values.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-runtime.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_bedrockagentcore as bedrockagentcore
            
            cfn_runtime_props = bedrockagentcore.CfnRuntimeProps(
                agent_runtime_artifact=bedrockagentcore.CfnRuntime.AgentRuntimeArtifactProperty(
                    container_configuration=bedrockagentcore.CfnRuntime.ContainerConfigurationProperty(
                        container_uri="containerUri"
                    )
                ),
                agent_runtime_name="agentRuntimeName",
                network_configuration=bedrockagentcore.CfnRuntime.NetworkConfigurationProperty(
                    network_mode="networkMode"
                ),
                role_arn="roleArn",
            
                # the properties below are optional
                authorizer_configuration=bedrockagentcore.CfnRuntime.AuthorizerConfigurationProperty(
                    custom_jwt_authorizer=bedrockagentcore.CfnRuntime.CustomJWTAuthorizerConfigurationProperty(
                        discovery_url="discoveryUrl",
            
                        # the properties below are optional
                        allowed_audience=["allowedAudience"],
                        allowed_clients=["allowedClients"]
                    )
                ),
                description="description",
                environment_variables={
                    "environment_variables_key": "environmentVariables"
                },
                protocol_configuration="protocolConfiguration",
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e489b12cef85647a902e6bba6db3bf5f3ef1a856b74cf0fc5a7f8d1d0fa4a4b)
            check_type(argname="argument agent_runtime_artifact", value=agent_runtime_artifact, expected_type=type_hints["agent_runtime_artifact"])
            check_type(argname="argument agent_runtime_name", value=agent_runtime_name, expected_type=type_hints["agent_runtime_name"])
            check_type(argname="argument network_configuration", value=network_configuration, expected_type=type_hints["network_configuration"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument authorizer_configuration", value=authorizer_configuration, expected_type=type_hints["authorizer_configuration"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument environment_variables", value=environment_variables, expected_type=type_hints["environment_variables"])
            check_type(argname="argument protocol_configuration", value=protocol_configuration, expected_type=type_hints["protocol_configuration"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "agent_runtime_artifact": agent_runtime_artifact,
            "agent_runtime_name": agent_runtime_name,
            "network_configuration": network_configuration,
            "role_arn": role_arn,
        }
        if authorizer_configuration is not None:
            self._values["authorizer_configuration"] = authorizer_configuration
        if description is not None:
            self._values["description"] = description
        if environment_variables is not None:
            self._values["environment_variables"] = environment_variables
        if protocol_configuration is not None:
            self._values["protocol_configuration"] = protocol_configuration
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def agent_runtime_artifact(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnRuntime.AgentRuntimeArtifactProperty"]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-runtime.html#cfn-bedrockagentcore-runtime-agentruntimeartifact
        '''
        result = self._values.get("agent_runtime_artifact")
        assert result is not None, "Required property 'agent_runtime_artifact' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnRuntime.AgentRuntimeArtifactProperty"], result)

    @builtins.property
    def agent_runtime_name(self) -> builtins.str:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-runtime.html#cfn-bedrockagentcore-runtime-agentruntimename
        '''
        result = self._values.get("agent_runtime_name")
        assert result is not None, "Required property 'agent_runtime_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def network_configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnRuntime.NetworkConfigurationProperty"]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-runtime.html#cfn-bedrockagentcore-runtime-networkconfiguration
        '''
        result = self._values.get("network_configuration")
        assert result is not None, "Required property 'network_configuration' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnRuntime.NetworkConfigurationProperty"], result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-runtime.html#cfn-bedrockagentcore-runtime-rolearn
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def authorizer_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRuntime.AuthorizerConfigurationProperty"]]:
        '''Configuration for the authorizer.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-runtime.html#cfn-bedrockagentcore-runtime-authorizerconfiguration
        '''
        result = self._values.get("authorizer_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRuntime.AuthorizerConfigurationProperty"]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-runtime.html#cfn-bedrockagentcore-runtime-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def environment_variables(
        self,
    ) -> typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]]:
        '''Environment variable attributes.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-runtime.html#cfn-bedrockagentcore-runtime-environmentvariables
        '''
        result = self._values.get("environment_variables")
        return typing.cast(typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]], result)

    @builtins.property
    def protocol_configuration(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-runtime.html#cfn-bedrockagentcore-runtime-protocolconfiguration
        '''
        result = self._values.get("protocol_configuration")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map of tag keys and values.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-runtime.html#cfn-bedrockagentcore-runtime-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRuntimeProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_bedrockagentcore.CodeInterpreterCustomReference",
    jsii_struct_bases=[],
    name_mapping={"code_interpreter_id": "codeInterpreterId"},
)
class CodeInterpreterCustomReference:
    def __init__(self, *, code_interpreter_id: builtins.str) -> None:
        '''A reference to a CodeInterpreterCustom resource.

        :param code_interpreter_id: The CodeInterpreterId of the CodeInterpreterCustom resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_bedrockagentcore as bedrockagentcore
            
            code_interpreter_custom_reference = bedrockagentcore.CodeInterpreterCustomReference(
                code_interpreter_id="codeInterpreterId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89dc37aef7efb202707ab991eff3008383de6de10f2228d9e9beb350d3f170d5)
            check_type(argname="argument code_interpreter_id", value=code_interpreter_id, expected_type=type_hints["code_interpreter_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "code_interpreter_id": code_interpreter_id,
        }

    @builtins.property
    def code_interpreter_id(self) -> builtins.str:
        '''The CodeInterpreterId of the CodeInterpreterCustom resource.'''
        result = self._values.get("code_interpreter_id")
        assert result is not None, "Required property 'code_interpreter_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodeInterpreterCustomReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.aws_bedrockagentcore.IBrowserCustomRef")
class IBrowserCustomRef(_constructs_77d1e7e8.IConstruct, typing_extensions.Protocol):
    '''(experimental) Indicates that this resource can be referenced as a BrowserCustom.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="browserCustomRef")
    def browser_custom_ref(self) -> BrowserCustomReference:
        '''(experimental) A reference to a BrowserCustom resource.

        :stability: experimental
        '''
        ...


class _IBrowserCustomRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a BrowserCustom.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_bedrockagentcore.IBrowserCustomRef"

    @builtins.property
    @jsii.member(jsii_name="browserCustomRef")
    def browser_custom_ref(self) -> BrowserCustomReference:
        '''(experimental) A reference to a BrowserCustom resource.

        :stability: experimental
        '''
        return typing.cast(BrowserCustomReference, jsii.get(self, "browserCustomRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IBrowserCustomRef).__jsii_proxy_class__ = lambda : _IBrowserCustomRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_bedrockagentcore.ICodeInterpreterCustomRef")
class ICodeInterpreterCustomRef(
    _constructs_77d1e7e8.IConstruct,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a CodeInterpreterCustom.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="codeInterpreterCustomRef")
    def code_interpreter_custom_ref(self) -> CodeInterpreterCustomReference:
        '''(experimental) A reference to a CodeInterpreterCustom resource.

        :stability: experimental
        '''
        ...


class _ICodeInterpreterCustomRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a CodeInterpreterCustom.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_bedrockagentcore.ICodeInterpreterCustomRef"

    @builtins.property
    @jsii.member(jsii_name="codeInterpreterCustomRef")
    def code_interpreter_custom_ref(self) -> CodeInterpreterCustomReference:
        '''(experimental) A reference to a CodeInterpreterCustom resource.

        :stability: experimental
        '''
        return typing.cast(CodeInterpreterCustomReference, jsii.get(self, "codeInterpreterCustomRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICodeInterpreterCustomRef).__jsii_proxy_class__ = lambda : _ICodeInterpreterCustomRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_bedrockagentcore.IRuntimeEndpointRef")
class IRuntimeEndpointRef(_constructs_77d1e7e8.IConstruct, typing_extensions.Protocol):
    '''(experimental) Indicates that this resource can be referenced as a RuntimeEndpoint.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="runtimeEndpointRef")
    def runtime_endpoint_ref(self) -> "RuntimeEndpointReference":
        '''(experimental) A reference to a RuntimeEndpoint resource.

        :stability: experimental
        '''
        ...


class _IRuntimeEndpointRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a RuntimeEndpoint.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_bedrockagentcore.IRuntimeEndpointRef"

    @builtins.property
    @jsii.member(jsii_name="runtimeEndpointRef")
    def runtime_endpoint_ref(self) -> "RuntimeEndpointReference":
        '''(experimental) A reference to a RuntimeEndpoint resource.

        :stability: experimental
        '''
        return typing.cast("RuntimeEndpointReference", jsii.get(self, "runtimeEndpointRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRuntimeEndpointRef).__jsii_proxy_class__ = lambda : _IRuntimeEndpointRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_bedrockagentcore.IRuntimeRef")
class IRuntimeRef(_constructs_77d1e7e8.IConstruct, typing_extensions.Protocol):
    '''(experimental) Indicates that this resource can be referenced as a Runtime.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="runtimeRef")
    def runtime_ref(self) -> "RuntimeReference":
        '''(experimental) A reference to a Runtime resource.

        :stability: experimental
        '''
        ...


class _IRuntimeRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Runtime.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_bedrockagentcore.IRuntimeRef"

    @builtins.property
    @jsii.member(jsii_name="runtimeRef")
    def runtime_ref(self) -> "RuntimeReference":
        '''(experimental) A reference to a Runtime resource.

        :stability: experimental
        '''
        return typing.cast("RuntimeReference", jsii.get(self, "runtimeRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRuntimeRef).__jsii_proxy_class__ = lambda : _IRuntimeRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_bedrockagentcore.RuntimeEndpointReference",
    jsii_struct_bases=[],
    name_mapping={"agent_runtime_endpoint_arn": "agentRuntimeEndpointArn"},
)
class RuntimeEndpointReference:
    def __init__(self, *, agent_runtime_endpoint_arn: builtins.str) -> None:
        '''A reference to a RuntimeEndpoint resource.

        :param agent_runtime_endpoint_arn: The AgentRuntimeEndpointArn of the RuntimeEndpoint resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_bedrockagentcore as bedrockagentcore
            
            runtime_endpoint_reference = bedrockagentcore.RuntimeEndpointReference(
                agent_runtime_endpoint_arn="agentRuntimeEndpointArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__056e5ef22e335ff5e02bdd57f3e564e80393e99c891cc1890f945dd001ef5b8f)
            check_type(argname="argument agent_runtime_endpoint_arn", value=agent_runtime_endpoint_arn, expected_type=type_hints["agent_runtime_endpoint_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "agent_runtime_endpoint_arn": agent_runtime_endpoint_arn,
        }

    @builtins.property
    def agent_runtime_endpoint_arn(self) -> builtins.str:
        '''The AgentRuntimeEndpointArn of the RuntimeEndpoint resource.'''
        result = self._values.get("agent_runtime_endpoint_arn")
        assert result is not None, "Required property 'agent_runtime_endpoint_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RuntimeEndpointReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_bedrockagentcore.RuntimeReference",
    jsii_struct_bases=[],
    name_mapping={"agent_runtime_id": "agentRuntimeId"},
)
class RuntimeReference:
    def __init__(self, *, agent_runtime_id: builtins.str) -> None:
        '''A reference to a Runtime resource.

        :param agent_runtime_id: The AgentRuntimeId of the Runtime resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_bedrockagentcore as bedrockagentcore
            
            runtime_reference = bedrockagentcore.RuntimeReference(
                agent_runtime_id="agentRuntimeId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8847701d5ac2ffc328a04478df4877176577ccf780cdf31ccc35b7d9bbcc331a)
            check_type(argname="argument agent_runtime_id", value=agent_runtime_id, expected_type=type_hints["agent_runtime_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "agent_runtime_id": agent_runtime_id,
        }

    @builtins.property
    def agent_runtime_id(self) -> builtins.str:
        '''The AgentRuntimeId of the Runtime resource.'''
        result = self._values.get("agent_runtime_id")
        assert result is not None, "Required property 'agent_runtime_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RuntimeReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, IBrowserCustomRef, _ITaggableV2_4e6798f8)
class CfnBrowserCustom(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnBrowserCustom",
):
    '''Resource definition for AWS::BedrockAgentCore::BrowserCustom.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-browsercustom.html
    :cloudformationResource: AWS::BedrockAgentCore::BrowserCustom
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_bedrockagentcore as bedrockagentcore
        
        cfn_browser_custom = bedrockagentcore.CfnBrowserCustom(self, "MyCfnBrowserCustom",
            name="name",
            network_configuration=bedrockagentcore.CfnBrowserCustom.BrowserNetworkConfigurationProperty(
                network_mode="networkMode"
            ),
        
            # the properties below are optional
            description="description",
            execution_role_arn="executionRoleArn",
            recording_config=bedrockagentcore.CfnBrowserCustom.RecordingConfigProperty(
                enabled=False,
                s3_location=bedrockagentcore.CfnBrowserCustom.S3LocationProperty(
                    bucket="bucket",
                    prefix="prefix"
                )
            ),
            tags={
                "tags_key": "tags"
            }
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        network_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnBrowserCustom.BrowserNetworkConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        description: typing.Optional[builtins.str] = None,
        execution_role_arn: typing.Optional[builtins.str] = None,
        recording_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBrowserCustom.RecordingConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of the browser.
        :param network_configuration: Network configuration for browser.
        :param description: The description of the browser.
        :param execution_role_arn: The Amazon Resource Name (ARN) of the IAM role.
        :param recording_config: Recording configuration for browser.
        :param tags: A map of tag keys and values.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e817ad5ee6496ab54cf569758c4d73da62a4d6f5cf0c34866960f6e4677343e1)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnBrowserCustomProps(
            name=name,
            network_configuration=network_configuration,
            description=description,
            execution_role_arn=execution_role_arn,
            recording_config=recording_config,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12637c5685b21eb50c5acd05eb9308d8266fc2816549a6a2816d9399823e8551)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f14f4b2516dbe32242e98828488dc4abcc900e39ac20507ae2fd0d16a3a0457c)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrBrowserArn")
    def attr_browser_arn(self) -> builtins.str:
        '''The ARN of a Browser resource.

        :cloudformationAttribute: BrowserArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrBrowserArn"))

    @builtins.property
    @jsii.member(jsii_name="attrBrowserId")
    def attr_browser_id(self) -> builtins.str:
        '''The id of the browser.

        :cloudformationAttribute: BrowserId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrBrowserId"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''Timestamp when the browser was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrLastUpdatedAt")
    def attr_last_updated_at(self) -> builtins.str:
        '''Timestamp when the browser was last updated.

        :cloudformationAttribute: LastUpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastUpdatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''Status of browser.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="browserCustomRef")
    def browser_custom_ref(self) -> BrowserCustomReference:
        '''A reference to a BrowserCustom resource.'''
        return typing.cast(BrowserCustomReference, jsii.get(self, "browserCustomRef"))

    @builtins.property
    @jsii.member(jsii_name="cdkTagManager")
    def cdk_tag_manager(self) -> _TagManager_0a598cb3:
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "cdkTagManager"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the browser.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7c7dc0414899a74bed53146d246f036f214f82b031723849419726e12bcee67)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="networkConfiguration")
    def network_configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnBrowserCustom.BrowserNetworkConfigurationProperty"]:
        '''Network configuration for browser.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnBrowserCustom.BrowserNetworkConfigurationProperty"], jsii.get(self, "networkConfiguration"))

    @network_configuration.setter
    def network_configuration(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnBrowserCustom.BrowserNetworkConfigurationProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b89dfccc35ccd0a377234eb3e008038ad66200df7a4f3c63bf61ebf273a7f42e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the browser.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d16faa304c4f18b8bba1ee70b209c47d9944346a1e88926b4ee4ea5fe723fd64)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="executionRoleArn")
    def execution_role_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the IAM role.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "executionRoleArn"))

    @execution_role_arn.setter
    def execution_role_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2dd292342e1165d23c8ce68a72d30c745d42a2586b394e8bcb4aa1ec13e9cc74)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "executionRoleArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="recordingConfig")
    def recording_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBrowserCustom.RecordingConfigProperty"]]:
        '''Recording configuration for browser.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBrowserCustom.RecordingConfigProperty"]], jsii.get(self, "recordingConfig"))

    @recording_config.setter
    def recording_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBrowserCustom.RecordingConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__089c5a25d69d7c7abf4193f45206b584472351088cbe92835bb014923a48f2e7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recordingConfig", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map of tag keys and values.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__22e813ff9c64c23f175682396c7a13b02b9193809d3629b73f2ecac10192c8c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnBrowserCustom.BrowserNetworkConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"network_mode": "networkMode"},
    )
    class BrowserNetworkConfigurationProperty:
        def __init__(self, *, network_mode: builtins.str) -> None:
            '''Network configuration for browser.

            :param network_mode: Network modes supported by browser.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-browsercustom-browsernetworkconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                browser_network_configuration_property = bedrockagentcore.CfnBrowserCustom.BrowserNetworkConfigurationProperty(
                    network_mode="networkMode"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f0d5bebf1ad5159cc9014318eaa4c540145c82225bd9e29170035b0a29d0ee07)
                check_type(argname="argument network_mode", value=network_mode, expected_type=type_hints["network_mode"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "network_mode": network_mode,
            }

        @builtins.property
        def network_mode(self) -> builtins.str:
            '''Network modes supported by browser.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-browsercustom-browsernetworkconfiguration.html#cfn-bedrockagentcore-browsercustom-browsernetworkconfiguration-networkmode
            '''
            result = self._values.get("network_mode")
            assert result is not None, "Required property 'network_mode' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BrowserNetworkConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnBrowserCustom.RecordingConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"enabled": "enabled", "s3_location": "s3Location"},
    )
    class RecordingConfigProperty:
        def __init__(
            self,
            *,
            enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            s3_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBrowserCustom.S3LocationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Recording configuration for browser.

            :param enabled: Default: - false
            :param s3_location: S3 Location Configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-browsercustom-recordingconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                recording_config_property = bedrockagentcore.CfnBrowserCustom.RecordingConfigProperty(
                    enabled=False,
                    s3_location=bedrockagentcore.CfnBrowserCustom.S3LocationProperty(
                        bucket="bucket",
                        prefix="prefix"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__754929ea2dabad59807821380b38b3ef1b1955a5473f5469b18a7dcc81600948)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
                check_type(argname="argument s3_location", value=s3_location, expected_type=type_hints["s3_location"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if enabled is not None:
                self._values["enabled"] = enabled
            if s3_location is not None:
                self._values["s3_location"] = s3_location

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''
            :default: - false

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-browsercustom-recordingconfig.html#cfn-bedrockagentcore-browsercustom-recordingconfig-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def s3_location(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBrowserCustom.S3LocationProperty"]]:
            '''S3 Location Configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-browsercustom-recordingconfig.html#cfn-bedrockagentcore-browsercustom-recordingconfig-s3location
            '''
            result = self._values.get("s3_location")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBrowserCustom.S3LocationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RecordingConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnBrowserCustom.S3LocationProperty",
        jsii_struct_bases=[],
        name_mapping={"bucket": "bucket", "prefix": "prefix"},
    )
    class S3LocationProperty:
        def __init__(self, *, bucket: builtins.str, prefix: builtins.str) -> None:
            '''S3 Location Configuration.

            :param bucket: 
            :param prefix: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-browsercustom-s3location.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                s3_location_property = bedrockagentcore.CfnBrowserCustom.S3LocationProperty(
                    bucket="bucket",
                    prefix="prefix"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6787b09f9e077c274ab79cdf45ea5157eec8aea8960e77f8e128fab67b3cbc26)
                check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
                check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bucket": bucket,
                "prefix": prefix,
            }

        @builtins.property
        def bucket(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-browsercustom-s3location.html#cfn-bedrockagentcore-browsercustom-s3location-bucket
            '''
            result = self._values.get("bucket")
            assert result is not None, "Required property 'bucket' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def prefix(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-browsercustom-s3location.html#cfn-bedrockagentcore-browsercustom-s3location-prefix
            '''
            result = self._values.get("prefix")
            assert result is not None, "Required property 'prefix' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3LocationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556, ICodeInterpreterCustomRef, _ITaggableV2_4e6798f8)
class CfnCodeInterpreterCustom(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnCodeInterpreterCustom",
):
    '''Resource definition for AWS::BedrockAgentCore::CodeInterpreterCustom.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-codeinterpretercustom.html
    :cloudformationResource: AWS::BedrockAgentCore::CodeInterpreterCustom
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_bedrockagentcore as bedrockagentcore
        
        cfn_code_interpreter_custom = bedrockagentcore.CfnCodeInterpreterCustom(self, "MyCfnCodeInterpreterCustom",
            name="name",
            network_configuration=bedrockagentcore.CfnCodeInterpreterCustom.CodeInterpreterNetworkConfigurationProperty(
                network_mode="networkMode"
            ),
        
            # the properties below are optional
            description="description",
            execution_role_arn="executionRoleArn",
            tags={
                "tags_key": "tags"
            }
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        network_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnCodeInterpreterCustom.CodeInterpreterNetworkConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        description: typing.Optional[builtins.str] = None,
        execution_role_arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of the sandbox.
        :param network_configuration: Network configuration for code interpreter.
        :param description: Description of the code interpreter.
        :param execution_role_arn: The ARN of the IAM role.
        :param tags: A map of tag keys and values.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1aaa167a6af98d626969b5bd2de9377658de4e8d04df0b48dc5916f9e503a029)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnCodeInterpreterCustomProps(
            name=name,
            network_configuration=network_configuration,
            description=description,
            execution_role_arn=execution_role_arn,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab4b7a28e87b1af264773dfddc0e9da46bb99c921aa85fb942fcc7ca03680597)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf6d68ae9ee508df2d25ca9f4fa9a800c1215c05ac37929135ce20e393a44113)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCodeInterpreterArn")
    def attr_code_interpreter_arn(self) -> builtins.str:
        '''The ARN of a CodeInterpreter resource.

        :cloudformationAttribute: CodeInterpreterArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCodeInterpreterArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCodeInterpreterId")
    def attr_code_interpreter_id(self) -> builtins.str:
        '''The id of the code interpreter.

        :cloudformationAttribute: CodeInterpreterId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCodeInterpreterId"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''Timestamp when the code interpreter was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrLastUpdatedAt")
    def attr_last_updated_at(self) -> builtins.str:
        '''Timestamp when the code interpreter was last updated.

        :cloudformationAttribute: LastUpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastUpdatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''Status of Code interpreter.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="cdkTagManager")
    def cdk_tag_manager(self) -> _TagManager_0a598cb3:
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "cdkTagManager"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="codeInterpreterCustomRef")
    def code_interpreter_custom_ref(self) -> CodeInterpreterCustomReference:
        '''A reference to a CodeInterpreterCustom resource.'''
        return typing.cast(CodeInterpreterCustomReference, jsii.get(self, "codeInterpreterCustomRef"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the sandbox.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c58fa8bcb0ec87d3b6f75396018d3eeff06205adbf6ade289f0ac1710d71c909)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="networkConfiguration")
    def network_configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnCodeInterpreterCustom.CodeInterpreterNetworkConfigurationProperty"]:
        '''Network configuration for code interpreter.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnCodeInterpreterCustom.CodeInterpreterNetworkConfigurationProperty"], jsii.get(self, "networkConfiguration"))

    @network_configuration.setter
    def network_configuration(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnCodeInterpreterCustom.CodeInterpreterNetworkConfigurationProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a36911cef74e5cac559eb0b558b639739fba4dccbbc8a224553a0f0a0cace3cd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''Description of the code interpreter.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f33607ff407017e2c7ecefbc727c6f7660550a46fe6b356799810d75ccf8d662)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="executionRoleArn")
    def execution_role_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the IAM role.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "executionRoleArn"))

    @execution_role_arn.setter
    def execution_role_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__597443cc8b5cdaed2db807a1545702d23f8f925435f13cd3d17111236aba2428)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "executionRoleArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map of tag keys and values.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__466065bbc5e5f3997568d60c567b51bbc4a9a4900e6ce6da9f9499f85329a3a4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnCodeInterpreterCustom.CodeInterpreterNetworkConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"network_mode": "networkMode"},
    )
    class CodeInterpreterNetworkConfigurationProperty:
        def __init__(self, *, network_mode: builtins.str) -> None:
            '''Network configuration for code interpreter.

            :param network_mode: Network modes supported by code interpreter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-codeinterpretercustom-codeinterpreternetworkconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                code_interpreter_network_configuration_property = bedrockagentcore.CfnCodeInterpreterCustom.CodeInterpreterNetworkConfigurationProperty(
                    network_mode="networkMode"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__eae1295735d5d0996afa02b88ef9dddbd193fc77b25f7b69433fd57c1240bb3a)
                check_type(argname="argument network_mode", value=network_mode, expected_type=type_hints["network_mode"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "network_mode": network_mode,
            }

        @builtins.property
        def network_mode(self) -> builtins.str:
            '''Network modes supported by code interpreter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-codeinterpretercustom-codeinterpreternetworkconfiguration.html#cfn-bedrockagentcore-codeinterpretercustom-codeinterpreternetworkconfiguration-networkmode
            '''
            result = self._values.get("network_mode")
            assert result is not None, "Required property 'network_mode' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CodeInterpreterNetworkConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556, IRuntimeRef, _ITaggableV2_4e6798f8)
class CfnRuntime(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnRuntime",
):
    '''Resource Type definition for AWS::BedrockAgentCore::Runtime.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-runtime.html
    :cloudformationResource: AWS::BedrockAgentCore::Runtime
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_bedrockagentcore as bedrockagentcore
        
        cfn_runtime = bedrockagentcore.CfnRuntime(self, "MyCfnRuntime",
            agent_runtime_artifact=bedrockagentcore.CfnRuntime.AgentRuntimeArtifactProperty(
                container_configuration=bedrockagentcore.CfnRuntime.ContainerConfigurationProperty(
                    container_uri="containerUri"
                )
            ),
            agent_runtime_name="agentRuntimeName",
            network_configuration=bedrockagentcore.CfnRuntime.NetworkConfigurationProperty(
                network_mode="networkMode"
            ),
            role_arn="roleArn",
        
            # the properties below are optional
            authorizer_configuration=bedrockagentcore.CfnRuntime.AuthorizerConfigurationProperty(
                custom_jwt_authorizer=bedrockagentcore.CfnRuntime.CustomJWTAuthorizerConfigurationProperty(
                    discovery_url="discoveryUrl",
        
                    # the properties below are optional
                    allowed_audience=["allowedAudience"],
                    allowed_clients=["allowedClients"]
                )
            ),
            description="description",
            environment_variables={
                "environment_variables_key": "environmentVariables"
            },
            protocol_configuration="protocolConfiguration",
            tags={
                "tags_key": "tags"
            }
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        agent_runtime_artifact: typing.Union[_IResolvable_da3f097b, typing.Union["CfnRuntime.AgentRuntimeArtifactProperty", typing.Dict[builtins.str, typing.Any]]],
        agent_runtime_name: builtins.str,
        network_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnRuntime.NetworkConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        role_arn: builtins.str,
        authorizer_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRuntime.AuthorizerConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        environment_variables: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]] = None,
        protocol_configuration: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param agent_runtime_artifact: 
        :param agent_runtime_name: 
        :param network_configuration: 
        :param role_arn: 
        :param authorizer_configuration: Configuration for the authorizer.
        :param description: 
        :param environment_variables: Environment variable attributes.
        :param protocol_configuration: 
        :param tags: A map of tag keys and values.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8f75c2b58380182b53165109480fecdbf9bcd35c2fcfcfea5141466ba05b7e7)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnRuntimeProps(
            agent_runtime_artifact=agent_runtime_artifact,
            agent_runtime_name=agent_runtime_name,
            network_configuration=network_configuration,
            role_arn=role_arn,
            authorizer_configuration=authorizer_configuration,
            description=description,
            environment_variables=environment_variables,
            protocol_configuration=protocol_configuration,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41eb1aeeb420a432d00eafdf7061763658f434f8c1b3fac5748e0b80cf168cda)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ffbc19212156590bcfcec54a917d56095cf1d0e95a1f4f4107501a8cf457feb7)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAgentRuntimeArn")
    def attr_agent_runtime_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: AgentRuntimeArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAgentRuntimeArn"))

    @builtins.property
    @jsii.member(jsii_name="attrAgentRuntimeId")
    def attr_agent_runtime_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: AgentRuntimeId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAgentRuntimeId"))

    @builtins.property
    @jsii.member(jsii_name="attrAgentRuntimeVersion")
    def attr_agent_runtime_version(self) -> builtins.str:
        '''
        :cloudformationAttribute: AgentRuntimeVersion
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAgentRuntimeVersion"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''
        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrLastUpdatedAt")
    def attr_last_updated_at(self) -> builtins.str:
        '''
        :cloudformationAttribute: LastUpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastUpdatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''
        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrWorkloadIdentityDetails")
    def attr_workload_identity_details(self) -> _IResolvable_da3f097b:
        '''Configuration for workload identity.

        :cloudformationAttribute: WorkloadIdentityDetails
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrWorkloadIdentityDetails"))

    @builtins.property
    @jsii.member(jsii_name="cdkTagManager")
    def cdk_tag_manager(self) -> _TagManager_0a598cb3:
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "cdkTagManager"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="runtimeRef")
    def runtime_ref(self) -> RuntimeReference:
        '''A reference to a Runtime resource.'''
        return typing.cast(RuntimeReference, jsii.get(self, "runtimeRef"))

    @builtins.property
    @jsii.member(jsii_name="agentRuntimeArtifact")
    def agent_runtime_artifact(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnRuntime.AgentRuntimeArtifactProperty"]:
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnRuntime.AgentRuntimeArtifactProperty"], jsii.get(self, "agentRuntimeArtifact"))

    @agent_runtime_artifact.setter
    def agent_runtime_artifact(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnRuntime.AgentRuntimeArtifactProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9afa965e1f7852c99b813a59ddc326e4e8b2e629273fff790e48abcc309421fb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "agentRuntimeArtifact", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="agentRuntimeName")
    def agent_runtime_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "agentRuntimeName"))

    @agent_runtime_name.setter
    def agent_runtime_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20e5f3a5d4d3f3cf24f87565ebb2f7c531ed9e006970eb5a59dee4eeed670f19)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "agentRuntimeName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="networkConfiguration")
    def network_configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnRuntime.NetworkConfigurationProperty"]:
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnRuntime.NetworkConfigurationProperty"], jsii.get(self, "networkConfiguration"))

    @network_configuration.setter
    def network_configuration(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnRuntime.NetworkConfigurationProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76a3b80aa643920bb76e97b49e6d7c54f3367df4203a420045d6d631a4d54658)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__712719ad084eaaa1f88407e6da1dd4ed68fa570a04329676de9d476fde02ebfe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="authorizerConfiguration")
    def authorizer_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRuntime.AuthorizerConfigurationProperty"]]:
        '''Configuration for the authorizer.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRuntime.AuthorizerConfigurationProperty"]], jsii.get(self, "authorizerConfiguration"))

    @authorizer_configuration.setter
    def authorizer_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRuntime.AuthorizerConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__577d498b775175712bf02d50d4dc0a7fa74d069187c6c0daba641442a844c29e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authorizerConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__86887c96ad11d54aa9be7288cd5dfe9a9b3cb370236b2cf8c98f0ea09d7246e2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="environmentVariables")
    def environment_variables(
        self,
    ) -> typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]]:
        '''Environment variable attributes.'''
        return typing.cast(typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]], jsii.get(self, "environmentVariables"))

    @environment_variables.setter
    def environment_variables(
        self,
        value: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27b52f571e16cbee3d0cb6aef888169b2fdf172a92199c29075b1bbfe5eb3091)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "environmentVariables", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="protocolConfiguration")
    def protocol_configuration(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protocolConfiguration"))

    @protocol_configuration.setter
    def protocol_configuration(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd16ca9a4cf1077fb69bea991264277b990667565406b724c960232073239095)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocolConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map of tag keys and values.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13c0ee18c00618ce3d55cf861e88265d3db540867ff55146671310649d3ccaee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnRuntime.AgentRuntimeArtifactProperty",
        jsii_struct_bases=[],
        name_mapping={"container_configuration": "containerConfiguration"},
    )
    class AgentRuntimeArtifactProperty:
        def __init__(
            self,
            *,
            container_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRuntime.ContainerConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''
            :param container_configuration: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-runtime-agentruntimeartifact.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                agent_runtime_artifact_property = bedrockagentcore.CfnRuntime.AgentRuntimeArtifactProperty(
                    container_configuration=bedrockagentcore.CfnRuntime.ContainerConfigurationProperty(
                        container_uri="containerUri"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__51346444ae527a839c6fcfd4fd456eeea9b11da43bf9dadd9b152cfc716ecfd2)
                check_type(argname="argument container_configuration", value=container_configuration, expected_type=type_hints["container_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if container_configuration is not None:
                self._values["container_configuration"] = container_configuration

        @builtins.property
        def container_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRuntime.ContainerConfigurationProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-runtime-agentruntimeartifact.html#cfn-bedrockagentcore-runtime-agentruntimeartifact-containerconfiguration
            '''
            result = self._values.get("container_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRuntime.ContainerConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AgentRuntimeArtifactProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnRuntime.AuthorizerConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"custom_jwt_authorizer": "customJwtAuthorizer"},
    )
    class AuthorizerConfigurationProperty:
        def __init__(
            self,
            *,
            custom_jwt_authorizer: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRuntime.CustomJWTAuthorizerConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Configuration for the authorizer.

            :param custom_jwt_authorizer: Configuration for custom JWT authorizer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-runtime-authorizerconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                authorizer_configuration_property = bedrockagentcore.CfnRuntime.AuthorizerConfigurationProperty(
                    custom_jwt_authorizer=bedrockagentcore.CfnRuntime.CustomJWTAuthorizerConfigurationProperty(
                        discovery_url="discoveryUrl",
                
                        # the properties below are optional
                        allowed_audience=["allowedAudience"],
                        allowed_clients=["allowedClients"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__bb18338480d08b211086521e0155635de6c3b54cf6ebbb5a7ee690c697991b4b)
                check_type(argname="argument custom_jwt_authorizer", value=custom_jwt_authorizer, expected_type=type_hints["custom_jwt_authorizer"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if custom_jwt_authorizer is not None:
                self._values["custom_jwt_authorizer"] = custom_jwt_authorizer

        @builtins.property
        def custom_jwt_authorizer(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRuntime.CustomJWTAuthorizerConfigurationProperty"]]:
            '''Configuration for custom JWT authorizer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-runtime-authorizerconfiguration.html#cfn-bedrockagentcore-runtime-authorizerconfiguration-customjwtauthorizer
            '''
            result = self._values.get("custom_jwt_authorizer")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRuntime.CustomJWTAuthorizerConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AuthorizerConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnRuntime.ContainerConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"container_uri": "containerUri"},
    )
    class ContainerConfigurationProperty:
        def __init__(self, *, container_uri: builtins.str) -> None:
            '''
            :param container_uri: The ECR URI of the container.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-runtime-containerconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                container_configuration_property = bedrockagentcore.CfnRuntime.ContainerConfigurationProperty(
                    container_uri="containerUri"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f0740ce1d3425c4e128b2f49784ee2a02ae6e81129ade5290d001575f4ecacb8)
                check_type(argname="argument container_uri", value=container_uri, expected_type=type_hints["container_uri"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "container_uri": container_uri,
            }

        @builtins.property
        def container_uri(self) -> builtins.str:
            '''The ECR URI of the container.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-runtime-containerconfiguration.html#cfn-bedrockagentcore-runtime-containerconfiguration-containeruri
            '''
            result = self._values.get("container_uri")
            assert result is not None, "Required property 'container_uri' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ContainerConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnRuntime.CustomJWTAuthorizerConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "discovery_url": "discoveryUrl",
            "allowed_audience": "allowedAudience",
            "allowed_clients": "allowedClients",
        },
    )
    class CustomJWTAuthorizerConfigurationProperty:
        def __init__(
            self,
            *,
            discovery_url: builtins.str,
            allowed_audience: typing.Optional[typing.Sequence[builtins.str]] = None,
            allowed_clients: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Configuration for custom JWT authorizer.

            :param discovery_url: OpenID Connect discovery URL.
            :param allowed_audience: List of allowed audiences.
            :param allowed_clients: List of allowed clients.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-runtime-customjwtauthorizerconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                custom_jWTAuthorizer_configuration_property = bedrockagentcore.CfnRuntime.CustomJWTAuthorizerConfigurationProperty(
                    discovery_url="discoveryUrl",
                
                    # the properties below are optional
                    allowed_audience=["allowedAudience"],
                    allowed_clients=["allowedClients"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6479ff33c6925aa85dcd6d4587cd46a0d073bd9992bb93c306d366f07cda2391)
                check_type(argname="argument discovery_url", value=discovery_url, expected_type=type_hints["discovery_url"])
                check_type(argname="argument allowed_audience", value=allowed_audience, expected_type=type_hints["allowed_audience"])
                check_type(argname="argument allowed_clients", value=allowed_clients, expected_type=type_hints["allowed_clients"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "discovery_url": discovery_url,
            }
            if allowed_audience is not None:
                self._values["allowed_audience"] = allowed_audience
            if allowed_clients is not None:
                self._values["allowed_clients"] = allowed_clients

        @builtins.property
        def discovery_url(self) -> builtins.str:
            '''OpenID Connect discovery URL.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-runtime-customjwtauthorizerconfiguration.html#cfn-bedrockagentcore-runtime-customjwtauthorizerconfiguration-discoveryurl
            '''
            result = self._values.get("discovery_url")
            assert result is not None, "Required property 'discovery_url' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def allowed_audience(self) -> typing.Optional[typing.List[builtins.str]]:
            '''List of allowed audiences.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-runtime-customjwtauthorizerconfiguration.html#cfn-bedrockagentcore-runtime-customjwtauthorizerconfiguration-allowedaudience
            '''
            result = self._values.get("allowed_audience")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def allowed_clients(self) -> typing.Optional[typing.List[builtins.str]]:
            '''List of allowed clients.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-runtime-customjwtauthorizerconfiguration.html#cfn-bedrockagentcore-runtime-customjwtauthorizerconfiguration-allowedclients
            '''
            result = self._values.get("allowed_clients")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomJWTAuthorizerConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnRuntime.NetworkConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"network_mode": "networkMode"},
    )
    class NetworkConfigurationProperty:
        def __init__(self, *, network_mode: builtins.str) -> None:
            '''
            :param network_mode: Network mode configuration type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-runtime-networkconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                network_configuration_property = bedrockagentcore.CfnRuntime.NetworkConfigurationProperty(
                    network_mode="networkMode"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f7ef3688e7eda46e5ab607f7c059dd5ed308816790e532f38188518d3a7c9b0f)
                check_type(argname="argument network_mode", value=network_mode, expected_type=type_hints["network_mode"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "network_mode": network_mode,
            }

        @builtins.property
        def network_mode(self) -> builtins.str:
            '''Network mode configuration type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-runtime-networkconfiguration.html#cfn-bedrockagentcore-runtime-networkconfiguration-networkmode
            '''
            result = self._values.get("network_mode")
            assert result is not None, "Required property 'network_mode' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NetworkConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnRuntime.WorkloadIdentityDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={"workload_identity_arn": "workloadIdentityArn"},
    )
    class WorkloadIdentityDetailsProperty:
        def __init__(self, *, workload_identity_arn: builtins.str) -> None:
            '''Configuration for workload identity.

            :param workload_identity_arn: ARN of the workload identity.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-runtime-workloadidentitydetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                workload_identity_details_property = bedrockagentcore.CfnRuntime.WorkloadIdentityDetailsProperty(
                    workload_identity_arn="workloadIdentityArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__68380bfa2496b392a6192eeab7bae5b15e67d93a4946dff9481dca7e2b9da401)
                check_type(argname="argument workload_identity_arn", value=workload_identity_arn, expected_type=type_hints["workload_identity_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "workload_identity_arn": workload_identity_arn,
            }

        @builtins.property
        def workload_identity_arn(self) -> builtins.str:
            '''ARN of the workload identity.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-runtime-workloadidentitydetails.html#cfn-bedrockagentcore-runtime-workloadidentitydetails-workloadidentityarn
            '''
            result = self._values.get("workload_identity_arn")
            assert result is not None, "Required property 'workload_identity_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WorkloadIdentityDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556, IRuntimeEndpointRef, _ITaggableV2_4e6798f8)
class CfnRuntimeEndpoint(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnRuntimeEndpoint",
):
    '''Resource definition for AWS::BedrockAgentCore::RuntimeEndpoint.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-runtimeendpoint.html
    :cloudformationResource: AWS::BedrockAgentCore::RuntimeEndpoint
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_bedrockagentcore as bedrockagentcore
        
        cfn_runtime_endpoint = bedrockagentcore.CfnRuntimeEndpoint(self, "MyCfnRuntimeEndpoint",
            agent_runtime_id="agentRuntimeId",
            name="name",
        
            # the properties below are optional
            agent_runtime_version="agentRuntimeVersion",
            description="description",
            tags={
                "tags_key": "tags"
            }
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        agent_runtime_id: builtins.str,
        name: builtins.str,
        agent_runtime_version: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param agent_runtime_id: The ID of the parent Agent Runtime.
        :param name: 
        :param agent_runtime_version: 
        :param description: 
        :param tags: A map of tag keys and values.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f889c0edf8dd4715192bf69e6433f02f671ca35ed9b8e8f7622b298a7b14955a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnRuntimeEndpointProps(
            agent_runtime_id=agent_runtime_id,
            name=name,
            agent_runtime_version=agent_runtime_version,
            description=description,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2e6a578bb33afa13fb1d85d1b682fc96e67f21a5fb168de296365084e02f261)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91be73ce07416705255e5e1569db31b3f488f1376320ddae8d8803981071f602)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAgentRuntimeArn")
    def attr_agent_runtime_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: AgentRuntimeArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAgentRuntimeArn"))

    @builtins.property
    @jsii.member(jsii_name="attrAgentRuntimeEndpointArn")
    def attr_agent_runtime_endpoint_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: AgentRuntimeEndpointArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAgentRuntimeEndpointArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''
        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrFailureReason")
    def attr_failure_reason(self) -> builtins.str:
        '''The reason for failure if the endpoint is in a failed state.

        :cloudformationAttribute: FailureReason
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrFailureReason"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The unique ID of the Agent Runtime Endpoint itself.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrLastUpdatedAt")
    def attr_last_updated_at(self) -> builtins.str:
        '''
        :cloudformationAttribute: LastUpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastUpdatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrLiveVersion")
    def attr_live_version(self) -> builtins.str:
        '''
        :cloudformationAttribute: LiveVersion
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLiveVersion"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''
        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrTargetVersion")
    def attr_target_version(self) -> builtins.str:
        '''
        :cloudformationAttribute: TargetVersion
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTargetVersion"))

    @builtins.property
    @jsii.member(jsii_name="cdkTagManager")
    def cdk_tag_manager(self) -> _TagManager_0a598cb3:
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "cdkTagManager"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="runtimeEndpointRef")
    def runtime_endpoint_ref(self) -> RuntimeEndpointReference:
        '''A reference to a RuntimeEndpoint resource.'''
        return typing.cast(RuntimeEndpointReference, jsii.get(self, "runtimeEndpointRef"))

    @builtins.property
    @jsii.member(jsii_name="agentRuntimeId")
    def agent_runtime_id(self) -> builtins.str:
        '''The ID of the parent Agent Runtime.'''
        return typing.cast(builtins.str, jsii.get(self, "agentRuntimeId"))

    @agent_runtime_id.setter
    def agent_runtime_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ceb50df9e5593b49d2fbdc6aac8e77c6be9322ee82ceea79d7d86478e1a9d74)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "agentRuntimeId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f380de6caf6e91bd3b0399e46b356f219d19dd4297d832ed74437f4653be82c3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="agentRuntimeVersion")
    def agent_runtime_version(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "agentRuntimeVersion"))

    @agent_runtime_version.setter
    def agent_runtime_version(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45c0052c9218918d9940523a8d7f016f7eaf5fe73a714ee05b2ba7a94aa9df9f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "agentRuntimeVersion", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__479a4b8aa6bb0db70941c7bc7a41e153fdbf533d62d2c2dc2ae2edf57fb46e99)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map of tag keys and values.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1df913b08f181c8777324479d4caab3dc1c0e41137ac1db4a0b10f478ad63ce7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]


__all__ = [
    "BrowserCustomReference",
    "CfnBrowserCustom",
    "CfnBrowserCustomProps",
    "CfnCodeInterpreterCustom",
    "CfnCodeInterpreterCustomProps",
    "CfnRuntime",
    "CfnRuntimeEndpoint",
    "CfnRuntimeEndpointProps",
    "CfnRuntimeProps",
    "CodeInterpreterCustomReference",
    "IBrowserCustomRef",
    "ICodeInterpreterCustomRef",
    "IRuntimeEndpointRef",
    "IRuntimeRef",
    "RuntimeEndpointReference",
    "RuntimeReference",
]

publication.publish()

def _typecheckingstub__45e545da2b3da370563839cf7802f81e77f186bac4ddee7d944e49364fcf8806(
    *,
    browser_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08f9adb5e20b52bbdc47438decbd54e3ebb4b1976cbf46432a19597fc6589c39(
    *,
    name: builtins.str,
    network_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnBrowserCustom.BrowserNetworkConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    description: typing.Optional[builtins.str] = None,
    execution_role_arn: typing.Optional[builtins.str] = None,
    recording_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBrowserCustom.RecordingConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b5217aa9ccd0ec964b92c3a48855bb1494914c435606fcee5b0faefd790d264(
    *,
    name: builtins.str,
    network_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCodeInterpreterCustom.CodeInterpreterNetworkConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    description: typing.Optional[builtins.str] = None,
    execution_role_arn: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03746d507f3e8e95afbebc436c73d1ac1fc643ccea60f817b99b76cb41ccf5fb(
    *,
    agent_runtime_id: builtins.str,
    name: builtins.str,
    agent_runtime_version: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e489b12cef85647a902e6bba6db3bf5f3ef1a856b74cf0fc5a7f8d1d0fa4a4b(
    *,
    agent_runtime_artifact: typing.Union[_IResolvable_da3f097b, typing.Union[CfnRuntime.AgentRuntimeArtifactProperty, typing.Dict[builtins.str, typing.Any]]],
    agent_runtime_name: builtins.str,
    network_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnRuntime.NetworkConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    role_arn: builtins.str,
    authorizer_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRuntime.AuthorizerConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    environment_variables: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]] = None,
    protocol_configuration: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89dc37aef7efb202707ab991eff3008383de6de10f2228d9e9beb350d3f170d5(
    *,
    code_interpreter_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__056e5ef22e335ff5e02bdd57f3e564e80393e99c891cc1890f945dd001ef5b8f(
    *,
    agent_runtime_endpoint_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8847701d5ac2ffc328a04478df4877176577ccf780cdf31ccc35b7d9bbcc331a(
    *,
    agent_runtime_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e817ad5ee6496ab54cf569758c4d73da62a4d6f5cf0c34866960f6e4677343e1(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    network_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnBrowserCustom.BrowserNetworkConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    description: typing.Optional[builtins.str] = None,
    execution_role_arn: typing.Optional[builtins.str] = None,
    recording_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBrowserCustom.RecordingConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12637c5685b21eb50c5acd05eb9308d8266fc2816549a6a2816d9399823e8551(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f14f4b2516dbe32242e98828488dc4abcc900e39ac20507ae2fd0d16a3a0457c(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7c7dc0414899a74bed53146d246f036f214f82b031723849419726e12bcee67(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b89dfccc35ccd0a377234eb3e008038ad66200df7a4f3c63bf61ebf273a7f42e(
    value: typing.Union[_IResolvable_da3f097b, CfnBrowserCustom.BrowserNetworkConfigurationProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d16faa304c4f18b8bba1ee70b209c47d9944346a1e88926b4ee4ea5fe723fd64(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2dd292342e1165d23c8ce68a72d30c745d42a2586b394e8bcb4aa1ec13e9cc74(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__089c5a25d69d7c7abf4193f45206b584472351088cbe92835bb014923a48f2e7(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnBrowserCustom.RecordingConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22e813ff9c64c23f175682396c7a13b02b9193809d3629b73f2ecac10192c8c2(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0d5bebf1ad5159cc9014318eaa4c540145c82225bd9e29170035b0a29d0ee07(
    *,
    network_mode: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__754929ea2dabad59807821380b38b3ef1b1955a5473f5469b18a7dcc81600948(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    s3_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBrowserCustom.S3LocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6787b09f9e077c274ab79cdf45ea5157eec8aea8960e77f8e128fab67b3cbc26(
    *,
    bucket: builtins.str,
    prefix: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1aaa167a6af98d626969b5bd2de9377658de4e8d04df0b48dc5916f9e503a029(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    network_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCodeInterpreterCustom.CodeInterpreterNetworkConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    description: typing.Optional[builtins.str] = None,
    execution_role_arn: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab4b7a28e87b1af264773dfddc0e9da46bb99c921aa85fb942fcc7ca03680597(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf6d68ae9ee508df2d25ca9f4fa9a800c1215c05ac37929135ce20e393a44113(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c58fa8bcb0ec87d3b6f75396018d3eeff06205adbf6ade289f0ac1710d71c909(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a36911cef74e5cac559eb0b558b639739fba4dccbbc8a224553a0f0a0cace3cd(
    value: typing.Union[_IResolvable_da3f097b, CfnCodeInterpreterCustom.CodeInterpreterNetworkConfigurationProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f33607ff407017e2c7ecefbc727c6f7660550a46fe6b356799810d75ccf8d662(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__597443cc8b5cdaed2db807a1545702d23f8f925435f13cd3d17111236aba2428(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__466065bbc5e5f3997568d60c567b51bbc4a9a4900e6ce6da9f9499f85329a3a4(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eae1295735d5d0996afa02b88ef9dddbd193fc77b25f7b69433fd57c1240bb3a(
    *,
    network_mode: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8f75c2b58380182b53165109480fecdbf9bcd35c2fcfcfea5141466ba05b7e7(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    agent_runtime_artifact: typing.Union[_IResolvable_da3f097b, typing.Union[CfnRuntime.AgentRuntimeArtifactProperty, typing.Dict[builtins.str, typing.Any]]],
    agent_runtime_name: builtins.str,
    network_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnRuntime.NetworkConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    role_arn: builtins.str,
    authorizer_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRuntime.AuthorizerConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    environment_variables: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]] = None,
    protocol_configuration: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41eb1aeeb420a432d00eafdf7061763658f434f8c1b3fac5748e0b80cf168cda(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ffbc19212156590bcfcec54a917d56095cf1d0e95a1f4f4107501a8cf457feb7(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9afa965e1f7852c99b813a59ddc326e4e8b2e629273fff790e48abcc309421fb(
    value: typing.Union[_IResolvable_da3f097b, CfnRuntime.AgentRuntimeArtifactProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20e5f3a5d4d3f3cf24f87565ebb2f7c531ed9e006970eb5a59dee4eeed670f19(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76a3b80aa643920bb76e97b49e6d7c54f3367df4203a420045d6d631a4d54658(
    value: typing.Union[_IResolvable_da3f097b, CfnRuntime.NetworkConfigurationProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__712719ad084eaaa1f88407e6da1dd4ed68fa570a04329676de9d476fde02ebfe(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__577d498b775175712bf02d50d4dc0a7fa74d069187c6c0daba641442a844c29e(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnRuntime.AuthorizerConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86887c96ad11d54aa9be7288cd5dfe9a9b3cb370236b2cf8c98f0ea09d7246e2(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27b52f571e16cbee3d0cb6aef888169b2fdf172a92199c29075b1bbfe5eb3091(
    value: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd16ca9a4cf1077fb69bea991264277b990667565406b724c960232073239095(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13c0ee18c00618ce3d55cf861e88265d3db540867ff55146671310649d3ccaee(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51346444ae527a839c6fcfd4fd456eeea9b11da43bf9dadd9b152cfc716ecfd2(
    *,
    container_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRuntime.ContainerConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb18338480d08b211086521e0155635de6c3b54cf6ebbb5a7ee690c697991b4b(
    *,
    custom_jwt_authorizer: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRuntime.CustomJWTAuthorizerConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0740ce1d3425c4e128b2f49784ee2a02ae6e81129ade5290d001575f4ecacb8(
    *,
    container_uri: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6479ff33c6925aa85dcd6d4587cd46a0d073bd9992bb93c306d366f07cda2391(
    *,
    discovery_url: builtins.str,
    allowed_audience: typing.Optional[typing.Sequence[builtins.str]] = None,
    allowed_clients: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7ef3688e7eda46e5ab607f7c059dd5ed308816790e532f38188518d3a7c9b0f(
    *,
    network_mode: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68380bfa2496b392a6192eeab7bae5b15e67d93a4946dff9481dca7e2b9da401(
    *,
    workload_identity_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f889c0edf8dd4715192bf69e6433f02f671ca35ed9b8e8f7622b298a7b14955a(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    agent_runtime_id: builtins.str,
    name: builtins.str,
    agent_runtime_version: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2e6a578bb33afa13fb1d85d1b682fc96e67f21a5fb168de296365084e02f261(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91be73ce07416705255e5e1569db31b3f488f1376320ddae8d8803981071f602(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ceb50df9e5593b49d2fbdc6aac8e77c6be9322ee82ceea79d7d86478e1a9d74(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f380de6caf6e91bd3b0399e46b356f219d19dd4297d832ed74437f4653be82c3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45c0052c9218918d9940523a8d7f016f7eaf5fe73a714ee05b2ba7a94aa9df9f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__479a4b8aa6bb0db70941c7bc7a41e153fdbf533d62d2c2dc2ae2edf57fb46e99(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1df913b08f181c8777324479d4caab3dc1c0e41137ac1db4a0b10f478ad63ce7(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass
