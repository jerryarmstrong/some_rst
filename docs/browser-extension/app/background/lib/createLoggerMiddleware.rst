app/background/lib/createLoggerMiddleware.ts
============================================

Last edited: 2020-09-01 18:17:54

Contents:

.. code-block:: ts

    import { createLogger } from "../../core/utils"

const log = createLogger("sol:rpc")

export default function createLoggerMiddleware(opts: { origin: string }) {
  return function loggerMiddleware(req: any, res: any, next: any) {
    next((/** @type {Function} */ cb: any) => {
      if (res.error) {
        log("Error in RPC response:\n", res)
      }
      if (req.isMetamaskInternal) {
        return
      }
      log("RPC (%s): %O -> %O", opts.origin, req, res)
      cb()
    })
  }
}


