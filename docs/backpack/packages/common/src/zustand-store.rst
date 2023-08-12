packages/common/src/zustand-store.ts
====================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: ts

    import { create } from "zustand";

type jsFn = (code: string) => void;

interface State {
  injectJavaScript: jsFn | undefined;
  setInjectJavaScript: (injectJavaScript: jsFn) => void;
}

export const useStore = create<State>((set) => ({
  injectJavaScript: undefined,
  setInjectJavaScript: (injectJavaScript: jsFn) =>
    set(() => ({ injectJavaScript })),
}));


