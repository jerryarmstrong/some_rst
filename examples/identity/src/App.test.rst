examples/identity/src/App.test.tsx
==================================

Last edited: 2022-08-04 13:38:52

Contents:

.. code-block:: tsx

    import React from 'react';
import { render, screen } from '@testing-library/react';
import App from './App';

test('renders learn react link', () => {
  render(<App />);
  const linkElement = screen.getByText(/learn react/i);
  expect(linkElement).toBeInTheDocument();
});


