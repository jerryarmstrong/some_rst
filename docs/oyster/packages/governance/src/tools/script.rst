packages/governance/src/tools/script.ts
=======================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: ts

    // nameOf operator
// https://schneidenbach.gitbooks.io/typescript-cookbook/content/nameof-operator.html
export function nameOf<T>(name: keyof T) {
  return name;
}

export function getNameOf<T>() {
  return (name: keyof T) => name;
}

export function getErrorMessage(ex: any) {
  if (ex instanceof Error) {
    return ex.message;
  }

  return JSON.stringify(ex);
}

export function arrayToRecord<T>(
  source: readonly T[],
  getKey: (item: T) => string,
) {
  return source.reduce((all, a) => ({ ...all, [getKey(a)]: a }), {}) as Record<
    string,
    T
  >;
}


