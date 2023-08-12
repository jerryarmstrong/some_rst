apps/backend-serverless/src/utilities/clients/database-services.utility.ts
==========================================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: ts

    export type Pagination = {
    pageSize: number;
    page: number;
};

export const calculatePaginationSkip = (pagination: Pagination) => {
    return pagination.pageSize * (pagination.page - 1);
};

export const DEFAULT_PAGINATION_SIZE = 10;


