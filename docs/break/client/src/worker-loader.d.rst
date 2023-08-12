client/src/worker-loader.d.ts
=============================

Last edited: 2022-06-08 08:09:30

Contents:

.. code-block:: ts

    declare module "worker-loader!*" {
  class WebpackWorker extends Worker {
    constructor();
  }

  export default WebpackWorker;
}


