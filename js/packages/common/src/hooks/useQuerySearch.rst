js/packages/common/src/hooks/useQuerySearch.ts
==============================================

Last edited: 2022-06-29 06:18:54

Contents:

.. code-block:: ts

    import { useMemo } from 'react';
import { useLocation } from 'react-router-dom';

export function useQuerySearch() {
  const { search } = useLocation();
  return useMemo(() => new URLSearchParams(search), [search]);
}


