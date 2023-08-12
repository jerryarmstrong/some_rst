packages/ui/react/src/utils/styles/cx.ts
========================================

Last edited: 2022-07-15 16:27:40

Contents:

.. code-block:: ts

    import { createTailwindMerge } from 'tailwind-merge';

type ClassValue = string | null | false | undefined;

export const merge = createTailwindMerge(() => ({
  cacheSize: 500,
  prefix: 'rui-',
  theme: {},
  classGroups: {},
  conflictingClassGroups: {},
}));

/**
 * Converts a variadic list of tailwind classes into a flat
 */
export function cx(...classes: ClassValue[]) {
  return merge(...classes);
}


