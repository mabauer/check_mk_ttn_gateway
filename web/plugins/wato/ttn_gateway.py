#!/usr/bin/python
# -*- mode: Python; encoding: utf-8; indent-offset: 4; autowrap: nil -*-

from cmk.gui.i18n import _
from cmk.gui.valuespec import (
    Dictionary,
    TextAscii,
)

from cmk.gui.plugins.wato import (
    rulespec_registry,
    HostRulespec,
)

from cmk.gui.plugins.wato.datasource_programs import (
    RulespecGroupDatasourcePrograms,
)

def _valuespec_special_agents_ttn_gateway():
    return Dictionary(
        elements=[
            ("eui", TextAscii(title=_("Gateway EUI"), allow_empty=False)),
        ],
        optional_keys=False,
        title=_("TTN Gateway Parameters"),
    )

rulespec_registry.register(
    HostRulespec(
        group=RulespecGroupDatasourcePrograms,
        name="special_agents:ttn_gateway",
        valuespec=_valuespec_special_agents_ttn_gateway,
    ))