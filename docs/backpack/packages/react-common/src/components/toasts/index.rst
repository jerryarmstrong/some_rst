packages/react-common/src/components/toasts/index.tsx
=====================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: tsx

    import { toast as toastLibrary } from "react-toastify";

import { Success } from "./Success";

export const toast = {
  success: (title, body) => {
    toastLibrary(<Success title={title} body={body} />, {
      position: "top-center",
      hideProgressBar: true,
    });
  },
};


