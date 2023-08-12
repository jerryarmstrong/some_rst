clients/js-solita/src/revisions/shared/amountOperator.ts
========================================================

Last edited: 2023-08-01 17:12:05

Contents:

.. code-block:: ts

    export enum AmountOperator {
  Lt, // Less Than
  LtEq, // Less Than or Equal To
  Eq, // Equal To
  GtEq, // Greater Than or Equal To
  Gt, // Greater Than
}

export type AmountOperatorString = '<' | '<=' | '=' | '>=' | '>';

export const parseAmountOperator = (
  operator: AmountOperator | AmountOperatorString,
): AmountOperator => {
  return (
    {
      '<': AmountOperator.Lt,
      '<=': AmountOperator.LtEq,
      '=': AmountOperator.Eq,
      '>=': AmountOperator.GtEq,
      '>': AmountOperator.Gt,
    }[operator] ?? operator
  );
};

export const parseAmountOperatorString = (
  operator: AmountOperator | AmountOperatorString,
): AmountOperatorString => {
  return (
    {
      [AmountOperator.Lt]: '<',
      [AmountOperator.LtEq]: '<=',
      [AmountOperator.Eq]: '=',
      [AmountOperator.GtEq]: '>=',
      [AmountOperator.Gt]: '>',
    }[operator] ?? operator
  );
};


