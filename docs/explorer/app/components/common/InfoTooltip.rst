app/components/common/InfoTooltip.tsx
=====================================

Last edited: 2023-07-31 09:08:44

Contents:

.. code-block:: tsx

    import React, { ReactNode, useState } from 'react';
import { HelpCircle } from 'react-feather';

type Props = {
    text: string;
    children?: ReactNode;
    bottom?: boolean;
    right?: boolean;
};

type State = 'hide' | 'show';

function Popover({ state, bottom, right, text }: { state: State; bottom?: boolean; right?: boolean; text: string }) {
    if (state === 'hide') return null;
    return (
        <div className={`popover bs-popover-${bottom ? 'bottom' : 'top'}${right ? ' right' : ''} show`}>
            <div className={`arrow${right ? ' right' : ''}`} />
            <div className="popover-body">{text}</div>
        </div>
    );
}

export function InfoTooltip({ bottom, right, text, children }: Props) {
    const [state, setState] = useState<State>('hide');

    const justify = right ? 'end' : 'start';
    return (
        <div
            className="popover-container w-100"
            onMouseOver={() => setState('show')}
            onMouseOut={() => setState('hide')}
        >
            <div className={`d-flex align-items-center justify-content-${justify}`}>
                {children} <HelpCircle className="ms-2" size={13} />
            </div>
            <Popover bottom={bottom} right={right} state={state} text={text} />
        </div>
    );
}


