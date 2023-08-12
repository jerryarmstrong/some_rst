app/src/atoms/token-pair-cards-blank.tsx
========================================

Last edited: 2023-07-21 18:33:07

Contents:

.. code-block:: tsx

    import { Blank } from "./pair-card";
import * as Styled from "./token-pair-cards-blank.styled";

export default () => (
  <Styled.BlankCardList>
    {new Array(3).fill(null).map((_, i) => (
      // eslint-disable-next-line react/no-array-index-key
      <li key={`blank-${i}`}>
        <Blank />
      </li>
    ))}
  </Styled.BlankCardList>
);


