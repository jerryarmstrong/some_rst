app/src/atoms/interval-progress.styled.tsx
==========================================

Last edited: 2023-07-21 18:33:07

Contents:

.. code-block:: tsx

    import Box from "@mui/material/Box";
import CircularProgress from "@mui/material/CircularProgress";
import { styled } from "@mui/material/styles";

export const Progress = styled(Box)`
  position: relative;
`;

export const ProgressBackground = styled(CircularProgress)`
  color: ${(p) => p.theme.palette.grey["500"]};
`;

export const ProgressCustom = styled(CircularProgress)`
  left: 0;
  position: absolute;
`;

export const ProgressCounter = styled(CircularProgress)``;


