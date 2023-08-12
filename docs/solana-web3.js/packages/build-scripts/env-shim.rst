packages/build-scripts/env-shim.ts
==================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    // Clever obfuscation to prevent the build system from inlining the value of `NODE_ENV`
export const __DEV__ = /* @__PURE__ */ (() => (process as any)['en' + 'v'].NODE_ENV === 'development')();


