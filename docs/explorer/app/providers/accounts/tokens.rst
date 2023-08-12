app/providers/accounts/tokens.tsx
=================================

Last edited: 2023-07-31 09:08:44

Contents:

.. code-block:: tsx

    'use client';

import * as Cache from '@providers/cache';
import { ActionType, FetchStatus } from '@providers/cache';
import { useCluster } from '@providers/cluster';
import { Connection, PublicKey } from '@solana/web3.js';
import { Cluster } from '@utils/cluster';
import { reportError } from '@utils/sentry';
import { TokenAccountInfo } from '@validators/accounts/token';
import React from 'react';
import { create } from 'superstruct';

import { getTokenInfos } from '@/app/utils/token-info';

export type TokenInfoWithPubkey = {
    info: TokenAccountInfo;
    pubkey: PublicKey;
    logoURI?: string;
    symbol?: string;
    name?: string;
};

interface AccountTokens {
    tokens?: TokenInfoWithPubkey[];
}

type State = Cache.State<AccountTokens>;
type Dispatch = Cache.Dispatch<AccountTokens>;

const StateContext = React.createContext<State | undefined>(undefined);
const DispatchContext = React.createContext<Dispatch | undefined>(undefined);

type ProviderProps = { children: React.ReactNode };
export function TokensProvider({ children }: ProviderProps) {
    const { url } = useCluster();
    const [state, dispatch] = Cache.useReducer<AccountTokens>(url);

    React.useEffect(() => {
        dispatch({ type: ActionType.Clear, url });
    }, [dispatch, url]);

    return (
        <StateContext.Provider value={state}>
            <DispatchContext.Provider value={dispatch}>{children}</DispatchContext.Provider>
        </StateContext.Provider>
    );
}

export const TOKEN_PROGRAM_ID = new PublicKey('TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA');

async function fetchAccountTokens(dispatch: Dispatch, pubkey: PublicKey, cluster: Cluster, url: string) {
    const key = pubkey.toBase58();
    dispatch({
        key,
        status: FetchStatus.Fetching,
        type: ActionType.Update,
        url,
    });

    let status;
    let data;
    try {
        const { value } = await new Connection(url, 'processed').getParsedTokenAccountsByOwner(pubkey, {
            programId: TOKEN_PROGRAM_ID,
        });

        const tokens: TokenInfoWithPubkey[] = value.slice(0, 101).map(accountInfo => {
            const parsedInfo = accountInfo.account.data.parsed.info;
            const info = create(parsedInfo, TokenAccountInfo);
            return { info, pubkey: accountInfo.pubkey };
        });

        // Fetch symbols and logos for tokens
        const tokenMintInfos = await getTokenInfos(tokens.map(t => t.info.mint), cluster, url);
        if (tokenMintInfos) {
            const mappedTokenInfos = Object.fromEntries(tokenMintInfos.map(t => [t.address, {
                logoURI: t.logoURI,
                name: t.name,
                symbol: t.symbol
            }]))
            tokens.forEach(t => {
                const tokenInfo = mappedTokenInfos[t.info.mint.toString()]
                if (tokenInfo) {
                    t.logoURI = tokenInfo.logoURI ?? undefined;
                    t.symbol = tokenInfo.symbol;
                    t.name = tokenInfo.name;
                }
            })
        }

        data = {
            tokens
        };
        status = FetchStatus.Fetched;
    } catch (error) {
        if (cluster !== Cluster.Custom) {
            reportError(error, { url });
        }
        status = FetchStatus.FetchFailed;
    }
    dispatch({ data, key, status, type: ActionType.Update, url });
}

export function useAccountOwnedTokens(address: string): Cache.CacheEntry<AccountTokens> | undefined {
    const context = React.useContext(StateContext);

    if (!context) {
        throw new Error(`useAccountOwnedTokens must be used within a AccountsProvider`);
    }

    return context.entries[address];
}

export function useFetchAccountOwnedTokens() {
    const dispatch = React.useContext(DispatchContext);
    if (!dispatch) {
        throw new Error(`useFetchAccountOwnedTokens must be used within a AccountsProvider`);
    }

    const { cluster, url } = useCluster();
    return React.useCallback(
        (pubkey: PublicKey) => {
            fetchAccountTokens(dispatch, pubkey, cluster, url);
        },
        [dispatch, cluster, url]
    );
}


