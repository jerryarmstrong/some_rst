getting-started-react-cra5/src/App.test.js
==========================================

Last edited: 2023-05-10 12:33:36

Contents:

.. code-block:: js

    import { render, screen } from '@testing-library/react';
import App from './App';

test('renders learn react link', () => {
  render(<App />);
  const linkElement = screen.getByText(/NFT Mint Address/i);
  expect(linkElement).toBeInTheDocument();
});


