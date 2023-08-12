packages/governance/src/hooks/accountHooks.ts
=============================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: ts

    import { PublicKey } from '@solana/web3.js';
import { useEffect, useState } from 'react';

import {
  getAccountTypes,
  GovernanceAccount,
  GovernanceAccountClass,
} from '@solana/spl-governance';
import { GovernanceAccountParser } from '@solana/spl-governance';

import { GenericAccountParser, ParsedAccountBase } from '@oyster/common';
import { MemcmpFilter } from '@solana/spl-governance';
import { useAccountChangeTracker } from '../contexts/GovernanceContext';
import { useRpcContext } from './useRpcContext';
import { none, Option, some } from '../tools/option';
import { getGovernanceAccounts } from '@solana/spl-governance';
import { ProgramAccount } from '@solana/spl-governance';
import { arrayToRecord } from '../tools/script';

// Fetches Governance program account using the given key and subscribes to updates
export function useGovernanceAccountByPubkey<
  TAccount extends GovernanceAccount
>(accountClass: GovernanceAccountClass, pubkey: PublicKey | undefined) {
  const [account, setAccount] = useState<Option<ProgramAccount<TAccount>>>();

  const { connection, endpoint } = useRpcContext();
  const accountChangeTracker = useAccountChangeTracker();

  const getByPubkey = pubkey?.toBase58();

  useEffect(() => {
    if (!pubkey) {
      return;
    }

    const sub = (async () => {
      // TODO: Add retries for transient errors
      try {
        const accountInfo = await connection.getAccountInfo(pubkey);
        if (accountInfo) {
          const loadedAccount = GovernanceAccountParser(accountClass)(
            pubkey,
            accountInfo!,
          );
          setAccount(some(loadedAccount));
        } else {
          setAccount(none());
        }
      } catch (ex) {
        console.error(`Can't load ${pubkey.toBase58()} account`, ex);
        setAccount(none());
      }

      return accountChangeTracker.onAccountUpdated(update => {
        if (update.pubkey === getByPubkey) {
          const account = GovernanceAccountParser(accountClass)(
            new PublicKey(update.pubkey),
            update.accountInfo,
          ) as ProgramAccount<TAccount>;

          setAccount(some(account));
        }
      });
    })();

    return () => {
      sub.then(dispose => dispose());
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [getByPubkey, connection, endpoint]);

  return account;
}

// Fetches Governance program account using the given PDA args and subscribes to updates
export function useGovernanceAccountByPda<TAccount extends GovernanceAccount>(
  accountClass: GovernanceAccountClass,
  getPda: () => Promise<PublicKey | undefined>,
  pdaArgs: any[],
) {
  const [pda, setPda] = useState<PublicKey | undefined>();

  const pdaArgsKey = JSON.stringify(pdaArgs);

  useEffect(() => {
    (async () => {
      const resolvedPda = await getPda();
      setPda(resolvedPda);
    })();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [pdaArgsKey]);

  return useGovernanceAccountByPubkey<TAccount>(accountClass, pda);
}

// Fetches Governance program accounts using the given filter and subscribes to updates
export function useGovernanceAccountsByFilter<
  TAccount extends GovernanceAccount
>(accountClass: GovernanceAccountClass, filters: (MemcmpFilter | undefined)[]) {
  const [accounts, setAccounts] = useState<
    Record<string, ProgramAccount<TAccount>>
  >({});

  const { connection, endpoint, programId } = useRpcContext();

  const accountChangeTracker = useAccountChangeTracker();

  // Use stringify to get stable dependency for useEffect to  ensure we load the initial snapshot of accounts only once
  // If it causes performance issues then we should use object compare logic https://stackoverflow.com/questions/53601931/custom-useeffect-second-argument
  const filterKey = JSON.stringify(filters);

  useEffect(() => {
    if (filters.some(f => !f)) {
      return;
    }

    const queryFilters = filters.map(f => f!);
    const accountTypes = getAccountTypes(accountClass);

    const sub = (async () => {
      try {
        // TODO: add retries for transient errors
        const loadedAccounts = await getGovernanceAccounts<TAccount>(
          connection,
          programId,
          (accountClass as any) as new (args: any) => TAccount,
          queryFilters,
        );
        setAccounts(arrayToRecord(loadedAccounts, a => a.pubkey.toBase58()));
      } catch (ex) {
        console.error(`Can't load ${accountClass.name}`, ex);
        setAccounts({});
      }

      const disposeUpdateTracker = accountChangeTracker.onAccountUpdated(
        update => {
          if (accountTypes.some(at => update.accountType === at)) {
            const isMatch = !queryFilters.some(
              f => !f.isMatch(update.accountInfo.data),
            );

            const account = GovernanceAccountParser(accountClass)(
              new PublicKey(update.pubkey),
              update.accountInfo,
            ) as ProgramAccount<TAccount>;

            setAccounts((acts: any) => {
              if (isMatch) {
                return {
                  ...acts,
                  [update.pubkey]: account,
                };
              } else if (acts[update.pubkey]) {
                return {
                  ...Object.keys(acts)
                    .filter(k => k !== update.pubkey)
                    .reduce((res, key) => {
                      res[key] = acts[key];
                      return res;
                    }, {} as any),
                };
              } else {
                return acts;
              }
            });
          }
        },
      );

      const disposeRemoveTracker = accountChangeTracker.onAccountRemoved(
        remove => {
          if (accountTypes.some(at => remove.accountType === at)) {
            setAccounts((acts: any) => {
              if (acts[remove.pubkey]) {
                return {
                  ...Object.keys(acts)
                    .filter(k => k !== remove.pubkey)
                    .reduce((res, key) => {
                      res[key] = acts[key];
                      return res;
                    }, {} as any),
                };
              } else {
                return acts;
              }
            });
          }
        },
      );

      return { disposeRemoveTracker, disposeUpdateTracker };
    })();

    return () => {
      sub.then(({ disposeRemoveTracker, disposeUpdateTracker }) => {
        disposeRemoveTracker();
        disposeUpdateTracker();
      });
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [filterKey, connection, endpoint]);

  return Object.values(accounts);
}

export function useGovernanceAccountByFilter<
  TAccount extends GovernanceAccount
>(accountClass: GovernanceAccountClass, filters: (MemcmpFilter | undefined)[]) {
  const accounts = useGovernanceAccountsByFilter<TAccount>(
    accountClass,
    filters,
  );

  if (accounts.length === 0) {
    return undefined;
  }

  if (accounts.length === 1) {
    return accounts[0];
  }

  throw new Error(
    `Filters ${filters} returned multiple accounts ${accounts} for ${accountClass.name} while a single result was expected`,
  );
}

// Fetches Account using the given PDA args
export function useAccountByPda(
  getPda: () => Promise<PublicKey | undefined>,
  pdaArgs: any[],
) {
  const { connection } = useRpcContext();
  const [account, setAccount] = useState<Option<ParsedAccountBase>>();

  const pdaArgsKey = JSON.stringify(pdaArgs);

  useEffect(() => {
    const sub = (async () => {
      const pdaPk = await getPda();
      let subId = 0;

      if (pdaPk) {
        try {
          const accountInfo = await connection.getAccountInfo(pdaPk);

          if (accountInfo) {
            setAccount(some(GenericAccountParser(pdaPk, accountInfo)));
          } else {
            setAccount(none());
          }
        } catch (ex) {
          console.error(`Can't load ${pdaPk.toBase58()} account`, ex);
          setAccount(none());
        }

        subId = connection.onAccountChange(pdaPk, a =>
          setAccount(some(GenericAccountParser(pdaPk, a))),
        );
      } else {
        setAccount(none());
      }

      return () => {
        subId > 0 && connection.removeAccountChangeListener(subId);
      };
    })();

    return () => {
      sub.then(dispose => dispose());
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [pdaArgsKey]);

  return account;
}


