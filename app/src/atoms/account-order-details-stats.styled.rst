app/src/atoms/account-order-details-stats.styled.tsx
====================================================

Last edited: 2023-07-21 18:33:07

Contents:

.. code-block:: tsx

    import Box from "@mui/material/Box";
import Card from "@mui/material/Card";
import Grid from "@mui/material/Grid";
import { styled } from "@mui/material/styles";

export const Container = styled(Box)`
  padding: ${({ theme }) => theme.spacing(2)};
`;

export const Stat = styled(Card)``;

export const Column = styled(Grid)`
  display: flex;
  flex-direction: column;
`;


