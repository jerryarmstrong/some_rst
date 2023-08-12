app/src/atoms/interval-button.styled.tsx
========================================

Last edited: 2023-07-21 18:33:07

Contents:

.. code-block:: tsx

    import Button from "@mui/material/Button";
import { styled } from "@mui/material/styles";

export const ScheduleButton = styled(Button)`
  padding: 0 4px;
  text-transform: capitalize;

  &.Mui-disabled {
    color: ${(p) => p.theme.palette.grey.A700};
    border-color: ${(p) => p.theme.palette.grey.A700};
  }
  &.Mui-disabled + * {
    border-left-color: ${(p) => p.theme.palette.grey.A700};
  }
`;

export const SelectedScheduleButton = styled(Button)`
  padding: 0 4px;
  text-transform: capitalize;

  &.Mui-disabled {
    color: ${(p) => p.theme.palette.success.dark};
    border-color: ${(p) => p.theme.palette.success.dark};
  }
  &.Mui-disabled + * {
    border-left-color: ${(p) => p.theme.palette.success.dark};
  }
`;

export const MobileScheduleButton = styled(ScheduleButton)`
  padding: 0 2px;
  font-size: 12px;
  text-transform: capitalize;
`;

export const MobileSelectedScheduleButton = styled(SelectedScheduleButton)`
  padding: 0 2px;
  font-size: 12px;
  text-transform: capitalize;
`;


