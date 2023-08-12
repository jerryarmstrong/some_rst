src/amman/components/AmmanVersionView.tsx
=========================================

Last edited: 2022-08-30 20:54:29

Contents:

.. code-block:: tsx

    import { AmmanVersionInfo } from "../AmmanVersionChecker";
import { useAmmanVersion } from "../providers";

export function AmmanVersionView() {
  const [versionInfo] = useAmmanVersion();

  if (!versionInfo.initialized) {
    return <PendingVersion />;
  } else if (versionInfo.resolved) {
    return <ResolvedVersion versionInfo={versionInfo} />;
  } else {
    return <UnresolvedVersion versionInfo={versionInfo} />;
  }
}

function PendingVersion() {
  return <span className="text-warning">Amman version pending</span>;
}

function ResolvedVersion({ versionInfo }: { versionInfo: AmmanVersionInfo }) {
  if (versionInfo.requiredVersionSatisfied) {
    return (
      <span className="text-primary">Amman {versionInfo.ammanVersion}</span>
    );
  } else {
    return <UpgradeAmman versionInfo={versionInfo} />;
  }
}

function UnresolvedVersion({ versionInfo }: { versionInfo: AmmanVersionInfo }) {
  if (!versionInfo.ammanConnected) {
    return <span className="text-warning">Amman not connected</span>;
  } else if (!versionInfo.relayConnected) {
    return <span className="text-warning">Amman Relay not connected</span>;
  } else {
    return <UpgradeAmman versionInfo={versionInfo} />;
  }
}

function UpgradeAmman({ versionInfo }: { versionInfo: AmmanVersionInfo }) {
  return (
    <span className="text-danger">
      Amman {versionInfo.ammanVersion} should upgrade to {">="}
      {versionInfo.ammanClientRequiredVersion}
    </span>
  );
}


