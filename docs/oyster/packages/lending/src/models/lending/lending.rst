packages/lending/src/models/lending/lending.ts
==============================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: ts

    export enum LendingInstruction {
  InitLendingMarket = 0,
  InitReserve = 1,
  InitObligation = 2,
  DepositReserveLiquidity = 3,
  WithdrawReserveLiquidity = 4,
  BorrowLiquidity = 5,
  RepayOblogationLiquidity = 6,
  LiquidateObligation = 7,
  AccrueReserveInterest = 8,
}


