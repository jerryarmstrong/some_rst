src/serializers.ts
==================

Last edited: 2023-07-06 15:09:22

Contents:

.. code-block:: ts

    import { R_OK } from 'constants'
import path from 'path'
import { canAccess } from './utils'

export type SerializerSnippets = {
  importSnippet: string
  resolveFunctionsSnippet: string
  serialize: string
  deserialize: string
}

export class CustomSerializers {
  private constructor(readonly serializers: Map<string, string>) {}

  static create(projectRoot: string, serializers: Map<string, string>) {
    const resolvedSerializers = new Map()
    for (const [key, val] of serializers) {
      resolvedSerializers.set(key, path.resolve(projectRoot, val))
    }
    verifyAccess(resolvedSerializers)
    return new CustomSerializers(resolvedSerializers)
  }

  static get empty() {
    return CustomSerializers.create('', new Map())
  }

  serializerPathFor(typeName: string, modulePath: string) {
    const fullPath = this.serializers.get(typeName)
    return fullPath == null ? null : path.relative(modulePath, fullPath)
  }

  snippetsFor(
    typeName: string,
    modulePath: string,
    builtinSerializer: string
  ): SerializerSnippets {
    const p = this.serializerPathFor(typeName, modulePath)
    const mdl = (() => {
      if (p == null) return null
      const ext = path.extname(p)
      return ext.length > 0 ? p.slice(0, -ext.length) : p
    })()

    const importSnippet =
      mdl == null ? '' : `import * as customSerializer from '${mdl}';\n`

    const resolveFunctionsSnippet =
      mdl == null
        ? ''
        : `
const serializer = customSerializer as unknown as {
  serialize: typeof ${builtinSerializer}.serialize;
  deserialize: typeof ${builtinSerializer}.deserialize;
};

const resolvedSerialize = typeof serializer.serialize === 'function' 
  ? serializer.serialize.bind(serializer)
  : ${builtinSerializer}.serialize.bind(${builtinSerializer});
const resolvedDeserialize = typeof serializer.deserialize === 'function' 
  ? serializer.deserialize.bind(serializer) 
  : ${builtinSerializer}.deserialize.bind(${builtinSerializer});
`.trim()

    return {
      importSnippet,
      resolveFunctionsSnippet,
      serialize:
        mdl == null ? `${builtinSerializer}.serialize` : 'resolvedSerialize',
      deserialize:
        mdl == null
          ? `${builtinSerializer}.deserialize`
          : 'resolvedDeserialize',
    }
  }
}

function verifyAccess(serializers: Map<string, string>) {
  const violations = []
  for (const [key, val] of serializers) {
    if (!canAccess(val, R_OK)) {
      violations.push(
        `Cannot access de/serializer for ${key} resolved to ${val}`
      )
    }
  }
  if (violations.length > 0) {
    throw new Error(
      `Encountered issues resolving de/serializers:\n ${violations.join(
        '\n  '
      )}`
    )
  }
}


