examples/point-of-sale/src/client/hooks/useLinkWithQuery.ts
===========================================================

Last edited: 2023-05-03 15:27:33

Contents:

.. code-block:: ts

    import { useRouter } from 'next/router';
import { useMemo } from 'react';
import { createURLWithQuery } from '../utils/createURLWithQuery';
import { useConfig } from './useConfig';

export function useLinkWithQuery(pathname: string) {
    const { baseURL } = useConfig();
    const { query } = useRouter();

    return useMemo(() => String(createURLWithQuery(pathname, baseURL, query)), [pathname, baseURL, query]);
}


