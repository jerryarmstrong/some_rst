app/src/utils/logger.ts
=======================

Last edited: 2023-07-21 18:33:07

Contents:

.. code-block:: ts

    export default () => ({
  debug(data: {}) {
    console.debug(data); // eslint-disable-line no-console
  },
  error(e: Error, text?: string) {
    console.error(text || e.message, e); // eslint-disable-line no-console
  },
});


