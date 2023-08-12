src/utils/fs.ts
===============

Last edited: 2023-08-11 16:30:29

Contents:

.. code-block:: ts

    import { promises as fs } from 'fs'

/** @private */
export async function canAccess(p: string) {
  try {
    await fs.access(p)
    return true
  } catch (_) {
    return false
  }
}

/** @private */
export async function ensureDir(dir: string) {
  if (!(await canAccess(dir))) {
    await fs.mkdir(dir, { recursive: true })
    return
  }
  // dir already exists, make sure it isn't a file
  const stat = await fs.stat(dir)
  if (!stat.isDirectory()) {
    throw new Error(`'${dir}' is not a directory`)
  }
}


