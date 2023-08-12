src/amman/CustomAddressLabelsMonitor.ts
=======================================

Last edited: 2022-08-30 20:54:29

Contents:

.. code-block:: ts

    import { AccountStatesResolver } from "./AccountStatesResolver";
import {
  AmmanClient,
  CLEAR_ADDRESS_LABELS,
  UPDATE_ADDRESS_LABELS,
} from "./amman-client";
import { strict as assert } from "assert";

export type HandleAddressLabelsChanged = (labels: Map<string, string>) => void;

export class CustomAddressLabelsMonitor {
  private _labels: Map<string, string> = new Map();

  private constructor(
    readonly ammanClient: AmmanClient,
    readonly handleAddressLablesChanged: HandleAddressLabelsChanged
  ) {
    this.ammanClient
      .on(UPDATE_ADDRESS_LABELS, this.onUpdateLabels)
      .on(CLEAR_ADDRESS_LABELS, this.onClearLabels)
      .requestKnownAddressLabels();
  }

  private onUpdateLabels = (labels: Record<string, string>) => {
    this._labels = new Map([
      ...Array.from(this._labels),
      ...Object.entries(labels),
    ]);
    this.handleAddressLablesChanged(this._labels);
    for (const address of Object.keys(labels)) {
      if (address.length <= 44) {
        AccountStatesResolver.instance.requestAccountStates(address);
      }
    }
  };

  private onClearLabels = () => {
    this._labels.clear();
    this.handleAddressLablesChanged(this._labels);
  };

  get(address: string) {
    return this._labels.get(address);
  }

  private static _instance?: CustomAddressLabelsMonitor;
  static get instance() {
    assert(
      this._instance != null,
      "CustomAddressLabelsMonitor.setInstance needs to be called first"
    );
    return this._instance;
  }
  static setInstance(
    ammanClient: AmmanClient,
    handleAddressLablesChanged: HandleAddressLabelsChanged
  ): CustomAddressLabelsMonitor {
    return (
      CustomAddressLabelsMonitor._instance ??
      (CustomAddressLabelsMonitor._instance = new CustomAddressLabelsMonitor(
        ammanClient,
        handleAddressLablesChanged
      ))
    );
  }
}


