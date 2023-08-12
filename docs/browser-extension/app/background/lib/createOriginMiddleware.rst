app/background/lib/createOriginMiddleware.ts
============================================

Last edited: 2020-09-01 18:17:54

Contents:

.. code-block:: ts

    import { Store } from "../store"

export default function createOriginMiddleware(opts: { origin: string; store: Store }) {
  return function originMiddleware(req: any, res: any, next: any) {
    const { origin, store } = opts

    req.origin = origin

    if (origin.startsWith("chrome-extension://")) {
      //todo: should check for full ext url
      next()
      return
    }

    if (store.isOriginAuthorized(origin)) {
      next()
      return
    }

    if (
      req.method === "wallet_requestAccounts" ||
      req.method === "wallet_getCluster" ||
      req.method === "wallet_getState"
    ) {
      next()
      return
    }

    res.err = "authorized origin require to request: " + req.method
    return
  }
}


