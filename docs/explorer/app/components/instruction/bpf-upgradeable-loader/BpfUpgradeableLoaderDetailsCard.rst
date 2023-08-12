app/components/instruction/bpf-upgradeable-loader/BpfUpgradeableLoaderDetailsCard.tsx
=====================================================================================

Last edited: 2023-07-31 09:08:44

Contents:

.. code-block:: tsx

    import { Address } from '@components/common/Address';
import { ParsedInstruction, ParsedTransaction, PublicKey, SignatureResult } from '@solana/web3.js';
import { camelToTitleCase } from '@utils/index';
import { reportError } from '@utils/sentry';
import { ParsedInfo } from '@validators/index';
import React from 'react';
import { create, Struct } from 'superstruct';

import { InstructionCard } from '../InstructionCard';
import { UnknownDetailsCard } from '../UnknownDetailsCard';
import {
    CloseInfo,
    DeployWithMaxDataLenInfo,
    ExtendProgramInfo,
    InitializeBufferInfo,
    SetAuthorityInfo,
    UpgradeInfo,
    WriteInfo,
} from './types';

type DetailsProps = {
    tx: ParsedTransaction;
    ix: ParsedInstruction;
    index: number;
    result: SignatureResult;
    innerCards?: JSX.Element[];
    childIndex?: number;
};

export function BpfUpgradeableLoaderDetailsCard(props: DetailsProps) {
    try {
        const parsed = create(props.ix.parsed, ParsedInfo);
        switch (parsed.type) {
            case 'initializeBuffer': {
                return renderDetails<InitializeBufferInfo>(props, parsed, InitializeBufferInfo);
            }
            case 'write': {
                return renderDetails<WriteInfo>(props, parsed, WriteInfo);
            }
            case 'deployWithMaxDataLen': {
                return renderDetails<DeployWithMaxDataLenInfo>(props, parsed, DeployWithMaxDataLenInfo);
            }
            case 'upgrade': {
                return renderDetails<UpgradeInfo>(props, parsed, UpgradeInfo);
            }
            case 'setAuthority': {
                return renderDetails<SetAuthorityInfo>(props, parsed, SetAuthorityInfo);
            }
            case 'close': {
                return renderDetails<CloseInfo>(props, parsed, CloseInfo);
            }
            case 'extendProgram': {
                return renderDetails<ExtendProgramInfo>(props, parsed, ExtendProgramInfo);
            }
            default:
                return <UnknownDetailsCard {...props} />;
        }
    } catch (error) {
        reportError(error, {
            signature: props.tx.signatures[0],
        });
        return <UnknownDetailsCard {...props} />;
    }
}

function renderDetails<T extends object>(props: DetailsProps, parsed: ParsedInfo, struct: Struct<T>) {
    const info = create(parsed.info, struct);

    const attributes: JSX.Element[] = [];
    for (const entry of Object.entries<any>(info)) {
        const key = entry[0];
        let value = entry[1];
        if (value instanceof PublicKey) {
            value = <Address pubkey={value} alignRight link />;
        } else if (key === 'bytes') {
            value = <pre className="d-inline-block text-start mb-0 data-wrap">{value}</pre>;
        }

        attributes.push(
            <tr key={key}>
                <td>
                    {camelToTitleCase(key)} {key === 'bytes' && <span className="text-muted">(Base 64)</span>}
                </td>
                <td className="text-lg-end">{value}</td>
            </tr>
        );
    }

    return (
        <InstructionCard {...props} title={`BPF Upgradeable Loader: ${camelToTitleCase(parsed.type)}`}>
            <tr>
                <td>Program</td>
                <td className="text-lg-end">
                    <Address pubkey={props.ix.programId} alignRight link />
                </td>
            </tr>
            {attributes}
        </InstructionCard>
    );
}


