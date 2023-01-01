# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = equipment_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Any, List, TypeVar, Callable, Type, cast

T = TypeVar("T")


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class EquipmentElement:
    id: int
    quantity: int

    @staticmethod
    def from_dict(obj: Any) -> 'EquipmentElement':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        quantity = from_int(obj.get("quantity"))
        return EquipmentElement(id, quantity)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["quantity"] = from_int(self.quantity)
        return result


def equipment_from_dict(s: Any) -> List[EquipmentElement]:
    return from_list(EquipmentElement.from_dict, s)


def equipment_to_dict(x: List[EquipmentElement]) -> Any:
    return from_list(lambda x: to_class(EquipmentElement, x), x)