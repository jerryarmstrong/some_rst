packages/test-matchers/toBeFrozenObject.ts
==========================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    expect.extend({
    toBeFrozenObject(actual: object) {
        return {
            message: () => `Expected object ${this.isNot ? 'not ' : ''}to be frozen`,
            pass: Object.isFrozen(actual),
        };
    },
});

declare global {
    // eslint-disable-next-line @typescript-eslint/no-namespace
    namespace jest {
        interface AsymmetricMatchers {
            toBeFrozenObject(): void;
        }
        interface Matchers<R> {
            toBeFrozenObject(): R;
        }
    }
}

export {};


