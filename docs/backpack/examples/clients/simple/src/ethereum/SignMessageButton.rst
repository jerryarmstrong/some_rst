examples/clients/simple/src/ethereum/SignMessageButton.tsx
==========================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: tsx

    import type { FC } from "react";
import { useSignMessage } from "wagmi";

export const SignMessageButton: FC = () => {
  const { data, isError, isLoading, isSuccess, signMessage } = useSignMessage({
    message: "Hello, world!",
  });

  return (
    <div>
      <button disabled={isLoading} onClick={() => signMessage()}>
        Sign the message: Hello, world!
      </button>
      {isSuccess && <div>Signature: {data}</div>}
      {isError && <div>Error signing message</div>}
    </div>
  );
};


