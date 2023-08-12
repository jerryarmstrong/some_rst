packages/core/react/src/useLocalStorage.native.ts
=================================================

Last edited: 2022-10-02 20:43:04

Contents:

.. code-block:: ts

    import { useState } from 'react';
import type { useLocalStorage as baseUseLocalStorage } from './useLocalStorage.js';

export const useLocalStorage: typeof baseUseLocalStorage = function useLocalStorage<T>(
    _key: string,
    defaultState: T
): [T, React.Dispatch<React.SetStateAction<T>>] {
    /**
     * Until such time as we have a strategy for implementing wallet
     * memorization on React Native, simply punt and return a no-op.
     */
    return useState(defaultState);
};


