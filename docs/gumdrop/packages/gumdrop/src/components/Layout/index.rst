packages/gumdrop/src/components/Layout/index.tsx
================================================

Last edited: 2022-08-25 19:21:42

Contents:

.. code-block:: tsx

    import React from 'react';
import { Layout } from 'antd';

import { AppBar } from '../AppBar';

const { Header, Content } = Layout;

export const AppLayout = React.memo(function AppLayoutImpl(props: any) {
  return (
    <>
      <Layout id={'main-layout'}>
        <span id={'main-bg'}></span>
        <span id={'bg-gradient'}></span>
        <span id={'static-header-gradient'}></span>
        <span id={'static-end-gradient'}></span>
        <Layout id={'width-layout'}>
          <Content
            style={{
              padding: '30px 48px ',
              flex: 'unset',
            }}
          >
            <Header className="App-Bar">
              <AppBar />
            </Header>
          </Content>
          <Content
            style={{
              overflow: 'scroll',
              paddingLeft: '96px',
              paddingRight: '96px',
              paddingBottom: '30px',
              paddingTop: '-30px',
            }}
          >
            {props.children}
          </Content>
        </Layout>
      </Layout>
    </>
  );
});


