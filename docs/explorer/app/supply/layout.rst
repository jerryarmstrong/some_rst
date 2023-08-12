app/supply/layout.tsx
=====================

Last edited: 2023-07-31 09:08:44

Contents:

.. code-block:: tsx

    import { RichListProvider } from '@providers/richList';
import { SupplyProvider } from '@providers/supply';
import { PropsWithChildren } from 'react';

export default function SupplyLayout({ children }: PropsWithChildren<Record<string, never>>) {
  return (
    <SupplyProvider>
      <RichListProvider>
        {children}
      </RichListProvider>
    </SupplyProvider>
  );
}


