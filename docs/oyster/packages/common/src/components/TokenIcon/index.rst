packages/common/src/components/TokenIcon/index.tsx
==================================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: tsx

    import React, { useState } from 'react';
import { PublicKey } from '@solana/web3.js';
import { getTokenIcon, KnownTokenMap } from '../../utils';
import { useConnectionConfig } from '../../contexts/connection';
import { Identicon } from '../Identicon';

export const TokenIcon = (props: {
  mintAddress?: string | PublicKey;
  style?: React.CSSProperties;
  size?: number;
  className?: string;
  tokenMap?: KnownTokenMap;
}) => {
  const [showIcon, setShowIcon] = useState(true);

  let icon: string | undefined = '';
  if (props.tokenMap) {
    icon = getTokenIcon(props.tokenMap, props.mintAddress);
  } else {
    const { tokenMap } = useConnectionConfig();
    icon = getTokenIcon(tokenMap, props.mintAddress);
  }

  const size = props.size || 20;

  if (showIcon && icon) {
    return (
      <img
        alt="Token icon"
        className={props.className}
        key={icon}
        width={props.style?.width || size.toString()}
        height={props.style?.height || size.toString()}
        src={icon}
        style={{
          marginRight: '0.5rem',
          marginTop: '0.11rem',
          borderRadius: '10rem',
          backgroundColor: 'white',
          backgroundClip: 'padding-box',
          ...props.style,
        }}
        onError={() => setShowIcon(false)}
      />
    );
  }
  return (
    <Identicon
      address={props.mintAddress}
      style={{
        marginRight: '0.5rem',
        width: size,
        height: size,
        marginTop: 2,
        ...props.style,
      }}
    />
  );
};

export const PoolIcon = (props: {
  mintA: string;
  mintB: string;
  style?: React.CSSProperties;
  className?: string;
}) => {
  return (
    <div className={props.className} style={{ display: 'flex' }}>
      <TokenIcon
        mintAddress={props.mintA}
        style={{ marginRight: '-0.5rem', ...props.style }}
      />
      <TokenIcon mintAddress={props.mintB} />
    </div>
  );
};


