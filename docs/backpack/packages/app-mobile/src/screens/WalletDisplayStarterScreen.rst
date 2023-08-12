packages/app-mobile/src/screens/WalletDisplayStarterScreen.tsx
==============================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: tsx

    import { Suspense } from "react";

import { ErrorBoundary } from "react-error-boundary";

import { ScreenLoading, ScreenError } from "~components/index";

function Container() {
  return null;
}

export function WalletDisplayStarterScreen() {
  return (
    <ErrorBoundary
      fallbackRender={({ error }) => <ScreenError error={error} />}
    >
      <Suspense fallback={<ScreenLoading />}>
        <Container />
      </Suspense>
    </ErrorBoundary>
  );
}


