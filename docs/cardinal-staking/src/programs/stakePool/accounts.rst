src/programs/stakePool/accounts.ts
==================================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: ts

    import type { AccountData } from "@cardinal/common";
import { BorshAccountsCoder, utils } from "@coral-xyz/anchor";
import type { Commitment, Connection } from "@solana/web3.js";
import { PublicKey } from "@solana/web3.js";

import type { StakePoolData } from ".";
import { STAKE_POOL_ADDRESS, STAKE_POOL_IDL } from ".";
import type {
  GroupStakeEntryData,
  IdentifierData,
  StakeAuthorizationData,
  StakeBoosterData,
  StakeEntryData,
} from "./constants";
import {
  AUTHORITY_OFFSET,
  GROUP_STAKER_OFFSET,
  POOL_OFFSET,
  stakePoolProgram,
  STAKER_OFFSET,
} from "./constants";
import { findIdentifierId } from "./pda";

export const getStakePool = async (
  connection: Connection,
  stakePoolId: PublicKey,
  commitment?: Commitment
): Promise<AccountData<StakePoolData>> => {
  const program = stakePoolProgram(connection, undefined, { commitment });
  const parsed = await program.account.stakePool.fetch(stakePoolId);
  return {
    parsed,
    pubkey: stakePoolId,
  };
};

export const getStakePools = async (
  connection: Connection,
  stakePoolIds: PublicKey[],
  commitment?: Commitment
): Promise<AccountData<StakePoolData>[]> => {
  const program = stakePoolProgram(connection, undefined, { commitment });
  const stakePools = (await program.account.stakePool.fetchMultiple(
    stakePoolIds
  )) as StakePoolData[];
  return stakePools.map((tm, i) => ({
    parsed: tm,
    pubkey: stakePoolIds[i]!,
  }));
};

export const getAllStakePools = async (
  connection: Connection,
  commitment?: Commitment
): Promise<AccountData<StakePoolData>[]> => {
  const programAccounts = await connection.getProgramAccounts(
    STAKE_POOL_ADDRESS,
    {
      filters: [
        {
          memcmp: {
            offset: 0,
            bytes: utils.bytes.bs58.encode(
              BorshAccountsCoder.accountDiscriminator("stakePool")
            ),
          },
        },
      ],
      commitment,
    }
  );
  const stakePoolDatas: AccountData<StakePoolData>[] = [];
  const coder = new BorshAccountsCoder(STAKE_POOL_IDL);
  programAccounts.forEach((account) => {
    try {
      const stakePoolData: StakePoolData = coder.decode(
        "stakePool",
        account.account.data
      );
      if (stakePoolData) {
        stakePoolDatas.push({
          ...account,
          parsed: stakePoolData,
        });
      }
      // eslint-disable-next-line no-empty
    } catch (e) {}
  });
  return stakePoolDatas.sort((a, b) =>
    a.pubkey.toBase58().localeCompare(b.pubkey.toBase58())
  );
};

export const getStakeEntriesForUser = async (
  connection: Connection,
  user: PublicKey,
  commitment?: Commitment
): Promise<AccountData<StakeEntryData>[]> => {
  const programAccounts = await connection.getProgramAccounts(
    STAKE_POOL_ADDRESS,
    {
      filters: [{ memcmp: { offset: STAKER_OFFSET, bytes: user.toBase58() } }],
      commitment,
    }
  );

  const stakeEntryDatas: AccountData<StakeEntryData>[] = [];
  const coder = new BorshAccountsCoder(STAKE_POOL_IDL);
  programAccounts.forEach((account) => {
    try {
      const stakeEntryData: StakeEntryData = coder.decode(
        "stakeEntry",
        account.account.data
      );
      if (stakeEntryData) {
        stakeEntryDatas.push({
          ...account,
          parsed: stakeEntryData,
        });
      }
    } catch (e) {
      console.log(`Failed to decode token manager data`);
    }
  });

  return stakeEntryDatas.sort((a, b) =>
    a.pubkey.toBase58().localeCompare(b.pubkey.toBase58())
  );
};

export const getAllActiveStakeEntries = async (
  connection: Connection,
  commitment?: Commitment
): Promise<AccountData<StakeEntryData>[]> => {
  const programAccounts = await connection.getProgramAccounts(
    STAKE_POOL_ADDRESS,
    {
      filters: [
        {
          memcmp: {
            offset: 0,
            bytes: utils.bytes.bs58.encode(
              BorshAccountsCoder.accountDiscriminator("stakeEntry")
            ),
          },
        },
      ],
      commitment,
    }
  );
  const stakeEntryDatas: AccountData<StakeEntryData>[] = [];
  const coder = new BorshAccountsCoder(STAKE_POOL_IDL);
  programAccounts.forEach((account) => {
    try {
      const stakeEntryData: StakeEntryData = coder.decode(
        "stakeEntry",
        account.account.data
      );
      if (
        stakeEntryData &&
        stakeEntryData.lastStaker.toString() !== PublicKey.default.toString()
      ) {
        stakeEntryDatas.push({
          ...account,
          parsed: stakeEntryData,
        });
      }
    } catch (e) {
      // console.log(`Failed to decode stake entry data`);
    }
  });

  return stakeEntryDatas.sort((a, b) =>
    a.pubkey.toBase58().localeCompare(b.pubkey.toBase58())
  );
};

