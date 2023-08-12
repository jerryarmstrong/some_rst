packages/gumdrop/src/hooks/useQuerySearch.tsx
=============================================

Last edited: 2022-08-25 19:21:42

Contents:

.. code-block:: tsx

    import React from 'react';
import { useLocation } from 'react-router-dom';

export function useQuerySearch() {
  const { search } = useLocation();
  return React.useMemo(() => new URLSearchParams(search), [search]);
}


