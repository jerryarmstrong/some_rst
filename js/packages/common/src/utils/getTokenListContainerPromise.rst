js/packages/common/src/utils/getTokenListContainerPromise.ts
============================================================

Last edited: 2022-06-29 06:18:54

Contents:

.. code-block:: ts

    import {
  TokenListContainer,
  TokenListProvider,
} from '@solana/spl-token-registry';

let _cachedTokenListContainerPromise: Promise<TokenListContainer> | null;

export function getTokenListContainerPromise() {
  if (_cachedTokenListContainerPromise == null) {
    _cachedTokenListContainerPromise = new TokenListProvider().resolve();
  }
  return _cachedTokenListContainerPromise;
}


