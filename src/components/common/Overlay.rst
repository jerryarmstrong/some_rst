src/components/common/Overlay.tsx
=================================

Last edited: 2022-08-30 20:54:29

Contents:

.. code-block:: tsx

    import React from "react";

type OverlayProps = {
  show: boolean;
};

export function Overlay({ show }: OverlayProps) {
  return (
    <div
      className={`modal-backdrop fade ${
        show ? "show" : "disable-pointer-events"
      }`}
    ></div>
  );
}


