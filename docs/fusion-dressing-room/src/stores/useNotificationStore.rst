src/stores/useNotificationStore.tsx
===================================

Last edited: 2023-03-12 23:06:11

Contents:

.. code-block:: tsx

    import create, { State } from "zustand";
import produce from "immer";

interface NotificationStore extends State {
  notifications: Array<{
    type: string
    message: string
    description?: string
    txid?: string
  }>
  set: (x: any) => void
}

const useNotificationStore = create<NotificationStore>((set, _get) => ({
  notifications: [],
  set: (fn) => set(produce(fn)),
}))

export default useNotificationStore


