src/pages/_app.tsx
==================

Last edited: 2023-07-18 16:28:32

Contents:

.. code-block:: tsx

    import { AppProps } from 'next/app';
import Script from 'next/script';
import React from 'react';

import '@/styles/globals.css';
import '@/styles/stylesheet-family-support.css';

const GoogleTag = React.memo(
  function GoogleTag() {
    return (
      <React.Fragment>
        <Script
          async
          src='https://www.googletagmanager.com/gtag/js?id=G-TG90SK6TGB'
        />
        <Script id='gta'>{`
          window.dataLayer = window.dataLayer || [];
          function gtag(){dataLayer.push(arguments);}
          gtag('js', new Date());
          gtag('config', 'G-TG90SK6TGB');
        `}</Script>
      </React.Fragment>
    );
  },
  () => true
);

function MyApp({ Component, pageProps }: AppProps) {
  return (
    <>
      <GoogleTag />
      <Component {...pageProps} />
    </>
  );
}

export default MyApp;


