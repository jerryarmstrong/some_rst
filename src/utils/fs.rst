src/utils/fs.ts
===============

Last edited: 2022-10-10 15:06:28

Contents:

.. code-block:: ts

    import { Keypair } from '@solana/web3.js'
import { R_OK } from 'constants'
import { promises as pfs } from 'fs'
import * as fs from 'fs'
import * as path from 'path'

import { strict as assert } from 'assert'
import { logError } from './log'

export async function canAccess(p: string): Promise<boolean> {
  try {
    await pfs.access(p, R_OK)
    return true
  } catch (e) {
    return false
  }
}

export function canAccessSync(p: string): boolean {
  try {
    fs.accessSync(p, R_OK)
    return true
  } catch (e) {
    return false
  }
}

export async function keypairFromFile(fullPath: string): Promise<Keypair> {
  assert(
    await canAccess(fullPath),
    `File ${fullPath} does not exist or is not readable`
  )
  const keypairString = await pfs.readFile(fullPath, 'utf8')
  try {
    const secretKey = Uint8Array.from(JSON.parse(keypairString))
    return Keypair.fromSecretKey(secretKey)
  } catch (err) {
    logError(err)
    throw new Error(`File ${fullPath} does not contain a valid keypair`)
  }
}

export function keypairFromFileSync(fullPath: string): Keypair {
  assert(
    canAccessSync(fullPath),
    `File ${fullPath} does not exist or is not readable`
  )
  const keypairString = fs.readFileSync(fullPath, 'utf8')
  try {
    const secretKey = Uint8Array.from(JSON.parse(keypairString))
    return Keypair.fromSecretKey(secretKey)
  } catch (err) {
    logError(err)
    throw new Error(`File ${fullPath} does not contain a valid keypair`)
  }
}

export function resolvePath(relPath: string): string {
  return path.resolve(process.cwd(), relPath)
}


