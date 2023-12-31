src/program/instruction_data.js
===============================

Last edited: 2020-07-29 22:45:43

Contents:

.. code-block:: js

    /**
 * The commands (encoded as Transaction Instructions) that are accepted by the
 * Move loader program
 *
 * @flow
 */

import * as lo from 'buffer-layout';
import {PublicKey} from '@solana/web3.js';

export const publicKeyLayout = (property: string = 'publicKey'): Object => {
  return lo.blob(32, property);
};

/**
 * Solana on-chain Move script or module loader instructions
 */
export const Instruction = {
  Write: 0, // Write data chunk
  Finalize: 1, // Finalize
  CreateGenesis: 2, // Create genesis account
};

/**
 * Libra Transaction Argument types
 */
export const TransactionArgument = {
  U64: 0,
  Address: 1,
  ByteArray: 2,
  String: 3,
};

/**
 * Solana on-chain InvokeMain Move loader commands
 */
const Executable = {
  RunScript: 0, // Run a script
};

/**
 * Libra's mint account address structurally equivalent
 * to a Solana public key
 */
function getMintAddress(): PublicKey {
  return new PublicKey('1111111111111111111111111111GKSfy');
}

/**
 * Returns the instruction data to create a genesis account
 */
export function createGenesis(amount: number): Buffer {
  const layout = lo.struct([lo.u32('instruction'), lo.nu64('amount')]);

  const buffer = Buffer.alloc(layout.span);
  layout.encode(
    {
      instruction: Instruction.CreateGenesis,
      amount,
    },
    buffer,
  );
  return buffer;
}

/**
 * Runs a move script
 */
export function runScript(
  senderPublicKey: PublicKey,
  functionName: string,
  args: ?Buffer,
): Buffer {
  const layout = lo.struct([
    lo.u32('instruction'),
    publicKeyLayout('senderAddress'),
    lo.nu64('functionNameLength'),
    lo.blob(functionName.length, 'functionName'),
  ]);

  var buffer = Buffer.alloc(layout.span);
  layout.encode(
    {
      instruction: Executable.RunScript,
      senderAddress: senderPublicKey.toBuffer(),
      functionNameLength: functionName.length,
      functionName: Buffer.from(functionName, 'ascii'),
    },
    buffer,
  );
  if (args) {
    buffer = Buffer.concat([buffer, args]);
  }
  return buffer;
}

/**
 * Returns the instruction data to call mint_to_address Move script
 */
export function runMintToAddress(
  payeePublicKey: PublicKey,
  amount: number,
): Buffer {
  const layout = lo.struct([
    lo.u32('instruction'),
    publicKeyLayout('senderAddress'),
    lo.nu64('functionNameLength'),
    lo.blob(4, 'functionName'),
    lo.nu64('numArgs'),
    lo.u32('addressType'),
    publicKeyLayout('payeeAddress'),
    lo.u32('valueType'),
    lo.nu64('amount'),
  ]);

  const buffer = Buffer.alloc(layout.span);
  layout.encode(
    {
      instruction: Executable.RunScript,
      senderAddress: getMintAddress().toBuffer(),
      functionNameLength: 4,
      functionName: Buffer.from('main', 'ascii'),
      numArgs: 2,
      addressType: TransactionArgument.Address,
      payeeAddress: payeePublicKey.toBuffer(),
      valueType: TransactionArgument.U64,
      amount,
    },
    buffer,
  );
  return buffer;
}

/**
 * Returns the instruction data to call the pay_from_sender Move script
 */
export function runPayFromSender(
  senderPublicKey: PublicKey,
  payeePublicKey: PublicKey,
  amount: number,
): Buffer {
  const layout = lo.struct([
    lo.u32('instruction'),
    publicKeyLayout('senderAddress'),
    lo.nu64('functionNameLength'),
    lo.blob(4, 'functionName'),
    lo.nu64('numArgs'),
    lo.u32('addressType'),
    publicKeyLayout('payeeAddress'),
    lo.u32('valueType'),
    lo.nu64('amount'),
  ]);

  const buffer = Buffer.alloc(layout.span);
  layout.encode(
    {
      instruction: Executable.RunScript,
      senderAddress: senderPublicKey.toBuffer(),
      functionNameLength: 4,
      functionName: Buffer.from('main', 'ascii'),
      numArgs: 2,
      addressType: TransactionArgument.Address,
      payeeAddress: payeePublicKey.toBuffer(),
      valueType: TransactionArgument.U64,
      amount,
    },
    buffer,
  );
  return buffer;
}


