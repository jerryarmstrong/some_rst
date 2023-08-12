src/components/ClusterStatusButton.tsx
======================================

Last edited: 2022-08-30 20:54:29

Contents:

.. code-block:: tsx

    import React from "react";
import {
  useCluster,
  ClusterStatus,
  Cluster,
  useClusterModal,
} from "providers/cluster";
import { useAmmanVersion } from "../amman";

export function ClusterStatusBanner() {
  const [, setShow] = useClusterModal();

  return (
    <div className="container d-md-none my-4">
      <div onClick={() => setShow(true)}>
        <Button />
      </div>
    </div>
  );
}

export function ClusterStatusButton() {
  const [, setShow] = useClusterModal();

  return (
    <div onClick={() => setShow(true)}>
      <Button />
    </div>
  );
}

function Button() {
  const { status, cluster, name, customUrl } = useCluster();
  const statusName = cluster !== Cluster.Custom ? `${name}` : `${customUrl}`;
  const [versionInfo] = useAmmanVersion();

  const btnClasses = (variant: string) => {
    return `btn d-block btn-${variant}`;
  };

  if (cluster === Cluster.Amman) {
    if (versionInfo.ammanConnected) {
      return <Connected btnClasses={btnClasses} statusName={statusName} />;
    }
    if (!versionInfo.initialized) {
      return <Connecting btnClasses={btnClasses} statusName={statusName} />;
    }
    return <Failure btnClasses={btnClasses} statusName={statusName} />;
  } else {
    switch (status) {
      case ClusterStatus.Connected:
        return <Connected btnClasses={btnClasses} statusName={statusName} />;

      case ClusterStatus.Connecting:
        return <Connecting btnClasses={btnClasses} statusName={statusName} />;

      case ClusterStatus.Failure:
        return <Failure btnClasses={btnClasses} statusName={statusName} />;
    }
  }
}

function Connected({
  btnClasses,
  statusName,
}: {
  btnClasses: (variant: string) => string;
  statusName: string;
}) {
  return (
    <span className={btnClasses("primary")}>
      <span className="fe fe-check-circle me-2"></span>
      {statusName}
    </span>
  );
}
function Connecting({
  btnClasses,
  statusName,
}: {
  btnClasses: (variant: string) => string;
  statusName: string;
}) {
  const spinnerClasses = "spinner-grow spinner-grow-sm me-2";
  return (
    <span className={btnClasses("warning")}>
      <span className={spinnerClasses} role="status" aria-hidden="true"></span>
      {statusName}
    </span>
  );
}
function Failure({
  btnClasses,
  statusName,
}: {
  btnClasses: (variant: string) => string;
  statusName: string;
}) {
  return (
    <span className={btnClasses("danger")}>
      <span className="fe fe-alert-circle me-2"></span>
      {statusName}
    </span>
  );
}


