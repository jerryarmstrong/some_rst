packages/governance/src/tools/sdk/bpfUpgradeableLoader/accounts.ts
==================================================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: ts

    import { utils } from '@oyster/common';
import { Connection, PublicKey } from '@solana/web3.js';
import { create } from 'superstruct';
import { ProgramDataAccountInfo } from '../../validators/accounts/upgradeable-program';

export async function getProgramDataAddress(programId: PublicKey) {
  const { bpf_upgrade_loader: bpfUpgradableLoaderId } = utils.programIds();

  const [programDataAddress] = await PublicKey.findProgramAddress(
    [programId.toBuffer()],
    bpfUpgradableLoaderId,
  );

  return programDataAddress;
}

export async function getProgramDataAccount(
  connection: Connection,
  programId: PublicKey,
) {
  const programDataAddress = await getProgramDataAddress(programId);
  const account = await connection.getParsedAccountInfo(programDataAddress);

  if (!account || !account.value) {
    throw new Error(
      `Program data account ${programDataAddress.toBase58()} for program ${programId.toBase58()} not found`,
    );
  }

  const accountInfo = account.value;

  if (
    !(
      'parsed' in accountInfo.data &&
      accountInfo.data.program === 'bpf-upgradeable-loader'
    )
  ) {
    throw new Error(
      `Invalid program data account ${programDataAddress.toBase58()} for program ${programId.toBase58()}`,
    );
  }

  let programData = create(
    accountInfo.data.parsed.info,
    ProgramDataAccountInfo,
  );
  return programData;
}


