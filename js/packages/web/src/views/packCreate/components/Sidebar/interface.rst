js/packages/web/src/views/packCreate/components/Sidebar/interface.ts
====================================================================

Last edited: 2022-06-29 06:18:54

Contents:

.. code-block:: ts

    import { CreatePackSteps } from '../../types';

export interface SidebarProps {
  step: CreatePackSteps;
  isValidStep: boolean;
  setStep: (step: CreatePackSteps) => void;
  submit: () => void;
  buttonLoading?: boolean;
}


