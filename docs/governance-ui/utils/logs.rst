utils/logs.ts
=============

Last edited: 2023-05-19 22:20:18

Contents:

.. code-block:: ts

    import * as Sentry from '@sentry/react'

export const trySentryLog = ({
  tag,
  objToStringify,
}: {
  tag: string
  objToStringify: any
}) => {
  try {
    Sentry.captureMessage(JSON.stringify(objToStringify), {
      tags: { tag: tag },
    })
  } catch (e) {
    console.log(e, 'error in sentry log')
  }
}


