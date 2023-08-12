index.d.ts
==========

Last edited: 2020-04-16 02:43:45

Contents:

.. code-block:: ts

    declare module 'gatsby-plugin-intl' {
  import * as gatsby from 'gatsby';
  import React from 'react';

  export * from 'react-intl';

  export class Link<TState> extends gatsby.Link<TState> {}
  export const navigate: typeof gatsby.navigate;
  export const changeLocale: (language: string, to?: string) => void;
  export const IntlContextProvider: React.Provider;
  export const IntlContextConsumer: React.Consumer;
}

