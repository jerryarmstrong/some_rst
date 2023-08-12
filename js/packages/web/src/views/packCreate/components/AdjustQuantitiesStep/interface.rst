js/packages/web/src/views/packCreate/components/AdjustQuantitiesStep/interface.ts
=================================================================================

Last edited: 2022-06-29 06:18:54

Contents:

.. code-block:: ts

    import { PackState } from '../../interface';

export enum InputType {
  weight = 'weight',
  maxSupply = 'maxSupply',
}

export interface AdjustQuantitiesStepProps
  extends Pick<
    PackState,
    | 'allowedAmountToRedeem'
    | 'distributionType'
    | 'selectedItems'
    | 'weightByMetadataKey'
    | 'supplyByMetadataKey'
  > {
  setPackState: (values: Partial<PackState>) => void;
  isUnlimited: boolean;
}


