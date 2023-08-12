src/programs/groupRewardDistributor/accounts.ts
===============================================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: ts

    import type { AccountData } from "@cardinal/common";
import { BorshAccountsCoder, utils } from "@coral-xyz/anchor";
import type { Commitment, Connection, PublicKey } from "@solana/web3.js";

import {
  GROUP_REWARD_DISTRIBUTOR_ADDRESS,
  GROUP_REWARD_DISTRIBUTOR_IDL,
} from ".";
import type {
  GroupRewardCounterData,
  GroupRewardDistributorData,
  GroupRewardEntryData,
} from "./constants";
import { groupRewardDistributorProgram } from "./constants";

export const getGroupRewardCounter = async (
  connection: Connection,
  groupRewardCounterId: PublicKey,
  commitment?: Commitment
): Promise<AccountData<GroupRewardCounterData>> => {
  const program = groupRewardDistributorProgram(connection, undefined, {
    commitment,
  });
  const parsed = (await program.account.groupRewardCounter.fetch(
    groupRewardCounterId
  )) as GroupRewardCounterData;
  return {
    parsed,
    pubkey: groupRewardCounterId,
  };
};

export const getGroupRewardCounters = async (
  connection: Connection,
  groupRewardCounterIds: PublicKey[],
  commitment?: Commitment
): Promise<AccountData<GroupRewardCounterData>[]> => {
  const program = groupRewardDistributorProgram(connection, undefined, {
    commitment,
  });
  const groupRewardCounters =
    (await program.account.groupRewardCounter.fetchMultiple(
      groupRewardCounterIds
    )) as GroupRewardCounterData[];
  return groupRewardCounters.map((entry, i) => ({
    parsed: entry,
    pubkey: groupRewardCounterIds[i]!,
  }));
};

export const getGroupRewardEntry = async (
  connection: Connection,
  groupRewardEntryId: PublicKey,
  commitment?: Commitment
): Promise<AccountData<GroupRewardEntryData>> => {
  const program = groupRewardDistributorProgram(connection, undefined, {
    commitment,
  });
  const parsed = (await program.account.groupRewardEntry.fetch(
    groupRewardEntryId
  )) as GroupRewardEntryData;
  return {
    parsed,
    pubkey: groupRewardEntryId,
  };
};

export const getGroupRewardEntries = async (
  connection: Connection,
  groupRewardEntryIds: PublicKey[],
  commitment?: Commitment
): Promise<AccountData<GroupRewardEntryData>[]> => {
  const program = groupRewardDistributorProgram(connection, undefined, {
    commitment,
  });
  const groupRewardEntries =
    (await program.account.groupRewardEntry.fetchMultiple(
      groupRewardEntryIds
    )) as GroupRewardEntryData[];
  return groupRewardEntries.map((entry, i) => ({
    parsed: entry,
    pubkey: groupRewardEntryIds[i]!,
  }));
};

export const getGroupRewardDistributor = async (
  connection: Connection,
  groupRewardDistributorId: PublicKey,
  commitment?: Commitment
): Promise<AccountData<GroupRewardDistributorData>> => {
  const program = groupRewardDistributorProgram(connection, undefined, {
    commitment,
  });
  const parsed = (await program.account.groupRewardDistributor.fetch(
    groupRewardDistributorId
  )) as GroupRewardDistributorData;
  return {
    parsed,
    pubkey: groupRewardDistributorId,
  };
};

export const getGroupRewardDistributors = async (
  connection: Connection,
  groupRewardDistributorIds: PublicKey[],
  commitment?: Commitment
): Promise<AccountData<GroupRewardDistributorData>[]> => {
  const program = groupRewardDistributorProgram(connection, undefined, {
    commitment,
  });
  const groupRewardDistributors =
    (await program.account.groupRewardDistributor.fetchMultiple(
      groupRewardDistributorIds
    )) as GroupRewardDistributorData[];
  return groupRewardDistributors.map((distributor, i) => ({
    parsed: distributor,
    pubkey: groupRewardDistributorIds[i]!,
  }));
};

export const getGroupRewardEntriesForGroupRewardDistributor = async (
  connection: Connection,
  groupRewardDistributorId: PublicKey,
  commitment?: Commitment
): Promise<AccountData<GroupRewardEntryData>[]> => {
  const programAccounts = await connection.getProgramAccounts(
    GROUP_REWARD_DISTRIBUTOR_ADDRESS,
    {
      filters: [
        {
          memcmp: {
            offset: 0,
            bytes: utils.bytes.bs58.encode(
              BorshAccountsCoder.accountDiscriminator("groupRewardEntry")
            ),
          },
        },
        {
          memcmp: {
            offset: 8 + 1 + 32,
            bytes: groupRewardDistributorId.toBase58(),
          },
        },
      ],
      commitment,
    }
  );
  const groupRewardEntryDatas: AccountData<GroupRewardEntryData>[] = [];
  const coder = new BorshAccountsCoder(GROUP_REWARD_DISTRIBUTOR_IDL);
  programAccounts.forEach((account) => {
    try {
      const groupRewardEntryData: GroupRewardEntryData = coder.decode(
        "groupRewardEntry",
        account.account.data
      );
      if (groupRewardEntryData) {
        groupRewardEntryDatas.push({
          ...account,
          parsed: groupRewardEntryData,
        });
      }
      // eslint-disable-next-line no-empty
    } catch (e) {}
  });
  return groupRewardEntryDatas.sort((a, b) =>
    a.pubkey.toBase58().localeCompare(b.pubkey.toBase58())
  );
};

export const getAllGroupRewardEntries = async (
  connection: Connection,
  commitment?: Commitment
): Promise<AccountData<GroupRewardEntryData>[]> => {
  const programAccounts = await connection.getProgramAccounts(
    GROUP_REWARD_DISTRIBUTOR_ADDRESS,
    {
      filters: [
        {
          memcmp: {
            offset: 0,
            bytes: utils.bytes.bs58.encode(
              BorshAccountsCoder.accountDiscriminator("groupRewardEntry")
            ),
          },
        },
      ],
      commitment,
    }
  );
  const groupRewardEntryDatas: AccountData<GroupRewardEntryData>[] = [];
  const coder = new BorshAccountsCoder(GROUP_REWARD_DISTRIBUTOR_IDL);
  programAccounts.forEach((account) => {
    try {
      const groupRewardEntryData: GroupRewardEntryData = coder.decode(
        "groupRewardEntry",
        account.account.data
      );
      if (groupRewardEntryData) {
        groupRewardEntryDatas.push({
          ...account,
          parsed: groupRewardEntryData,
        });
      }
      // eslint-disable-next-line no-empty
    } catch (e) {}
  });
  return groupRewardEntryDatas.sort((a, b) =>
    a.pubkey.toBase58().localeCompare(b.pubkey.toBase58())
  );
};


