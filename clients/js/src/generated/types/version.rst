clients/js/src/generated/types/version.ts
=========================================

Last edited: 2023-08-12 00:00:44

Contents:

.. code-block:: ts

    /**
 * This code was AUTOGENERATED using the kinobi library.
 * Please DO NOT EDIT THIS FILE, instead use visitors
 * to add features, then rerun kinobi to update it.
 *
 * @see https://github.com/metaplex-foundation/kinobi
 */

import { Serializer, scalarEnum } from '@metaplex-foundation/umi/serializers';

export enum Version {
  V1,
}

export type VersionArgs = Version;

/** @deprecated Use `getVersionSerializer()` without any argument instead. */
export function getVersionSerializer(
  _context: object
): Serializer<VersionArgs, Version>;
export function getVersionSerializer(): Serializer<VersionArgs, Version>;
export function getVersionSerializer(
  _context: object = {}
): Serializer<VersionArgs, Version> {
  return scalarEnum<Version>(Version, { description: 'Version' }) as Serializer<
    VersionArgs,
    Version
  >;
}


