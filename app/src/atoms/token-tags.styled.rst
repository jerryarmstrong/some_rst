app/src/atoms/token-tags.styled.tsx
===================================

Last edited: 2023-07-21 18:33:07

Contents:

.. code-block:: tsx

    import Chip from "@mui/material/Chip";
import Stack from "@mui/material/Stack";
import { styled } from "@mui/material/styles";

export const Tags = styled(Stack)`
  flex-wrap: wrap;
`;

export const Tag = styled(Chip)`
  border-radius: 6px;
  cursor: pointer;
`;


