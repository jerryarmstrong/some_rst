amman/src/utils/path.ts
=======================

Last edited: 2022-11-03 12:19:53

Contents:

.. code-block:: ts

    import { strict as assert } from 'assert'

/** @private */
export function assertValidPathSegmentWithoutSpaces(p: string, msg?: string) {
  assert(/^[a-zA-Z0-9_-]+$/.test(p), `Invalid path segment: ${p}. ${msg ?? ''}`)
}


