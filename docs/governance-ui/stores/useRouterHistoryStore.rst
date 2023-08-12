stores/useRouterHistoryStore.tsx
================================

Last edited: 2023-05-19 22:20:18

Contents:

.. code-block:: tsx

    import create, { State } from 'zustand'

interface RouterHistoryStore extends State {
  history: string[]
  setHistory: (history: string[]) => void
}

const useRouterHistoryStore = create<RouterHistoryStore>((set, _get) => ({
  history: [],
  setHistory: (history) => {
    set({ history: history })
  },
}))

export default useRouterHistoryStore


