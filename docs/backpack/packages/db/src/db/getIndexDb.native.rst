packages/db/src/db/getIndexDb.native.ts
=======================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: ts

    /*
 * This is added to instruct dexie to use
 * the shimmed indexedDB
 * https://github.com/dexie/Dexie.js/issues/354#issuecomment-714642331
 */
export const getIndexDb = () => ({
  // @ts-ignore
  indexedDB: global.window.indexedDB,
});


