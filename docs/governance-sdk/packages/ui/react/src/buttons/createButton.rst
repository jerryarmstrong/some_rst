packages/ui/react/src/buttons/createButton.ts
=============================================

Last edited: 2022-07-15 16:27:40

Contents:

.. code-block:: ts

    import React from 'react';

import { createFactory } from '../utils/styles/elementFactory';

export const createButton = createFactory<
  React.ButtonHTMLAttributes<HTMLButtonElement>,
  HTMLButtonElement
>('button');


