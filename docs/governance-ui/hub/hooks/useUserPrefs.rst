hub/hooks/useUserPrefs.ts
=========================

Last edited: 2023-05-19 22:20:18

Contents:

.. code-block:: ts

    import { useContext } from 'react';

import { context } from '@hub/providers/UserPrefs';

export function useUserPrefs() {
  return useContext(context);
}


