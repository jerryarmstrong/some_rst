client/src/components/ClusterStatusButton.tsx
=============================================

Last edited: 2022-06-08 08:09:30

Contents:

.. code-block:: tsx

    import React from "react";
import { useServer, useClusterModal } from "../providers/server";

function ClusterStatusButton() {
  const [, setShow] = useClusterModal();
  const { name } = useServer();
  return (
    <span
      className="btn lift d-block btn-info text-white"
      onClick={() => setShow(true)}
    >
      {name}
    </span>
  );
}

export default ClusterStatusButton;


