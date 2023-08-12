test/examples/named-returns/named-returns.test.ts
=================================================

Last edited: 2023-03-29 13:30:41

Contents:

.. code-block:: ts

    import expect from 'expect';
import { Contract } from '../../../src';
import { loadContract } from '../utils';

describe('Named Returns', () => {
    let contract: Contract;

    before(async function () {
        this.timeout(150000);
        ({ contract } = await loadContract(__dirname, 'Test'));
    });

    it('work', async function () {
        const {
            result: [a, b],
        } = await contract.functions.noop(1, 2);
        expect(a.toString()).toEqual('1');
        expect(b.toString()).toEqual('2');
    });
});


