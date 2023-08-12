app/src/contexts/coingecko-api-context.tsx
==========================================

Last edited: 2023-07-21 18:33:07

Contents:

.. code-block:: tsx

    import type { FC, ReactNode } from "react";
import { createContext, useState } from "react";

import { ContractApi } from "../api/coingecko";

export type CoingeckoApiContextType = {
  contractApi: ContractApi;
};

export const ApiContext = createContext<CoingeckoApiContextType | undefined>(
  undefined
);

export const CoingeckoApiProvider: FC<{ children: ReactNode }> = ({
  children,
}) => {
  const [context] = useState<CoingeckoApiContextType>({
    contractApi: new ContractApi(),
  });

  return <ApiContext.Provider value={context}>{children}</ApiContext.Provider>;
};


