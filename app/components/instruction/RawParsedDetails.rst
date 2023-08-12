app/components/instruction/RawParsedDetails.tsx
===============================================

Last edited: 2023-07-31 09:08:44

Contents:

.. code-block:: tsx

    import { ParsedInstruction } from '@solana/web3.js';
import React from 'react';

export function RawParsedDetails({ ix, children }: { ix: ParsedInstruction; children?: React.ReactNode }) {
    return (
        <>
            {children}

            <tr>
                <td>
                    Instruction Data <span className="text-muted">(JSON)</span>
                </td>
                <td className="text-lg-end">
                    <pre className="d-inline-block text-start json-wrap">{JSON.stringify(ix.parsed, null, 2)}</pre>
                </td>
            </tr>
        </>
    );
}