export const getAllStakeEntriesForPool = async (
  connection: Connection,
  stakePoolId: PublicKey,
  commitment?: Commitment
): Promise<AccountData<StakeEntryData>[]> => {
  const programAccounts = await connection.getProgramAccounts(
    STAKE_POOL_ADDRESS,
    {
      filters: [
        {
          memcmp: {
            offset: 0,
            bytes: utils.bytes.bs58.encode(
              BorshAccountsCoder.accountDiscriminator("stakeEntry")
            ),
          },
        },
        {
          memcmp: { offset: POOL_OFFSET, bytes: stakePoolId.toBase58() },
        },
      ],
      commitment,
    }
  );
  const stakeEntryDatas: AccountData<StakeEntryData>[] = [];
  const coder = new BorshAccountsCoder(STAKE_POOL_IDL);
  programAccounts.forEach((account) => {
    try {
      const stakeEntryData: StakeEntryData = coder.decode(
        "stakeEntry",
        account.account.data
      );
      stakeEntryDatas.push({
        ...account,
        parsed: stakeEntryData,
      });
    } catch (e) {
      // console.log(`Failed to decode stake entry data`);
    }
  });

  return stakeEntryDatas.sort((a, b) =>
    a.pubkey.toBase58().localeCompare(b.pubkey.toBase58())
  );
};

export const getActiveStakeEntriesForPool = async (
  connection: Connection,
  stakePoolId: PublicKey,
  commitment?: Commitment
): Promise<AccountData<StakeEntryData>[]> => {
  const programAccounts = await connection.getProgramAccounts(
    STAKE_POOL_ADDRESS,
    {
      filters: [
        {
          memcmp: { offset: POOL_OFFSET, bytes: stakePoolId.toBase58() },
        },
      ],
      commitment,
    }
  );
  const stakeEntryDatas: AccountData<StakeEntryData>[] = [];
  const coder = new BorshAccountsCoder(STAKE_POOL_IDL);
  programAccounts.forEach((account) => {
    try {
      const stakeEntryData: StakeEntryData = coder.decode(
        "stakeEntry",
        account.account.data
      );
      if (
        stakeEntryData &&
        stakeEntryData.lastStaker.toString() !== PublicKey.default.toString()
      ) {
        stakeEntryDatas.push({
          ...account,
          parsed: stakeEntryData,
        });
      }
    } catch (e) {
      // console.log(`Failed to decode token manager data`);
    }
  });

  return stakeEntryDatas.sort((a, b) =>
    a.pubkey.toBase58().localeCompare(b.pubkey.toBase58())
  );
};

export const getActiveStakeEntryIdsForPool = async (
  connection: Connection,
  stakePoolId: PublicKey,
  commitment?: Commitment
): Promise<PublicKey[]> => {
  const programAccounts = await connection.getProgramAccounts(
    STAKE_POOL_ADDRESS,
    {
      filters: [
        {
          memcmp: { offset: POOL_OFFSET, bytes: stakePoolId.toBase58() },
        },
      ],
      commitment,
      dataSlice: {
        length: 32,
        offset: STAKER_OFFSET,
      },
    }
  );
  return programAccounts
    .filter((x) => {
      try {
        const lastStaker = new PublicKey(x.account.data);
        return !lastStaker.equals(PublicKey.default);
      } catch (error) {
        console.error(error);
        return false;
      }
    })
    .map((x) => x.pubkey);
};

export const getStakeEntry = async (
  connection: Connection,
  stakeEntryId: PublicKey,
  commitment?: Commitment
): Promise<AccountData<StakeEntryData>> => {
  const program = stakePoolProgram(connection, undefined, { commitment });
  const parsed = await program.account.stakeEntry.fetch(stakeEntryId);
  return {
    parsed,
    pubkey: stakeEntryId,
  };
};

export const getStakeEntries = async (
  connection: Connection,
  stakeEntryIds: PublicKey[],
  commitment?: Commitment
): Promise<AccountData<StakeEntryData>[]> => {
  const program = stakePoolProgram(connection, undefined, { commitment });
  const stakeEntries = (await program.account.stakeEntry.fetchMultiple(
    stakeEntryIds
  )) as StakeEntryData[];
  return stakeEntries.map((tm, i) => ({
    parsed: tm,
    pubkey: stakeEntryIds[i]!,
  }));
};

