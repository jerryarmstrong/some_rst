src/programs/receiptManager/accounts.ts
=======================================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: ts

    import type { AccountData } from "@cardinal/common";
import { tryGetAccount } from "@cardinal/common";
import { BorshAccountsCoder, utils } from "@coral-xyz/anchor";
import type { Commitment, Connection } from "@solana/web3.js";
import { PublicKey } from "@solana/web3.js";

import { REWARD_DISTRIBUTOR_ADDRESS } from "../rewardDistributor";
import type {
  ReceiptEntryData,
  ReceiptManagerData,
  RewardReceiptData,
} from "./constants";
import {
  RECEIPT_MANAGER_ADDRESS,
  RECEIPT_MANAGER_IDL,
  receiptManagerProgram,
} from "./constants";

export const getReceiptManager = async (
  connection: Connection,
  receiptManagerId: PublicKey,
  commitment?: Commitment
): Promise<AccountData<ReceiptManagerData>> => {
  const program = receiptManagerProgram(connection, undefined, { commitment });
  const parsed = (await program.account.receiptManager.fetch(
    receiptManagerId
  )) as ReceiptManagerData;
  return {
    parsed,
    pubkey: receiptManagerId,
  };
};

export const getAllreceiptManagers = async (
  connection: Connection,
  commitment?: Commitment
): Promise<AccountData<ReceiptManagerData>[]> =>
  getAllOfType<ReceiptManagerData>(connection, "receiptManager", commitment);

export const getReceiptManagersForPool = async (
  connection: Connection,
  stakePoolId: PublicKey,
  commitment?: Commitment
): Promise<AccountData<RewardReceiptData>[]> => {
  const programAccounts = await connection.getProgramAccounts(
    REWARD_DISTRIBUTOR_ADDRESS,
    {
      filters: [
        {
          memcmp: {
            offset: 0,
            bytes: utils.bytes.bs58.encode(
              BorshAccountsCoder.accountDiscriminator("receiptManager")
            ),
          },
        },
        {
          memcmp: {
            offset: 9,
            bytes: stakePoolId.toBase58(),
          },
        },
      ],
      commitment,
    }
  );
  const ReceiptManagerDatas: AccountData<RewardReceiptData>[] = [];
  const coder = new BorshAccountsCoder(RECEIPT_MANAGER_IDL);
  programAccounts.forEach((account) => {
    try {
      const ReceiptManagerData: RewardReceiptData = coder.decode(
        "receiptManager",
        account.account.data
      );
      if (ReceiptManagerData) {
        ReceiptManagerDatas.push({
          ...account,
          parsed: ReceiptManagerData,
        });
      }
      // eslint-disable-next-line no-empty
    } catch (e) {}
  });
  return ReceiptManagerDatas.sort((a, b) =>
    a.pubkey.toBase58().localeCompare(b.pubkey.toBase58())
  );
};

//////// RECEIPT ENTRY ////////
export const getReceiptEntry = async (
  connection: Connection,
  receiptEntryId: PublicKey,
  commitment?: Commitment
): Promise<AccountData<ReceiptEntryData>> => {
  const program = receiptManagerProgram(connection, undefined, { commitment });
  const parsed = (await program.account.receiptEntry.fetch(
    receiptEntryId
  )) as ReceiptEntryData;
  return {
    parsed,
    pubkey: receiptEntryId,
  };
};

//////// REWARD RECEIPT ////////
export const getRewardReceipt = async (
  connection: Connection,
  rewardReceiptId: PublicKey,
  commitment?: Commitment
): Promise<AccountData<RewardReceiptData>> => {
  const program = receiptManagerProgram(connection, undefined, { commitment });
  const parsed = (await program.account.rewardReceipt.fetch(
    rewardReceiptId
  )) as RewardReceiptData;
  return {
    parsed,
    pubkey: rewardReceiptId,
  };
};

export const getAllRewardReceipts = async (
  connection: Connection,
  commitment?: Commitment
): Promise<AccountData<ReceiptManagerData>[]> =>
  getAllOfType<ReceiptManagerData>(connection, "rewardReceipt", commitment);

export const getRewardReceiptsForManager = async (
  connection: Connection,
  rewardDistributorId: PublicKey,
  commitment?: Commitment
): Promise<AccountData<RewardReceiptData>[]> => {
  const programAccounts = await connection.getProgramAccounts(
    REWARD_DISTRIBUTOR_ADDRESS,
    {
      filters: [
        {
          memcmp: {
            offset: 0,
            bytes: utils.bytes.bs58.encode(
              BorshAccountsCoder.accountDiscriminator("rewardReceipt")
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
  const rewardReceiptDatas: AccountData<RewardReceiptData>[] = [];
  const coder = new BorshAccountsCoder(RECEIPT_MANAGER_IDL);
  programAccounts.forEach((account) => {
    try {
      const rewardReceiptData: RewardReceiptData = coder.decode(
        "rewardReceipt",
        account.account.data
      );
      if (rewardReceiptData) {
        rewardReceiptDatas.push({
          ...account,
          parsed: rewardReceiptData,
        });
      }
      // eslint-disable-next-line no-empty
    } catch (e) {}
  });
  return rewardReceiptDatas.sort((a, b) =>
    a.pubkey.toBase58().localeCompare(b.pubkey.toBase58())
  );
};

export const getClaimableRewardReceiptsForManager = async (
  connection: Connection,
  receiptManagerId: PublicKey,
  commitment?: Commitment
): Promise<AccountData<RewardReceiptData>[]> => {
  const ReceiptManagerData = await tryGetAccount(() =>
    getReceiptManager(connection, receiptManagerId, commitment)
  );
  if (!ReceiptManagerData) {
    throw `No reward receipt manager found for ${receiptManagerId.toString()}`;
  }
  const rewardReceipts = await getRewardReceiptsForManager(
    connection,
    receiptManagerId
  );
  return rewardReceipts.filter(
    (receipt) =>
      receipt.parsed.target.toString() !== PublicKey.default.toString()
  );
};

//////// utils ////////
export const getAllOfType = async <T>(
  connection: Connection,
  key: string,
  commitment?: Commitment
): Promise<AccountData<T>[]> => {
  const programAccounts = await connection.getProgramAccounts(
    RECEIPT_MANAGER_ADDRESS,
    {
      filters: [
        {
          memcmp: {
            offset: 0,
            bytes: utils.bytes.bs58.encode(
              BorshAccountsCoder.accountDiscriminator(key)
            ),
          },
        },
      ],
      commitment,
    }
  );

  const datas: AccountData<T>[] = [];
  const coder = new BorshAccountsCoder(RECEIPT_MANAGER_IDL);
  programAccounts.forEach((account) => {
    try {
      const data: T = coder.decode(key, account.account.data);
      if (data) {
        datas.push({
          ...account,
          parsed: data,
        });
      }
      // eslint-disable-next-line no-empty
    } catch (e) {}
  });

  return datas.sort((a, b) =>
    a.pubkey.toBase58().localeCompare(b.pubkey.toBase58())
  );
};


