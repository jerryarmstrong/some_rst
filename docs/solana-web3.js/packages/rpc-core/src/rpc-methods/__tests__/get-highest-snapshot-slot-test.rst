packages/rpc-core/src/rpc-methods/__tests__/get-highest-snapshot-slot-test.ts
=============================================================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    // TODO: Again, until we can manipulate the local validator more,
// this test can't be implemented properly.
describe('getHighestSnapshotSlot', () => {
    describe('when there is at least one valid snapshot', () => {
        it.todo('returns the highest snapshot slot information that the node has snapshots for');
    });

    describe('when there are no snapshots yet', () => {
        // TODO:
        //  Error code -32008
        //  Message: "No snapshot"
        it.todo('throws an error');
    });
});


