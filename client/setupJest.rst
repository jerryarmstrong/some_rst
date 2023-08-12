client/setupJest.ts
===================

Last edited: 2022-06-08 08:09:30

Contents:

.. code-block:: ts

    import { GlobalWithFetchMock } from "jest-fetch-mock";

const customGlobal: GlobalWithFetchMock = global as GlobalWithFetchMock;
customGlobal.fetch = require("jest-fetch-mock");
customGlobal.fetchMock = customGlobal.fetch;


