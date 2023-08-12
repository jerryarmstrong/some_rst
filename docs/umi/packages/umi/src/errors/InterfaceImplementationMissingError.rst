packages/umi/src/errors/InterfaceImplementationMissingError.ts
==============================================================

Last edited: 2023-07-27 15:49:41

Contents:

.. code-block:: ts

    import { SdkError } from './SdkError';

/** @category Errors */
export class InterfaceImplementationMissingError extends SdkError {
  readonly name: string = 'InterfaceImplementationMissingError';

  constructor(interfaceName: string, contextVariable: string) {
    const interfaceBasename = interfaceName.replace(/Interface$/, '');
    const message =
      `Tried using ${interfaceName} but no implementation of that interface was found. ` +
      `Make sure an implementation is registered, ` +
      `e.g. via "context.${contextVariable} = new My${interfaceBasename}();".`;
    super(message);
  }
}


