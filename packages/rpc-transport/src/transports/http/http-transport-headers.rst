packages/rpc-transport/src/transports/http/http-transport-headers.ts
====================================================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    export type AllowedHttpRequestHeaders = Readonly<
    { [headerName: string]: string } & {
        // Someone can still sneak a forbidden header past Typescript if they do something like
        // fOo-BaR, but at that point they deserve the runtime failure.
        [K in DisallowedHeaders | ForbiddenHeaders as
            | K // `Foo-Bar`
            | Capitalize<Lowercase<K>> // `Foo-bar`
            | Lowercase<K> // `foo-bar`
            | Uncapitalize<K> // `foo-Bar`
            // `FOO-BAR`
            | Uppercase<K>]?: never;
    }
>;
// These are headers that we simply don't allow the developer to override because they're
// fundamental to the operation of the JSON-RPC transport.
type DisallowedHeaders = 'Accept' | 'Content-Length' | 'Content-Type' | 'Solana-Client';
type ForbiddenHeaders =
    | 'Accept-Charset'
    | 'Accept-Encoding'
    | 'Access-Control-Request-Headers'
    | 'Access-Control-Request-Method'
    | 'Connection'
    | 'Content-Length'
    | 'Cookie'
    | 'Date'
    | 'DNT'
    | 'Expect'
    | 'Host'
    | 'Keep-Alive'
    | 'Origin'
    | 'Permissions-Policy'
    // No currently available Typescript technique allows you to match on a prefix.
    // | 'Proxy-'
    // | 'Sec-'
    | 'Referer'
    | 'TE'
    | 'Trailer'
    | 'Transfer-Encoding'
    | 'Upgrade'
    | 'Via';

// These are headers which are fundamental to the JSON-RPC transport, and must not be modified.
const DISALLOWED_HEADERS: Record<string, boolean> = {
    accept: true,
    'content-length': true,
    'content-type': true,
};
// https://developer.mozilla.org/en-US/docs/Glossary/Forbidden_header_name
const FORBIDDEN_HEADERS: Record<string, boolean> = {
    'accept-charset': true,
    'accept-encoding': true,
    'access-control-request-headers': true,
    'access-control-request-method': true,
    connection: true,
    'content-length': true,
    cookie: true,
    date: true,
    dnt: true,
    expect: true,
    host: true,
    'keep-alive': true,
    origin: true,
    'permissions-policy': true,
    // No currently available Typescript technique allows you to match on a prefix.
    // 'proxy-':true,
    // 'sec-':true,
    referer: true,
    te: true,
    trailer: true,
    'transfer-encoding': true,
    upgrade: true,
    via: true,
};

export function assertIsAllowedHttpRequestHeaders(
    headers: Record<string, string>
): asserts headers is AllowedHttpRequestHeaders {
    const badHeaders = Object.keys(headers).filter(headerName => {
        const lowercaseHeaderName = headerName.toLowerCase();
        return (
            DISALLOWED_HEADERS[headerName.toLowerCase()] === true ||
            FORBIDDEN_HEADERS[headerName.toLowerCase()] === true ||
            lowercaseHeaderName.startsWith('proxy-') ||
            lowercaseHeaderName.startsWith('sec-')
        );
    });
    if (badHeaders.length > 0) {
        throw new Error(
            `${badHeaders.length > 1 ? 'These headers are' : 'This header is'} forbidden: ` +
                `\`${badHeaders.join('`, `')}\`. Learn more at ` +
                'https://developer.mozilla.org/en-US/docs/Glossary/Forbidden_header_name.'
        );
    }
}

/**
 * Lowercasing header names makes it easier to override user-supplied headers, such as those defined
 * in the `DisallowedHeaders` type.
 */
export function normalizeHeaders<T extends Record<string, string>>(
    headers: T
): { [K in keyof T & string as Lowercase<K>]: T[K] } {
    const out: Record<string, string> = {};
    for (const headerName in headers) {
        out[headerName.toLowerCase()] = headers[headerName];
    }
    return out as { [K in keyof T & string as Lowercase<K>]: T[K] };
}


