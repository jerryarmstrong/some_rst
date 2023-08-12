packages/library-legacy/test/cluster.test.ts
============================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    import {expect} from 'chai';

import {clusterApiUrl} from '../src/utils/cluster';

describe('Cluster Util', () => {
  it('invalid', () => {
    expect(() => {
      clusterApiUrl('abc123' as any);
    }).to.throw();
  });

  it('devnet', () => {
    expect(clusterApiUrl()).to.eq('https://api.devnet.solana.com');
    expect(clusterApiUrl('devnet')).to.eq('https://api.devnet.solana.com');
    expect(clusterApiUrl('devnet', true)).to.eq(
      'https://api.devnet.solana.com',
    );
    expect(clusterApiUrl('devnet', false)).to.eq(
      'http://api.devnet.solana.com',
    );
  });
});


