tests/raw.ts
============

Last edited: 2022-07-16 19:07:11

Contents:

.. code-block:: ts

    import * as anchor from '@project-serum/anchor';
import { Program } from '@project-serum/anchor';
import { Raw } from '../target/types/raw';

describe('raw', () => {
  // Configure the client to use the local cluster.
  anchor.setProvider(anchor.Provider.env());

  const program = anchor.workspace.Raw as Program<Raw>;

  it('Is initialized!', async () => {

  });
});


