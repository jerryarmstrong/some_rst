app/src/atoms/details-card.styled.tsx
=====================================

Last edited: 2023-07-21 18:33:07

Contents:

.. code-block:: tsx

    import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";
import { styled } from "@mui/material/styles";

export const Container = styled(Box)`
  justify-content: center;
  min-width: 125px;
  padding: ${(p) => p.theme.spacing(1)} ${(p) => p.theme.spacing(2)};
`;

export const Content = styled(Box)`
  padding: 2px;
  text-align: center;
  border: 0;
`;

export const Title = styled(Typography)`
  font-size: 14px;
  white-space: nowrap;
`;


