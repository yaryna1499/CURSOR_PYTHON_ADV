import functools
from enum import Enum

import psutil as ps
import json, toml, yaml

# (!) Note: depends on PIP packages: psultil toml pyyaml


__all__ = "methods"


def _parse_spec(spec):
    """Convert library-internal data structures.

    Conversion is done intogeneral Python types.
    """

    if hasattr(spec, "_asdict"):
        # assume namedtuple
        spec = spec._asdict()

    if isinstance(spec, dict):
        return {k: _parse_spec(v) for k, v in spec.items()}
    if isinstance(spec, list):
        return [_parse_spec(itm) for itm in spec]
    if isinstance(spec, Enum):
        return spec.name
    return spec


# Dict of a form:
# formatter_name: (mimetype, format_function)
# ...
formatters = {
    "json": ("application/json", json.dumps),
    "toml": ("text", toml.dumps),
    "yaml": ("text", functools.partial(yaml.dump, sort_keys=False)),
    "repr": ("text", repr),
}


def method_api(method, format="json", **kwargs):
    global res, mime
    """Call method, parse result and format it accordingly."""
    # TODO: add args handling
    if format.lower() not in formatters:
        raise KeyError("Format does not exist.")

    spec = method(**kwargs)

    parsed = _parse_spec(spec)  # convert to Python native structures
    mime, func = formatters[format]
    res = func(parsed)

    return res, mime


# dict of methods wrapped for api calls of a form:
# method_name: method_callable

# start building
methods = dict.fromkeys(
    [
        "boot_time",
        "cpu_count",
        "cpu_freq",
        "cpu_percent",
        "cpu_stats",
        "cpu_times",
        "cpu_times_percent",
        "disk_io_counters",
        "disk_partitions",
        "getloadavg",
        "net_if_stats",
        "net_io_counters",
        "sensors_battery",
        "sensors_fans",
        "sensors_temperatures",
        "swap_memory",
        "virtual_memory",
        "wait_procs",
    ]
)
# get original methods by name
methods = {name: getattr(ps, name) for name in methods}
# patch one as it requires argument
methods["disk_usage"] = functools.partial(ps.disk_usage, "/")
# now wrap methods
methods = {name: functools.partial(method_api, func) for name, func in methods.items()}

if __name__ == "__main__":
    spec = ps.cpu_count()
    res = _parse_spec(spec)

    mtd = methods["cpu_count"]
    res, mime = mtd(logical=False)
    print(f"Res:\n{res}")
