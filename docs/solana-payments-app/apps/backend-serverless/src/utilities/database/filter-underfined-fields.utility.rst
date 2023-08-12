apps/backend-serverless/src/utilities/database/filter-underfined-fields.utility.ts
==================================================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: ts

    export const filterUndefinedFields = <T extends object>(obj: T): Partial<T> => {
    const filteredObj: Partial<T> = {};

    for (const key in obj) {
        if (obj.hasOwnProperty(key)) {
            const value = obj[key];
            if (value !== undefined) {
                filteredObj[key] = value;
            }
        }
    }

    return filteredObj;
};


