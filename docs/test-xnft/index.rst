index.ts
========

Last edited: 2023-05-25 17:26:04

Contents:

.. code-block:: ts

    import { PublicKey, SystemProgram, Transaction } from "@solana/web3.js";

const button = document.getElementById("submit")!;
const originalText = button.textContent;

button.addEventListener("click", async () => {
  button.setAttribute("disabled", "true");
  button.textContent = "sending...";

  const transferTransaction = new Transaction().add(
    SystemProgram.transfer({
      fromPubkey: window.xnft.solana.publicKey,
      toPubkey: new PublicKey("So11111111111111111111111111111111111111112"),
      lamports: 1,
    })
  );

  try {
    const sig = await window.xnft.solana.sendAndConfirm(transferTransaction);
    button.textContent = "sent, tx: " + sig;
  } catch (err) {
    console.error(err);
    button.textContent = "tx error";
  }

  setTimeout(resetButton, 1000);
});

const resetButton = () => {
  button.removeAttribute("disabled");
  button.textContent = originalText;
};


