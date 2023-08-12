app/components/common/Overlay.tsx
=================================

Last edited: 2023-07-31 09:08:44

Contents:

.. code-block:: tsx

    import React from 'react';

type OverlayProps = {
    show: boolean;
};

export function Overlay({ show }: OverlayProps) {
    return <div className={`modal-backdrop fade ${show ? 'show' : 'disable-pointer-events'}`}></div>;
}


