test/examples/print/print.test.ts
=================================

Last edited: 2023-03-29 13:30:41

Contents:

.. code-block:: ts

    import expect from 'expect';
import { Contract } from '../../../src';
import { loadContract } from '../utils';

describe('Print', () => {
    let contract: Contract;

    before(async function () {
        this.timeout(150000);
        ({ contract } = await loadContract(__dirname, 'Print'));
    });

    it('logs', async function () {
        await new Promise<void>((resolve, reject) => {
            const listenId = contract.addLogListener(async (message) => {
                expect(message).toEqual('Hello, World!');
                await contract.removeLogListener(listenId);
                resolve();
            });
            contract.functions.greet().catch(reject);
        });
    });
});


