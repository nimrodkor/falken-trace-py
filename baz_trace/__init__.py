import wrapt

from .baz import wrap_dd_span

wrapt.wrap_function_wrapper("ddtrace", "Tracer.start_span", wrap_dd_span)
