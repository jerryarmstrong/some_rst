packages/test-config/setup-fetch-mock.ts
========================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    import fetchMock, { enableFetchMocks } from 'jest-fetch-mock-fork';
enableFetchMocks();

beforeEach(() => {
    fetchMock.doMock();
});

afterEach(() => {
    fetchMock.resetMocks();
    fetchMock.dontMock();
});


