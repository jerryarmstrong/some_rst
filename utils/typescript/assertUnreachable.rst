utils/typescript/assertUnreachable.ts
=====================================

Last edited: 2023-08-11 18:13:34

Contents:

.. code-block:: ts

    export default function assertUnreachable(_: never): never {
  throw new Error('An unreachability assertion was reached')
}


