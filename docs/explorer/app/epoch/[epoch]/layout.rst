app/epoch/[epoch]/layout.tsx
============================

Last edited: 2023-07-31 09:08:44

Contents:

.. code-block:: tsx

    import { EpochProvider } from '@providers/epoch';
import { PropsWithChildren } from 'react';

export default function EpochLayout({ children }: PropsWithChildren<Record<string, never>>) {
  return (
    <EpochProvider>
      {children}
    </EpochProvider>
  );
}


