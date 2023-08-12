src/components/common/Address.tsx
=================================

Last edited: 2022-08-30 20:54:29

Contents:

.. code-block:: tsx

    import React from "react";
import { Link } from "react-router-dom";
import { PublicKey } from "@solana/web3.js";
import { clusterPath } from "utils/url";
import { displayAddress } from "utils/tx";
import { useCluster } from "providers/cluster";
import { Copyable } from "./Copyable";
import { useTokenRegistry } from "providers/mints/token-registry";
import { useState, useEffect } from "react";
import { Connection, programs } from "@metaplex/js";
import { useCustomAddressLabels } from "../../amman";

type Props = {
  pubkey: PublicKey;
  alignRight?: boolean;
  link?: boolean;
  raw?: boolean;
  truncate?: boolean;
  truncateUnknown?: boolean;
  truncateChars?: number;
  useMetadata?: boolean;
};

export function Address({
  pubkey,
  alignRight,
  link,
  raw,
  truncate,
  truncateUnknown,
  truncateChars,
  useMetadata,
}: Props) {
  const address = pubkey.toBase58();
  const { tokenRegistry } = useTokenRegistry();
  const { cluster } = useCluster();
  const [customAddressLabels] = useCustomAddressLabels();

  if (
    truncateUnknown &&
    address ===
      displayAddress(address, cluster, tokenRegistry, customAddressLabels)
  ) {
    truncate = true;
  }

  const displayLabel = displayAddress(
    address,
    cluster,
    tokenRegistry,
    customAddressLabels
  );
  let addressLabel = raw ? address : displayLabel;
  if (addressLabel !== displayLabel) {
    addressLabel = `${displayLabel} (${addressLabel})`;
    document.title = displayLabel;
  }

  var metaplexData = useTokenMetadata(useMetadata, address);
  if (metaplexData && metaplexData.data)
    addressLabel = metaplexData.data.data.name;
  if (truncateChars && addressLabel === address) {
    addressLabel = addressLabel.slice(0, truncateChars) + "…";
  }

  const content = (
    <Copyable text={address} replaceText={!alignRight}>
      <span className="font-monospace">
        {link ? (
          <Link
            className={truncate ? "text-truncate address-truncate" : ""}
            to={clusterPath(`/address/${address}`)}
          >
            {addressLabel}
          </Link>
        ) : (
          <span className={truncate ? "text-truncate address-truncate" : ""}>
            {addressLabel}
          </span>
        )}
      </span>
    </Copyable>
  );

  return (
    <>
      <div
        className={`d-none d-lg-flex align-items-center ${
          alignRight ? "justify-content-end" : ""
        }`}
      >
        {content}
      </div>
      <div className="d-flex d-lg-none align-items-center">{content}</div>
    </>
  );
}
export const useTokenMetadata = (
  useMetadata: boolean | undefined,
  pubkey: string
) => {
  const [data, setData] = useState<programs.metadata.MetadataData>();
  var { url } = useCluster();

  useEffect(() => {
    if (!useMetadata) return;
    if (pubkey && !data) {
      programs.metadata.Metadata.getPDA(pubkey)
        .then((pda) => {
          const connection = new Connection(url);
          programs.metadata.Metadata.load(connection, pda)
            .then((metadata) => {
              setData(metadata.data);
            })
            .catch(() => {
              setData(undefined);
            });
        })
        .catch(() => {
          setData(undefined);
        });
    }
  }, [useMetadata, pubkey, url, data, setData]);
  return { data };
};


