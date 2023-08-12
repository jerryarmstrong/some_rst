app/src/molecules/progress-button.tsx
=====================================

Last edited: 2023-07-21 18:33:07

Contents:

.. code-block:: tsx

    import { useMemo } from "react";
import CircularProgress from "@mui/material/CircularProgress";
import * as Styled from "./progress-button.styled";
import { ConnectWalletGuard } from "../organisms/wallet-guard";

export interface Props {
  disabled: boolean;
  form?: string;
  loading?: boolean;
  onClick?: () => void;
  text?: string;
}

export default ({ disabled, form, loading = false, onClick, text }: Props) => {
  const sx = useMemo(() => ({ marginLeft: "8px" }), []);

  return (
    <ConnectWalletGuard append={false}>
      <Styled.ActionButton
        form={form}
        disabled={disabled}
        onClick={onClick}
        type="submit"
      >
        {text}
        {loading ? <CircularProgress sx={sx} size={20} /> : undefined}
      </Styled.ActionButton>
    </ConnectWalletGuard>
  );
};


