packages/metavinci/src/components/AppBar/searchBox.tsx
======================================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: tsx

    import React from 'react';
import { Input } from 'antd';
import { SearchOutlined } from '@ant-design/icons';
import { Button } from 'antd';
import './searchBox.less';

const { Search } = Input;

export const SearchBox = ({}) => {
  return <Button className="search-btn" shape="circle" icon={<SearchOutlined />}>
  </Button>;

  const onSearch = (value: string) => console.log(value);

  return <Search placeholder={"Search for artists & NFTs"}
                 onSearch={onSearch}
                 className="search-box" />;
}


