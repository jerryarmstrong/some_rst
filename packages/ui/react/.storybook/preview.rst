packages/ui/react/.storybook/preview.js
=======================================

Last edited: 2022-07-15 16:27:40

Contents:

.. code-block:: js

    
import theme from './theme';
import '../styles.css';
import './fonts.css';

export const parameters = {
  actions: { argTypesRegex: "^on[A-Z].*" },
  controls: {
    matchers: {
      color: /(background|color)$/i,
      date: /Date$/,
    },
  },
  docs: {
    theme,
  }
}


