apps/merchant-ui/src/lib/utils.ts
=================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: ts

    import { ClassValue, clsx } from 'clsx';
import { twMerge } from 'tailwind-merge';

export function cn(...inputs: ClassValue[]) {
    return twMerge(clsx(inputs));
}


