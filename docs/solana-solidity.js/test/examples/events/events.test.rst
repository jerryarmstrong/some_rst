test/examples/events/events.test.ts
===================================

Last edited: 2023-03-29 13:30:41

Contents:

.. code-block:: ts

    import { LogDescription } from '@ethersproject/abi';
import expect from 'expect';
import { Contract } from '../../../src';
import { loadContract } from '../utils';

describe('Events', () => {
    let contract: Contract;

    // events are broken with solang:latest and this library
    xit('get returned in contract deploy results', async function () {
        this.timeout(150000);

        const result = await loadContract(__dirname, 'Events');
        contract = result.contract;
        const events = result.events;
        expect(events.length).toEqual(1);

        const [{ args }] = events;
        expect(args.length).toEqual(3);
        expect(args[0].toString()).toEqual('102');
        expect(args[1]).toEqual(true);
        expect(args[2]).toEqual('foobar');
    });

    // events are broken with solang:latest and this library
    xit('can be subscribed', async function () {
        const event = await new Promise<LogDescription>((resolve, reject) => {
            const listenerId = contract.addEventListener(async (event) => {
                await contract.removeEventListener(listenerId);
                resolve(event);
            });
            contract.functions.first().catch(reject);
        });

        expect(event.name).toEqual('First');

        const { args } = event;
        expect(args.length).toEqual(3);
        expect(args[0].toString()).toEqual('102');
        expect(args[1]).toEqual(true);
        expect(args[2]).toEqual('foobar');
    });

    // events are broken with solang:latest and this library
    xit('get returned in contract call results', async function () {
        const { events } = await contract.functions.second();

        expect(events.length).toEqual(1);

        const [{ args }] = events;
        expect(args.length).toEqual(3);
        expect(args[0].toString()).toEqual('500332');
        expect(args[1]).toEqual('0x41424344');
        expect(args[2]).toEqual('0xcafe0123');
    });
});


