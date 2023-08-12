app/components/instruction/InstructionCard.tsx
==============================================

Last edited: 2023-07-31 09:08:44

Contents:

.. code-block:: tsx

    import { Address } from '@components/common/Address';
import { useScrollAnchor } from '@providers/scroll-anchor';
import { useFetchRawTransaction, useRawTransactionDetails } from '@providers/transactions/raw';
import { ParsedInstruction, SignatureResult, TransactionInstruction } from '@solana/web3.js';
import getInstructionCardScrollAnchorId from '@utils/get-instruction-card-scroll-anchor-id';
import React, { useContext } from 'react';
import { Code } from 'react-feather';

import { RawDetails } from './RawDetails';
import { RawParsedDetails } from './RawParsedDetails';
import { SignatureContext } from './SignatureContext';

type InstructionProps = {
    title: string;
    children?: React.ReactNode;
    result: SignatureResult;
    index: number;
    ix: TransactionInstruction | ParsedInstruction;
    defaultRaw?: boolean;
    innerCards?: JSX.Element[];
    childIndex?: number;
};

export function InstructionCard({
    title,
    children,
    result,
    index,
    ix,
    defaultRaw,
    innerCards,
    childIndex,
}: InstructionProps) {
    const [resultClass] = ixResult(result, index);
    const [showRaw, setShowRaw] = React.useState(defaultRaw || false);
    const signature = useContext(SignatureContext);
    const rawDetails = useRawTransactionDetails(signature);

    let raw: TransactionInstruction | undefined = undefined;
    if (rawDetails && childIndex === undefined) {
        raw = rawDetails?.data?.raw?.transaction.instructions[index];
    }

    const fetchRaw = useFetchRawTransaction();
    const fetchRawTrigger = () => fetchRaw(signature);

    const rawClickHandler = () => {
        if (!defaultRaw && !showRaw && !raw) {
            fetchRawTrigger();
        }

        return setShowRaw(r => !r);
    };
    const scrollAnchorRef = useScrollAnchor(
        getInstructionCardScrollAnchorId(childIndex != null ? [index + 1, childIndex + 1] : [index + 1])
    );
    return (
        <div className="card" ref={scrollAnchorRef}>
            <div className="card-header">
                <h3 className="card-header-title mb-0 d-flex align-items-center">
                    <span className={`badge bg-${resultClass}-soft me-2`}>
                        #{index + 1}
                        {childIndex !== undefined ? `.${childIndex + 1}` : ''}
                    </span>
                    {title}
                </h3>

                <button
                    disabled={defaultRaw}
                    className={`btn btn-sm d-flex align-items-center ${showRaw ? 'btn-black active' : 'btn-white'}`}
                    onClick={rawClickHandler}
                >
                    <Code className="me-2" size={13} /> Raw
                </button>
            </div>
            <div className="table-responsive mb-0">
                <table className="table table-sm table-nowrap card-table">
                    <tbody className="list">
                        {showRaw ? (
                            <>
                                <tr>
                                    <td>Program</td>
                                    <td className="text-lg-end">
                                        <Address pubkey={ix.programId} alignRight link />
                                    </td>
                                </tr>
                                {'parsed' in ix ? (
                                    <RawParsedDetails ix={ix}>{raw ? <RawDetails ix={raw} /> : null}</RawParsedDetails>
                                ) : (
                                    <RawDetails ix={ix} />
                                )}
                            </>
                        ) : (
                            children
                        )}
                        {innerCards && innerCards.length > 0 && (
                            <>
                                <tr className="table-sep">
                                    <td colSpan={3}>Inner Instructions</td>
                                </tr>
                                <tr>
                                    <td colSpan={3}>
                                        <div className="inner-cards">{innerCards}</div>
                                    </td>
                                </tr>
                            </>
                        )}
                    </tbody>
                </table>
            </div>
        </div>
    );
}

function ixResult(result: SignatureResult, index: number) {
    if (result.err) {
        const err = result.err as any;
        const ixError = err['InstructionError'];
        if (ixError && Array.isArray(ixError)) {
            const [errorIndex, error] = ixError;
            if (Number.isInteger(errorIndex) && errorIndex === index) {
                return ['warning', `Error: ${JSON.stringify(error)}`];
            }
        }
        return ['dark'];
    }
    return ['success'];
}


