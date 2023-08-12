app/popup/pages/wallet-page.tsx
===============================

Last edited: 2020-09-01 18:17:54

Contents:

.. code-block:: tsx

    import React from "react"
import Container from "@material-ui/core/Container"
import { AccountList } from "../components/account-list"
import Grid from "@material-ui/core/Grid"
import { DebugButtons } from "../components/debug-buttons"
import { LoadingIndicator } from "../components/loading-indicator"
import { usePopupState } from "../context/background"
import { withLayout } from "../components/layout"

export const WalletPageBase: React.FC = () => {
  const popupState = usePopupState()
  const isProdNetwork = popupState.selectedNetwork.cluster === "mainnet-beta"

  if (!popupState?.selectedAccount) {
    return <LoadingIndicator />
  }

  return (
    <Container fixed maxWidth="md">
      <Grid container spacing={3}>
        <Grid item xs={12}>
          <AccountList account={popupState?.selectedAccount} />
        </Grid>
        {isProdNetwork ? null : (
          <Grid item xs={12}>
            <DebugButtons />
          </Grid>
        )}
      </Grid>
    </Container>
  )
}

export const WalletPage = withLayout(WalletPageBase)


