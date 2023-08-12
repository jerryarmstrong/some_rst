src/components/common/VerifiedBadge.tsx
=======================================

Last edited: 2022-08-30 20:54:29

Contents:

.. code-block:: tsx

    import { VerifiableBuild } from "utils/program-verification";

export function VerifiedBadge({
  verifiableBuild,
  deploySlot,
}: {
  verifiableBuild: VerifiableBuild;
  deploySlot: number;
}) {
  if (verifiableBuild && verifiableBuild.verified_slot === deploySlot) {
    return (
      <h3 className="mb-0">
        <a
          className="c-pointer badge bg-success-soft rank"
          href={verifiableBuild.url}
          target="_blank"
          rel="noreferrer"
        >
          {verifiableBuild.label}: Verified
        </a>
      </h3>
    );
  } else {
    return (
      <h3 className="mb-0">
        <span className="badge bg-warning-soft rank">
          {verifiableBuild.label}: Unverified
        </span>
      </h3>
    );
  }
}

export function CheckingBadge() {
  return (
    <h3 className="mb-0">
      <span className="badge bg-dark rank">Checking</span>
    </h3>
  );
}


