app/src/atoms/mode-toggle.tsx
=============================

Last edited: 2023-07-21 18:33:07

Contents:

.. code-block:: tsx

    import type { MouseEvent } from "react";
import { useCallback } from "react";
import * as Styled from "./mode-toggle.styled";
import i18n from "../i18n";

export interface Props {
  mode: string;
  onChange: (mode: string) => void;
}

export const modes = new Map([
  ["pairs", "pairs"],
  ["exchange", "exchange"],
  ["orders", "orders"],
]);

export default ({ mode, onChange: handleChange = () => {} }: Props) => {
  const onChange = useCallback(
    (_: MouseEvent<HTMLElement>, value: string | null) => {
      if (value) handleChange(value);
    },
    [handleChange]
  );

  const pairs = modes.get("pairs") as string;
  const exchange = modes.get("exchange") as string;
  const orders = modes.get("orders") as string;

  return (
    <Styled.ModeButtonGroup
      value={mode}
      exclusive
      onChange={onChange}
      aria-label={i18n.AriaLabelSpaces}
    >
      <Styled.ModeButton value={exchange} aria-label={exchange}>
        {i18n.SpacesTabsTrade}
      </Styled.ModeButton>
      <Styled.ModeButton value={orders} aria-label={orders}>
        {i18n.SpacesTabsOrders}
      </Styled.ModeButton>
      <Styled.ModeButton value={pairs} aria-label={pairs}>
        {i18n.SpacesTabsStats}
      </Styled.ModeButton>
    </Styled.ModeButtonGroup>
  );
};


