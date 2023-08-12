packages/governance/src/views/devtools/DevToolsView.tsx
=======================================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: tsx

    import React, { useState } from 'react';

import { useConnection, useWallet } from '@oyster/common';
import { Button, Space } from 'antd';
import { generateGovernanceArtifacts } from '../../actions/devtools/generateGovernanceArtifacts';
import './style.less';
import { CreateMint } from './createMint';

// import { ControlTestBench } from './controlTests';

export const DevToolsView = () => {
  return (
    <div>
      <GovernanceArtifacts></GovernanceArtifacts>
    </div>
  );
};

const GovernanceArtifacts = () => {
  const connection = useConnection();
  const wallet = useWallet();

  const [realmName, setRealmName] = useState('');
  const [communityMint, setCommunityMint] = useState('');
  const [councilMint, setCouncilMint] = useState('');
  const [tokenGovernance, setTokenGovernance] = useState({
    tokenAccountAddress: '',
    beneficiaryTokenAccountAddress: '',
  });

  const [generated, setGenerated] = useState(false);

  const onGenerateArtifacts = async () => {
    setGenerated(false);

    // Create user info account for Raydium staking
    // await createAccount(
    //   connection,
    //   wallet,
    //   88,
    //   new PublicKey('EhhTKczWMGQt46ynNeRX1WfeagwwJd7ufHvCDjRxjo5Q'),
    // );

    // return;

    const {
      communityMintAddress,
      councilMintAddress,
      realmName,
      tokenGovernance,
    } = await generateGovernanceArtifacts(connection, wallet);

    setCommunityMint(communityMintAddress.toBase58());
    setCouncilMint(councilMintAddress.toBase58());
    setRealmName(realmName);
    setTokenGovernance(tokenGovernance);

    setGenerated(true);
  };

  return (
    <Space direction="vertical" size="large">
      <div>
        <h2>Governance Artifacts</h2>
        <Button
          onClick={() => onGenerateArtifacts()}
          disabled={!wallet.connected}
        >
          Generate
        </Button>
        {generated && (
          <>
            <div>
              <h3>realm name: </h3>
              <div className="test-data">{realmName}</div>
            </div>

            <div>
              <h3>community mint / governed account: </h3>
              <div className="test-data">{communityMint}</div>
            </div>

            <div>
              <h3>council mint: </h3>
              <div className="test-data">{councilMint}</div>
            </div>

            <div>
              <h3>token governance - token account: </h3>
              <div className="test-data">
                {tokenGovernance.tokenAccountAddress}
              </div>
            </div>
            <div>
              <h3>token governance - beneficiary token account: </h3>
              <div className="test-data">
                {tokenGovernance.beneficiaryTokenAccountAddress}
              </div>
            </div>
          </>
        )}
        <div>{/* <ControlTestBench></ControlTestBench> */}</div>
      </div>
      <CreateMint></CreateMint>
    </Space>
  );
};


