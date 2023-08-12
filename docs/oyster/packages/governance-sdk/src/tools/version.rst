packages/governance-sdk/src/tools/version.ts
============================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: ts

    export function parseVersion(version: string) {
  var arr = version.split('.');

  // parse int or default to 0
  var major = parseInt(arr[0]) || 0;
  var minor = parseInt(arr[1]) || 0;
  var patch = parseInt(arr[2]) || 0;
  return {
    major,
    minor,
    patch,
  };
}


