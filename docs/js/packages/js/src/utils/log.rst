packages/js/src/utils/log.ts
============================

Last edited: 2023-05-26 09:49:40

Contents:

.. code-block:: ts

    /* eslint-disable no-console */
import debug from 'debug';

export const logErrorDebug = debug('mp-sdk:error');
export const logInfoDebug = debug('mp-sdk:info');
export const logDebug = debug('mp-sdk:debug');
export const logTrace = debug('mp-sdk:trace');

export const logError = logErrorDebug.enabled
  ? logErrorDebug
  : console.error.bind(console);
export const logInfo = logInfoDebug.enabled
  ? logInfoDebug
  : console.log.bind(console);


