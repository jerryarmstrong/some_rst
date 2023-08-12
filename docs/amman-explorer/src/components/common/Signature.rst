src/components/common/Signature.tsx
===================================

Last edited: 2022-08-30 20:54:29

Contents:

.. code-block:: tsx

    import React from "react";
import { Link } from "react-router-dom";
import { TransactionSignature } from "@solana/web3.js";
import { clusterPath } from "utils/url";
import { Copyable } from "./Copyable";

type Props = {
  signature: TransactionSignature;
  alignRight?: boolean;
  link?: boolean;
  truncate?: boolean;
  truncateChars?: number;
  addressLabel?: string;
};

export function Signature({
  signature,
  alignRight,
  link,
  truncate,
  truncateChars,
  addressLabel,
}: Props) {
  let signatureLabel = signature;

  if (truncateChars) {
    signatureLabel = signature.slice(0, truncateChars) + "…";
  }
  const signatureDisplay =
    addressLabel == null ? (
      <>{signatureLabel}</>
    ) : (
      <>
        <span>{addressLabel}</span>
        <span className="opacity-25 display-6 ms-3">{signatureLabel}</span>
      </>
    );

  return (
    <div
      className={`d-flex align-items-center ${
        alignRight ? "justify-content-end" : ""
      }`}
    >
      <Copyable text={signature} replaceText={!alignRight}>
        <span className="font-monospace">
          {link ? (
            <Link
              className={truncate ? "text-truncate signature-truncate" : ""}
              to={clusterPath(`/tx/${signature}`)}
            >
              {signatureDisplay}
            </Link>
          ) : (
            signatureDisplay
          )}
        </span>
      </Copyable>
    </div>
  );
}


