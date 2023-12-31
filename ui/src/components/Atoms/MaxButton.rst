ui/src/components/Atoms/MaxButton.tsx
=====================================

Last edited: 2023-08-09 02:22:59

Contents:

.. code-block:: tsx

    import { twMerge } from "tailwind-merge";

interface Props {
  maxBalance?: number;
  onChangeAmount?: (amount: number) => void;
}
export function MaxButton(props: Props) {
  if (props.maxBalance && props.onChangeAmount) {
    return (
      <button
        className={twMerge(
          "h-min",
          "w-min",
          "bg-purple-500",
          "rounded",
          "py-1",
          "px-2",
          "text-white"
        )}
        onClick={() => props.onChangeAmount(props.maxBalance)}
      >
        Max
      </button>
    );
  } else {
    return <></>;
  }
}


