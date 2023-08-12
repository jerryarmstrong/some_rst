js/packages/web/src/views/packCreate/components/Header/interface.ts
===================================================================

Last edited: 2022-06-29 06:18:54

Contents:

.. code-block:: ts

    import { CreatePackSteps } from '../../types';

export interface HeaderProps {
  step: CreatePackSteps;
}

export interface HeaderContentRecord {
  title: string;
  subtitle?: string;
}


