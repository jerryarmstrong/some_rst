packages/governance-sdk/tests/tools/units.ts
============================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: ts

    const SECONDS_PER_DAY = 86400

export function getTimestampFromDays(days: number) {
  return days * SECONDS_PER_DAY
}

