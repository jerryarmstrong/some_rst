clients/js-solita-candy-guard/src/utils/log.ts
==============================================

Last edited: 2023-08-11 23:25:39

Contents:

.. code-block:: ts

    import debug from 'debug';

export const logError = debug('candy-guard:error');
export const logInfo = debug('candy-guard:info');
export const logDebug = debug('candy-guard:debug');
export const logTrace = debug('candy-guard:trace');


