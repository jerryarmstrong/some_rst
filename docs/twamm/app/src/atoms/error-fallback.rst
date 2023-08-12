app/src/atoms/error-fallback.tsx
================================

Last edited: 2023-07-21 18:33:07

Contents:

.. code-block:: tsx

    import Alert from "@mui/material/Alert";

export default ({ error }: { error: Error }) => (
  <Alert severity="error">{error.message ?? "Unknown Error"}</Alert>
);


