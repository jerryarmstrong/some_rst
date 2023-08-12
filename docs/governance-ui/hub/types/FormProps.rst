hub/types/FormProps.ts
======================

Last edited: 2023-05-19 22:20:18

Contents:

.. code-block:: ts

    import { FormCallbacks } from './FormCallbacks';

export type FormProps<P extends object> = P & FormCallbacks<P>;


