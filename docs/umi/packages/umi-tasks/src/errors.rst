packages/umi-tasks/src/errors.ts
================================

Last edited: 2023-07-27 15:49:41

Contents:

.. code-block:: ts

    /** @category Errors */
export class TaskError extends Error {
  readonly name: string = 'TaskError';
}

/** @category Errors */
export class TaskIsAlreadyRunningError extends TaskError {
  readonly name: string = 'TaskIsAlreadyRunningError';

  constructor() {
    const message =
      `Trying to re-run a task that hasn't completed yet. ` +
      `Ensure the task has completed using "await" before trying to run it again.`;
    super(message);
  }
}


