packages/library-legacy/test/account.test.ts
============================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    import {expect} from 'chai';
import {Buffer} from 'buffer';

import {Account} from '../src/account';

describe('Account', () => {
  it('generate new account', () => {
    const account = new Account();
    expect(account.secretKey).to.have.length(64);
  });

  it('account from secret key', () => {
    const secretKey = Buffer.from([
      153, 218, 149, 89, 225, 94, 145, 62, 233, 171, 46, 83, 227, 223, 173, 87,
      93, 163, 59, 73, 190, 17, 37, 187, 146, 46, 51, 73, 79, 73, 136, 40, 27,
      47, 73, 9, 110, 62, 93, 189, 15, 207, 169, 192, 192, 205, 146, 217, 171,
      59, 33, 84, 75, 52, 213, 221, 74, 101, 217, 139, 135, 139, 153, 34,
    ]);
    const account = new Account(secretKey);
    expect(account.publicKey.toBase58()).to.eq(
      '2q7pyhPwAwZ3QMfZrnAbDhnh9mDUqycszcpf86VgQxhF',
    );
  });
});


