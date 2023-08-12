src/components/instruction/serum/NewOrderDetailsCard.tsx
========================================================

Last edited: 2022-08-30 20:54:29

Contents:

.. code-block:: tsx

    import React from "react";
import { SignatureResult, TransactionInstruction } from "@solana/web3.js";
import { InstructionCard } from "../InstructionCard";
import { Address } from "components/common/Address";
import { NewOrder } from "./types";

export function NewOrderDetailsCard(props: {
  ix: TransactionInstruction;
  index: number;
  result: SignatureResult;
  info: NewOrder;
  innerCards?: JSX.Element[];
  childIndex?: number;
}) {
  const { ix, index, result, info, innerCards, childIndex } = props;

  return (
    <InstructionCard
      ix={ix}
      index={index}
      result={result}
      title="Serum Program: New Order"
      innerCards={innerCards}
      childIndex={childIndex}
    >
      <tr>
        <td>Program</td>
        <td className="text-lg-end">
          <Address pubkey={info.programId} alignRight link />
        </td>
      </tr>

      <tr>
        <td>Market</td>
        <td className="text-lg-end">
          <Address pubkey={info.accounts.market} alignRight link />
        </td>
      </tr>

      <tr>
        <td>Open Orders</td>
        <td className="text-lg-end">
          <Address pubkey={info.accounts.openOrders} alignRight link />
        </td>
      </tr>

      <tr>
        <td>Request Queue</td>
        <td className="text-lg-end">
          <Address pubkey={info.accounts.requestQueue} alignRight link />
        </td>
      </tr>

      <tr>
        <td>Payer</td>
        <td className="text-lg-end">
          <Address pubkey={info.accounts.payer} alignRight link />
        </td>
      </tr>

      <tr>
        <td>Open Orders Owner</td>
        <td className="text-lg-end">
          <Address pubkey={info.accounts.openOrdersOwner} alignRight link />
        </td>
      </tr>

      <tr>
        <td>Base Vault</td>
        <td className="text-lg-end">
          <Address pubkey={info.accounts.baseVault} alignRight link />
        </td>
      </tr>

      <tr>
        <td>Quote Vault</td>
        <td className="text-lg-end">
          <Address pubkey={info.accounts.quoteVault} alignRight link />
        </td>
      </tr>

      <tr>
        <td>Side</td>
        <td className="text-lg-end">{info.data.side}</td>
      </tr>

      <tr>
        <td>Order Type</td>
        <td className="text-lg-end">{info.data.orderType}</td>
      </tr>

      <tr>
        <td>Limit Price</td>
        <td className="text-lg-end">{info.data.limitPrice.toString(10)}</td>
      </tr>

      <tr>
        <td>Max Quantity</td>
        <td className="text-lg-end">{info.data.maxQuantity.toString(10)}</td>
      </tr>

      <tr>
        <td>Client Id</td>
        <td className="text-lg-end">{info.data.clientId.toString(10)}</td>
      </tr>
    </InstructionCard>
  );
}


