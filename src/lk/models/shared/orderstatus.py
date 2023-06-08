"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import orderstatuses as shared_orderstatuses
from dataclasses_json import Undefined, dataclass_json
from lk import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class OrderStatus:
    r"""Represents info about new order status"""
    
    order_id: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('order_id') }})
    r"""This field could be numeric string"""
    status: shared_orderstatuses.OrderStatuses = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    r"""This field could be numeric string"""
    