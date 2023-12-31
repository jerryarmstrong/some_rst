src/lib/wait/index.ts
=====================

Last edited: 2023-04-18 16:02:26

Contents:

.. code-block:: ts

    import * as TA from 'fp-ts/Task';
import * as TE from 'fp-ts/TaskEither';

export function wait(ms: number) {
  return new Promise<true>((resolve) => {
    setTimeout(() => resolve(true), ms);
  })
}

export function waitT(ms: number): TA.Task<true> {
  return () => wait(ms);
}

export function waitTE(ms: number): TE.TaskEither<never, true> {
  return TE.fromTask(waitT(ms));
}


