utils/notifications.tsx
=======================

Last edited: 2023-05-19 22:20:18

Contents:

.. code-block:: tsx

    import useNotificationStore from '../stores/useNotificationStore'

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

  setNotificationStore((state) => {
    state.notifications = [
      ...notifications,
      { type: 'success', ...newNotification },
    ]
  })
}


