src/generateIdl.ts
==================

Last edited: 2023-08-11 16:31:48

Contents:

.. code-block:: ts

    import type { Idl } from '@metaplex-foundation/kinobi';
import { existsSync, rmSync, writeFileSync } from 'fs';
import generateUsingAnchor from './generators/anchor';
import generateUsingShank from './generators/shank';
import { getIdlPath, logError, logInfo } from './utils';
import { GeneratorOptions } from './types';

export async function generateIdl(config: GeneratorOptions): Promise<void> {
  removeCurrentIdl(config);
  const idl = await handleGenerator(config);
  const enhancedIdl = enhanceIdl(config, idl);
  writeIdl(config, enhancedIdl);
}

function removeCurrentIdl(config: GeneratorOptions): void {
  if (config.removeExistingIdl === false) return;
  const idlPath = getIdlPath(config);
  if (!existsSync(idlPath)) return;

  try {
    rmSync(idlPath);
    logInfo(`Removed existing IDL at ${idlPath}.`);
  } catch (error) {
    logError(`Failed to remove existing IDL at ${idlPath}.`);
  }
}

async function handleGenerator(config: GeneratorOptions): Promise<Idl> {
  if (config.generator === 'anchor') {
    return generateUsingAnchor(config);
  }

  if (config.generator === 'shank') {
    return generateUsingShank(config);
  }

  // @ts-ignore
  throw new Error(`Unrecognized IDL generator: ${config.generator}`);
}

function enhanceIdl(config: GeneratorOptions, idl: Idl): Idl {
  return config.idlHook ? config.idlHook(idl) : idl;
}

function writeIdl(config: GeneratorOptions, idl: Idl): void {
  const idlPath = getIdlPath(config);
  writeFileSync(idlPath, JSON.stringify(idl, null, 2));
}


