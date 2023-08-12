src/components/common/Slot.tsx
==============================

Last edited: 2022-08-30 20:54:29

Contents:

.. code-block:: tsx

    import React from "react";
import { Link } from "react-router-dom";
import { clusterPath } from "utils/url";
import { Copyable } from "./Copyable";

type Props = {
  slot: number;
  link?: boolean;
};
export function Slot({ slot, link }: Props) {
  return (
    <span className="font-monospace">
      {link ? (
        <Copyable text={slot.toString()}>
          <Link to={clusterPath(`/block/${slot}`)}>
            {slot.toLocaleString("en-US")}
          </Link>
        </Copyable>
      ) : (
        slot.toLocaleString("en-US")
      )}
    </span>
  );
}


