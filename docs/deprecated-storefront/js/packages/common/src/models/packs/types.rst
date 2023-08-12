js/packages/common/src/models/packs/types.ts
============================================

Last edited: 2022-06-29 06:18:54

Contents:

.. code-block:: ts

    export enum PackDistributionType {
  MaxSupply,
  Fixed,
  Unlimited,
}

export enum PackKey {
  Uninitialized,
  PackSet,
  PackCard,
  PackVoucher,
  ProvingProcess,
}

export enum PackSetState {
  NotActivated,
  Activated,
  Deactivated,
  Ended,
}


