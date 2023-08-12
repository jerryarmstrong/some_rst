components/treasuryV2/Details/tabState.ts
=========================================

Last edited: 2023-05-19 22:20:18

Contents:

.. code-block:: ts

    import create, { State } from 'zustand'

interface TabState extends State {
  selected: { [key: string]: unknown }
  get<T>(key: string): T | undefined
  set<T>(key: string, val: T): void
}

export const useTabState = create<TabState>((set, get) => ({
  selected: {},
  get: <T>(key: string) => get().selected[key] as T | undefined,
  set: <T>(key: string, val: T) =>
    set((s) => {
      s.selected[key] = val
    }),
}))


