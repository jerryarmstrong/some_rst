src/amman/AmmanVersionChecker.ts
================================

Last edited: 2022-08-30 20:54:29

Contents:

.. code-block:: ts

    import { AmmanVersion } from "@metaplex-foundation/amman-client";
import EventEmitter from "eventemitter3";
import { AmmanClient } from "./amman-client";

const UNRESOLVED_VERSION: [number, number, number] = [0, 0, 0];
export class AmmanVersionInfo {
  constructor(
    readonly version: AmmanVersion,
    readonly initialized = true,
    readonly ammanConnected: boolean,
    readonly relayConnected: boolean
  ) {}

  get ammanVersion(): string {
    return !this.resolved
      ? "v0.?.?"
      : `v${this.version[0]}.${this.version[1]}.${this.version[2]}`;
  }

  get ammanClientRequiredVersion(): string {
    const version = AmmanClient.MIN_AMMAN_CLI_VERSION_REQUIRED;
    return `v${version[0]}.${version[1]}.${version[2]}`;
  }

  get requiredVersionSatisfied(): boolean {
    const version = AmmanClient.MIN_AMMAN_CLI_VERSION_REQUIRED;
    if (this.version[0] > version[0]) return true;
    if (this.version[0] < version[0]) return false;
    if (this.version[1] > version[1]) return true;
    if (this.version[1] < version[1]) return false;
    return this.version[2] >= version[2];
  }
  get resolved() {
    return (
      this.version[0] !== UNRESOLVED_VERSION[0] ||
      this.version[1] !== UNRESOLVED_VERSION[1] ||
      this.version[2] !== UNRESOLVED_VERSION[2]
    );
  }

  static unresolved(ammanConnected: boolean, relayConnected: boolean) {
    return new AmmanVersionInfo(
      UNRESOLVED_VERSION,
      true,
      ammanConnected,
      relayConnected
    );
  }

  static uninitialized() {
    return new AmmanVersionInfo(UNRESOLVED_VERSION, false, false, false);
  }
}

export type OnAmmanVersionInfo = (versionInfo: AmmanVersionInfo) => void;
export class AmmanVersionChecker extends EventEmitter {
  private constructor(
    readonly ammanClient: AmmanClient,
    readonly setAmmanVersionInfo: OnAmmanVersionInfo,
    updateInterval = 3000
  ) {
    super();
    setInterval(() => this.requestVersionInfo(), updateInterval);
  }

  private static _instance?: AmmanVersionChecker;

  async requestVersionInfo() {
    const info: AmmanVersionInfo = await this.ammanClient.fetchAmmanVersion();
    this.setAmmanVersionInfo(info);
  }

  static instance(
    ammanClient: AmmanClient,
    setAmmanVersionInfo: OnAmmanVersionInfo
  ) {
    if (AmmanVersionChecker._instance == null) {
      AmmanVersionChecker._instance = new AmmanVersionChecker(
        ammanClient,
        setAmmanVersionInfo
      );
      AmmanVersionChecker._instance.requestVersionInfo();
    }
    return AmmanVersionChecker._instance;
  }
}


