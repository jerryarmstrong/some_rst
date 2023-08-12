app/utils/sentry.ts
===================

Last edited: 2023-07-31 09:08:44

Contents:

.. code-block:: ts

    'use client';

import * as Sentry from '@sentry/nextjs';

type Tags =
    | {
          [key: string]: string;
      }
    | undefined;

export function reportError(err: unknown, tags: Tags) {
    if (err instanceof Error) {
        console.error(err, err.message);
        try {
            Sentry.captureException(err, {
                tags,
            });
        } catch (err) {
            // Sentry can fail if error rate limit is reached
        }
    }
}


