test/setup.js
=============

Last edited: 2023-08-11 18:13:34

Contents:

.. code-block:: js

    import '@testing-library/jest-dom/extend-expect'

jest.mock('next/router', () => require('next-router-mock'))


