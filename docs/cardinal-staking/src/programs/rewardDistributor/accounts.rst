src/programs/rewardDistributor/accounts.ts
==========================================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: ts

    import type { AccountData } from "@cardinal/common";
import { BorshAccountsCoder, utils } from "@coral-xyz/anchor";
import type { Commitment, Connection, PublicKey } from "@solana/web3.js";

import { REWARD_DISTRIBUTOR_ADDRESS, REWARD_DISTRIBUTOR_IDL } from ".";
import type { RewardDistributorData, RewardEntryData } from "./constants";
import { rewardDistributorProgram } from "./constants";

export const getRewardEntry = async (
  connection: Connection,
  rewardEntryId: PublicKey,
  commitment?: Commitment
): Promise<AccountData<RewardEntryData>> => {
  const program = rewardDistributorProgram(connection, undefined, {
    commitment,
  });
  const parsed = (await program.account.rewardEntry.fetch(
    rewardEntryId
  )) as RewardEntryData;
  return {
    parsed,
    pubkey: rewardEntryId,
  };
};

export const getRewardEntries = async (
  connection: Connection,
  rewardEntryIds: PublicKey[],
  commitment?: Commitment
): Promise<AccountData<RewardEntryData>[]> => {
  const program = rewardDistributorProgram(connection, undefined, {
    commitment,
  });
  const rewardEntries = (await program.account.rewardEntry.fetchMultiple(
    rewardEntryIds
  )) as RewardEntryData[];
  return rewardEntries.map((entry, i) => ({
    parsed: entry,
    pubkey: rewardEntryIds[i]!,
  }));
};

export const getRewardDistributor = async (
  connection: Connection,
  rewardDistributorId: PublicKey,
  commitment?: Commitment
): Promise<AccountData<RewardDistributorData>> => {
  const program = rewardDistributorProgram(connection, undefined, {
    commitment,
  });
  const parsed = (await program.account.rewardDistributor.fetch(
    rewardDistributorId
  )) as RewardDistributorData;
  return {
    parsed,
    pubkey: rewardDistributorId,
  };
};

export const getRewardDistributors = async (
  connection: Connection,
  rewardDistributorIds: PublicKey[],
  commitment?: Commitment
): Promise<AccountData<RewardDistributorData>[]> => {
  const program = rewardDistributorProgram(connection, undefined, {
    commitment,
  });
  const rewardDistributors =
    (await program.account.rewardDistributor.fetchMultiple(
      rewardDistributorIds
    )) as RewardDistributorData[];
  return rewardDistributors.map((distributor, i) => ({
    parsed: distributor,
    pubkey: rewardDistributorIds[i]!,
  }));
};

export const getRewardEntriesForRewardDistributor = async (
  connection: Connection,
  rewardDistributorId: PublicKey,
  commitment?: Commitment
): Promise<AccountData<RewardEntryData>[]> => {
  const programAccounts = await connection.getProgramAccounts(
    REWARD_DISTRIBUTOR_ADDRESS,
    {
      filters: [
        {
          memcmp: {
            offset: 0,
            bytes: utils.bytes.bs58.encode(
              BorshAccountsCoder.accountDiscriminator("rewardEntry")
            ),
          },
        },
        {
          memcmp: {
            offset: 41,
            bytes: rewardDistributorId.toBase58(),
          },
        },
      ],
      commitment,
    }
  );
  const rewardEntryDatas: AccountData<RewardEntryData>[] = [];
  const coder = new BorshAccountsCoder(REWARD_DISTRIBUTOR_IDL);
  programAccounts.forEach((account) => {
    try {
      const rewardEntryData: RewardEntryData = coder.decode(
        "rewardEntry",
        account.account.data
      );
      if (rewardEntryData) {
        rewardEntryDatas.push({
          ...account,
          parsed: rewardEntryData,
        });
      }
      // eslint-disable-next-line no-empty
    } catch (e) {}
  });
  return rewardEntryDatas.sort((a, b) =>
    a.pubkey.toBase58().localeCompare(b.pubkey.toBase58())
  );
};

export const getAllRewardEntries = async (
  connection: Connection,
  commitment?: Commitment
): Promise<AccountData<RewardEntryData>[]> => {
  const programAccounts = await connection.getProgramAccounts(
    REWARD_DISTRIBUTOR_ADDRESS,
    {
      filters: [
        {
          memcmp: {
            offset: 0,
            bytes: utils.bytes.bs58.encode(
              BorshAccountsCoder.accountDiscriminator("rewardEntry")
            ),
          },
        },
      ],
      commitment,
    }
  );
  const rewardEntryDatas: AccountData<RewardEntryData>[] = [];
  const coder = new BorshAccountsCoder(REWARD_DISTRIBUTOR_IDL);
  programAccounts.forEach((account) => {
    try {
      const rewardEntryData: RewardEntryData = coder.decode(
        "rewardEntry",
        account.account.data
      );
      if (rewardEntryData) {
        rewardEntryDatas.push({
          ...account,
          parsed: rewardEntryData,
        });
      }
      // eslint-disable-next-line no-empty
    } catch (e) {}
  });
  return rewardEntryDatas.sort((a, b) =>
    a.pubkey.toBase58().localeCompare(b.pubkey.toBase58())
  );
};


