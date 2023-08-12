js/packages/web/src/views/packCreate/components/SelectItemsStep/utils.ts
========================================================================

Last edited: 2022-06-29 06:18:54

Contents:

.. code-block:: ts

    import { StringPublicKey } from '@oyster/common';

import { SafetyDepositDraft } from '../../../../actions/createAuctionManager';

export const isSelected = ({
  selectedItems,
  pubkey,
}: {
  selectedItems: Record<string, SafetyDepositDraft>;
  pubkey?: StringPublicKey;
}): boolean => !!(pubkey && selectedItems[pubkey]);


