packages/governance/src/components/RealmBadge/realmBadge.tsx
============================================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: tsx

    import { PublicKey } from '@solana/web3.js';
import React from 'react';
import { TokenIcon } from '@oyster/common';
import './style.less';

export function RealmBadge({
  communityMint,
  councilMint,
  size = 40,
}: {
  communityMint: PublicKey | undefined;
  councilMint?: PublicKey;
  size?: number;
}) {
  return (
    <div style={{ position: 'relative' }}>
      <TokenIcon mintAddress={communityMint} size={size} />
      {councilMint && (
        <div className="council-token-icon">
          <TokenIcon
            style={{
              position: 'absolute',
              top: 0.5 * size,
              left: 0.75 * size,
            }}
            mintAddress={councilMint}
            size={0.5 * size}
          />
        </div>
      )}
    </div>
  );
}


