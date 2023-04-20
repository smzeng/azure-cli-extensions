# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "network perimeter profile access-rule update",
)
class Update(AAZCommand):
    """Creates or updates a network access rule.

    :example: Update access rule
        az network perimeter profile access-rule update -n MyAccessRule --profile-name MyProfile --perimeter-name MyPerimeter -g MyResourceGroup --address-prefixes "[10.10.0.0/16]"
    """

    _aaz_info = {
        "version": "2021-02-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.network/networksecurityperimeters/{}/profiles/{}/accessrules/{}", "2021-02-01-preview"],
        ]
    }

    AZ_SUPPORT_GENERIC_UPDATE = True

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.access_rule_name = AAZStrArg(
            options=["-n", "--name", "--access-rule-name"],
            help="The name of the NSP access rule.",
            required=True,
            id_part="child_name_2",
        )
        _args_schema.perimeter_name = AAZStrArg(
            options=["--perimeter-name"],
            help="The name of the network security perimeter.",
            required=True,
            id_part="name",
        )
        _args_schema.profile_name = AAZStrArg(
            options=["--profile-name"],
            help="The name of the NSP profile.",
            required=True,
            id_part="child_name_1",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "Parameters"

        _args_schema = cls._args_schema
        _args_schema.location = AAZResourceLocationArg(
            arg_group="Parameters",
            help="Resource location.",
            nullable=True,
            fmt=AAZResourceLocationArgFormat(
                resource_group_arg="resource_group",
            ),
        )
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            arg_group="Parameters",
            help="Resource tags.",
            nullable=True,
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg(
            nullable=True,
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.address_prefixes = AAZListArg(
            options=["--address-prefixes"],
            arg_group="Properties",
            help="Inbound address prefixes (IPv4/IPv6)",
            nullable=True,
        )
        _args_schema.direction = AAZStrArg(
            options=["--direction"],
            arg_group="Properties",
            help="Direction that specifies whether the access rules is inbound/outbound.",
            nullable=True,
            enum={"Inbound": "Inbound", "Outbound": "Outbound"},
        )
        _args_schema.email_addresses = AAZListArg(
            options=["--email-addresses"],
            arg_group="Properties",
            help="Outbound rules email address format.",
            nullable=True,
        )
        _args_schema.fqdn = AAZListArg(
            options=["--fqdn"],
            arg_group="Properties",
            help="Outbound rules fully qualified domain name format.",
            nullable=True,
        )
        _args_schema.nsp = AAZListArg(
            options=["--nsp"],
            arg_group="Properties",
            help="Inbound rule specified by the perimeter id.",
            nullable=True,
        )
        _args_schema.phone_numbers = AAZListArg(
            options=["--phone-numbers"],
            arg_group="Properties",
            help="Outbound rules phone number format.",
            nullable=True,
        )
        _args_schema.subscriptions = AAZListArg(
            options=["--subscriptions"],
            arg_group="Properties",
            help="Subscription id in the ARM id format.",
            nullable=True,
        )

        address_prefixes = cls._args_schema.address_prefixes
        address_prefixes.Element = AAZStrArg(
            nullable=True,
        )

        email_addresses = cls._args_schema.email_addresses
        email_addresses.Element = AAZStrArg(
            nullable=True,
        )

        fqdn = cls._args_schema.fqdn
        fqdn.Element = AAZStrArg(
            nullable=True,
        )

        nsp = cls._args_schema.nsp
        nsp.Element = AAZObjectArg(
            nullable=True,
        )

        _element = cls._args_schema.nsp.Element
        _element.id = AAZStrArg(
            options=["id"],
            help="NSP id in the ARM id format.",
            nullable=True,
        )

        phone_numbers = cls._args_schema.phone_numbers
        phone_numbers.Element = AAZStrArg(
            nullable=True,
        )

        subscriptions = cls._args_schema.subscriptions
        subscriptions.Element = AAZObjectArg(
            nullable=True,
        )

        _element = cls._args_schema.subscriptions.Element
        _element.id = AAZStrArg(
            options=["id"],
            help="Subscription ID in the ARM ID fromat.",
            nullable=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.NspAccessRulesGet(ctx=self.ctx)()
        self.pre_instance_update(self.ctx.vars.instance)
        self.InstanceUpdateByJson(ctx=self.ctx)()
        self.InstanceUpdateByGeneric(ctx=self.ctx)()
        self.post_instance_update(self.ctx.vars.instance)
        self.NspAccessRulesCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    @register_callback
    def pre_instance_update(self, instance):
        pass

    @register_callback
    def post_instance_update(self, instance):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class NspAccessRulesGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkSecurityPerimeters/{networkSecurityPerimeterName}/profiles/{profileName}/accessRules/{accessRuleName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "accessRuleName", self.ctx.args.access_rule_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "networkSecurityPerimeterName", self.ctx.args.perimeter_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "profileName", self.ctx.args.profile_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2021-02-01-preview",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()
            _UpdateHelper._build_schema_nsp_access_rule_read(cls._schema_on_200)

            return cls._schema_on_200

    class NspAccessRulesCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200, 201]:
                return self.on_200_201(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkSecurityPerimeters/{networkSecurityPerimeterName}/profiles/{profileName}/accessRules/{accessRuleName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "accessRuleName", self.ctx.args.access_rule_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "networkSecurityPerimeterName", self.ctx.args.perimeter_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "profileName", self.ctx.args.profile_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2021-02-01-preview",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=self.ctx.vars.instance,
            )

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()
            _UpdateHelper._build_schema_nsp_access_rule_read(cls._schema_on_200_201)

            return cls._schema_on_200_201

    class InstanceUpdateByJson(AAZJsonInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance(self.ctx.vars.instance)

        def _update_instance(self, instance):
            _instance_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=instance,
                typ=AAZObjectType
            )
            _builder.set_prop("location", AAZStrType, ".location")
            _builder.set_prop("name", AAZStrType, ".access_rule_name")
            _builder.set_prop("properties", AAZObjectType)
            _builder.set_prop("tags", AAZDictType, ".tags")

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("addressPrefixes", AAZListType, ".address_prefixes")
                properties.set_prop("direction", AAZStrType, ".direction")
                properties.set_prop("emailAddresses", AAZListType, ".email_addresses")
                properties.set_prop("fullyQualifiedDomainNames", AAZListType, ".fqdn")
                properties.set_prop("networkSecurityPerimeters", AAZListType, ".nsp")
                properties.set_prop("phoneNumbers", AAZListType, ".phone_numbers")
                properties.set_prop("subscriptions", AAZListType, ".subscriptions")

            address_prefixes = _builder.get(".properties.addressPrefixes")
            if address_prefixes is not None:
                address_prefixes.set_elements(AAZStrType, ".")

            email_addresses = _builder.get(".properties.emailAddresses")
            if email_addresses is not None:
                email_addresses.set_elements(AAZStrType, ".")

            fully_qualified_domain_names = _builder.get(".properties.fullyQualifiedDomainNames")
            if fully_qualified_domain_names is not None:
                fully_qualified_domain_names.set_elements(AAZStrType, ".")

            network_security_perimeters = _builder.get(".properties.networkSecurityPerimeters")
            if network_security_perimeters is not None:
                network_security_perimeters.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.networkSecurityPerimeters[]")
            if _elements is not None:
                _elements.set_prop("id", AAZStrType, ".id")

            phone_numbers = _builder.get(".properties.phoneNumbers")
            if phone_numbers is not None:
                phone_numbers.set_elements(AAZStrType, ".")

            subscriptions = _builder.get(".properties.subscriptions")
            if subscriptions is not None:
                subscriptions.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.subscriptions[]")
            if _elements is not None:
                _elements.set_prop("id", AAZStrType, ".id")

            tags = _builder.get(".tags")
            if tags is not None:
                tags.set_elements(AAZStrType, ".")

            return _instance_value

    class InstanceUpdateByGeneric(AAZGenericInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance_by_generic(
                self.ctx.vars.instance,
                self.ctx.generic_update_args
            )


class _UpdateHelper:
    """Helper class for Update"""

    _schema_nsp_access_rule_read = None

    @classmethod
    def _build_schema_nsp_access_rule_read(cls, _schema):
        if cls._schema_nsp_access_rule_read is not None:
            _schema.id = cls._schema_nsp_access_rule_read.id
            _schema.location = cls._schema_nsp_access_rule_read.location
            _schema.name = cls._schema_nsp_access_rule_read.name
            _schema.properties = cls._schema_nsp_access_rule_read.properties
            _schema.tags = cls._schema_nsp_access_rule_read.tags
            _schema.type = cls._schema_nsp_access_rule_read.type
            return

        cls._schema_nsp_access_rule_read = _schema_nsp_access_rule_read = AAZObjectType()

        nsp_access_rule_read = _schema_nsp_access_rule_read
        nsp_access_rule_read.id = AAZStrType(
            flags={"read_only": True},
        )
        nsp_access_rule_read.location = AAZStrType()
        nsp_access_rule_read.name = AAZStrType()
        nsp_access_rule_read.properties = AAZObjectType()
        nsp_access_rule_read.tags = AAZDictType()
        nsp_access_rule_read.type = AAZStrType(
            flags={"read_only": True},
        )

        properties = _schema_nsp_access_rule_read.properties
        properties.address_prefixes = AAZListType(
            serialized_name="addressPrefixes",
        )
        properties.direction = AAZStrType()
        properties.email_addresses = AAZListType(
            serialized_name="emailAddresses",
        )
        properties.fully_qualified_domain_names = AAZListType(
            serialized_name="fullyQualifiedDomainNames",
        )
        properties.network_security_perimeters = AAZListType(
            serialized_name="networkSecurityPerimeters",
        )
        properties.phone_numbers = AAZListType(
            serialized_name="phoneNumbers",
        )
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )
        properties.subscriptions = AAZListType()

        address_prefixes = _schema_nsp_access_rule_read.properties.address_prefixes
        address_prefixes.Element = AAZStrType()

        email_addresses = _schema_nsp_access_rule_read.properties.email_addresses
        email_addresses.Element = AAZStrType()

        fully_qualified_domain_names = _schema_nsp_access_rule_read.properties.fully_qualified_domain_names
        fully_qualified_domain_names.Element = AAZStrType()

        network_security_perimeters = _schema_nsp_access_rule_read.properties.network_security_perimeters
        network_security_perimeters.Element = AAZObjectType()

        _element = _schema_nsp_access_rule_read.properties.network_security_perimeters.Element
        _element.id = AAZStrType()
        _element.location = AAZStrType(
            flags={"read_only": True},
        )
        _element.perimeter_guid = AAZStrType(
            serialized_name="perimeterGuid",
            flags={"read_only": True},
        )

        phone_numbers = _schema_nsp_access_rule_read.properties.phone_numbers
        phone_numbers.Element = AAZStrType()

        subscriptions = _schema_nsp_access_rule_read.properties.subscriptions
        subscriptions.Element = AAZObjectType()

        _element = _schema_nsp_access_rule_read.properties.subscriptions.Element
        _element.id = AAZStrType()

        tags = _schema_nsp_access_rule_read.tags
        tags.Element = AAZStrType()

        _schema.id = cls._schema_nsp_access_rule_read.id
        _schema.location = cls._schema_nsp_access_rule_read.location
        _schema.name = cls._schema_nsp_access_rule_read.name
        _schema.properties = cls._schema_nsp_access_rule_read.properties
        _schema.tags = cls._schema_nsp_access_rule_read.tags
        _schema.type = cls._schema_nsp_access_rule_read.type


__all__ = ["Update"]
