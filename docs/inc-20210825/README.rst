README.md
=========

Last edited: 2021-09-02 06:22:54

Contents:

.. code-block:: md

    ## Usage
### Install prerequisites
#### System development libraries
```
sudo apt install libssl-dev libudev-dev pkg-config gcc
```
#### Rust
```
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```
### Minimum Solana Configuration

#### Initialize default keypair file

This is only needed as part of program's initialization.
SOL isn't used for `audit` mode. Only needed for `cleanup` mode to send actual
cleanup transactions if any.

```
solana-keygen new
```

Otherwise, this program would fail to execute at all with
`error: No such file or directory (os error 2)`.

### Availability of private keys

`cleanup` mode requires the existence of private keys of spl-token owners locally.
This usually means the need to store them in the Solana CLI's JSON format.

However, only public key _addresses_ will be needed with its `--dry-run` option.
In that case, equivalent `spl-token revoke ...` must be executed with corresponding
private keys to clean-up them.

`audit` mode doesn't require private keys, only public key _addresses_ of
spl-token owners.

### Targeted vulnerable account cleanup
The following command will revoke any existing delegations on all wallet:mint
pairs provided. Specify addresses for all mints that your organization supports
as well as every user deposit SOL wallet generated before epoch 216. Wallets
must be specified as the path to a keypair file in `solana-keygen new` format.
It may be necessary to run this command in multiple batches if the command line
is too long for the shell.
#### Dry-run
First a dry-run to be sure everything looks OK
```
cargo run -- cleanup \
--dry-run \
--mint MINT1_ADDRESS \
--mint MINT2_ADDRESS \
... \
--mint MINTN_ADDRESS \
DEPOSIT_SOL_WALLET1_PATH \
DEPOSIT_SOL_WALLET2_PATH \
... \
DEPOSIT_SOL_WALLETN_PATH
```
#### Effective run
If everything looks OK from the [dry-run](#dry-run), run the same command again
with the `--dry-run` argument removed.
### Targeted transaction history audit
The following will generate an audit report for the transaction history of each
token account, flagging suspicious and malicious behavior. As with
[cleanup](#targeted-vulnerable-account-cleanup), specify the addresses for every
mint your organization supports as well as every user deposit SOL wallet
generated before epoch 216. Wallets must be specified as the path to a keypair
file in `solana-keygen new` format. It may be necessary to run this command in
multiple batches if the command line is to long for the shell.
#### Run
```
cargo run -- audit \
--mint MINT1_ADDRESS \
--mint MINT2_ADDRESS \
... \
--mint MINTN_ADDRESS \
DEPOSIT_SOL_WALLET1_PATH \
DEPOSIT_SOL_WALLET2_PATH \
... \
DEPOSIT_SOL_WALLETN_PATH | tee report.csv
```
#### Expected output

```
audit
Summary Reassigned Token Account Report
Status,Account Address,Owner Address,Set Owner Signature,Delegation Signature,Possibly Fraudulent Transfer and Burn Signatures
<Records for each address with Safe or other status>
...
```

If you only see the headers with no records, the pointed RPC URL might not have
full transaction history. Try to use other RPC by the `-u` option or edit the
solana cli config file on your environment.

Also, there will be no records printed if the given owner address holds no spl-token
at all.

### Full vulnerable account cleanup
It is possible that an attacker created vulnerable accounts for mints that your
organization does not yet support in the hope that one day they will be supported
and deposits can be exploited. To clean up all potentially vulnerable accounts,
re-run the [cleanup](#targeted-vulnerable-account-cleanup) command, this time
omitting all `--mint ...` arguments. This process may take quite some time depending
on how many unique tokens have been sent to each wallet.

# Disclaimer

All claims, content, designs, algorithms, estimates, roadmaps,
specifications, and performance measurements described in this project
are done with the Solana Foundation's ("SF") good faith efforts. It is up to
the reader to check and validate their accuracy and truthfulness.
Furthermore nothing in this project constitutes a solicitation for
investment.

Any content produced by SF or developer resources that SF provides, are
for educational and inspiration purposes only. SF does not encourage,
induce or sanction the deployment, integration or use of any such
applications (including the code comprising the Solana blockchain
protocol) in violation of applicable laws or regulations and hereby
prohibits any such deployment, integration or use. This includes use of
any such applications by the reader (a) in violation of export control
or sanctions laws of the United States or any other applicable
jurisdiction, (b) if the reader is located in or ordinarily resident in
a country or territory subject to comprehensive sanctions administered
by the U.S. Office of Foreign Assets Control (OFAC), or (c) if the
reader is or is working on behalf of a Specially Designated National
(SDN) or a person subject to similar blocking or denied party
prohibitions.

The reader should be aware that U.S. export control and sanctions laws
prohibit U.S. persons (and other persons that are subject to such laws)
from transacting with persons in certain countries and territories or
that are on the SDN list. As a project based primarily on open-source
software, it is possible that such sanctioned persons may nevertheless
bypass prohibitions, obtain the code comprising the Solana blockchain
protocol (or other project code or applications) and deploy, integrate,
or otherwise use it. Accordingly, there is a risk to individuals that
other persons using the Solana blockchain protocol may be sanctioned
persons and that transactions with such persons would be a violation of
U.S. export controls and sanctions law. This risk applies to
individuals, organizations, and other ecosystem participants that
deploy, integrate, or use the Solana blockchain protocol code directly
(e.g., as a node operator), and individuals that transact on the Solana
blockchain through light clients, third party interfaces, and/or wallet
software.


