packages/app-mobile/src/graphql/RelayEnvironment.tsx
====================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: tsx

    import { useMemo } from "react";

import { RelayEnvironmentProvider } from "react-relay";

import { createEnvironment } from "./create-relay-environment";

export default function RelayEnvironment({
  children,
}: {
  children: React.ReactNode;
}): React.ReactElement {
  const environment = useMemo(() => {
    return createEnvironment();
  }, []);

  return (
    <RelayEnvironmentProvider environment={environment}>
      {children}
    </RelayEnvironmentProvider>
  );
}


