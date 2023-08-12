src/components/common/Epoch.tsx
===============================

Last edited: 2022-08-30 20:54:29

Contents:

.. code-block:: tsx

    import React from "react";
import { Link } from "react-router-dom";
import { clusterPath } from "utils/url";
import { Copyable } from "./Copyable";

type Props = {
  epoch: number;
  link?: boolean;
};
export function Epoch({ epoch, link }: Props) {
  return (
    <span className="font-monospace">
      {link ? (
        <Copyable text={epoch.toString()}>
          <Link to={clusterPath(`/epoch/${epoch}`)}>
            {epoch.toLocaleString("en-US")}
          </Link>
        </Copyable>
      ) : (
        epoch.toLocaleString("en-US")
      )}
    </span>
  );
}


