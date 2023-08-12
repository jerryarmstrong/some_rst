src/App.test.js
===============

Last edited: 2021-05-21 14:15:46

Contents:

.. code-block:: js

    import React from 'react';
import { render } from '@testing-library/react';
import App from './App';

test('renders learn react link', () => {
  const { getByText } = render(<App />);
  const linkElement = getByText(/learn react/i);
  expect(linkElement).toBeInTheDocument();
});


