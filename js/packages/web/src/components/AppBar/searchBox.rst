js/packages/web/src/components/AppBar/searchBox.tsx
===================================================

Last edited: 2022-06-29 06:18:54

Contents:

.. code-block:: tsx

    import React from 'react';
import { SearchOutlined } from '@ant-design/icons';
import { Button } from 'antd';

export const SearchBox = () => {
  return (
    <Button
      className="search-btn"
      shape="circle"
      icon={<SearchOutlined />}
    ></Button>
  );
};


