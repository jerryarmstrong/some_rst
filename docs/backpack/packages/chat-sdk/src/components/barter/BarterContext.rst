packages/chat-sdk/src/components/barter/BarterContext.tsx
=========================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: tsx

    import React, { useContext } from "react";

type BarterContext = {
  setSelectNft: any;
  room: string;
  barterId: number;
};

interface ExtendedBarterContext extends BarterContext {
  children: any;
}

export const _BarterContext = React.createContext<BarterContext | null>(null);

export function BarterProvider(props: ExtendedBarterContext) {
  return (
    <_BarterContext.Provider
      value={{
        setSelectNft: props.setSelectNft,
        room: props.room,
        barterId: props.barterId,
      }}
    >
      {props.children}
    </_BarterContext.Provider>
  );
}

export function useBarterContext(): BarterContext {
  const ctx = useContext(_BarterContext);
  if (!ctx) {
    throw new Error("context not found");
  }
  return ctx;
}


