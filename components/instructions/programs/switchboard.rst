components/instructions/programs/switchboard.tsx
================================================

Last edited: 2023-08-11 18:13:34

Contents:

.. code-block:: tsx

    import { Connection } from '@solana/web3.js'

const INSTRUCTIONS = {
  202: {
    name: 'Fund Oracle',
    accounts: [],
    getDataUI: async (connection: Connection, data: Uint8Array) => {
      return (
        <>
          <div>{JSON.stringify(data)}</div>
        </>
      )
    },
  },
}

export const SWITCHBOARD_INSTRUCTIONS = {
  SW1TCH7qEPTdLsDHRgPuMQjbQxKdH2aBStViMFnt64f: INSTRUCTIONS,
}


