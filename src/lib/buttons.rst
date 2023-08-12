src/lib/buttons.ts
==================

Last edited: 2023-07-18 16:28:32

Contents:

.. code-block:: ts

    import React from 'react';

import clsxm from '@/lib/clsxm';

import { BASE_STYLES } from '@/styles/buttons';

export function createFactory<
  P extends { className?: string },
  R extends HTMLElement
>(tag: string) {
  return (customStyles: string) => {
    return React.forwardRef<R, P>((props, ref) => {
      const { className, ...rest } = props;

      return React.createElement(tag, {
        ref,
        className: clsxm(customStyles, className, BASE_STYLES),
        ...rest,
      });
    });
  };
}

export const createAnchor = createFactory<
  React.AnchorHTMLAttributes<HTMLAnchorElement>,
  HTMLAnchorElement
>('a');

export const createButton = createFactory<
  React.ButtonHTMLAttributes<HTMLButtonElement>,
  HTMLButtonElement
>('button');


