packages/ui/react/src/buttons/Tertiary.tsx
==========================================

Last edited: 2022-07-15 16:27:40

Contents:

.. code-block:: tsx

    import React, { forwardRef } from 'react';

import { TERTIARY_WRAPPER, TERTIARY } from '../utils/styles/common/button';

import { createButton } from './createButton';

type ButtonProps = React.ButtonHTMLAttributes<HTMLButtonElement>;

const TertiaryWrapper = createButton(TERTIARY_WRAPPER);

export const Tertiary = forwardRef<HTMLButtonElement, ButtonProps>((props, ref) => {
  const { className, children, ...rest } = props;

  return (
    <TertiaryWrapper className={className} {...rest} ref={ref}>
      <div className={TERTIARY}>{children}</div>
    </TertiaryWrapper>
  );
});


