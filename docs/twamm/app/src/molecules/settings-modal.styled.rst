app/src/molecules/settings-modal.styled.tsx
===========================================

Last edited: 2023-07-21 18:33:07

Contents:

.. code-block:: tsx

    import Divider from "@mui/material/Divider";
import Stack from "@mui/material/Stack";
import Typography from "@mui/material/Typography";
import { styled } from "@mui/material/styles";

export const Line = styled(Divider)`
  border-color: ${(p) => p.theme.palette.text.secondary};
`;

export const Setting = styled(Stack)`
  align-items: center;
  justify-content: space-between;
`;

export const ClusterSetting = styled(Stack)`
  align-items: left;
`;

export const SettingLabel = styled(Typography)`
  flex-grow: 1;
`;


