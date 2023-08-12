src/utils/notifications.tsx
===========================

Last edited: 2023-06-24 05:42:55

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


