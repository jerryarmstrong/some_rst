app/block/[slot]/programs/page.tsx
==================================

Last edited: 2023-07-31 09:08:44

Contents:

.. code-block:: tsx

    import { Metadata } from 'next/types';

import BlockProgramsTabClient from './page-client';

type Props = Readonly<{
    params: {
        slot: string;
    };
}>;

export async function generateMetadata({ params: { slot } }: Props): Promise<Metadata> {
    return {
        description: `Statistics pertaining to programs which were active during block ${slot} on Solana`,
        title: `Programs Active In Block | ${slot} | Solana`,
    };
}

export default function BlockProgramsTab(props: Props) {
    return <BlockProgramsTabClient {...props} />;
}


