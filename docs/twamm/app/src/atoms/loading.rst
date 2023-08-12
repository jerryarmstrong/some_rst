app/src/atoms/loading.tsx
=========================

Last edited: 2023-07-21 18:33:07

Contents:

.. code-block:: tsx

    import CircularProgress from "@mui/material/CircularProgress";

import * as Styled from "./loading.styled";

export default (props: { size?: number }) => (
  <Styled.Container>
    <CircularProgress size={props.size} />
  </Styled.Container>
);


