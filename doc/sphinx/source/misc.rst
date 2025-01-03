Miscellaneous procedures
-------------------------
Listing of all miscellaneous procedures in the Neo4j Graph Data Science Python Client API.
This includes procedures for configuring the library.
These all assume that an object of :class:`.GraphDataScience` is available as `gds`.


.. py:function:: gds.alpha.config.defaults.list(key: Optional[str] = None, username: Optional[str] = None) -> DataFrame

    List defaults; global by default, but also optionally for a specific user and/ or key
.. deprecated:: 2.5.0
        Since GDS server version 2.5.0 you should use the endpoint :func:`gds.config.defaults.list` instead.

.. py:function:: gds.alpha.config.defaults.set(key: str, value: Any, username: Optional[str] = None) -> None

    Set a default; global by, default, but also optionally for a specific user
.. deprecated:: 2.5.0
    Since GDS server version 2.5.0 you should use the endpoint :func:`gds.config.defaults.set` instead.

.. py:function:: gds.alpha.config.limits.list(key: Optional[str] = None, username: Optional[str] = None) -> DataFrame

    List limits; global by default, but also optionally for a specific user and/ or key
.. deprecated:: 2.5.0
        Since GDS server version 2.5.0 you should use the endpoint :func:`gds.config.limits.list` instead.

.. py:function:: gds.alpha.config.limits.set(key: str, value: Any, username: Optional[str] = None) -> None

    Set a limit; global by, default, but also optionally for a specific user
.. deprecated:: 2.5.0
        Since GDS server version 2.5.0 you should use the endpoint :func:`gds.config.limits.set` instead.
.. py:function:: gds.config.defaults.list(key: Optional[str] = None, username: Optional[str] = None) -> DataFrame

    List defaults; global by default, but also optionally for a specific user and/ or key

.. py:function:: gds.config.defaults.set(key: str, value: Any, username: Optional[str] = None) -> None

    Set a default; global by, default, but also optionally for a specific user

.. py:function:: gds.config.limits.list(key: Optional[str] = None, username: Optional[str] = None) -> DataFrame

    List limits; global by default, but also optionally for a specific user and/ or key

.. py:function:: gds.config.limits.set(key: str, value: Any, username: Optional[str] = None) -> None

    Set a limit; global by, default, but also optionally for a specific user

.. py:function:: gds.alpha.systemMonitor() -> Series[Any]
    Get an overview of the system's workload and available resources
.. deprecated:: 2.5.0
        Since GDS server version 2.5.0 you should use the endpoint :func:`gds.systemMonitor` instead.

.. py:function:: gds.alpha.userLog() -> DataFrame
    Log warnings and hints for currently running tasks.
    .. deprecated:: 2.5.0
            Since GDS server version 2.5.0 you should use the endpoint :func:`gds.userLog` instead.

.. py:function:: gds.beta.listProgress(job_id: Optional[str] = None) -> DataFrame
    List progress events for currently running tasks.
.. deprecated:: 2.5.0
    Since GDS server version 2.5.0 you should use the endpoint :func:`gds.listProgress` instead.   

.. py:function:: gds.systemMonitor() -> Series[Any]

    Get an overview of the system's workload and available resources

.. py:function:: gds.listProgress(job_id: Optional[str] = None) -> DataFrame

    List progress events for currently running tasks.

.. py:function:: gds.memory.list() -> Series[Any]

   Returns memory details about the running tasks and projected graphs

.. py:function:: gds.memory.summary() -> Series[Any]

   Returns the memory summary of a user

.. py:function:: gds.debug.sysInfo() -> Series[Any]

    Returns details about the status of the system

.. py:function:: gds.debug.arrow() -> Series[Any]

    Returns details about the status of the GDS Arrow Flight server

.. py:function:: gds.util.asNode(node_id: int) -> Any

    Return a node object for the given node id or null if none exists.

.. py:function:: gds.util.asNodes(node_ids: List[int]) -> List[Any]

    Return a list of node objects for the given node id or an empty list if none exists.

.. py:function:: gds.util.nodeProperty(G: Graph, node_id: int, property_key: str, node_label: str = "*") -> Any

    Returns a node property value from a named in-memory graph.

.. py:function:: gds.version() -> str

    Return the installed graph data science library version.

.. py:function:: gds.server_version() -> ServerVersion

    Return the installed graph data science library version.

.. py:function:: gds.license.state() -> Series[Any]

    Returns details about the graph data science library license.

.. py:function:: gds.is_licensed() -> bool

    Return True if the graph data science library is licensed.

.. py:function:: gds.userLog() -> DataFrame
    Log warnings and hints for currently running tasks.
