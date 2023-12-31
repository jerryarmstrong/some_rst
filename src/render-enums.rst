src/render-enums.ts
===================

Last edited: 2023-07-06 15:09:22

Contents:

.. code-block:: ts

    export function renderScalarEnum(
  name: string,
  variants: string[],
  includeExport: boolean
) {
  const exp = includeExport ? 'export ' : ''
  return `
/**
 * @category enums
 * @category generated
 */
${exp}enum ${name} {
  ${variants.join(',\n  ')}    
}`.trim()
}

export function renderScalarEnums(
  map: Map<string, string[]>,
  includeExport = false
) {
  const codes = []
  for (const [name, variants] of map) {
    codes.push(renderScalarEnum(name, variants, includeExport))
  }
  return codes
}


