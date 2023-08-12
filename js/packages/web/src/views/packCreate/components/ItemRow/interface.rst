js/packages/web/src/views/packCreate/components/ItemRow/interface.ts
====================================================================

Last edited: 2022-06-29 06:18:54

Contents:

.. code-block:: ts

    import { ReactElement } from 'react';
import { SafetyDepositDraft } from '../../../../actions/createAuctionManager';

export interface ItemRowProps {
  isSelected?: boolean;
  onClick?: () => void;
  item: SafetyDepositDraft;
  children?: ReactElement;
  showSupply?: boolean;
}


