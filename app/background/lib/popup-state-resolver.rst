app/background/lib/popup-state-resolver.ts
==========================================

Last edited: 2020-09-01 18:17:54

Contents:

.. code-block:: ts

    import { AVAILABLE_NETWORKS, PopupState } from "../../core/types"
import { ActionManager } from "./action-manager"
import { Store } from "../store"

export class PopupStateResolver {
  private store: Store
  private actionManager: ActionManager

  constructor(store: Store, actionManager: ActionManager) {
    this.store = store
    this.actionManager = actionManager
  }

  get = (): PopupState => {
    let state: PopupState = {
      walletState: "uninitialized",
      accounts: [],
      selectedNetwork: this.store.selectedNetwork,
      availableNetworks: AVAILABLE_NETWORKS,
      selectedAccount: this.store.selectedAccount,
      authorizedOrigins: [],
      actions: this.actionManager.getOrderedActions(),
      tokens: this.store.getTokens(this.store.selectedNetwork),
    }

    if (this.store.hasSecretBox()) {
      state.walletState = "locked"
    }
    if (this.store.hasWallet()) {
      state.walletState = "unlocked"
      state.accounts = this.store.wallet?.getPublicKeysAsBs58() || []
      state.authorizedOrigins = this.store.authorizedOrigins
    }

    return state
  }
}


