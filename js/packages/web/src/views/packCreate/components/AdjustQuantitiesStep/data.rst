js/packages/web/src/views/packCreate/components/AdjustQuantitiesStep/data.ts
============================================================================

Last edited: 2022-06-29 06:18:54

Contents:

.. code-block:: ts

    import { PackDistributionType } from '@oyster/common';

export const DISTRIBUTION_TYPES_DATA: Record<
  PackDistributionType,
  { title: string; subtitle: string }
> = {
  [PackDistributionType.MaxSupply]: {
    title: 'Supply',
    subtitle:
      "The chance of getting a card will be based on the card's supply that is left",
  },
  [PackDistributionType.Fixed]: {
    title: 'Weighted Supply',
    subtitle: 'Weighted chance of getting each card with limited card supply',
  },
  [PackDistributionType.Unlimited]: {
    title: 'Weighted',
    subtitle: 'Weighted chance of getting each card',
  },
};


