js/packages/web/src/views/packCreate/components/Sidebar/data.ts
===============================================================

Last edited: 2022-06-29 06:18:54

Contents:

.. code-block:: ts

    import { CreatePackSteps } from '../../types';

export const STEPS_TITLES: Record<CreatePackSteps, string> = {
  [CreatePackSteps.SelectItems]: 'Select Items',
  [CreatePackSteps.SelectVoucher]: 'Select Voucher',
  [CreatePackSteps.AdjustQuantities]: 'Adjust Quantities',
  [CreatePackSteps.ReviewAndMint]: 'Review & Mint',
};

export const CONTINUE_TITLES: Record<CreatePackSteps, string> = {
  [CreatePackSteps.SelectItems]: 'Continue to Voucher',
  [CreatePackSteps.SelectVoucher]: 'Continue to Quantities',
  [CreatePackSteps.AdjustQuantities]: 'Continue to Mint',
  [CreatePackSteps.ReviewAndMint]: 'Confirm & Mint',
};


