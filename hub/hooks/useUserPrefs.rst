hub/hooks/useUserPrefs.ts
=========================

Last edited: 2023-08-11 18:13:34

Contents:

.. code-block:: ts

    import { useContext } from 'react';

import { context } from '@hub/providers/UserPrefs';

export function useUserPrefs() {
  return useContext(context);
}


