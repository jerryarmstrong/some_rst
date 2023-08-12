hub/hooks/useJWT.ts
===================

Last edited: 2023-05-19 22:20:18

Contents:

.. code-block:: ts

    import { useContext } from 'react';

import { context } from '@hub/providers/JWT';

export function useJWT() {
  const value = useContext(context);
  return [value.jwt, value.setJwt] as const;
}


