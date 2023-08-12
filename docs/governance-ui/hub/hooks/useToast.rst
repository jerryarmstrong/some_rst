hub/hooks/useToast.ts
=====================

Last edited: 2023-05-19 22:20:18

Contents:

.. code-block:: ts

    import { useContext } from 'react';

import { context, ToastType } from '@hub/providers/Toast';

export function useToast() {
  const value = useContext(context);
  return { publish: value.publish };
}

export { ToastType };


