src/amman/log.ts
================

Last edited: 2022-08-30 20:54:29

Contents:

.. code-block:: ts

    import debug from "debug";

export const logError = debug("amman:error");
export const logInfo = debug("amman:info");
export const logDebug = debug("amman:debug");
export const logTrace = debug("amman:trace");


