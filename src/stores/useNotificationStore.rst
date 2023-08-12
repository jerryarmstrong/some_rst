src/stores/useNotificationStore.tsx
===================================

Last edited: 2023-06-24 05:42:55

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


