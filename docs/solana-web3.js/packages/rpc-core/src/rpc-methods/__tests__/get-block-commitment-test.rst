packages/rpc-core/src/rpc-methods/__tests__/get-block-commitment-test.ts
========================================================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    describe('getBlockCommitment', () => {
    // TODO: We need a good way to feed `getBlockCommitment` a recent block.
    // This would actually return a value for commitment.
    // This is tricky to do without `getSlot`, and we'll need some kind
    // of manipulation capability over test-validator to pull it off without
    // another RPC call.
    it.todo('returns the block commitment for a recent block');

    // TODO: We also need a reliable way to feed `getBlockCommitment` an old block.
    it.todo('returns the block commitment for an older block, which has null commitment');
});


