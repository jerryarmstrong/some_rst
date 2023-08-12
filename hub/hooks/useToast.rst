hub/hooks/useToast.ts
=====================

Last edited: 2023-08-11 18:13:34

Contents:

.. code-block:: ts

    import { useContext } from 'react';

import { context, ToastType } from '@hub/providers/Toast';

export function useToast() {
  const value = useContext(context);
  return { publish: value.publish };
}

export { ToastType };


