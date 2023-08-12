packages/ui/material-ui/src/useWalletDialog.ts
==============================================

Last edited: 2023-08-07 04:48:35

Contents:

.. code-block:: ts

    import { createContext, useContext } from 'react';

export interface WalletDialogContextState {
    open: boolean;
    setOpen: (open: boolean) => void;
}

export const WalletDialogContext = createContext<WalletDialogContextState>({} as WalletDialogContextState);

export function useWalletDialog(): WalletDialogContextState {
    return useContext(WalletDialogContext);
}


