src/components/common/TableCardBody.tsx
=======================================

Last edited: 2022-08-30 20:54:29

Contents:

.. code-block:: tsx

    import React from "react";

export function TableCardBody({ children }: { children: React.ReactNode }) {
  return (
    <div className="table-responsive mb-0">
      <table className="table table-sm table-nowrap card-table">
        <tbody className="list">{children}</tbody>
      </table>
    </div>
  );
}


