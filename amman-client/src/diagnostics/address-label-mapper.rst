amman-client/src/diagnostics/address-label-mapper.ts
====================================================

Last edited: 2022-11-03 12:19:53

Contents:

.. code-block:: ts

    const TX = '📒'
const CREATOR = '👩‍🎨'
const CREATE = '🌱'

const labelMap: Map<RegExp, string> = new Map([
  [/^(tx|trans|transaction):?/i, TX],
  [/^(creator):?/i, CREATOR],
  [/^(create|init):?/i, CREATE],
])

export function mapLabel(label: string) {
  for (const [rx, symbol] of labelMap) {
    if (rx.test(label)) {
      return `${label.replace(rx, symbol)}`
    }
  }
  return label
}


