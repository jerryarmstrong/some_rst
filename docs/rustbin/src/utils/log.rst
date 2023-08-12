src/utils/log.ts
================

Last edited: 2023-08-11 16:30:29

Contents:

.. code-block:: ts

    import debug from 'debug'

export const logError = debug('rustbin:error')
export const logInfo = debug('rustbin:info')
export const logDebug = debug('rustbin:debug')
export const logTrace = debug('rustbin:trace')


