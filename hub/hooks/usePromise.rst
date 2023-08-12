hub/hooks/usePromise.ts
=======================

Last edited: 2023-08-11 18:13:34

Contents:

.. code-block:: ts

    import { useRef } from 'react';

export function usePromise<T>() {
  const resolver = useRef<((value: T) => void) | null>(null);
  const promise = useRef<Promise<T>>(
    new Promise((resolve) => {
      resolver.current = (value: T) => resolve(value);
    }),
  );

  return [promise.current, (value: T) => resolver.current?.(value)] as const;
}


