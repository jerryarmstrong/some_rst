app/src/atoms/loading.styled.tsx
================================

Last edited: 2023-07-21 18:33:07

Contents:

.. code-block:: tsx

    import Box from "@mui/material/Box";
import { styled } from "@mui/material/styles";

export const Container = styled(Box)`
  display: flex;
  justify-content: center;
  padding: ${(p) => p.theme.spacing(1)};
`;


