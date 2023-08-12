js/packages/web/src/views/packCreate/components/SelectItemsStep/interface.ts
============================================================================

Last edited: 2022-06-29 06:18:54

Contents:

.. code-block:: ts

    import { SafetyDepositDraft } from '../../../../actions/createAuctionManager';

export interface SelectItemsStepProps {
  handleSelectItem: (item: SafetyDepositDraft) => void;
  items: SafetyDepositDraft[];
  selectedItems: Record<string, SafetyDepositDraft>;
  showSupply?: boolean;
  emptyMessage?: string;
  isLoading?: boolean;
}


