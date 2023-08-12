src/lib/clsxm.ts
================

Last edited: 2023-07-18 16:28:32

Contents:

.. code-block:: ts

    import clsx, { ClassValue } from 'clsx';
import { twMerge } from 'tailwind-merge';

/** Merge classes with tailwind-merge with clsx full feature */
export default function clsxm(...classes: ClassValue[]) {
  return twMerge(clsx(...classes));
}


