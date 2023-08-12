clients/js-solita-candy-guard/test/setup/log.ts
===============================================

Last edited: 2023-08-11 23:25:39

Contents:

.. code-block:: ts

    import debug from 'debug';
export const logError = debug('man:test:error');
export const logInfo = debug('man:test:info');
export const logDebug = debug('man:test:debug');
export const logTrace = debug('man:test:trace');


