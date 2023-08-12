src/pages/SupplyPage.tsx
========================

Last edited: 2022-08-30 20:54:29

Contents:

.. code-block:: tsx

    import React from "react";
import { TopAccountsCard } from "components/TopAccountsCard";
import { SupplyCard } from "components/SupplyCard";

export function SupplyPage() {
  return (
    <div className="container mt-4">
      <SupplyCard />
      <TopAccountsCard />
    </div>
  );
}


