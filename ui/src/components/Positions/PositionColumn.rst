ui/src/components/Positions/PositionColumn.tsx
==============================================

Last edited: 2023-08-09 02:22:59

Contents:

.. code-block:: tsx

    export const COL_WIDTHS = {
  1: 14,
  2: 13,
  3: 13,
  4: 13,
  5: 13,
  6: 13,
  7: 18,
} as const;

export function PositionColumn(props: {
  children: React.ReactNode;
  num: keyof typeof COL_WIDTHS;
}) {
  return (
    <div style={{ width: `${COL_WIDTHS[props.num]}%` }}>{props.children}</div>
  );
}