export const getPoolIdentifier = async (
  connection: Connection,
  commitment?: Commitment
): Promise<AccountData<IdentifierData>> => {
  const program = stakePoolProgram(connection, undefined, { commitment });
  const identifierId = findIdentifierId();
  const parsed = await program.account.identifier.fetch(identifierId);
  return {
    parsed,
    pubkey: identifierId,
  };
};

export const getStakeAuthorization = async (
  connection: Connection,
  stakeAuthorizationId: PublicKey,
  commitment?: Commitment
): Promise<AccountData<StakeAuthorizationData>> => {
  const program = stakePoolProgram(connection, undefined, { commitment });
  const parsed = await program.account.stakeAuthorizationRecord.fetch(
    stakeAuthorizationId
  );
  return {
    parsed,
    pubkey: stakeAuthorizationId,
  };
};

export const getStakeAuthorizations = async (
  connection: Connection,
  stakeAuthorizationIds: PublicKey[],
  commitment?: Commitment
): Promise<AccountData<StakeAuthorizationData>[]> => {
  const program = stakePoolProgram(connection, undefined, { commitment });
  const stakeAuthorizations =
    (await program.account.stakeAuthorizationRecord.fetchMultiple(
      stakeAuthorizationIds
    )) as StakeAuthorizationData[];

  return stakeAuthorizations.map((data, i) => ({
    parsed: data,
    pubkey: stakeAuthorizationIds[i]!,
  }));
};

export const getStakeAuthorizationsForPool = async (
  connection: Connection,
  poolId: PublicKey,
  commitment?: Commitment
): Promise<AccountData<StakeAuthorizationData>[]> => {
  const programAccounts = await connection.getProgramAccounts(
    STAKE_POOL_ADDRESS,
    {
      filters: [
        {
          memcmp: {
            offset: 0,
            bytes: utils.bytes.bs58.encode(
              BorshAccountsCoder.accountDiscriminator(
                "stakeAuthorizationRecord"
              )
            ),
          },
        },
        {
          memcmp: { offset: POOL_OFFSET, bytes: poolId.toBase58() },
        },
      ],
      commitment,
    }
  );

  const stakeAuthorizationDatas: AccountData<StakeAuthorizationData>[] = [];
  const coder = new BorshAccountsCoder(STAKE_POOL_IDL);
  programAccounts.forEach((account) => {
    try {
      const data: StakeAuthorizationData = coder.decode(
        "stakeAuthorizationRecord",
        account.account.data
      );
      stakeAuthorizationDatas.push({
        ...account,
        parsed: data,
      });
      // eslint-disable-next-line no-empty
    } catch (e) {}
  });

  return stakeAuthorizationDatas.sort((a, b) =>
    a.pubkey.toBase58().localeCompare(b.pubkey.toBase58())
  );
};

export const getStakePoolsByAuthority = async (
  connection: Connection,
  user: PublicKey,
  commitment?: Commitment
): Promise<AccountData<StakePoolData>[]> => {
  const programAccounts = await connection.getProgramAccounts(
    STAKE_POOL_ADDRESS,
    {
      filters: [
        {
          memcmp: {
            offset: 0,
            bytes: utils.bytes.bs58.encode(
              BorshAccountsCoder.accountDiscriminator("stakePool")
            ),
          },
        },
        {
          memcmp: {
            offset: AUTHORITY_OFFSET,
            bytes: user.toBase58(),
          },
        },
      ],
      commitment,
    }
  );
  const stakePoolDatas: AccountData<StakePoolData>[] = [];
  const coder = new BorshAccountsCoder(STAKE_POOL_IDL);
  programAccounts.forEach((account) => {
    try {
      const stakePoolData: StakePoolData = coder.decode(
        "stakePool",
        account.account.data
      );
      if (stakePoolData) {
        stakePoolDatas.push({
          ...account,
          parsed: stakePoolData,
        });
      }
      // eslint-disable-next-line no-empty
    } catch (e) {}
  });
  return stakePoolDatas.sort((a, b) =>
    a.pubkey.toBase58().localeCompare(b.pubkey.toBase58())
  );
};

