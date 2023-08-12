app/components/common/LoadingCard.tsx
=====================================

Last edited: 2023-07-31 09:08:44

Contents:

.. code-block:: tsx

    import React from 'react';

export function LoadingCard({ message }: { message?: string }) {
    return (
        <div className="card">
            <div className="card-body text-center">
                <span className="align-text-top spinner-grow spinner-grow-sm me-2"></span>
                {message || 'Loading'}
            </div>
        </div>
    );
}


