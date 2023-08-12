examples/point-of-sale/src/client/hooks/useFullscreen.ts
========================================================

Last edited: 2023-05-03 15:27:33

Contents:

.. code-block:: ts

    import { createContext, useContext } from 'react';

export interface FullscreenContextState {
    fullscreen: boolean;
    toggleFullscreen(): void;
}

export const FullscreenContext = createContext<FullscreenContextState>({} as FullscreenContextState);

export function useFullscreen(): FullscreenContextState {
    return useContext(FullscreenContext);
}


