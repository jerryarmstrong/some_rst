packages/ui/react/src/utils/styles/elementFactory.ts
====================================================

Last edited: 2022-07-15 16:27:40

Contents:

.. code-block:: ts

    import { createElement, forwardRef } from 'react';

import { cx } from './cx';

export function createFactory<P extends { className?: string }, R extends HTMLElement>(
  tag: string
) {
  return (customStyles: string) => {
    return forwardRef<R, P>((props, ref) => {
      const { className, ...rest } = props;

      return createElement(tag, {
        ref,
        className: cx(customStyles, className),
        ...rest,
      });
    });
  };
}


