src/wallet-adapters/solong/index.tsx
====================================

Last edited: 2021-03-16 20:45:52

Contents:

.. code-block:: tsx

    import EventEmitter from "eventemitter3";
import { PublicKey, Transaction } from "@solana/web3.js";
import { WalletAdapter } from "../../contexts/wallet";
import { notify } from "../../utils/notifications";

export class SolongWalletAdapter extends EventEmitter implements WalletAdapter {
  _publicKey: PublicKey | null;
  _onProcess: boolean;
  constructor() {
    super();
    this._publicKey = null;
    this._onProcess = false;
    this.connect = this.connect.bind(this);
  }

  get publicKey() {
    return this._publicKey;
  }

  async signTransaction(transaction: Transaction) {
    return (window as any).solong.signTransaction(transaction);
  }

  connect() {
    if (this._onProcess) {
      return;
    }

    if ((window as any).solong === undefined) {
      notify({
        message: "Solong Error",
        description: "Please install solong wallet from Chrome ",
      });
      return;
    }

    this._onProcess = true;
    (window as any).solong
      .selectAccount()
      .then((account: any) => {
        this._publicKey = new PublicKey(account);
        this.emit("connect", this._publicKey);
      })
      .catch(() => {
        this.disconnect();
      })
      .finally(() => {
        this._onProcess = false;
      });
  }

  disconnect() {
    if (this._publicKey) {
      this._publicKey = null;
      this.emit("disconnect");
    }
  }
}


