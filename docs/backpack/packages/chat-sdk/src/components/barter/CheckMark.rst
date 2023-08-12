packages/chat-sdk/src/components/barter/CheckMark.tsx
=====================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: tsx

    import { Check } from "@coral-xyz/react-common";
import CheckIcon from "@mui/icons-material/Check";
export const CheckMark = () => {
  return (
    <div
      style={{
        width: 25,
        height: 25,
        background: "#4C94FF",
        borderRadius: 16,
        border: "2px solid #F0F0F2",
      }}
    >
      <CheckIcon
        style={{ color: "white", marginTop: 2, fontSize: 15, marginLeft: 3 }}
      />
    </div>
  );
};


