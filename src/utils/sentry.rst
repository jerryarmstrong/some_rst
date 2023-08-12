src/utils/sentry.ts
===================

Last edited: 2022-08-30 20:54:29

Contents:

.. code-block:: ts

    type Tags =
  | {
      [key: string]: string;
    }
  | undefined;

export function reportError(err: unknown, tags: Tags) {
  if (err instanceof Error) {
    console.error(err, err.message, tags);
  }
}


