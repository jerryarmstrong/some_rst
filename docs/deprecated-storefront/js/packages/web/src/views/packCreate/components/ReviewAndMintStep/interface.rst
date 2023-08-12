js/packages/web/src/views/packCreate/components/ReviewAndMintStep/interface.ts
==============================================================================

Last edited: 2022-06-29 06:18:54

Contents:

.. code-block:: ts

    import { InfoFormState, PackState } from '../../interface';

export interface ReviewAndMintStepProps
  extends InfoFormState,
    Pick<
      PackState,
      'allowedAmountToRedeem' | 'supplyByMetadataKey' | 'distributionType'
    > {}


