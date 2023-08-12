src/amman/pages/AmmanGuidePage.tsx
==================================

Last edited: 2022-08-30 20:54:29

Contents:

.. code-block:: tsx

    import React from "react";
import { Link } from "react-router-dom";
import { Copyable } from "../../components/common/Copyable";
import { TableCardBody } from "../../components/common/TableCardBody";
import { useAmmanVersion } from "../providers";

export function AmmanGuidePage() {
  // TODO(thlorenz): what do we do if another cluster is selected here?
  const [verrsionInfo] = useAmmanVersion();
  const { ammanConnected } = verrsionInfo;
  return (
    <div className="container mt-4">
      <AmmanConnectionGreeting ammanConnected={ammanConnected} />
      <h2 className="mt-4">Amman Explorer Guide</h2>
      <Installation ammanConnected={ammanConnected} />
      <Usage />
      <APIUsage />
      <CliExample />
    </div>
  );
}

const btnClasses = (variant: string) => {
  return `p-3 d-block btn-${variant}`;
};

function AmmanConnectionGreeting(props: { ammanConnected: boolean }) {
  return props.ammanConnected ? (
    <span className={btnClasses("primary")}>
      <span className="fe fe-check-circle me-2"></span>
      Amman Connected
    </span>
  ) : (
    <span className={btnClasses("danger")}>
      <span className="fe fe-alert-circle me-2"></span>
      Amman Not Connected
    </span>
  );
}

function Installation({ ammanConnected }: { ammanConnected: boolean }) {
  const installSolanaUrl =
    "https://docs.solana.com/cli/install-solana-cli-tools";
  const ammanInstall = "npm install -g @metaplex-foundation/amman";
  const ammanStart = "amman start ";
  const refresh = ammanConnected ? null : (
    <tr>
      <td>4. Reload this Page check Amman Connection </td>
      <td className="text-lg-end">
        <Link to="/guide" onClick={() => window.location.reload()}>
          Reload
        </Link>
      </td>
    </tr>
  );

  return (
    <div className="card">
      <div className="card-header align-items-center">
        <h3 className="card-header-title text-primary">Installation</h3>
      </div>
      <TableCardBody>
        <tr>
          <td>1. Install Solana</td>
          <td className="text-lg-end">
            <a href={installSolanaUrl} target="_blank" rel="noreferrer">
              {installSolanaUrl}
            </a>
          </td>
        </tr>
        <tr>
          <td>2. Install Amman</td>
          <td className="text-lg-end">
            <Copyable text={ammanInstall}>
              <code className="m-3 p-3">{ammanInstall}</code>
            </Copyable>
          </td>
        </tr>
        <tr>
          <td>3. Launch Amman in Separate Terminal</td>
          <td className="text-lg-end">
            <Copyable text={ammanStart}>
              <code className="m-3 p-3">{ammanStart}</code>
            </Copyable>
          </td>
        </tr>
        {refresh}
      </TableCardBody>
    </div>
  );
}

function Usage() {
  const createWallet = `solana-keygen new --no-bip39-passphrase -s -o ./wallet.json`;
  const airdrop = `amman airdrop ./wallet.json -l wallet`;
  const ammanHelp = `amman --help`;
  const ammanStop = `amman stop`;

  return (
    <div className="card">
      <div className="card-header align-items-center">
        <h3 className="card-header-title text-primary">Command Line Usage</h3>
      </div>
      <TableCardBody>
        <tr>
          <td>1. Open new Terminal</td>
          <td> </td>
        </tr>
        <tr>
          <td>2. Create Wallet</td>
          <td className="text-lg-end">
            <Copyable text={createWallet}>
              <code className="m-3 p-3">{createWallet}</code>
            </Copyable>
          </td>
        </tr>
        <tr>
          <td>
            3. Airdrop to the Wallet and label it <em>wallet</em>
          </td>
          <td className="text-lg-end">
            <Copyable text={airdrop}>
              <code className="m-3 p-3">{airdrop}</code>
            </Copyable>
          </td>
        </tr>
        <tr>
          <td>4. Inspect transaction in Amman Explorer</td>
          <td className="text-lg-end">
            <em>It'll show up under "Recent Transactions" above</em>
          </td>
        </tr>
        <tr>
          <td>5. Discover more Amman Commands</td>
          <td className="text-lg-end">
            <Copyable text={ammanHelp}>
              <code className="m-3 p-3">{ammanHelp}</code>
            </Copyable>
          </td>
        </tr>
        <tr>
          <td>
            6. When finished Stop Amman (<em>Ctrl-C also works</em>)
          </td>
          <td className="text-lg-end">
            <Copyable text={ammanStop}>
              <code className="m-3 p-3">{ammanStop}</code>
            </Copyable>
          </td>
        </tr>
      </TableCardBody>

      <div className="card-header align-items-center">
        <h4 className="card-header-title text-secondary">
          Amman Command Line Screencast
        </h4>
      </div>
      <iframe
        className="row m-3"
        width="560"
        height="315"
        src="https://www.youtube.com/embed/i5Yx2-Xm-h8"
        title="YouTube video player"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
      ></iframe>
    </div>
  );
}

