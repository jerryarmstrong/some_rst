app/components/common/TableCardBody.tsx
=======================================

Last edited: 2023-07-31 09:08:44

Contents:

.. code-block:: tsx

    import React from 'react';

export function TableCardBody({ children }: { children: React.ReactNode }) {
    return (
        <div className="table-responsive mb-0">
            <table className="table table-sm table-nowrap card-table">
                <tbody className="list">{children}</tbody>
            </table>
        </div>
    );
}


