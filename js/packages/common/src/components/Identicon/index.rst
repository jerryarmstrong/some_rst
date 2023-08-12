js/packages/common/src/components/Identicon/index.tsx
=====================================================

Last edited: 2022-06-29 06:18:54

Contents:

.. code-block:: tsx

    import React, { useEffect, useRef } from 'react';

import Jazzicon from '@metamask/jazzicon';
import bs58 from 'bs58';
import { PublicKey } from '@solana/web3.js';

export const Identicon = (props: {
  address?: string | PublicKey;
  style?: React.CSSProperties;
  className?: string;
  alt?: string;
}) => {
  const { style, className, alt } = props;
  const address =
    typeof props.address === 'string'
      ? props.address
      : props.address?.toBase58();
  const ref = useRef<HTMLDivElement>();

  useEffect(() => {
    if (address && ref.current) {
      try {
        ref.current.innerHTML = '';
        ref.current.className = className || '';
        ref.current.appendChild(
          Jazzicon(
            style?.width || 16,
            parseInt(bs58.decode(address).toString('hex').slice(5, 15), 16),
          ),
        );
      } catch (err) {
        // TODO
      }
    }
  }, [address, style, className]);

  return (
    <div
      className="identicon-wrapper"
      title={alt}
      ref={ref as any}
      style={props.style}
    />
  );
};


