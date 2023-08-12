app/src/molecules/progress-button.styled.tsx
============================================

Last edited: 2023-07-21 18:33:07

Contents:

.. code-block:: tsx

    import Button from "@mui/material/Button";
import { styled } from "@mui/material/styles";

export const ActionButton = styled(Button)`
  background-color: #4bbeff;
  border-radius: 40px;
  color: #000;
  display: flex;
  height: 48px;
  justify-content: center;
  text-transform: capitalize;
  width: 100%;

  &.MuiButton-root:hover,
  &.MuiButton-root:focus,
  &.MuiButton-root:active {
    background-color: #1ebeff;
  }
`;


