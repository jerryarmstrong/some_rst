app/src/organisms/token-field.tsx
=================================

Last edited: 2023-07-21 18:33:07

Contents:

.. code-block:: tsx

    import TextField from "@mui/material/TextField";

export interface Props {
  onClick: () => void;
}

export default ({ onClick, ...props }: Props) => (
  // eslint-disable-next-line react/jsx-props-no-spreading
  <TextField fullWidth onClick={onClick} {...props} />
);


