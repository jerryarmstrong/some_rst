js/packages/web/src/views/packCreate/components/Header/index.tsx
================================================================

Last edited: 2022-06-29 06:18:54

Contents:

.. code-block:: tsx

    import React from 'react';
import { HEADER_CONTENT } from './data';
import { HeaderProps } from './interface';

const Header: React.FC<HeaderProps> = ({ step, children }) => {
  const { title } = HEADER_CONTENT[step];

  return (
    <div className="create-pack-header">
      <p className="create-pack-header__title">{title}</p>
      {children}
    </div>
  );
};

export default Header;


