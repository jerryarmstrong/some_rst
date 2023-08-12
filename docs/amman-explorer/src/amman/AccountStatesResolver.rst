src/amman/AccountStatesResolver.ts
==================================

Last edited: 2022-08-30 20:54:29

Contents:

.. code-block:: ts

    import { AmmanClient, RESOLVED_ACCOUNT_STATES } from "./amman-client";
import { strict as assert } from "assert";
import { CustomAddressLabelsMonitor } from "./CustomAddressLabelsMonitor";
import { AccountDiff, RelayAccountState } from "@metaplex-foundation/amman-client";
import { UnreachableCaseError } from "./utils";

export enum AccountDiffType {
  Added,
  Removed,
  Changed,
}

function getAccountDiffType(diff: AccountDiff[number]): AccountDiffType {
  switch (diff.kind) {
    case "N":
    case "A":
      return AccountDiffType.Added;
    case "D":
      return AccountDiffType.Removed;
    case "E":
      return diff.lhs == null
        ? AccountDiffType.Added
        : diff.rhs == null
        ? AccountDiffType.Removed
        : AccountDiffType.Changed;
    default:
      // @ts-ignore we did cover all cases here
      throw new UnreachableCaseError(diff.kind);
  }
}

function mapAccountDiffByPath(
  accountDiff?: AccountDiff
): Map<string, AccountDiffType> | undefined {
  if (accountDiff == null) return undefined;
  const map = new Map();
  for (const diff of accountDiff) {
    if (diff.path != null && diff.path.length > 0) {
      map.set(diff.path.join("."), getAccountDiffType(diff));
    }
  }
  return map;
}

export type ResolvedAccountState = Omit<RelayAccountState, "accountDiff"> & {
  accountDiff?: Map<string, AccountDiffType>;
};
export type ResolvedAccountStates = {
  states: ResolvedAccountState[];
  accountAddress: string;
};
export type HandleAccountStatesResolved = (
  resolvedAccountStates: Map<string, ResolvedAccountStates>
) => void;

export class AccountStatesResolver {
  private readonly resolvedAccountStates: Map<string, ResolvedAccountStates> =
    new Map();
  handleAccountStatesResolved: HandleAccountStatesResolved = () => {};

  private constructor(readonly ammanClient: AmmanClient) {
    this.ammanClient.on(RESOLVED_ACCOUNT_STATES, this.onResolvedAccountStates);
  }

  requestAccountStates(accountAddress: string) {
    this.ammanClient.requestAccountStates(accountAddress);
  }

  private onResolvedAccountStates = (
    accountAddress: string,
    accountStates: RelayAccountState[]
  ) => {
    // Ensure that we don't emit an event when account states are the same
    const currentStates = this.resolvedAccountStates.get(accountAddress);
    if (
      currentStates != null &&
      currentStates.states.length === accountStates.length
    )
      return;

    const labeledStates: ResolvedAccountState[] = [];
    for (const state of accountStates) {
      const labeledState: RelayAccountState = { ...state, account: {} };
      for (const [key, val] of Object.entries(state.account)) {
        const label =
          typeof val === "string"
            ? CustomAddressLabelsMonitor.instance.get(val)
            : undefined;
        labeledState.account[key] = label != null ? `${label} (${val})` : val;
      }
      labeledStates.push({
        ...labeledState,
        accountDiff: mapAccountDiffByPath(labeledState.accountDiff),
      });
    }
    this.resolvedAccountStates.set(accountAddress, {
      states: labeledStates,
      accountAddress,
    });
    this.handleAccountStatesResolved(new Map(this.resolvedAccountStates));
  };

  private static _instance?: AccountStatesResolver;
  static get instance() {
    assert(
      AccountStatesResolver._instance != null,
      "AccountInfoResolver.setInstance needs to be called first"
    );
    return AccountStatesResolver._instance;
  }
  static setInstance(ammanClient: AmmanClient): AccountStatesResolver {
    if (AccountStatesResolver._instance != null) {
      console.warn("can only set AccountInfoResolver instance once");
      return AccountStatesResolver._instance;
    }
    return (AccountStatesResolver._instance = new AccountStatesResolver(
      ammanClient
    ));
  }
}