function APIUsage() {
  const ammanConfigUrl =
    "https://github.com/metaplex-foundation/amman#sample-validatorrelaystorage-config";
  const ammanAddrUrl =
    "https://metaplex-foundation.github.io/amman/docs/classes/AddressLabels.html";

  const codeStep = (title: string, code: string | null, className = "") => {
    const codeCell =
      code == null ? null : (
        <td className="text-lg-end">
          <Copyable text={CLI_EXAMPLE}>
            <code className="m-3 p-3">{code}</code>
          </Copyable>
        </td>
      );

    return (
      <tr>
        <td className={className}>{title}</td>
        {codeCell}
      </tr>
    );
  };

  const linkStep = (title: string, link: string, className = "") => (
    <tr>
      <td className={className}>{title}</td>
      <td className="text-lg-end">
        <a href={link} target="_blank" rel="noreferrer">
          {link}
        </a>
      </td>
    </tr>
  );
  return (
    <div className="card">
      <div className="card-header align-items-center">
        <h3 className="card-header-title text-primary">
          API TypeScript/JavaScript
        </h3>
      </div>
      <TableCardBody>
        <tr>
          <td>
            1. <em>Optionally</em> add an <code>.ammanrc.js</code> config to
            your project
          </td>
          <td className="text-lg-end">
            <a href={ammanConfigUrl} target="_blank" rel="noreferrer">
              {ammanConfigUrl}
            </a>
          </td>
        </tr>
        {codeStep(
          "2. Install Amman Client as part of your Project",
          "yarn add -D @metaplex-foundation/amman-client"
        )}
        {codeStep(
          "3. Import Amman",
          "import { Amman, LOCALHOST } from '@metaplex-foundation/amman-client"
        )}
        {codeStep("4 Initialize Amman", null, "text-primary")}
        {linkStep(
          "4.a Read up on Amman.init",
          "https://metaplex-foundation.github.io/amman/docs/classes/Amman.html#instance"
        )}
        {codeStep(
          "4.b Initalize an Amman Instance (pass options when desired)",
          "export const amman = Amman.instance()"
        )}
        {codeStep("5. Airdrop to a new Account", null, "text-primary")}
        {codeStep(
          "5.a Generate a labeled Keypair with Amman",
          "const [payer, payerPair] = amman.genKeypair('payer')"
        )}
        {linkStep(
          "5.b Read up on amman.airdrop",
          "https://metaplex-foundation.github.io/amman/docs/classes/Amman.html#airdrop"
        )}
        {codeStep(
          "5.c Create a web3.js Connection",
          "const connection = new Connection(LOCALHOST)",
          "m-3"
        )}
        {codeStep(
          "5.d Airdrop to the Keypair",
          "await amman.airdrop(connection, payer, 2)"
        )}
        {codeStep("6. Learn more about the Amman API", null, "text-primary")}
        <tr>
          <td>
            6.a Label acounts via <code>amman.addr</code>
          </td>
          <td className="text-lg-end">
            <a href={ammanAddrUrl} target="_blank" rel="noreferrer">
              {ammanAddrUrl}
            </a>
          </td>
        </tr>
        {linkStep(
          "6.b Send transactions via the payer transaction handler",
          "https://metaplex-foundation.github.io/amman/docs/classes/Amman.html#payerTransactionHandler"
        )}
      </TableCardBody>
    </div>
  );
}

function CliExample() {
  return (
    <div className="card">
      <div className="card-header align-items-center">
        <h3 className="card-header-title text-primary">
          Full Command Line Example
        </h3>
      </div>
      <TableCardBody>
        <p className="m-3">
          Follow
          <a className="me-0 pe-0 d-inline" href={walkThruUrl} rel="noreferrer">
            this walk through,
          </a>
          <span>watch the screencast above or run the script below</span>
        </p>
        <Copyable text={CLI_EXAMPLE}>
          <pre className="m-3 p-3">{CLI_EXAMPLE}</pre>
        </Copyable>
      </TableCardBody>
    </div>
  );
}
// -----------------
// CLI Example
// -----------------

const walkThruUrl =
  "https://gist.github.com/thlorenz/0a4fd8afe81dc1ba81e63619ed5a77bf#file-walk-thru-md";

const CLI_EXAMPLE = `
#!/usr/bin/env bash

## Prepare Wallets

solana-keygen new --silent --no-bip39-passphrase --outfile solpair1.json 
solana-keygen new --silent --no-bip39-passphrase --outfile solpair2.json 

### Airdrop and label them

amman airdrop ./solpair1.json -l soladdr1
amman airdrop ./solpair2.json -l soladdr2

### Use first one as default wallet

solana config set --keypair ./solpair1.json

amman account soladdr1

## Token Creation

amman run -l token1 -l tx-create-token1 -- \
  spl-token create-token --mint-authority ./solpair1.json

## Token Account Creation

amman run -l ata-tok1-addr1 -l tx-create-ata-tok1-addr1 -- \
  spl-token create-account +token1 --owner +soladdr1

## Token Minting

amman run -l tx-mint-token1-to-ata-tok1-addr1 -t -- \
  spl-token mint +token1 10 +ata-tok1-addr1 --mint-authority ./solpair1.json

## Token Transferring

### Create ATA for 'soladdr2'

amman run -l ata-tok1-addr2 -l tx-ata-tok1-addr2 -- \
  spl-token create-account +token1 --owner +soladdr2

### Transfer the token Soladdr2

amman run -l tx-transfer-token1-addr2 -t -- \
  spl-token transfer +token1 1 +soladdr2 --owner ./solpair1.json
`;


