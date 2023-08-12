test/setup.js
=============

Last edited: 2023-05-19 22:20:18

Contents:

.. code-block:: js

    import '@testing-library/jest-dom/extend-expect'

jest.mock('next/router', () => require('next-router-mock'))


