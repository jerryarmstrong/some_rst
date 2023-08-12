packages/umi/src/HttpResponse.ts
================================

Last edited: 2023-07-27 15:49:41

Contents:

.. code-block:: ts

    import type { HttpResponseHeaders } from './HttpHeaders';

/**
 * Defines a HTTP Response with custom data.
 * @category Http
 */
export type HttpResponse<D = any> = {
  data: D;
  body: string;
  ok: boolean;
  status: number;
  statusText: string;
  headers: HttpResponseHeaders;
};


