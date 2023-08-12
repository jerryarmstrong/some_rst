amman/src/storage/types.ts
==========================

Last edited: 2022-11-03 12:19:53

Contents:

.. code-block:: ts

    import { AMMAN_DEFAULT_MOCK_STORAGE_ID } from '@metaplex-foundation/amman-client'

export const ContentTypes = [
  'image/jpeg',
  'image/png',
  'image/gif',
  'image/bmp',
  'image/svg+xml',
  'image/webp',
  'image/x-icon',
] as const

export type ContentType = typeof ContentTypes[number]

/**
 * Configures the Amman Mock Storage
 *
 * @category config
 */
export type StorageConfig = {
  enabled: boolean
  storageId: string
  clearOnStart: boolean
}

/**
 * The Default Amman Storage Configuration
 *
 * @category config
 */
export const DEFAULT_STORAGE_CONFIG: StorageConfig = {
  enabled: process.env.CI == null,
  storageId: AMMAN_DEFAULT_MOCK_STORAGE_ID,
  clearOnStart: true,
}


