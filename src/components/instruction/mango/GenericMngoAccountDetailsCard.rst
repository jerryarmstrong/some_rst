src/components/instruction/mango/GenericMngoAccountDetailsCard.tsx
==================================================================

Last edited: 2022-08-30 20:54:29

Contents:

.. code-block:: tsx

    import { SignatureResult, TransactionInstruction } from "@solana/web3.js";
import { Address } from "components/common/Address";
import { InstructionCard } from "../InstructionCard";

export function GenericMngoAccountDetailsCard(props: {
  ix: TransactionInstruction;
  index: number;
  result: SignatureResult;
  mangoAccountKeyLocation: number;
  title: String;
  innerCards?: JSX.Element[];
  childIndex?: number;
}) {
  const {
    ix,
    index,
    result,
    mangoAccountKeyLocation,
    title,
    innerCards,
    childIndex,
  } = props;
  const mangoAccount = ix.keys[mangoAccountKeyLocation];

  return (
    <InstructionCard
      ix={ix}
      index={index}
      result={result}
      title={"Mango Program: " + title}
      innerCards={innerCards}
      childIndex={childIndex}
    >
      <tr>
        <td>Mango account</td>
        <td>
          <Address pubkey={mangoAccount.pubkey} alignRight link />
        </td>
      </tr>
    </InstructionCard>
  );
}


