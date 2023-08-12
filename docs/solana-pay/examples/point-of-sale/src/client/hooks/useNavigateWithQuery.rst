examples/point-of-sale/src/client/hooks/useNavigateWithQuery.ts
===============================================================

Last edited: 2023-05-03 15:27:33

Contents:

.. code-block:: ts

    import { useRouter } from 'next/router';
import { useCallback } from 'react';
import { createURLWithQuery } from '../utils/createURLWithQuery';
import { useConfig } from './useConfig';

export interface NavigateOptions {
    replace: boolean;
}

export function useNavigateWithQuery() {
    const { baseURL } = useConfig();
    const router = useRouter();
    const { query } = router;

    return useCallback(
        (pathname: string, replace = false) => {
            const url = String(createURLWithQuery(pathname, baseURL, query));
            if (replace) {
                router.replace(url);
            } else {
                router.push(url);
            }
        },
        [baseURL, query, router]
    );
}


