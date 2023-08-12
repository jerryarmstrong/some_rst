hub/types/FormProps.ts
======================

Last edited: 2023-08-11 18:13:34

Contents:

.. code-block:: ts

    import { FormCallbacks } from './FormCallbacks';

export type FormProps<P extends object> = P & FormCallbacks<P>;


