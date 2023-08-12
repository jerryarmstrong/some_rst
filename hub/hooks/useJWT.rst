hub/hooks/useJWT.ts
===================

Last edited: 2023-08-11 18:13:34

Contents:

.. code-block:: ts

    import { useContext } from 'react';

import { context } from '@hub/providers/JWT';

export function useJWT() {
  const value = useContext(context);
  return [value.jwt, value.setJwt] as const;
}


