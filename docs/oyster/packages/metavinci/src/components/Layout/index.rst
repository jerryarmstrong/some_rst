packages/metavinci/src/components/Layout/index.tsx
==================================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: tsx

    import React from 'react';
import { Layout } from 'antd';

import './../../App.less';
import './index.less';
import { LABELS } from '../../constants';
import { AppBar } from '../AppBar';

const { Header, Content, Footer } = Layout;

export const AppLayout = React.memo((props: any) => {

  return (
    <>
      <div className="App">
        <Layout title={LABELS.APP_TITLE}>
          <Header className="App-Bar">
            <AppBar />
          </Header>
          <Content style={{ overflow: 'scroll' }}>
            {props.children}
          </Content>
        </Layout>
      </div>
    </>
  );
});


