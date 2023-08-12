app/utils/get-instruction-card-scroll-anchor-id.ts
==================================================

Last edited: 2023-07-31 09:08:44

Contents:

.. code-block:: ts

    export default function getInstructionCardScrollAnchorId(
    // An array of instruction sequence numbers, starting with the
    // top level instruction number. Instruction numbers start from 1.
    instructionNumberPath: number[]
): string {
    return `ix-${instructionNumberPath.join('-')}`;
}


