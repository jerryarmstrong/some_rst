src/utils/notifications.tsx
===========================

Last edited: 2023-03-12 23:06:11

Contents:

.. code-block:: tsx

    import useNotificationStore from "../stores/useNotificationStore";

export function notify(newNotification: {
  type?: string
  message: string
  description?: string
  txid?: string
}) {
  const {
    notifications,
    set: setNotificationStore,
  } = useNotificationStore.getState()

  setNotificationStore((state: { notifications: any[] }) => {
    state.notifications = [
      ...notifications,
      { type: 'success', ...newNotification },
    ]
  })
}


