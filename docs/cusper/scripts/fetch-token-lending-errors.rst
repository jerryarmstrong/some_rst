scripts/fetch-token-lending-errors.ts
=====================================

Last edited: 2021-12-28 22:07:55

Contents:

.. code-block:: ts

    import axios from 'axios'
import fs from 'fs/promises'
import path from 'path'
import { Options, format } from 'prettier'
import { ErrorMeta } from '../src/types'

const TOKEN_LENDING_ERROR_URL =
  'https://raw.githubusercontent.com/solana-labs/solana-program-library/master/token-lending/program/src/error.rs'

const tokenLendingErrorsFile = path.join(
  __dirname,
  '..',
  'src',
  'errors',
  'token-lending.ts'
)

const formatOpts: Options = {
  semi: false,
  singleQuote: true,
  trailingComma: 'es5',
  useTabs: false,
  tabWidth: 2,
  arrowParens: 'always',
  printWidth: 80,
  parser: 'typescript',
}
const errorMacroRx = /#\[error\("([^"]+")\)\]/

async function fetchTokenLendingError() {
  const res = await axios.get(TOKEN_LENDING_ERROR_URL)
  if (res.status !== 200) {
    throw new Error(
      `Fetch ${TOKEN_LENDING_ERROR_URL} came back ${res.status} (${res.statusText})`
    )
  }

  return res.data
}

function parseText(text: string) {
  const lines = text.split('\n')
  const errorMetas: ErrorMeta[] = []
  let errorCode = 0
  for (let i = 0; i < lines.length; i++) {
    const macroMatch = lines[i].match(errorMacroRx)
    if (macroMatch == null) continue

    const message = macroMatch[1]
    const name = lines[i + 1].trim().replace(/,/, '')
    errorMetas.push({
      code: errorCode,
      message,
      name,
    })
    errorCode++
    i++
  }
  return errorMetas
}

async function main() {
  const text = await fetchTokenLendingError()
  const errorMetas = parseText(text)
  const errorMetaMap: Map<number, ErrorMeta> = errorMetas.reduce(
    (map, meta) => {
      map.set(meta.code, meta)
      return map
    },
    new Map()
  )
  const mapArray = JSON.stringify(Array.from(errorMetaMap), null, 2)
  const code = `// Generated via ./scripts/fetch-token-lending-errors.ts

import { ErrorMeta } from './types'
export const tokenLendingErrors: Map<number, ErrorMeta> = new Map(${mapArray})
`
  const formatted = format(code, formatOpts)
  return fs.writeFile(tokenLendingErrorsFile, formatted, 'utf8')
}

main()
  .then(() => process.exit(0))
  .catch((err: any) => {
    console.error(err)
    process.exit(1)
  })