export const getAllStakeEntries = async (
  connection: Connection,
  commitment?: Commitment
): Promise<AccountData<StakeEntryData>[]> => {
  const programAccounts = await connection.getProgramAccounts(
    STAKE_POOL_ADDRESS,
    {
      filters: [
        {
          memcmp: {
            offset: 0,
            bytes: utils.bytes.bs58.encode(
              BorshAccountsCoder.accountDiscriminator("stakeEntry")
            ),
          },
        },
      ],
      commitment,
    }
  );
  const stakeEntryDatas: AccountData<StakeEntryData>[] = [];
  const coder = new BorshAccountsCoder(STAKE_POOL_IDL);
  programAccounts.forEach((account) => {
    try {
      const stakeEntryData: StakeEntryData = coder.decode(
        "stakeEntry",
        account.account.data
      );
      if (stakeEntryData) {
        stakeEntryDatas.push({
          ...account,
          parsed: stakeEntryData,
        });
      }
      // eslint-disable-next-line no-empty
    } catch (e) {}
  });
  return stakeEntryDatas.sort((a, b) =>
    a.pubkey.toBase58().localeCompare(b.pubkey.toBase58())
  );
};

export const getStakeBooster = async (
  connection: Connection,
  stakeBoosterId: PublicKey,
  commitment?: Commitment
): Promise<AccountData<StakeBoosterData>> => {
  const program = stakePoolProgram(connection, undefined, { commitment });
  const parsed = await program.account.stakeBooster.fetch(stakeBoosterId);
  return {
    parsed,
    pubkey: stakeBoosterId,
  };
};

export const getGroupStakeEntriesForUser = async (
  connection: Connection,
  user: PublicKey,
  commitment?: Commitment
): Promise<AccountData<GroupStakeEntryData>[]> => {
  const programAccounts = await connection.getProgramAccounts(
    STAKE_POOL_ADDRESS,
    {
      filters: [
        {
          memcmp: {
            offset: 0,
            bytes: utils.bytes.bs58.encode(
              BorshAccountsCoder.accountDiscriminator("groupStakeEntry")
            ),
          },
        },
        { memcmp: { offset: GROUP_STAKER_OFFSET, bytes: user.toBase58() } },
      ],
      commitment,
    }
  );

  const groupStakeEntryDatas: AccountData<GroupStakeEntryData>[] = [];
  const coder = new BorshAccountsCoder(STAKE_POOL_IDL);
  programAccounts.forEach((account) => {
    try {
      const groupStakeEntryData: GroupStakeEntryData = coder.decode(
        "groupStakeEntry",
        account.account.data
      );
      if (groupStakeEntryData) {
        groupStakeEntryDatas.push({
          ...account,
          parsed: groupStakeEntryData,
        });
      }
    } catch (e) {
      console.log(`Failed to decode token manager data`);
    }
  });

  return groupStakeEntryDatas.sort((a, b) =>
    a.pubkey.toBase58().localeCompare(b.pubkey.toBase58())
  );
};

export const getAllGroupStakeEntries = async (
  connection: Connection,
  commitment?: Commitment
): Promise<AccountData<GroupStakeEntryData>[]> => {
  const programAccounts = await connection.getProgramAccounts(
    STAKE_POOL_ADDRESS,
    {
      filters: [
        {
          memcmp: {
            offset: 0,
            bytes: utils.bytes.bs58.encode(
              BorshAccountsCoder.accountDiscriminator("groupStakeEntry")
            ),
          },
        },
      ],
      commitment,
    }
  );
  const groupStakeEntryDatas: AccountData<GroupStakeEntryData>[] = [];
  const coder = new BorshAccountsCoder(STAKE_POOL_IDL);
  programAccounts.forEach((account) => {
    try {
      const groupStakeEntryData: GroupStakeEntryData = coder.decode(
        "groupStakeEntry",
        account.account.data
      );
      if (groupStakeEntryData) {
        groupStakeEntryDatas.push({
          ...account,
          parsed: groupStakeEntryData,
        });
      }
    } catch (e) {
      console.log(`Failed to decode group stake entry data`);
    }
  });

  return groupStakeEntryDatas.sort((a, b) =>
    a.pubkey.toBase58().localeCompare(b.pubkey.toBase58())
  );
};

export const getGroupStakeEntry = async (
  connection: Connection,
  groupStakeEntryId: PublicKey,
  commitment?: Commitment
): Promise<AccountData<GroupStakeEntryData>> => {
  const program = stakePoolProgram(connection, undefined, { commitment });
  const parsed = await program.account.groupStakeEntry.fetch(groupStakeEntryId);
  return {
    parsed,
    pubkey: groupStakeEntryId,
  };
};

export const getGroupStakeEntries = async (
  connection: Connection,
  groupStakeEntryIds: PublicKey[],
  commitment?: Commitment
): Promise<AccountData<GroupStakeEntryData>[]> => {
  const program = stakePoolProgram(connection, undefined, { commitment });
  const groupStakeEntries =
    (await program.account.groupStakeEntry.fetchMultiple(
      groupStakeEntryIds
    )) as GroupStakeEntryData[];
  return groupStakeEntries.map((tm, i) => ({
    parsed: tm,
    pubkey: groupStakeEntryIds[i]!,
  }));
};


