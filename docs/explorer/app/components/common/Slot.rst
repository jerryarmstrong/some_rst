app/components/common/Slot.tsx
==============================

Last edited: 2023-07-31 09:08:44

Contents:

.. code-block:: tsx

    import { useClusterPath } from '@utils/url';
import Link from 'next/link';
import React from 'react';

import { Copyable } from './Copyable';

type Props = {
    slot: number | bigint;
    link?: boolean;
};
export function Slot({ slot, link }: Props) {
    const slotPath = useClusterPath({ pathname: `/block/${slot}` });
    return (
        <span className="font-monospace">
            {link ? (
                <Copyable text={slot.toString()}>
                    <Link href={slotPath}>{slot.toLocaleString('en-US')}</Link>
                </Copyable>
            ) : (
                slot.toLocaleString('en-US')
            )}
        </span>
    );
}


