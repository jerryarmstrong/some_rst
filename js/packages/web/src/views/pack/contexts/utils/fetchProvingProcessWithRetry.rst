js/packages/web/src/views/pack/contexts/utils/fetchProvingProcessWithRetry.ts
=============================================================================

Last edited: 2022-06-29 06:18:54

Contents:

.. code-block:: ts

    import {
  getUnixTs,
  ParsedAccount,
  sleep,
  StringPublicKey,
} from '@oyster/common';
import {
  getProvingProcessByPubkey,
  ProvingProcess,
} from '@oyster/common/dist/lib/models/packs/accounts/ProvingProcess';
import { Connection } from '@solana/web3.js';

interface FetchProvingProcessWithRetryParams {
  provingProcessKey: StringPublicKey;
  connection: Connection;
}

const SLEEP_TIMEOUT = 300;
const REQUEST_TIMEOUT = 15000;

export const fetchProvingProcessWithRetry = async ({
  provingProcessKey,
  connection,
}: FetchProvingProcessWithRetryParams): Promise<
  ParsedAccount<ProvingProcess>
> => {
  let provingProcess;
  const startTime = getUnixTs();

  while (!provingProcess && getUnixTs() - startTime < REQUEST_TIMEOUT) {
    try {
      provingProcess = await getProvingProcessByPubkey(
        connection,
        provingProcessKey,
      );
    } catch {
      // skip
    }

    await sleep(SLEEP_TIMEOUT);
  }

  return provingProcess;
};


