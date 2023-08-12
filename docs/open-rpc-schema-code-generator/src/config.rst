src/config.ts
=============

Last edited: 2021-10-02 02:46:04

Contents:

.. code-block:: ts

    
export interface IClientConfig {
  type: "client";
  name: string;
  language: "typescript" | "rust";
  outPath?: string;
}

export interface IServerConfig {
  type: "server";
  name: string;
  language: "typescript";
  outPath?: string;
}

export interface IDocsConfig {
  type: "docs";
  name: string;
  language: "gatsby";
  outPath?: string;
}

// Experimental
export interface ICustomConfig {
  type: "custom";
  name: string;
  customComponent: string;
  customType?: string;
  openRPCPath?: string | null;
  outPath?: string;
  language: "typescript" | "rust";
}

export type TComponentConfig = IClientConfig | IServerConfig | IDocsConfig | ICustomConfig;

