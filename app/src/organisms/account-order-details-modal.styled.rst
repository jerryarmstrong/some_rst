app/src/organisms/account-order-details-modal.styled.tsx
========================================================

Last edited: 2023-07-21 18:33:07

Contents:

.. code-block:: tsx

    import Box from "@mui/material/Box";
import { styled } from "@mui/material/styles";

export const Container = styled(Box)`
  padding: ${(p) => p.theme.spacing(2)};
`;

export const MobileContainer = styled(Box)`
  padding: ${(p) => p.theme.spacing(2)};
  padding-top: ${(p) => p.theme.spacing(4)};
`;

export const ContentHeader = styled(Box)`
  ${(p) => p.theme.typography.h5};
  color: ${(p) => p.theme.palette.common.white};
`;


