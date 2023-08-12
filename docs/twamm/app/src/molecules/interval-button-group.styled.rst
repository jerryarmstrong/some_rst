app/src/molecules/interval-button-group.styled.tsx
==================================================

Last edited: 2023-07-21 18:33:07

Contents:

.. code-block:: tsx

    import Box from "@mui/material/Box";
import Skeleton from "@mui/material/Skeleton";
import { styled } from "@mui/material/styles";

export const BlankIntervals = styled(Skeleton)`
  border-radius: 8px;
  height: 26.5px;
  width: 50%;
`;

export const Interval = styled(Box)`
  color: ${({ theme }) => theme.palette.text.primary};
`;


