examples/point-of-sale/src/client/utils/createURLWithQuery.ts
=============================================================

Last edited: 2023-05-03 15:27:33

Contents:

.. code-block:: ts

    import { ParsedUrlQuery } from 'querystring';

export function createURLWithQuery(url: string | URL, base: string | URL, query: ParsedUrlQuery): URL {
    url = new URL(url, base);

    for (const [key, value] of Object.entries(query)) {
        if (value) {
            if (Array.isArray(value)) {
                for (const v of value) {
                    url.searchParams.append(key, v);
                }
            } else {
                url.searchParams.append(key, value);
            }
        }
    }

    return url;
}


