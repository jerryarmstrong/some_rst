app/background/lib/createTabIdMiddleware.ts
===========================================

Last edited: 2020-09-01 18:17:54

Contents:

.. code-block:: ts

    export default function createTabIdMiddleware(opts: { tabId: number }) {
  return function tabIdMiddleware(req: any, _: any, next: any) {
    req.tabId = opts.tabId
    next()
  }
}


