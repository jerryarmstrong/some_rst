utils/notifications.tsx
=======================

Last edited: 2023-08-11 18:13:34

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


