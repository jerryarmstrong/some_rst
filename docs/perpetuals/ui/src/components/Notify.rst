ui/src/components/Notify.tsx
============================

Last edited: 2023-08-09 02:22:59

Contents:

.. code-block:: tsx

    import { toast } from "react-toastify";

// @ts-ignore
export const notify = (
  text: string | JSX.Element,
  type = "success",
  hideProgressBar = false
) =>
  toast[type](text, {
    position: "bottom-left",
    autoClose: 3000,
    hideProgressBar: hideProgressBar,
    closeOnClick: true,
    pauseOnHover: true,
    draggable: true,
    progress: undefined,
  });


