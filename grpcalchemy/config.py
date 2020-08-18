import logging
from typing import List, Optional, Tuple, Union

from configalchemy import BaseConfig
from grpc import ServerInterceptor


class DefaultConfig(BaseConfig):

    #: Directory of proto files and py files, support related path. e.g: protos/v1
    #: generated by the protocol buffer compiler
    PROTO_TEMPLATE_ROOT = ""
    PROTO_TEMPLATE_PATH = "protos"

    #: Max workers in service thread pool
    GRPC_SERVER_MAX_WORKERS = 8
    #: Multiple process support
    #: Prefer to use `multiprocessing.cpu_count()` in production.
    GRPC_SERVER_PROCESS_COUNT = 1

    #: An optional list of key-value pairs (channel args in gRPC runtime)
    #: to configure the channel.
    GRPC_SERVER_OPTIONS: List[Tuple[str, Union[str, int, bool]]] = []

    #: The maximum number of concurrent RPCs this server
    #: will service before returning RESOURCE_EXHAUSTED status, or None to
    #: indicate no limit.
    GRPC_SERVER_MAXIMUM_CONCURRENT_RPCS: Optional[int] = None

    #: If set `True` the server will be blocked after run
    GRPC_SERVER_RUN_WITH_BLOCK = True
    #: The host/domain name that this server can serve
    GRPC_SERVER_HOST = "127.0.0.1"
    #: The port this server listen.
    GRPC_SERVER_PORT = 50051

    #: logger level
    GRPC_ALCHEMY_LOGGER_LEVEL = logging.INFO
    GRPC_ALCHEMY_LOGGER_FORMATTER = "[PID %(process)d] %(message)s"

    #: Health Check
    GRPC_HEALTH_CHECKING_ENABLE = True
    GRPC_HEALTH_CHECKING_THREAD_POOL_NUM = 1

    #: Server Reflection
    GRPC_SEVER_REFLECTION_ENABLE = False

    #: Server Interceptors
    GRPC_INTERCEPTORS: List[ServerInterceptor] = []
